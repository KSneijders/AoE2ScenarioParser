import zlib
from src.helper.generator import *
from src.helper.parser import Parser
import resources.settings as settings
from src.pieces.file_header import FileHeaderPiece


class AoE2Scenario:
    file = b''
    file_header = b''
    file_data = b''

    def __init__(self, filename):
        print("Loading file: '" + filename + "'", end="")

        scenario = open("./../" + filename, "rb")
        self.file = scenario.read()
        scenario.seek(0)  # Reset file cursor to 0
        self.file_header = scenario.read(self._compute_header_length())
        self.file_data = zlib.decompress(scenario.read(), -zlib.MAX_WBITS)
        scenario.close()

        print(" .. .. .. .. File loaded!")

    def _create_file_generator(self, chunk_size):
        return create_file_generator(self.file, chunk_size)

    def _compute_header_length(self):
        return Parser.calculate_length(
            self._create_file_generator(settings.runtime.get('chunk_size')),
            FileHeaderPiece.data
        )

    def create_header_generator(self, chunk_size):
        return create_file_generator(self.file_header, chunk_size)

    def create_data_generator(self, chunk_size):
        return create_file_generator(self.file_data, chunk_size)

    def write_file(self, datatype, write_in_bytes=True):
        file = open("./../results/generated.aoe2scenario", "wb" if write_in_bytes else "w")
        for t in datatype:
            if t == "f":
                file.write(self.file if write_in_bytes else self.file.hex())
            elif t == "h":
                file.write(self.file_header if write_in_bytes else self.file_header.hex())
            elif t == "d":
                file.write(self.file_data if write_in_bytes else self.file_data.hex())
        file.close()
