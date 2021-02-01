import json
import zlib
from collections import OrderedDict
from typing import List, Type

from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.helper.exceptions import InvalidScenarioStructure, UnknownScenarioStructure
from AoE2ScenarioParser.helper.helper import create_textual_hex
from AoE2ScenarioParser.helper.incremental_generator import IncrementalGenerator
from AoE2ScenarioParser.objects.map_obj import MapObject
from AoE2ScenarioParser.objects.triggers_obj import TriggersObject
from AoE2ScenarioParser.objects.units_obj import UnitsObject
from AoE2ScenarioParser.pieces.aoe2_file_part import AoE2FilePart
from AoE2ScenarioParser.pieces.background_image import BackgroundImagePiece
from AoE2ScenarioParser.pieces.cinematics import CinematicsPiece
from AoE2ScenarioParser.pieces.data_header import DataHeaderPiece
from AoE2ScenarioParser.pieces.diplomacy import DiplomacyPiece
from AoE2ScenarioParser.pieces.file_header import FileHeaderPiece
from AoE2ScenarioParser.pieces.files import FilesPiece
from AoE2ScenarioParser.pieces.global_victory import GlobalVictoryPiece
from AoE2ScenarioParser.pieces.map import MapPiece
from AoE2ScenarioParser.pieces.messages import MessagesPiece
from AoE2ScenarioParser.pieces.options import OptionsPiece
from AoE2ScenarioParser.pieces.player_data_two import PlayerDataTwoPiece
from AoE2ScenarioParser.pieces.triggers import TriggersPiece
from AoE2ScenarioParser.pieces.units import UnitsPiece


class AoE2Scenario:
    @property
    def trigger_manager(self) -> TriggersObject:
        return self._object_manager.objects['TriggersObject']

    @property
    def unit_manager(self) -> UnitsObject:
        return self._object_manager.objects['UnitsObject']

    @property
    def map_manager(self) -> MapObject:
        return self._object_manager.objects['MapObject']

    def __init__(self):
        self.read_mode = None
        self.scenario_version = "???"
        self.game_version = "???"
        self.structure = {}
        self.pieces: OrderedDict[str, AoE2FilePart] = OrderedDict()
        self._object_manager = None

        # Used in debug functions
        self._file = None
        self._file_header = None
        self._decompressed_file_data = None

    @classmethod
    def from_file(cls, filename):
        print(f"\nSelected file: '{filename}'")
        helper.rprint("Reading scenario file...")
        igenerator = IncrementalGenerator.from_file(filename)
        helper.rprint("Reading scenario file finished successfully.", final=True)

        scenario = cls()
        scenario.read_mode = "from_file"
        scenario.game_version = "DE"
        scenario.scenario_version = get_file_version(igenerator)

        # Log game and scenario version
        print("\n############### Attributes ###############")
        print(f">>> Game version: '{scenario.game_version}'")
        print(f">>> Scenario version: {scenario.scenario_version}")
        print("##########################################")

        helper.rprint(f"\nLoading scenario structure...")
        scenario.load_structure()
        helper.rprint(f"Loading scenario structure finished successfully.", final=True)

        scenario._initialise(igenerator)

        return scenario

    def load_structure(self):
        if self.game_version == "???" or self.scenario_version == "???":
            raise ValueError("Both game and scenario version need to be set to load structure")
        self.structure = get_structure(self.game_version, self.scenario_version)

    def _initialise(self, raw_file_igenerator: IncrementalGenerator):
        helper.rprint("Parsing scenario file...", final=True)

        header = self._initialise_file_part('FileHeader', raw_file_igenerator)
        self._add_to_pieces(header)

        data_igenerator = IncrementalGenerator(
            name='Scenario Data',
            file_content=decompress_bytes(raw_file_igenerator.get_remaining_bytes())
        )

        for piece_name in self.structure.keys():
            if piece_name == "FileHeader":
                continue
            try:
                piece = self._initialise_file_part(piece_name, data_igenerator)
                self._add_to_pieces(piece)
            except (ValueError, TypeError) as e:
                print(f"\n[{e.__class__.__name__}] AoE2Scenario.parse_file: \n\tPiece: {piece_name}\n")
                self.write_error_file(trail_generator=data_igenerator)
                raise e

        helper.rprint(f"Parsing scenario file finished successfully.", final=True)

    def _initialise_file_part(self, name, igenerator):
        helper.rprint(f"\t🔄 Parsing {name}...")
        piece = self._parse_file_part(name)
        helper.rprint(f"\t🔄 Setting {name} data...")
        piece.set_data_from_generator(igenerator, self.pieces)
        helper.rprint(f"\t✔ {name}", final=True)
        return piece

    def _parse_file_part(self, name):
        return AoE2FilePart.from_structure(name, self.structure.get(name))

    def _add_to_pieces(self, piece):
        self.pieces[piece.name] = piece

    """ ##########################################################################################
    ####################################### Write functions ######################################
    ########################################################################################## """

    def write_to_file(self, filename):
        helper.rprint("\nFile writing from structure started...", final=True)
        self._write_from_structure(filename)
        helper.rprint("File writing finished successfully.", final=True)

    def _write_from_structure(self, filename):
        binary = self._get_file_part_data(self.pieces.get('FileHeader'))

        binary_list_to_be_compressed = []
        for file_part in self.pieces.values():
            if file_part.name == "FileHeader":
                continue
            binary_list_to_be_compressed.append(self._get_file_part_data(file_part))
        compressed = compress_bytes(b''.join(binary_list_to_be_compressed))

        file = open(filename, "wb")
        file.write(binary + compressed)
        file.close()

    def _get_file_part_data(self, file_part):
        helper.rprint(f"\t🔄 Reconstructing {file_part.name}...")
        value = file_part.get_data_as_bytes()
        helper.rprint(f"\t✔ {file_part.name}", final=True)
        return value

    def write_error_file(self, filename="error_file", trail_generator=None):
        self._debug_byte_structure_to_file(filename=filename, trail_generator=trail_generator)

    """ #############################################
    ################ Debug functions ################
    ############################################# """

    def _debug_write_from_source(self, filename, datatype, write_bytes=True):
        """This function is used as a test debugging writing. It writes parts of the read file to the filesystem."""
        print("File writing from source started with attributes " + datatype + "...")
        file = open(filename, "wb" if write_bytes else "w")
        selected_parts = []
        for t in datatype:
            if t == "f":
                selected_parts.append(self._file)
            elif t == "h":
                selected_parts.append(self._file_header)
            elif t == "d":
                selected_parts.append(self._decompressed_file_data)
        parts = None
        for part in selected_parts:
            if parts is None:
                parts = part
                continue
            parts += part
        file.write(parts if write_bytes else create_textual_hex(parts.hex()))
        file.close()
        print("File writing finished successfully.")

    def _retrieve_byte_structure(self, file_part):
        helper.rprint(f"\t🔄 Writing {file_part.name}...")
        value = file_part.get_byte_structure_as_string(self.pieces)
        helper.rprint(f"\t✔ {file_part.name}", final=True)
        return value

    def _debug_byte_structure_to_file(self, filename, trail_generator: IncrementalGenerator = None, commit=False):
        """ Used for debugging - Writes structure from read file to the filesystem in a easily readable manner. """
        if commit and hasattr(self, '_object_manager'):
            pass
            # self._object_manager.reconstruct(log_debug_write)

        helper.rprint("Writing structure to file...", final=True)
        with open(filename, 'w', encoding="utf-8") as f:
            result = []
            for piece in self.pieces.values():
                result.append(self._retrieve_byte_structure(piece))

            if trail_generator is not None:
                helper.rprint("\tWriting trail...")
                trail = trail_generator.get_remaining_bytes()

                result.append(f"\n\n{'#' * 27} TRAIL ({len(trail)})\n\n")
                result.append(helper.create_textual_hex(trail.hex(), space_distance=2, enter_distance=24))
                helper.rprint("\tWriting trail finished successfully.", final=True)

            f.write(''.join(result))
        helper.rprint("Writing structure to file finished successfully.", final=True)


def get_file_version(generator: IncrementalGenerator):
    """Get first 4 bytes of a file, which contains the version of the scenario"""
    return generator.get_bytes(4, update_progress=False).decode('ASCII')


def decompress_bytes(file_content):
    return zlib.decompress(file_content, -zlib.MAX_WBITS)


def compress_bytes(file_content):
    # https://stackoverflow.com/questions/3122145/zlib-error-error-3-while-decompressing-incorrect-header-check/22310760#22310760
    deflate_obj = zlib.compressobj(9, zlib.DEFLATED, -zlib.MAX_WBITS)
    compressed = deflate_obj.compress(file_content) + deflate_obj.flush()
    return compressed


def get_structure(game_version, scenario_version) -> dict:
    try:
        structure_file = open(f"versions/{game_version}/v{scenario_version}/structure.json", 'r')
    except FileNotFoundError:  # Unsupported version
        v = f"{game_version}:{scenario_version}"
        raise UnknownScenarioStructure(f"The version {v} is not supported by AoE2ScenarioParser. :(") from None

    structure = json.loads(structure_file.read())

    if "FileHeader" not in structure.keys():
        raise InvalidScenarioStructure(f"First piece in structure should always be FileHeader.")
    return structure


_header_structure: List[Type[AoE2FilePart]] = [
    FileHeaderPiece
]
_file_structure: List[Type[AoE2FilePart]] = [
    DataHeaderPiece,
    MessagesPiece,
    CinematicsPiece,
    BackgroundImagePiece,
    PlayerDataTwoPiece,
    GlobalVictoryPiece,
    DiplomacyPiece,
    OptionsPiece,
    MapPiece,
    UnitsPiece,
    TriggersPiece,
    FilesPiece,
]

# Define piece names
data_header_piece = "DataHeaderPiece"
messages_piece = "MessagesPiece"
cinematics_piece = "CinematicsPiece"
background_image_piece = "BackgroundImagePiece"
player_data_two_piece = "PlayerDataTwoPiece"
global_victory_piece = "GlobalVictoryPiece"
diplomacy_piece = "DiplomacyPiece"
options_piece = "OptionsPiece"
map_piece = "MapPiece"
units_piece = "UnitsPiece"
trigger_piece = "TriggersPiece"
files_piece = "FilesPiece"
