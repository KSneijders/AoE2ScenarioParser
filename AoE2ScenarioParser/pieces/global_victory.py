from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces import aoe2_piece


class GlobalVictoryPiece(aoe2_piece.AoE2Piece):
    def __init__(self, parser_obj=None, data=None, pieces=None):
        retrievers = [
            Retriever("separator", DataType("u32")),
            Retriever("conquest_required", DataType("u32")),
            Retriever("ruins", DataType("u32")),
            Retriever("artifacts", DataType("u32")),
            Retriever("discovery", DataType("u32")),
            Retriever("explored_percent_of_map_required", DataType("u32")),
            Retriever("gold", DataType("u32")),
            Retriever("all_custom_conditions_required", DataType("u32")),
            Retriever("mode", DataType("u32")),
            Retriever("required_score_for_score_victory", DataType("u32")),
            Retriever("time_for_timed_game_in_10ths_of_a_year", DataType("u32")),
        ]

        super().__init__("Global Victory", retrievers, parser_obj, data=data, pieces=pieces)

    @staticmethod
    def defaults(pieces):
        defaults = {
            'separator': 4294967197,
            'conquest_required': 1,
            'ruins': 0,
            'artifacts': 0,
            'discovery': 0,
            'explored_percent_of_map_required': 0,
            'gold': 0,
            'all_custom_conditions_required': 0,
            'mode': 0,
            'required_score_for_score_victory': 900,
            'time_for_timed_game_in_10ths_of_a_year': 9000,
        }
        return defaults
