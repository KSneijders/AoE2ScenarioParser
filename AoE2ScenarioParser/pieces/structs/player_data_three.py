from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.structs.aoe2_struct import AoE2Struct


class PlayerDataThreeStruct(AoE2Struct):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("constant_name", DataType("str16")),
            Retriever("initial_camera_x", DataType("f32")),
            Retriever("initial_camera_y", DataType("f32")),
            Retriever("unknown_similar_to_camera_x", DataType("s16")),
            Retriever("unknown_similar_to_camera_y", DataType("s16")),
            Retriever("aok_allied_victory", DataType("u8")),
            Retriever("player_count_for_diplomacy", DataType("u16"), save_as="diplo_player_count"),
            Retriever("diplomacy_for_interaction", DataType("u8"), set_repeat="{diplo_player_count}"),
            Retriever("diplomacy_for_ai_system", DataType("u32", repeat=9)),
            Retriever("color", DataType("u32")),
            Retriever("victory_version", DataType("f32"), save_as="vic_version"),
            Retriever("unknown", DataType("u16"), save_as="unknown_DAT"),
            Retriever("unknown_2", DataType("u8"), set_repeat="8 if {vic_version} == 2 else 0"),
            Retriever("unknown_structure_grand_theft_empires", DataType("44"), set_repeat="{unknown_DAT}"),
            Retriever("unknown_3", DataType("u8", repeat=7)),
            Retriever("unknown_4", DataType("s32")),
        ]

        super().__init__("Player Data #3", retrievers, parser_obj, data)
