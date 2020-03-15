from AoE2ScenarioParser.pieces import aoe2_piece
from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.structs.player_data_one import PlayerDataOneStruct


class DataHeaderPiece(aoe2_piece.AoE2Piece):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("Next unit ID to place", DataType("u32")),
            Retriever("Version", DataType("f32")),
            Retriever("Player names", DataType("c256", repeat=16)),
            Retriever("String table player names", DataType("u32", repeat=16)),
            Retriever("Player data#1", DataType(PlayerDataOneStruct, repeat=16)),
            Retriever("Conquest mode", DataType("u8")),
            Retriever("Mission items Counter", DataType("u16"), save_as="mic"),
            Retriever("Mission available", DataType("u16")),
            Retriever("Mission timeline", DataType("f32")),
            Retriever("Mission item", DataType("30"), set_repeat="{mic}"),
            Retriever("Unknown", DataType("64")),
            Retriever("Filename", DataType("str16"))
        ]

        super().__init__("Data Header", retrievers, parser_obj)
