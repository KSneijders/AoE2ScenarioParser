from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.aoe2_file_part import AoE2FilePart


class CinematicsPiece(AoE2FilePart):
    def __init__(self):
        retrievers = [
            Retriever("ascii_pregame", DataType("str16")),
            Retriever("ascii_victory", DataType("str16")),
            Retriever("ascii_loss", DataType("str16")),
            # Retriever("Separator (! in some version)", DataType("1")),
        ]

        super().__init__("Cinematics", retrievers)

    @staticmethod
    def defaults(pieces):
        defaults = {
            'ascii_pregame': '',
            'ascii_victory': '',
            'ascii_loss': '',
        }
        return defaults
