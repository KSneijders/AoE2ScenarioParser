import src.pieces.aoe2_piece as scenario_piece
from src.helper.datatype import DataType
from src.helper.retriever import Retriever
from src.pieces.structs.player_data_one import PlayerDataOneStruct


class DataHeaderPiece(scenario_piece.ScenarioPiece):
    def __init__(self, parser_obj):
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

        super().__init__(parser_obj, "Data Header", retrievers)
