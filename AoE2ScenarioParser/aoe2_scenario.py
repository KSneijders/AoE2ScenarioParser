import json
import zlib
from collections import OrderedDict
from typing import List, Type

from AoE2ScenarioParser.helper import generators, helper, parser
from AoE2ScenarioParser.helper.exceptions import InvalidScenarioStructure, UnknownScenarioStructure
from AoE2ScenarioParser.helper.helper import create_textual_hex, SimpleLogger
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
        self.scenario_version = "<<Unknown>>"
        self.game_version = "<<Unknown>>"
        self.structure = {}
        self.pieces: OrderedDict[str, AoE2FilePart] = OrderedDict()
        self._object_manager = None

        # Used in debug functions
        self._file_header = None
        self._decompressed_file_data = None
        self._file = None

    @classmethod
    def from_file_poc(cls, filename):
        print(f"\nSelected file: '{filename}'")
        file_content = read_file(filename)

        scenario = cls()
        scenario.read_mode = "from_file"
        scenario.game_version = "DE"
        scenario.scenario_version = get_file_version(file_content)

        # Log game and scenario version
        print("\n############### Attributes ###############")
        print(f">>> Game version: '{scenario.game_version}'")
        print(f">>> Scenario version: {scenario.scenario_version}")
        print("##########################################")

        helper.rprint(f"\nLoading scenario structure...")
        scenario.structure = get_structure_by_scenario(scenario)
        helper.rprint(f"Loading scenario structure finished successfully.", final=True)

        scenario._initialise(file_content)

        return scenario

    def add_to_pieces(self, piece):
        self.pieces[piece.name] = piece

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
        binary += compress_bytes(b''.join(binary_list_to_be_compressed))

        file = open(filename, "wb")
        file.write(binary)
        file.close()

    def _get_file_part_data(self, file_part):
        helper.rprint(f"\t🔄 Reconstructing {file_part.name}...")
        value = file_part.get_data_as_bytes()
        helper.rprint(f"\t✔ {file_part.name}", final=True)
        return value

    def _initialise_file_part(self, name, generator):
        helper.rprint(f"\t🔄 Parsing {name}...")
        piece = self._parse_file_part(name)
        helper.rprint(f"\t🔄 Setting {name} data...")
        piece.set_data_from_generator(generator, self.pieces)
        helper.rprint(f"\t✔ {name}", final=True)
        return piece

    def _initialise(self, file_content):
        helper.rprint("Parsing scenario file...", final=True)

        raw_file_generator = generators.create_generator(file_content)

        header = self._initialise_file_part('FileHeader', raw_file_generator)
        self.add_to_pieces(header)

        # Decompress the file (starting from where header ended)
        decompressed_file_data = decompress_bytes(file_content[header.byte_length:])

        scenario_data_generator = generators.create_generator(decompressed_file_data)
        for piece_name in self.structure.keys():
            if piece_name == "FileHeader":
                continue
            try:
                piece = self._initialise_file_part(piece_name, scenario_data_generator)
                self.add_to_pieces(piece)
            except (ValueError, TypeError) as e:
                print(f"\n[{e.__class__.__name__}] AoE2Scenario.parse_file: \n\tPiece: {piece_name}\n")
                self.write_error_file(generator_for_trail=scenario_data_generator)
                raise e

        helper.rprint(f"Parsing scenario file finished successfully.", final=True)

    def _parse_file_part(self, name):
        return AoE2FilePart.from_structure(name, self.structure.get(name))

    def write_error_file(self, filename="error_file", generator_for_trail=None):
        self._debug_byte_structure_to_file(filename=filename, generator_for_trail=generator_for_trail)

    def ___write_from_structure(self, filename, write_in_bytes=True, compress=True, commit_on_write=True):
        if hasattr(self, '_object_manager') and commit_on_write:
            self._object_manager.reconstruct(log_reconstructing=log_reconstructing)
        lgr = SimpleLogger(log_writing)
        lgr.print("\nFile writing from structure started...")

        pieces = OrderedDict(**self._parsed_header, **self._parsed_data)

        byte_header_list = []
        byte_data_list = []
        for key in self._parsed_header:
            lgr.print("\twriting " + key + "...", replace=True)
            for retriever in self._parsed_header[key].retrievers:
                byte_header_list.append(parser.retriever_to_bytes(retriever, pieces))
            lgr.print("\twriting " + key + " finished successfully.", replace=True)
            lgr.print()

        for key in self._parsed_data:
            lgr.print("\twriting " + key + "...", replace=True)
            for retriever in self._parsed_data[key].retrievers:
                try:
                    byte_data_list.append(parser.retriever_to_bytes(retriever, pieces))
                except AttributeError as e:
                    print("AttributeError occurred while writing '" + key + "' > '" + retriever.name + "'")
                    print("\n\n\nAn error occurred. Writing failed.")
                    raise e
            lgr.print("\twriting " + key + " finished successfully.", replace=True)
            lgr.print()

        file = open(filename, "wb" if write_in_bytes else "w")

        byte_header = b''.join(byte_header_list)
        byte_data = b''.join(byte_data_list)

        file.write(byte_header if write_in_bytes else create_textual_hex(byte_header.hex()))
        if compress:
            lgr.print("\tCompressing...", replace=True)
            # https://stackoverflow.com/questions/3122145/zlib-error-error-3-while-decompressing-incorrect-header-check/22310760#22310760
            deflate_obj = zlib.compressobj(9, zlib.DEFLATED, -zlib.MAX_WBITS)
            compressed = deflate_obj.compress(b''.join(byte_data_list)) + deflate_obj.flush()
            file.write(compressed if write_in_bytes else create_textual_hex(compressed.hex()))
            lgr.print("\tCompressing finished successfully.", replace=True)
            lgr.print()
        else:
            file.write(byte_data if write_in_bytes else create_textual_hex(byte_data.hex()))

        file.close()
        lgr.print("File writing finished successfully.")

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

    def _debug_byte_structure_to_file(self, filename, generator_for_trail=None, log_debug_write=True, commit=False):
        """ Used for debugging - Writes structure from read file to the filesystem in a easily readable manner. """
        if commit and hasattr(self, '_object_manager'):
            # self._object_manager.reconstruct(log_debug_write)
            self._write_from_structure(filename, log_writing=log_debug_write, log_reconstructing=log_debug_write)

        lgr = SimpleLogger(log_debug_write)

        pieces = OrderedDict(**self._parsed_header, **self._parsed_data)
        lgr.print("\nWriting structure to file...")
        with open(filename, 'w', encoding="utf-8") as output_file:
            result = []
            for key in self._parsed_header:
                lgr.print("\tWriting " + key + "...", replace=True)
                result.append(self._parsed_header[key].get_byte_structure_as_string(pieces))
                lgr.print("\tWriting " + key + " finished successfully.", replace=True)
                lgr.print()
            for key in self._parsed_data:
                if key == "MapPiece":
                    continue
                lgr.print("\tWriting " + key + "...", replace=True)
                result.append(self._parsed_data[key].get_byte_structure_as_string(pieces))
                lgr.print("\tWriting " + key + " finished successfully.", replace=True)
                lgr.print()

            if generator_for_trail is not None:
                lgr.print("\tWriting trail...", replace=True)
                trail_length = -1  # -1 == inf
                try:
                    trail = b''
                    i = 0
                    while i != trail_length:
                        trail += generators.repeat_generator(
                            generator=generator_for_trail,
                            run_times=1,
                            intended_stop_iteration=True,
                            return_bytes=True
                        )
                        i += 1
                except StopIteration:
                    pass  # Expected, if trail is not present or shorter than {trail_length} bytes
                if i != 0:
                    i += 1
                if i == trail_length:
                    i = str(i) + '+'
                if trail_length == -1:
                    trail_length = i
                result.append(f"\n\n{'#' * 27} TRAIL ({i}/{trail_length})\n\n")
                result.append(helper.create_textual_hex(trail.hex(), space_distance=2, enter_distance=24))
                lgr.print("\tWriting trail finished successfully.", replace=True)
                lgr.print()

            output_file.write(''.join(result))
            output_file.close()
        lgr.print("Writing structure to file finished successfully.")


def read_file(filename):
    helper.rprint("Reading scenario file...")
    with open(filename, "rb") as f:
        file_content = f.read()
    helper.rprint("Reading scenario file finished successfully.", final=True)
    return file_content


def get_file_version(file_content):
    return file_content[:4].decode('ASCII')


def decompress_bytes(file_content):
    return zlib.decompress(file_content, -zlib.MAX_WBITS)


def compress_bytes(file_content):
    # https://stackoverflow.com/questions/3122145/zlib-error-error-3-while-decompressing-incorrect-header-check/22310760#22310760
    deflate_obj = zlib.compressobj(9, zlib.DEFLATED, -zlib.MAX_WBITS)
    compressed = deflate_obj.compress(file_content) + deflate_obj.flush()
    return compressed


def get_structure_by_scenario(scenario: AoE2Scenario):
    return get_structure(scenario.game_version, scenario.scenario_version)


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
