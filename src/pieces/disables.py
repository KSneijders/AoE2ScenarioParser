import src.pieces.scenario_piece as scenario_piece
from src.helper.retriever import Retriever
from src.helper.datatype import DataType


class DisablesPiece(scenario_piece.ScenarioPiece):

    def __init__(self, parser_obj):
        retrievers = [
            Retriever("Per player number of disabled techs", DataType("u32", repeat=16), save_as="disabled_techs"),
            Retriever("Disabled technology IDs in player order", DataType("u32"), set_repeat="sum({disabled_techs})"),
            # Retriever("Per player extra number of disabled techs", DataType("u32", repeat=16)),  # Removed in DE?
            Retriever("Per player number of disabled units", DataType("u32", repeat=16), save_as="disabled_units"),
            Retriever("Disabled unit IDs in player order", DataType("u32"), set_repeat="sum({disabled_units})"),
            # Retriever("Per player extra number of disabled units", DataType("u32", repeat=16)),  # Removed in DE?
            Retriever("Per player number of disabled buildings",
                      DataType("u32", repeat=16), save_as="disabled_buildings"),
            Retriever("Disabled building IDs in player order",
                      DataType("u32"), set_repeat="sum({disabled_buildings})"),
            Retriever("Combat Mode", DataType("u32")),
            Retriever("Naval Mode", DataType("u32")),
            Retriever("All techs", DataType("u32")),
            Retriever("Per player starting age", DataType("u32", repeat=16)),  # 2: Dark 6 = Post | 1-8 players 9 GAIA
            Retriever("Unknown", DataType("36")),
        ]

        super().__init__(parser_obj, "Disables", retrievers)
