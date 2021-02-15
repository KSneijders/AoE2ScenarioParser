import time
from typing import Dict

from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.helper.retriever_dependency import RetrieverDependency, DependencyAction, DependencyTarget, \
    DependencyEval
from AoE2ScenarioParser.pieces import aoe2_piece


class FileHeaderPiece(aoe2_piece.AoE2Piece):
    dependencies: Dict[str, Dict[str, RetrieverDependency]] = {
        # "individual_victories_used": {
        #     "on_refresh": RetrieverDependency(
        #         DependencyAction.SET_REPEAT,
        #         DependencyTarget('self', 'version'),
        #         DependencyEval('0 if x == \'1.40\' else 1')
        #     ),
        #     "on_construct": RetrieverDependency(DependencyAction.REFRESH_SELF)
        # }
        # amount_of_unknown_numbers
        # unknown_numbers
        "amount_of_unknown_numbers": {
            "on_refresh": RetrieverDependency(
                DependencyAction.SET_VALUE, DependencyTarget("self", "unknown_numbers"),
                DependencyEval("len(x)")
            )
        },
        "unknown_numbers": {
            "on_refresh": RetrieverDependency(
                DependencyAction.SET_REPEAT, DependencyTarget("self", "amount_of_unknown_numbers")
            ),
            "on_construct": RetrieverDependency(DependencyAction.REFRESH_SELF),
            "on_commit": RetrieverDependency(
                DependencyAction.REFRESH, DependencyTarget("self", "amount_of_unknown_numbers")
            )
        },
        "trigger_count": {
            "on_refresh": RetrieverDependency(
                DependencyAction.SET_VALUE, DependencyTarget("TriggerPiece", "trigger_data"),
                DependencyEval("len(x)")
            )
        },
    }

    def __init__(self, parser_obj=None, data=None, pieces=None):
        retrievers = [
            Retriever("version", DataType("c4")),
            Retriever("header_length", DataType("u32")),
            Retriever("savable", DataType("s32")),
            Retriever("timestamp_of_last_save", DataType("u32")),
            Retriever("scenario_instructions", DataType("str32")),
            # Retriever("individual_victories_used", DataType("u32")),
            Retriever("player_count", DataType("u32")),
            Retriever("unknown_value", DataType("u32")),  # Always (?) 1k
            Retriever("unknown_value_2", DataType("u32")),  # Always (?) 1
            Retriever("amount_of_unknown_numbers", DataType("u32")),
            Retriever("unknown_numbers", DataType("u32")),
            Retriever("creator_name", DataType("str32")),
            Retriever("trigger_count", DataType("u32")),
        ]

        super().__init__("File Header", retrievers, parser_obj, data=data, pieces=pieces)

    @staticmethod
    def defaults(pieces):
        defaults = {
            'version': '1.41',
            'header_length': 0,
            'savable': 6,
            'timestamp_of_last_save': int(time.time()),
            'scenario_instructions': '',
            # 'individual_victories_used': 0,
            'player_count': 2,
            'unknown_value': 1000,
            'unknown_value_2': 1,
            'amount_of_unknown_numbers': 6,
            'unknown_numbers': [2, 3, 4, 5, 6, 7],
            'creator_name': 'KSneijders/AoE2ScenarioParser',
            'trigger_count': 0,
        }
        return defaults
