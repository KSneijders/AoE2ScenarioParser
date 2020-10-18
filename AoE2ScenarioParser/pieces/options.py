from AoE2ScenarioParser.pieces import aoe2_piece
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.helper.datatype import DataType


class OptionsPiece(aoe2_piece.AoE2Piece):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("per_player_number_of_disabled_techs", DataType("u32", repeat=16), save_as="disabled_techs"),
            Retriever("disabled_technology_ids_in_player_order", DataType("u32"), set_repeat="sum({disabled_techs})"),
            # Retriever("per_player_extra_number_of_disabled_techs", DataType("u32", repeat=16)),  # Removed in DE?
            Retriever("per_player_number_of_disabled_units", DataType("u32", repeat=16), save_as="disabled_units"),
            Retriever("disabled_unit_ids_in_player_order", DataType("u32"), set_repeat="sum({disabled_units})"),
            # Retriever("per_player_extra_number_of_disabled_units", DataType("u32", repeat=16)),  # Removed in DE?
            Retriever("per_player_number_of_disabled_buildings",
                      DataType("u32", repeat=16), save_as="disabled_buildings"),
            Retriever("disabled_building_IDs_in_player_order",
                      DataType("u32"), set_repeat="sum({disabled_buildings})"),
            Retriever("combat_mode", DataType("u32")),
            Retriever("naval_mode", DataType("u32")),
            Retriever("all_techs", DataType("u32")),
            Retriever("per_player_starting_age", DataType("u32", repeat=16)),  # 2: Dark 6 = Post | 1-8 players 9 GAIA
            Retriever("unknown", DataType("36")),
        ]

        super().__init__("Options", retrievers, parser_obj, data=data)

    @staticmethod
    def defaults():
        defaults = {
            'per_player_number_of_disabled_techs': [0] * 16,
            'disabled_technology_ids_in_player_order': [],
            'per_player_number_of_disabled_units': [0] * 16,
            'disabled_unit_ids_in_player_order': [],
            'per_player_number_of_disabled_buildings': [0] * 16,
            'disabled_building_IDs_in_player_order': [],
            'combat_mode': 0,
            'naval_mode': 0,
            'all_techs': 0,
            'per_player_starting_age': [2] * 16,
            'unknown': b'\x9d\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                       b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
        }
        return defaults


