from typing import Dict

from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.helper.retriever_dependency import RetrieverDependency
from AoE2ScenarioParser.pieces.structs.aoe2_struct import AoE2Struct


class ConditionStruct(AoE2Struct):
    dependencies: Dict[str, Dict[str, RetrieverDependency]] = {}

    def __init__(self, parser_obj=None, data=None, pieces=None):
        retrievers = [
            Retriever("condition_type", DataType("s32")),
            Retriever("static_value_21", DataType("s32")),  # Was always: 0x10
            Retriever("amount_or_quantity", DataType("s32")),  # Also technology state, also Difficulty
            Retriever("resource_type_or_tribute_list", DataType("s32")),
            Retriever("unit_object", DataType("s32")),
            Retriever("next_object", DataType("s32")),  # Old: Unit ID
            Retriever("object_list", DataType("s32")),
            Retriever("source_player", DataType("s32")),
            Retriever("technology", DataType("s32")),
            Retriever("timer", DataType("s32")),
            Retriever("unknown", DataType("s32")),
            Retriever("area_1_x", DataType("s32")),
            Retriever("area_1_y", DataType("s32")),
            Retriever("area_2_x", DataType("s32")),
            Retriever("area_2_y", DataType("s32")),
            Retriever("object_group", DataType("s32")),
            Retriever("object_type", DataType("s32")),  # -1: None, 1: Other, 2: Building, 3: Civilian, 4: Military
            Retriever("ai_signal", DataType("s32")),
            Retriever("inverted", DataType("s32")),
            Retriever("unknown_2", DataType("s32")),
            Retriever("variable", DataType("s32")),  # Number == VariableX
            Retriever("comparison", DataType("s32")),  # 0: ==, 1: <, 2: >, 3: <=, 4 >=
            Retriever("target_player", DataType("s32")),
        ]

        super().__init__("Condition", retrievers, parser_obj, data, pieces=pieces)

    @staticmethod
    def defaults(pieces):
        defaults = {
            'condition_type': 0,
            'static_value_21': 21,
            'amount_or_quantity': -1,
            'resource_type_or_tribute_list': -1,
            'unit_object': -1,
            'next_object': -1,
            'object_list': -1,
            'source_player': -1,
            'technology': -1,
            'timer': -1,
            'unknown': -1,
            'area_1_x': -1,
            'area_1_y': -1,
            'area_2_x': -1,
            'area_2_y': -1,
            'object_group': -1,
            'object_type': -1,
            'ai_signal': -1,
            'inverted': -1,
            'unknown_2': -1,
            'variable': -1,
            'comparison': -1,
            'target_player': -1,
        }
        return defaults
