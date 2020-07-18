from AoE2ScenarioParser.pieces import aoe2_piece
from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.structs.player_data_one import PlayerDataOneStruct


class DataHeaderPiece(aoe2_piece.AoE2Piece):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("next_unit_id_to_place", DataType("u32")),
            Retriever("version", DataType("f32")),
            Retriever("player_names", DataType("c256", repeat=16)),
            Retriever("string_table_player_names", DataType("u32", repeat=16)),
            Retriever("player_data_1", DataType(PlayerDataOneStruct, repeat=16)),
            Retriever("conquest_mode", DataType("u8")),
            Retriever("mission_items_counter", DataType("u16"), save_as="mic"),
            Retriever("mission_available", DataType("u16")),
            Retriever("mission_timeline", DataType("f32")),
            Retriever("mission_item", DataType("30"), set_repeat="{mic}"),
            Retriever("unknown", DataType("64")),
            Retriever("filename", DataType("str16"))
        ]

        super().__init__("Data Header", retrievers, parser_obj, data=data)
