from abc import ABC

from AoE2ScenarioParser.helper.generator import create_advanced_generator
from AoE2ScenarioParser.pieces.aoe2_piece import AoE2Piece


class AoE2Struct(AoE2Piece, ABC):
    def __init__(self, piece_type, retrievers, data=None, pieces=None):
        super().__init__(piece_type, retrievers, data, pieces)

        if data and parser_obj:
            gen = create_advanced_generator(data, 1)
            super().set_data_from_generator(gen)

    def _entry_to_string(self, name, data, datatype):
        return "\t\t\t" + name + ": " + data + " (" + datatype + ")\n"

    def get_header_string(self):
        return "############ " + self.piece_type + " ############  [STRUCT]"

    def __str__(self):
        """ Remove Terrain and EyeCandy Units from the __str__ representation. As it'd mostly be considered spam. """
        if self.piece_type in ["asd"]:  # Terrain
            return "."  # Recommended to keep as '.' due to the amount of tiles in a map (Tiny map = 14400) or units.
        elif self.piece_type in ["Unit"]:
            if self.retrievers[4].data == 1358:  # Eye Candy (eg. Fake plants)
                return "."
        return super().__str__()
