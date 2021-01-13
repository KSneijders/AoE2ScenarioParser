from AoE2ScenarioParser.pieces.aoe2_file_part import AoE2FilePart
from AoE2ScenarioParser.pieces.structs.aoe2_struct import AoE2StructModel


class AoE2Piece(AoE2FilePart):
    def __init__(self, name, retrievers):
        super().__init__(name, retrievers)

    @classmethod
    def from_structure(cls, piece_name, structure):
        piece = super().from_structure(piece_name, structure)

        for name, attr in structure.get('structs', {}).items():
            # Create struct model
            piece.struct_models[name] = AoE2StructModel.from_structure(name, attr)
        return piece

    def get_header_string(self):
        return "######################## " + self.name + " ######################## [PIECE]"

    def __repr__(self):
        return type(self).__name__
