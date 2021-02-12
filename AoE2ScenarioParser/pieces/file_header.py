import time
from typing import Dict

from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.helper.retriever_dependency import RetrieverDependency, DependencyAction, DependencyTarget, \
    DependencyEval
from AoE2ScenarioParser.pieces.aoe2_file_section import AoE2FileSection


class FileHeaderPiece(AoE2FileSection):
    dependencies: Dict[str, Dict[str, RetrieverDependency]] = {
        # "individual_victories_used": {
        #     "on_refresh": RetrieverDependency(
        #         DependencyAction.SET_REPEAT,
        #         DependencyTarget('self', 'version'),
        #         DependencyEval('0 if x == \'1.40\' else 1')
        #     ),
        #     "on_construct": RetrieverDependency(DependencyAction.REFRESH_SELF)
        # }
        "trigger_count": {
            "on_refresh": RetrieverDependency(
                DependencyAction.SET_VALUE, DependencyTarget("TriggersPiece", "trigger_data"),
                DependencyEval("len(x)")
            )
        },
    }

    def __init__(self):
        retrievers = [
            Retriever("version", DataType("c4")),
            Retriever("header_length", DataType("u32")),
            Retriever("savable", DataType("s32")),
            Retriever("timestamp_of_last_save", DataType("u32")),
            Retriever("scenario_instructions", DataType("str32")),
            # Retriever("individual_victories_used", DataType("u32")),
            Retriever("player_count", DataType("u32")),
            Retriever("data", DataType("36")),
            Retriever("creator_name", DataType("str32")),
            Retriever("trigger_count", DataType("u32")),
        ]

        super().__init__("FileHeaderPiece", retrievers)

    @staticmethod
    def defaults(pieces):
        defaults = {
            'version': '1.40',
            'header_length': 0,
            'savable': 6,
            'timestamp_of_last_save': int(time.time()),
            'scenario_instructions': '',
            # 'individual_victories_used': 0,
            'player_count': 2,
            'data': b'\xe8\x03\x00\x00\x01\x00\x00\x00\x06\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00'
                    b'\x00\x05\x00\x00\x00\x06\x00\x00\x00\x07\x00\x00\x00',
            'creator_name': 'KSneijders/AoE2ScenarioParser',
            'trigger_count': 0,
        }
        return defaults
