from AoE2ScenarioParser.pieces import aoe2_piece
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.helper.datatype import DataType


class FileHeaderPiece(aoe2_piece.AoE2Piece):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("version", DataType("c4"), save_as="scenario_version"),
            Retriever("header_length", DataType("u32")),
            Retriever("savable", DataType("s32")),
            Retriever("timestamp_of_last_save", DataType("u32")),
            Retriever("scenario_instructions", DataType("str32")),
            Retriever("individual_victories_used", DataType("u32")),
            Retriever("player_count", DataType("u32")),
            Retriever("data", DataType("36")),
            Retriever("creator_name", DataType("str32")),
            Retriever("trigger_count", DataType("u32")),
        ]

        super().__init__("File Header", retrievers, parser_obj, data=data)

# For when turning it back into bytes:
# import time
# timestamp = int(time.time()) <-- for seconds since epoch
