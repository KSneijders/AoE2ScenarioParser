import time

from AoE2ScenarioParser.pieces import aoe2_piece
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.helper.datatype import DataType


class FileHeaderPiece(aoe2_piece.AoE2Piece):
    def __init__(self, parser_obj=None, data=None):
        data_default = b'\xe8\x03\x00\x00\x01\x00\x00\x00\x06\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00' \
                       b'\x00\x05\x00\x00\x00\x06\x00\x00\x00\x07\x00\x00\x00'
        timestamp_of_last_save_default = int(time.time())

        retrievers = [
            Retriever("version", DataType("c4"), default='1.37', save_as="scenario_version"),
            Retriever("header_length", DataType("u32"), default=0),
            Retriever("savable", DataType("s32"), default=5),
            Retriever("timestamp_of_last_save", DataType("u32"), default=timestamp_of_last_save_default),
            Retriever("scenario_instructions", DataType("str32"), default=''),
            Retriever("individual_victories_used", DataType("u32"), default=0),
            Retriever("player_count", DataType("u32"), default=2),
            Retriever("data", DataType("36"), default=data_default),
            Retriever("creator_name", DataType("str32"), default='https://github.com/KSneijders/AoE2ScenarioParser'),
            Retriever("trigger_count", DataType("u32"), default=0),
        ]

        super().__init__("File Header", retrievers, parser_obj, data=data)
