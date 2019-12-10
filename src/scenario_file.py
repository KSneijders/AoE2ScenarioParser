import zlib
from src.helper.generator import *
from src.helper.parser import Parser
import resources.settings as settings
from src.pieces.data_header import DataHeaderPiece
from src.pieces.file_header import FileHeaderPiece
from src.pieces.messagespiece import MessagesPiece


class AoE2Scenario:
    file = b''
    file_header = b''
    file_data = b''
    file_structure = [
        FileHeaderPiece,
        DataHeaderPiece,
        # MessagesPiece,
    ]

    def __init__(self, filename):
        print("Loading file: '" + filename + "'", end="")

        scenario = open("./../" + filename, "rb")
        self.file = scenario.read()
        scenario.seek(0)  # Reset file cursor to 0
        self.file_header = scenario.read(self._compute_header_length())
        self.file_data = zlib.decompress(scenario.read(), -zlib.MAX_WBITS)
        scenario.close()

        print(" .. .. .. .. File loaded!")

    def _compute_header_length(self):
        return Parser.calculate_length(
            self._create_file_generator(settings.runtime.get('chunk_size')),
            FileHeaderPiece.retrievers
        )

    def _create_file_generator(self, chunk_size):
        return create_generator(self.file, chunk_size)

    def create_header_generator(self, chunk_size):
        return create_generator(self.file_header, chunk_size)

    def create_data_generator(self, chunk_size):
        return create_generator(self.file_data, chunk_size)

    def write_data_progress(self):
        progress_length = 0
        generator = self.create_data_generator(settings.runtime.get('chunk_size'))

        for i in range(1, len(self.file_structure)):
            progress_length += Parser.calculate_length(generator, self.file_structure[i].retrievers)
            print(progress_length)

        file = open("./../results/progress.aoe2scenario", "wb")
        file.write(self.file_data[progress_length:])
        file.close()

    def write_file(self, datatype, write_in_bytes=True):
        file = open("./../results/generated.aoe2scenario", "wb" if write_in_bytes else "w")
        for t in datatype:
            if t == "f":
                file.write(self.file if write_in_bytes else _create_readable_hex_string(self.file.hex()))
            elif t == "h":
                file.write(self.file_header if write_in_bytes else _create_readable_hex_string(self.file_header.hex()))
            elif t == "d":
                file.write(self.file_data if write_in_bytes else _create_readable_hex_string(self.file_data.hex()))
        file.close()


def _create_readable_hex_string(string):
    return insert_char(insert_char(string, " ", 2), "\n", 48)


# Credits: gurney alex @ https://stackoverflow.com/a/2657733/7230293
def insert_char(string, char, every=64):
    return char.join(string[i:i+every] for i in range(0, len(string), every))