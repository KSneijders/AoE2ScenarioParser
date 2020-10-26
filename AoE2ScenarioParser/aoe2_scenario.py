import collections
import time
import zlib

from AoE2ScenarioParser.helper import generator
from AoE2ScenarioParser.helper import parser
from AoE2ScenarioParser.helper.helper import create_textual_hex, SimpleLogger
from AoE2ScenarioParser.helper.retriever import get_retriever_by_name
from AoE2ScenarioParser.objects.aoe2_object_manager import AoE2ObjectManager
from AoE2ScenarioParser.objects.map_obj import MapObject
from AoE2ScenarioParser.objects.triggers_obj import TriggersObject
from AoE2ScenarioParser.objects.units_obj import UnitsObject
from AoE2ScenarioParser.pieces.background_image import BackgroundImagePiece
from AoE2ScenarioParser.pieces.cinematics import CinematicsPiece
from AoE2ScenarioParser.pieces.data_header import DataHeaderPiece
from AoE2ScenarioParser.pieces.diplomacy import DiplomacyPiece
from AoE2ScenarioParser.pieces.file_header import FileHeaderPiece
from AoE2ScenarioParser.pieces.global_victory import GlobalVictoryPiece
from AoE2ScenarioParser.pieces.map import MapPiece
from AoE2ScenarioParser.pieces.messages import MessagesPiece
from AoE2ScenarioParser.pieces.options import OptionsPiece
from AoE2ScenarioParser.pieces.player_data_two import PlayerDataTwoPiece
from AoE2ScenarioParser.pieces.triggers import TriggerPiece
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
        self.parser = None
        self._file_header = None
        self._file_data = None
        self._file = None

    @classmethod
    def from_file(cls, filename, log_reading=True, log_parsing=False):
        scenario = cls()

        print("\nPreparing & Loading file: '" + filename + "'...")
        scenario_file = open(filename, "rb")
        scenario._file = scenario_file.read()
        scenario_file.seek(0)  # Reset file cursor to 0

        scenario._file_header = scenario_file.read(scenario._compute_header_length())
        scenario._file_data = zlib.decompress(scenario_file.read(), -zlib.MAX_WBITS)

        scenario_file.close()
        print("File prepared and loaded.")

        scenario.parser = parser.Parser()
        scenario._read_file(log_reading=log_reading)
        scenario._object_manager = AoE2ObjectManager(scenario._parsed_header, scenario._parsed_data,
                                                     log_parsing=log_parsing)
        return scenario

    @classmethod
    def create(cls, log_creating=True, log_parsing=False):
        scenario = cls()

        lgr = SimpleLogger(log_creating)
        lgr.print("\nFile creation started...")

        scenario.parser = parser.Parser()
        scenario._parsed_header = collections.OrderedDict()
        scenario._parsed_data = collections.OrderedDict()

        for piece in _header_structure:
            piece_name = piece.__name__
            lgr.print("\tCreating " + piece_name + "...", replace_line=True)
            scenario._parsed_header[piece_name] = piece(scenario.parser, data=list(piece.defaults().values()))
            lgr.print("\tCreating " + piece_name + " finished successfully.", replace_line=True)
            lgr.print()
        for piece in _file_structure:
            piece_name = piece.__name__
            lgr.print("\tCreating " + piece_name + "...", replace_line=True)
            scenario._parsed_data[piece_name] = piece(scenario.parser, data=list(piece.defaults().values()))
            lgr.print("\tCreating " + piece_name + " finished successfully.", replace_line=True)
            lgr.print()
        lgr.print("\nFile creation finished successfully")

        scenario._object_manager = AoE2ObjectManager(scenario._parsed_header, scenario._parsed_data,
                                                     log_parsing=log_parsing)
        return scenario

    def _read_file(self, log_reading):
        lgr = SimpleLogger(log_reading)
        lgr.print("\nFile reading started...")

        self._parsed_header = collections.OrderedDict()
        self._parsed_data = collections.OrderedDict()
        header_generator = self._create_header_generator(1)
        data_generator = self._create_data_generator(1)

        current_piece = ""
        try:
            for piece_object in _header_structure:
                # Rerender pieces dict each time - changes constantly
                pieces = collections.OrderedDict(**self._parsed_header, **self._parsed_data)
                piece = piece_object(self.parser)
                piece_name = type(piece).__name__
                self._parsed_header[piece_name] = piece
                current_piece = piece_name

                lgr.print("\tReading " + piece_name + "...", replace_line=True)
                piece.set_data_from_generator(header_generator, pieces)
                lgr.print("\tReading " + piece_name + " finished successfully.", replace_line=True)
                lgr.print()

            for piece_object in _file_structure:
                # Rerender pieces dict each time - changes constantly
                pieces = collections.OrderedDict(**self._parsed_header, **self._parsed_data)
                piece = piece_object(self.parser)
                piece_name = type(piece).__name__
                self._parsed_data[piece_name] = piece
                current_piece = piece_name

                lgr.print("\tReading " + piece_name + "...", replace_line=True)
                piece.set_data_from_generator(data_generator, pieces)
                lgr.print("\tReading " + piece_name + " finished successfully.", replace_line=True)
                lgr.print()
        except StopIteration as e:
            print(f"\n[StopIteration] [EXIT] AoE2Scenario._read_file: \n\tPiece: {current_piece}\n")
            print("Writing ErrorFile...")
            self._debug_byte_structure_to_file("../ErrorFile", log_debug_write=False)
            time.sleep(1)
            print("ErrorFile written. \n\n\n ------------------------ STACK TRACE ------------------------\n\n")
            time.sleep(1)
            raise StopIteration(e)
        lgr.print("File reading finished successfully.")

    def write_to_file(self, filename, no_commit=False, log_writing=True, log_reconstructing=False):
        self._write_from_structure(filename, log_writing=log_writing, log_reconstructing=log_reconstructing)

    def _write_from_structure(self,
                              filename,
                              write_in_bytes=True,
                              compress=True,
                              log_writing=True,
                              log_reconstructing=False):
        if hasattr(self, '_object_manager'):
            self._object_manager.reconstruct(log_reconstructing=log_reconstructing)
        lgr = SimpleLogger(log_writing)
        lgr.print("\nFile writing from structure started...")

        byte_header = b''
        byte_data = b''

        for key in self._parsed_header:
            lgr.print("\twriting " + key + "...", replace_line=True)
            for retriever in self._parsed_header[key].retrievers:
                byte_header += parser.retriever_to_bytes(retriever)
            lgr.print("\twriting " + key + " finished successfully.", replace_line=True)
            lgr.print()

        for key in self._parsed_data:
            lgr.print("\twriting " + key + "...", replace_line=True)
            for retriever in self._parsed_data[key].retrievers:
                try:
                    byte_data += parser.retriever_to_bytes(retriever)
                except AttributeError as e:
                    print("AttributeError occurred while writing '" + key + "' > '" + retriever.name + "'")
                    print("\n\n\nAn error occurred. Writing failed.")
                    raise e
            lgr.print("\twriting " + key + " finished successfully.", replace_line=True)
            lgr.print()

        file = open(filename, "wb" if write_in_bytes else "w")
        file.write(byte_header if write_in_bytes else create_textual_hex(byte_header.hex()))

        if compress:
            lgr.print("\tCompressing...", replace_line=True)
            # https://stackoverflow.com/questions/3122145/zlib-error-error-3-while-decompressing-incorrect-header-check/22310760#22310760
            deflate_obj = zlib.compressobj(9, zlib.DEFLATED, -zlib.MAX_WBITS)
            compressed = deflate_obj.compress(byte_data) + deflate_obj.flush()
            file.write(compressed if write_in_bytes else create_textual_hex(compressed.hex()))
            lgr.print("\tCompressing finished successfully.", replace_line=True)
            lgr.print()
        else:
            file.write(byte_data if write_in_bytes else create_textual_hex(byte_data.hex()))

        file.close()
        lgr.print("File writing finished successfully.")

    def _create_header_generator(self, chunk_size):
        return generator.create_generator(self._file_header, chunk_size)

    def _create_data_generator(self, chunk_size):
        return generator.create_generator(self._file_data, chunk_size)

    def _create_file_generator(self, chunk_size):
        return generator.create_generator(self._file, chunk_size)

    def _compute_header_length(self):
        return parser.calculate_length(
            self._create_file_generator(1),
            FileHeaderPiece(parser.Parser()).retrievers
        )

    """ #############################################
    ################ Debug functions ################
    ############################################# """

    def _debug_log_effect_dataset(self):
        """ Used for debugging - Only reads One Trigger. """
        trigger_data = get_retriever_by_name(self._parsed_data['TriggerPiece'].retrievers, "Trigger data").data
        effects = get_retriever_by_name(trigger_data.retrievers, "Effect data").data

        for effect in effects:
            for retriever in effect.retrievers:
                # if retriever.data != -1 and \
                #         retriever.data != [] and \
                #         retriever.data != "" and \
                #         retriever.data != " " and \
                #         retriever.name != "static_value_46":
                if retriever.name != "static_value_46":
                    if retriever.name == "effect_type":
                        print("},\n" + str(retriever.data) + ": {")
                    print("\t\"" + retriever.name + "\": " +
                          (str(retriever.data) if type(retriever.data) is not str else "\"" + retriever.data + "\"")
                          + ",")
        print("}\n")

    def _debug_log_condition_dataset(self):
        """ Used for debugging - Only reads One Trigger. """
        trigger_data = get_retriever_by_name(self._parsed_data['TriggerPiece'].retrievers, "Trigger data").data
        conditions = get_retriever_by_name(trigger_data.retrievers, "Condition data").data

        for condition in conditions:
            for retriever in condition.retrievers:
                # if retriever.data != -1 and \
                #         retriever.data != [] and \
                #         retriever.data != "" and \
                #         retriever.data != " " and \
                #         retriever.name != "static_value_21":
                if retriever.name != "static_value_21":
                    if retriever.name == "condition_type":
                        print("},\n" + str(retriever.data) + ": {")
                    print("\t\"" + retriever.name + "\": " +
                          (str(retriever.data) if type(retriever.data) is not str else "\"" + retriever.data + "\"")
                          + ",")
        print("}\n")

    def _debug_write_from_source(self, filename, datatype, write_in_bytes=True):
        """This function is used as a test debugging writing. It writes parts of the read file to the filesystem."""
        print("File writing from source started with attributes " + datatype + "...")
        file = open(filename, "wb" if write_in_bytes else "w")
        for t in datatype:
            if t == "f":
                file.write(self._file if write_in_bytes else create_textual_hex(self._file.hex()))
            elif t == "h":
                file.write(self._file_header if write_in_bytes else create_textual_hex(self._file_header.hex()))
            elif t == "d":
                file.write(self._file_data if write_in_bytes else create_textual_hex(self._file_data.hex()))
        file.close()
        print("File writing finished successfully.")

    def _debug_byte_structure_to_file(self, filename, log_debug_write=True):
        """ Used for debugging - Writes structure from read file to the filesystem in a easily readable manner. """
        lgr = SimpleLogger(log_debug_write)

        lgr.print("\nWriting structure to file...")
        with open(filename, 'w') as output_file:
            result = ""
            for key in self._parsed_header:
                lgr.print("\tWriting " + key + "...", replace_line=True)
                result += self._parsed_header[key].get_byte_structure_as_string()
                lgr.print("\tWriting " + key + " finished successfully.", replace_line=True)
                lgr.print()
            for key in self._parsed_data:
                lgr.print("\tWriting " + key + "...", replace_line=True)
                result += self._parsed_data[key].get_byte_structure_as_string()
                lgr.print("\tWriting " + key + " finished successfully.", replace_line=True)
                lgr.print()

            output_file.write(result)
            output_file.close()
        lgr.print("Writing structure to file finished successfully.")


_header_structure = [
    FileHeaderPiece
]
_file_structure = [
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
    TriggerPiece,
]
