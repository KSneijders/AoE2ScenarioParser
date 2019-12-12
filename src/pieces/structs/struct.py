from src.helper.generator import create_generator
from src.pieces.scenario_piece import ScenarioPiece


class Struct(ScenarioPiece):
    def __init__(self, parser, piece_type, retrievers, data=None):
        super().__init__(parser, piece_type, retrievers, data)

        if data is not None:
            gen = create_generator(data, 1)
            super().set_data_from_generator(gen)

    def _entry_to_string(self, name, data, datatype):
        return "\t\t\t" + name + ": " + data + " (" + datatype + ")\n"

    def _to_string(self):
        if self.piece_type == "Terrain":
            return "."  # Recommended to keep as '.' due to the amount of tiles. (Tiny map = 14400)
        else:
            return super()._to_string()
