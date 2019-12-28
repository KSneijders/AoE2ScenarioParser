import zlib
import src.helper.generator as generator
import src.helper.parser as parser
import resources.settings as settings
import collections

from src.aoe2_object_manager import AoE2ObjectManager
from src.helper.datatype import DataType
from src.helper.retriever import Retriever
from src.objects.file_header_obj import FileHeaderObject
from src.pieces.background_image import BackgroundImagePiece
from src.pieces.cinematics import CinematicsPiece
from src.pieces.data_header import DataHeaderPiece
from src.pieces.diplomacy import DiplomacyPiece
from src.pieces.disables import DisablesPiece
from src.pieces.file_header import FileHeaderPiece
from src.pieces.global_victory import GlobalVictoryPiece
from src.pieces.map import MapPiece
from src.pieces.messages import MessagesPiece
from src.pieces.player_data_two import PlayerDataTwoPiece
from src.pieces.triggers import TriggerPiece
from src.pieces.units import UnitsPiece


class AoE2Scenario:
    def __init__(self, filename):
        print("Loading file: '" + filename + "'", end="")

        scenario = open(filename, "rb")
        self.file = scenario.read()
        scenario.seek(0)  # Reset file cursor to 0
        self.file_header = scenario.read(self._compute_header_length())
        self.file_data = zlib.decompress(scenario.read(), -zlib.MAX_WBITS)
        scenario.close()

        print(" .. .. .. .. File loaded!")

        self.parser = parser.Parser()

        self.write_file("hd", write_in_bytes=False)

        self._read_file()

        # self._write_from_structure()

    def _read_file(self):
        self.parsed_header = collections.OrderedDict()
        self.parsed_data = collections.OrderedDict()
        header_generator = self._create_header_generator(settings.runtime.get("chunk_size"))
        data_generator = self._create_data_generator(settings.runtime.get("chunk_size"))

        for _ in header_structure:
            piece = _(self.parser)
            print("Reading", piece.piece_type + "...", end="")
            piece.set_data_from_generator(header_generator)
            self.parsed_header[type(piece).__name__] = piece
            print("...Done!")
            print(piece)

        for _ in file_structure:
            piece = _(self.parser)
            print("Reading", piece.piece_type + "...", end="")
            piece.set_data_from_generator(data_generator)
            self.parsed_data[type(piece).__name__] = piece
            print("...Done!")
            print(piece)

        suffix = b''
        try:
            while True:
                suffix += self.parser.retrieve_value(data_generator, Retriever("suffix data", DataType("1")))
        except StopIteration as e:
            print(e)
        finally:
            print("Suffix done", len(suffix))
            self.suffix = suffix

        print("File reading done successfully!")

        print(self.parsed_header.keys())
        print(self.parsed_data.keys())

        om = AoE2ObjectManager(self.parsed_header, self.parsed_data)

        # fho = FileHeaderObject()
        # fho.set_from_pieces(self.parsed_header['FileHeaderPiece'])
        # print(fho)

    def _write_from_structure(self, write_in_bytes=True):
        byte_header = b''
        byte_data = b''

        for key in self.parsed_header:
            for retriever in self.parsed_header[key].retrievers:
                byte_header += parser.retriever_to_bytes(retriever)

        for key in self.parsed_data:
            for retriever in self.parsed_data[key].retrievers:
                return_bytes = parser.retriever_to_bytes(retriever)
                byte_data += return_bytes

        # https://stackoverflow.com/questions/3122145/zlib-error-error-3-while-decompressing-incorrect-header-check/22310760#22310760
        deflate_obj = zlib.compressobj(9, zlib.DEFLATED, -zlib.MAX_WBITS)
        compressed = deflate_obj.compress(byte_data + self.suffix) + deflate_obj.flush()

        file = open(settings.file.get("output"), "wb" if write_in_bytes else "w")
        file.write(byte_header if write_in_bytes else _create_readable_hex_string(byte_header.hex()))
        file.write(compressed if write_in_bytes else _create_readable_hex_string(compressed.hex()))
        file.close()

    def write_file(self, datatype, write_in_bytes=True):
        file = open("./../results/generated_map_" + datatype + ".aoe2scenario", "wb" if write_in_bytes else "w")
        for t in datatype:
            if t == "f":
                file.write(self.file if write_in_bytes else _create_readable_hex_string(self.file.hex()))
            elif t == "h":
                file.write(self.file_header if write_in_bytes else _create_readable_hex_string(self.file_header.hex()))
            elif t == "d":
                file.write(self.file_data if write_in_bytes else _create_readable_hex_string(self.file_data.hex()))
        file.close()

    def _create_header_generator(self, chunk_size):
        return generator.create_generator(self.file_header, chunk_size)

    def _create_data_generator(self, chunk_size):
        return generator.create_generator(self.file_data, chunk_size)

    def _create_file_generator(self, chunk_size):
        return generator.create_generator(self.file, chunk_size)

    def _compute_header_length(self):
        return parser.calculate_length(
            self._create_file_generator(settings.runtime.get('chunk_size')),
            FileHeaderPiece(parser.Parser()).retrievers
        )


header_structure = [
    FileHeaderPiece
]
file_structure = [
    DataHeaderPiece,
    MessagesPiece,
    CinematicsPiece,
    BackgroundImagePiece,
    PlayerDataTwoPiece,
    GlobalVictoryPiece,
    DiplomacyPiece,
    DisablesPiece,
    MapPiece,
    UnitsPiece,
    TriggerPiece,
]


def _create_readable_hex_string(string):
    return insert_char(insert_char(string, " ", 2), "\n", 48)


# Credits: gurney alex @ https://stackoverflow.com/a/2657733/7230293
def insert_char(string, char, every=64):
    return char.join(string[i:i + every] for i in range(0, len(string), every))
