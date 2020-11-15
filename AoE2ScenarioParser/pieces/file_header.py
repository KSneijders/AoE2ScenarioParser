import time

from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces import aoe2_piece


class FileHeaderPiece(aoe2_piece.AoE2Piece):
    def __init__(self, parser_obj=None, data=None, pieces=None):
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

        super().__init__("File Header", retrievers, parser_obj, data=data, pieces=pieces)

    @staticmethod
    def defaults(pieces):
        defaults = {
            'version': '1.37',
            'header_length': 0,
            'savable': 5,
            'timestamp_of_last_save': int(time.time()),
            'scenario_instructions': '',
            'individual_victories_used': 0,
            'player_count': 2,
            'data': b'\xe8\x03\x00\x00\x01\x00\x00\x00\x06\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00'
                    b'\x00\x05\x00\x00\x00\x06\x00\x00\x00\x07\x00\x00\x00',
            'creator_name': 'KSneijders/AoE2ScenarioParser',
            'trigger_count': 0,
        }
        return defaults
