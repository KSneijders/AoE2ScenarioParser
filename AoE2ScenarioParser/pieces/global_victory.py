from AoE2ScenarioParser.pieces import aoe2_piece
from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever


class GlobalVictoryPiece(aoe2_piece.AoE2Piece):
    def __init__(self, parser_obj=None, data=None):
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

        super().__init__("Global Victory", retrievers, parser_obj, data=data)
