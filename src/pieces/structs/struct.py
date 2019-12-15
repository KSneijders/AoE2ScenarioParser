from src.helper.generator import create_generator
import src.pieces.scenario_piece as scenario_piece


class Struct(scenario_piece.ScenarioPiece):
    def __init__(self, parser, piece_type, retrievers, data=None):
        super().__init__(parser, piece_type, retrievers, data)

        if data is not None:
            gen = create_generator(data, 1)
            super().set_data_from_generator(gen)

    def _entry_to_string(self, name, data, datatype):
        return "\t\t\t" + name + ": " + data + " (" + datatype + ")\n"

    def _to_string(self):
        if self.piece_type in ("Terrain", "Unit"):
            return "."  # Recommended to keep as '.' due to the amount of tiles. (Tiny map = 14400)
        else:
            return super()._to_string()
