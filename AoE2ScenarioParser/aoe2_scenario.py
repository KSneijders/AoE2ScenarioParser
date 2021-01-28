import json
import time
import zlib
from collections import OrderedDict
from typing import List, Type

from AoE2ScenarioParser.helper import generator, helper, parser
from AoE2ScenarioParser.helper.exceptions import InvalidScenarioStructure, UnknownScenarioStructure
from AoE2ScenarioParser.helper.helper import create_textual_hex, SimpleLogger
from AoE2ScenarioParser.objects.aoe2_object_manager import AoE2ObjectManager
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
        self.pieces = OrderedDict()
        self._object_manager = None

        # Used in debug functions
        self._file_header = None
        self._decompressed_file_data = None
        self._file = None

    # @classmethod
    # def from_file(cls, filename, log_reading=True, log_parsing=True):
    #     scenario = cls()
    #     scenario.read_mode = "from_file"
    #
    #     print("\nPreparing & Loading file: '" + filename + "'...")
    #     scenario_file = open(filename, "rb")
    #     scenario._file = scenario_file.read()
    #     scenario_file.seek(0)  # Reset file cursor to 0
    #
    #     scenario._file_header = scenario_file.read(scenario._compute_header_length())
    #     scenario._decompressed_file_data = zlib.decompress(scenario_file.read(), -zlib.MAX_WBITS)
    #
    #     scenario_file.close()
    #     print("File prepared and loaded.")
    #
    #     scenario._read_file(log_reading=log_reading)
    #     scenario._object_manager = AoE2ObjectManager(
    #         scenario._parsed_header,
    #         scenario._parsed_data,
    #         log_parsing=log_parsing
    #     )

    @classmethod
    def from_file_poc(cls, filename, log_reading=True, log_parsing=True):
        print(f"\nPreparing & Loading file: '{filename}'...")

        file_content = read_file(filename)

        scenario = cls()
        scenario.read_mode = "from_file"
        scenario.game_version = "DE"
        scenario.scenario_version = get_file_version(file_content)

        # Log game and scenario version
        print(f">>> Game version: {scenario.game_version}")
        print(f">>> Scenario version: {scenario.scenario_version}")

        helper.cprint(f"Loading scenario structure...", replace_line=True)
        try:
            structure = get_structure_by_scenario(scenario)
        except FileNotFoundError as e:  # Unsupported version
            v = f"{scenario.game_version}:{scenario.scenario_version}"
            raise UnknownScenarioStructure(f"The version {v} is not supported by AoE2ScenarioParser. :(") from None
        helper.cprint(f"Loading scenario structure finished successfully", replace_line=True, last_replace_line=True)

        print(f"\n Reading scenario...")
        helper.cprint("\tReading FileHeader...", replace_line=True)
        # Read and init header
        header = AoE2FilePart.from_structure('FileHeader', structure.get('FileHeader'))
        scenario.add_to_pieces(header)
        header.set_data_from_generator(generator.create_generator(file_content), scenario.pieces)
        helper.cprint("\tReading FileHeader finished successfully", replace_line=True, last_replace_line=True)

        # Todo: Refactor _debug_byte_structure_to_file so it works without these params
        scenario._parsed_header = {"FileHeaderPiece": header}
        scenario._parsed_data = scenario.pieces

        # Decompressed the file (starting from where header ended)
        decompressed_file_data = decompress_file_data(file_content, header.byte_length)

        lgr = SimpleLogger(should_log=log_reading)

        file_generator = generator.create_generator(decompressed_file_data)
        for piece_name in structure.keys():
            if piece_name == "FileHeader":
                continue
            try:
                lgr.print("\tReading " + piece_name + "...", replace_line=True)
                piece = AoE2FilePart.from_structure(piece_name, structure.get(piece_name))
                scenario.add_to_pieces(piece)
                piece.set_data_from_generator(file_generator, scenario.pieces)
                lgr.print("\tReading " + piece_name + " finished successfully.",
                          replace_line=True, last_replace_line=True)
            except (ValueError, TypeError) as e:
                print(f"\n[{e.__class__.__name__}] [EXIT] AoE2Scenario._read_file: \n\tPiece: {piece_name}\n")
                print("Writing ErrorFile...")
                scenario._debug_byte_structure_to_file(
                    filename="../ErrorFile",
                    generator_for_trail=file_generator,
                    log_debug_write=True
                )
                raise e

        helper.cprint(f"Reading scenario finished successfully", replace_line=True, last_replace_line=True)

        return scenario

    def add_to_pieces(self, piece):
        self.pieces[piece.name] = piece

    @classmethod
    def create_default(cls, log_creating=True, log_parsing=False):
        scenario = cls()
        scenario.read_mode = "create_default"

        lgr = SimpleLogger(log_creating)
        lgr.print("\nFile creation started...")

        scenario._parsed_header = OrderedDict()
        scenario._parsed_data = OrderedDict()
        pieces = OrderedDict(**scenario._parsed_header, **scenario._parsed_data)

        for piece in _header_structure:
            piece_name = piece.__name__
            lgr.print("\tCreating " + piece_name + "...", replace_line=True)
            scenario._parsed_header[piece_name] = piece(data=list(piece.defaults(pieces).values()), pieces=pieces)
            lgr.print("\tCreating " + piece_name + " finished successfully.", replace_line=True)
            lgr.print()
        for piece in _file_structure:
            pieces = OrderedDict(**scenario._parsed_header, **scenario._parsed_data)
            piece_name = piece.__name__
            lgr.print("\tCreating " + piece_name + "...", replace_line=True)
            scenario._parsed_data[piece_name] = piece(
                data=list(piece.defaults(pieces).values()),
                pieces=pieces
            )
            lgr.print("\tCreating " + piece_name + " finished successfully.", replace_line=True)
            lgr.print()
        lgr.print("File creation finished successfully.")

        scenario._object_manager = AoE2ObjectManager(scenario._parsed_header, scenario._parsed_data,
                                                     log_parsing=log_parsing)
        return scenario

    def _read_file(self, log_reading):
        lgr = SimpleLogger(log_reading)
        lgr.print("\nFile reading started...")

        self._parsed_header = OrderedDict()
        self._parsed_data = OrderedDict()
        header_generator = self._create_header_generator(1)
        data_generator = self._create_data_generator(1)

        current_piece = ""
        try:
            for piece_object in _header_structure:
                # Rerender pieces dict each time - changes constantly
                pieces = OrderedDict(**self._parsed_header, **self._parsed_data)
                piece = piece_object()
                piece_name = type(piece).__name__
                self._parsed_header[piece_name] = piece
                current_piece = piece_name

                lgr.print("\tReading " + piece_name + "...", replace_line=True)
                piece.set_data_from_generator(header_generator, pieces)
                lgr.print("\tReading " + piece_name + " finished successfully.", replace_line=True)
                lgr.print()

            for piece_object in _file_structure:
                # Rerender pieces dict each time - changes constantly
                pieces = OrderedDict(**self._parsed_header, **self._parsed_data)
                piece = piece_object()
                piece_name = type(piece).__name__
                self._parsed_data[piece_name] = piece
                current_piece = piece_name

                lgr.print("\tReading " + piece_name + "...", replace_line=True)
                piece.set_data_from_generator(data_generator, pieces)
                lgr.print("\tReading " + piece_name + " finished successfully.", replace_line=True)
                lgr.print()
        except Exception as e:
            print(f"\n[{e.__class__.__name__}] [EXIT] AoE2Scenario._read_file: \n\tPiece: {current_piece}\n")
            print("Writing ErrorFile...")
            self._debug_byte_structure_to_file(
                filename="../ErrorFile",
                generator_for_trail=data_generator,
                log_debug_write=True
            )
            time.sleep(1)
            print("\nErrorFile written. \n\n\n ------------------------ STACK TRACE ------------------------\n\n")
            time.sleep(1)
            raise e
        lgr.print("File reading finished successfully.")

    def write_to_file(self, filename, commit_on_write=True, log_writing=True, log_reconstructing=True):
        self._write_from_structure(
            filename,
            log_writing=log_writing,
            log_reconstructing=log_reconstructing,
            commit_on_write=commit_on_write,
        )

    def _write_from_structure(self,
                              filename,
                              write_in_bytes=True,
                              compress=True,
                              commit_on_write=True,
                              log_writing=True,
                              log_reconstructing=True):
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

    def _create_header_generator(self, chunk_size):
        return generator.create_advanced_generator(self._file_header, chunk_size)

    def _create_data_generator(self, chunk_size):
        return generator.create_advanced_generator(self._decompressed_file_data, chunk_size)

    def _create_file_generator(self, chunk_size):
        return generator.create_advanced_generator(self._file, chunk_size)

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
                        trail += generator.repeat_generator(
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
    scenario_file = open(filename, "rb")
    file_content = scenario_file.read()
    scenario_file.close()
    return file_content


def get_file_version(file_content):
    return file_content[:4].decode('ASCII')


def decompress_file_data(file_content, header_length):
    return zlib.decompress(file_content[header_length:], -zlib.MAX_WBITS)


def get_structure_by_scenario(scenario: AoE2Scenario) -> dict:
    structure = json.loads(
        open(f"versions/{scenario.game_version}/v{scenario.scenario_version}/structure.json", 'r').read()
    )

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
