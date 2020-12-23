from typing import Dict

from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.helper.retriever_dependency import DependencyAction, RetrieverDependency, DependencyTarget, \
    DependencyEval
from AoE2ScenarioParser.pieces.structs.aoe2_struct import AoE2Struct
from AoE2ScenarioParser.pieces.structs.condition import ConditionStruct
from AoE2ScenarioParser.pieces.structs.effect import EffectStruct


class TriggerStruct(AoE2Struct):
    dependencies: Dict[str, Dict[str, RetrieverDependency]] = {
        "number_of_effects": {
            "on_refresh": RetrieverDependency(
                DependencyAction.SET_VALUE, DependencyTarget("self", "effect_data"),
                DependencyEval("len(x)")
            )},
        "effect_data": {
            "on_refresh": RetrieverDependency(
                DependencyAction.SET_REPEAT, DependencyTarget("self", "number_of_effects")
            ),
            "on_construct": RetrieverDependency(DependencyAction.REFRESH_SELF),
            "on_commit": RetrieverDependency(
                DependencyAction.REFRESH, DependencyTarget("self", "number_of_effects")
            )
        },
        "effect_display_order_array": {
            "on_refresh": RetrieverDependency(
                DependencyAction.SET_REPEAT, DependencyTarget("self", "number_of_effects")
            ),
            "on_construct": RetrieverDependency(DependencyAction.REFRESH_SELF)
        },
        "number_of_conditions": {
            "on_refresh": RetrieverDependency(
                DependencyAction.SET_VALUE, DependencyTarget("self", "condition_data"),
                DependencyEval("len(x)")
            )
        },
        "condition_data": {
            "on_refresh": RetrieverDependency(
                DependencyAction.SET_REPEAT, DependencyTarget("self", "number_of_conditions")
            ),
            "on_construct": RetrieverDependency(DependencyAction.REFRESH_SELF),
            "on_commit": RetrieverDependency(
                DependencyAction.REFRESH, DependencyTarget("self", "number_of_conditions")
            )
        },
        "condition_display_order_array": {
            "on_refresh": RetrieverDependency(
                DependencyAction.SET_REPEAT,
                DependencyTarget("self", "number_of_conditions")
            ),
            "on_construct": RetrieverDependency(DependencyAction.REFRESH_SELF)
        },
    }

    def __init__(self):
        retrievers = [
            Retriever("enabled", DataType("u32")),
            Retriever("looping", DataType("s8")),
            Retriever("description_string_table_id", DataType("s32")),
            Retriever("display_as_objective", DataType("u8")),
            Retriever("objective_description_order", DataType("u32")),
            Retriever("make_header", DataType("u8")),
            Retriever("short_description_string_table_id", DataType("s32")),
            Retriever("display_on_screen", DataType("u8")),
            Retriever("unknown", DataType("5")),
            Retriever("mute_objectives", DataType("u8")),
            # Retriever("Trigger starting time", DataType("u32")),
            Retriever("trigger_description", DataType("str32")),
            Retriever("trigger_name", DataType("str32")),  # (max 44 characters in UI)
            Retriever("short_description", DataType("str32")),
            Retriever("number_of_effects", DataType("s32")),
            Retriever("effect_data", DataType(EffectStruct)),
            Retriever("effect_display_order_array", DataType("s32")),
            Retriever("number_of_conditions", DataType("s32")),
            Retriever("condition_data", DataType(ConditionStruct)),
            Retriever("condition_display_order_array", DataType("s32"))
        ]

        super().__init__("Trigger", retrievers)

    @staticmethod
    def defaults(pieces):
        defaults = {
            'enabled': 1,
            'looping': 0,
            'description_string_table_id': -1,
            'display_as_objective': 0,
            'objective_description_order': 0,
            'make_header': 0,
            'short_description_string_table_id': -1,
            'display_on_screen': 0,
            'unknown': b'\x00\x00\x00\x00\x00',
            'mute_objectives': 0,
            'trigger_description': '',
            'trigger_name': 'Trigger 0',
            'short_description': '',
            'number_of_effects': 0,
            'effect_data': [],
            'effect_display_order_array': [],
            'number_of_conditions': 0,
            'condition_data': [],
            'condition_display_order_array': [],
        }
        return defaults
