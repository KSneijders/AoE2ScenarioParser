import zlib
import collections

import AoE2ScenarioParser.helper.generator as generator
import AoE2ScenarioParser.helper.parser as parser
from AoE2ScenarioParser.aoe2_object_manager import AoE2ObjectManager
from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.helper import create_readable_hex_string
from AoE2ScenarioParser.helper.retriever import Retriever, find_retriever
from AoE2ScenarioParser.pieces.background_image import BackgroundImagePiece
from AoE2ScenarioParser.pieces.cinematics import CinematicsPiece
from AoE2ScenarioParser.pieces.data_header import DataHeaderPiece
from AoE2ScenarioParser.pieces.diplomacy import DiplomacyPiece
from AoE2ScenarioParser.pieces.options import OptionsPiece
from AoE2ScenarioParser.pieces.file_header import FileHeaderPiece
from AoE2ScenarioParser.pieces.global_victory import GlobalVictoryPiece
from AoE2ScenarioParser.pieces.map import MapPiece
from AoE2ScenarioParser.pieces.messages import MessagesPiece
from AoE2ScenarioParser.pieces.player_data_two import PlayerDataTwoPiece
from AoE2ScenarioParser.pieces.triggers import TriggerPiece
from AoE2ScenarioParser.pieces.units import UnitsPiece
from AoE2ScenarioParser.datasets import effect as effect_dataset
from AoE2ScenarioParser.datasets import condition as condition_dataset


class AoE2Scenario:
    def __init__(self, filename):
        print("\nLoading file: '" + filename + "'...")

        scenario = open(filename, "rb")
        self.file = scenario.read()
        scenario.seek(0)  # Reset file cursor to 0
        self.file_header = scenario.read(self._compute_header_length())
        self.file_data = zlib.decompress(scenario.read(), -zlib.MAX_WBITS)
        scenario.close()

        print("File loaded.")

        self.parser = parser.Parser()
        self._read_file()

    def _read_file(self):
        print("\nFile reading started...")
        self.parsed_header = collections.OrderedDict()
        self.parsed_data = collections.OrderedDict()
        header_generator = self._create_header_generator(1)
        data_generator = self._create_data_generator(1)

        structures = [_header_structure, _file_structure]
        structure_generators = [header_generator, data_generator]
        structure_parsed = [self.parsed_header, self.parsed_data]

        for index, structure in enumerate(structures):
            for piece_object in structure:
                piece = piece_object(self.parser)
                print("Reading", piece.piece_type + "...")
                piece.set_data_from_generator(structure_generators[index])
                structure_parsed[index][type(piece).__name__] = piece
                print("Reading", piece.piece_type, "finished successfully.")

        suffix = b''
        try:
            while True:
                suffix += self.parser.retrieve_value(data_generator, Retriever("suffix data", DataType("1")))
        except StopIteration as e:
            # print(e)
            pass
        finally:
            # print("Suffix done", len(suffix))
            self.suffix = suffix

        print("File reading finished successfully.")

        self.object_manager = AoE2ObjectManager(self.parsed_header, self.parsed_data)

    def write_to_file(self, filename):
        self._write_from_structure(filename)

    def _write_from_structure(self, filename, write_in_bytes=True):
        self.object_manager.reconstruct()
        print("\nFile writing from structure started...")
        byte_header = b''
        byte_data = b''

        for key in self.parsed_header:
            for retriever in self.parsed_header[key].retrievers:
                byte_header += parser.retriever_to_bytes(retriever)

        for key in self.parsed_data:
            for retriever in self.parsed_data[key].retrievers:
                try:
                    byte_data += parser.retriever_to_bytes(retriever)
                except AttributeError:
                    print(key, retriever)

        # https://stackoverflow.com/questions/3122145/zlib-error-error-3-while-decompressing-incorrect-header-check/22310760#22310760
        deflate_obj = zlib.compressobj(9, zlib.DEFLATED, -zlib.MAX_WBITS)
        compressed = deflate_obj.compress(byte_data + self.suffix) + deflate_obj.flush()

        file = open(filename, "wb" if write_in_bytes else "w")
        file.write(byte_header if write_in_bytes else create_readable_hex_string(byte_header.hex()))
        file.write(compressed if write_in_bytes else create_readable_hex_string(compressed.hex()))
        file.close()
        print("File writing finished successfully.")

    def write_file(self, datatype, write_in_bytes=True):
        print("File writing from source started with attributes " + datatype + "...")
        file = open("./../results/generated_map_" + datatype + ".aoe2scenario", "wb" if write_in_bytes else "w")
        for t in datatype:
            if t == "f":
                file.write(self.file if write_in_bytes else create_readable_hex_string(self.file.hex()))
            elif t == "h":
                file.write(self.file_header if write_in_bytes else create_readable_hex_string(self.file_header.hex()))
            elif t == "d":
                file.write(self.file_data if write_in_bytes else create_readable_hex_string(self.file_data.hex()))
        file.close()
        print("File writing finished successfully.")

    def _create_header_generator(self, chunk_size):
        return generator.create_generator(self.file_header, chunk_size)

    def _create_data_generator(self, chunk_size):
        return generator.create_generator(self.file_data, chunk_size)

    def _create_file_generator(self, chunk_size):
        return generator.create_generator(self.file, chunk_size)

    def _compute_header_length(self):
        return parser.calculate_length(
            self._create_file_generator(1),
            FileHeaderPiece(parser.Parser()).retrievers
        )

    def _log_all_data_keys(self):
        """ Used for debugging. """
        print("FileHeader:")
        print(self.parsed_header.keys())
        print("DataHeader:")
        print("odict_keys([")
        for x in self.parsed_data.keys():
            print("\t'" + x + "'")
        print("])")

    def _log_effect_dataset(self):
        """ Used for debugging - Only reads One Trigger. """
        trigger_data = find_retriever(self.parsed_data['TriggerPiece'].retrievers, "Trigger data").data
        effects = parser.listify(find_retriever(trigger_data.retrievers, "Effect data").data)

        for effect in effects:
            for retriever in effect.retrievers:
                if retriever.data != -1 and \
                        retriever.data != [] and \
                        retriever.data != "" and \
                        retriever.data != " " and \
                        retriever.name != "Check, (46)":
                    if retriever.name == "Effect type":
                        print("],\n" + str(retriever.data) + ": [")
                    # print(retriever)
                    print("\t\"" + str(effect_dataset.naming_conversion[retriever.name]) + "\",")
        print("]\n")

    def _log_condition_dataset(self):
        """ Used for debugging - Only reads One Trigger. """
        trigger_data = find_retriever(self.parsed_data['TriggerPiece'].retrievers, "Trigger data").data
        conditions = parser.listify(find_retriever(trigger_data.retrievers, "Condition data").data)

        for condition in conditions:
            for retriever in condition.retrievers:
                if retriever.data != -1 and \
                        retriever.data != [] and \
                        retriever.data != "" and \
                        retriever.data != " " and \
                        retriever.name != "Check, (21)":
                    # print(retriever)
                    if retriever.name == "Condition type":
                        print("],\n" + str(retriever.data) + ": [")
                    print("\t\"" + str(condition_dataset.naming_conversion[retriever.name]) + "\",")
        print("]\n")


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
