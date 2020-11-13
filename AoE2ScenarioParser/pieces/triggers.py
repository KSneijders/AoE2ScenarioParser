from typing import Dict

from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.helper.retriever_dependency import RetrieverDependency, DependencyAction, DependencyTarget, \
    DependencyEval
from AoE2ScenarioParser.pieces import aoe2_piece
from AoE2ScenarioParser.pieces.structs.trigger import TriggerStruct
from AoE2ScenarioParser.pieces.structs.variable import VariableStruct


class TriggerPiece(aoe2_piece.AoE2Piece):
    dependencies: Dict[str, Dict[str, RetrieverDependency]] = {
        "number_of_triggers": {
            "on_refresh": RetrieverDependency(
                DependencyAction.SET_VALUE, DependencyTarget("self", "trigger_data"),
                DependencyEval("len(x)")
            )
        },
        "trigger_data": {
            "on_refresh": RetrieverDependency(
                DependencyAction.SET_REPEAT, DependencyTarget("self", "number_of_triggers")
            ),
            "on_construct": RetrieverDependency(DependencyAction.REFRESH_SELF),
            "on_commit": RetrieverDependency(
                DependencyAction.REFRESH, DependencyTarget("self", "number_of_triggers")
            )
        },
        "trigger_display_order_array": {
            "on_refresh": RetrieverDependency(
                DependencyAction.SET_REPEAT, DependencyTarget("self", "number_of_triggers")
            ),
            "on_construct": RetrieverDependency(DependencyAction.REFRESH_SELF)
        },
        "number_of_variables": {
            "on_refresh": RetrieverDependency(
                DependencyAction.SET_VALUE, DependencyTarget("self", "variable_data"),
                DependencyEval("len(x)")
            )
        },
        "variable_data": {
            "on_refresh": RetrieverDependency(
                DependencyAction.SET_REPEAT, DependencyTarget("self", "number_of_variables")
            ),
            "on_construct": RetrieverDependency(DependencyAction.REFRESH_SELF),
            "on_commit": RetrieverDependency(
                DependencyAction.REFRESH, DependencyTarget("self", "number_of_variables")
            )
        },
    }

    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("trigger_version", DataType("f64")),
            Retriever("trigger_instruction_start", DataType("s8")),
            Retriever("number_of_triggers", DataType("s32")),
            Retriever("trigger_data", DataType(TriggerStruct)),
            Retriever("trigger_display_order_array", DataType("u32")),
            Retriever("unknown", DataType("1028")),
            Retriever("number_of_variables", DataType("u32")),
            Retriever("variable_data", DataType(VariableStruct)),
        ]

        super().__init__("Triggers", retrievers, parser_obj, data=data)

    @staticmethod
    def defaults():
        defaults = {
            'trigger_version': 2.2,
            'trigger_instruction_start': 0,
            'number_of_triggers': 0,
            'trigger_data': [],
            'trigger_display_order_array': [],
            'unknown': b'\x00' * 1028,
            'number_of_variables': 0,
            'variable_data': [],
        }
        return defaults
