from typing import Dict

from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.helper.retriever_dependency import RetrieverDependency, DependencyAction, DependencyTarget, \
    DependencyEval
from AoE2ScenarioParser.pieces.structs.aoe2_struct import AoE2Struct
from AoE2ScenarioParser.pieces.structs.unit import UnitStruct


class PlayerUnitsStruct(AoE2Struct):
    dependencies: Dict[str, Dict[str, RetrieverDependency]] = {
        "unit_count": {
            "on_refresh": RetrieverDependency(
                DependencyAction.SET_VALUE, DependencyTarget("self", "units"),
                DependencyEval("len(x)"))
        },
        "units": {
            "on_refresh": RetrieverDependency(
                DependencyAction.SET_REPEAT, DependencyTarget("self", "unit_count")),
            "on_construct": RetrieverDependency(DependencyAction.REFRESH_SELF),
            "on_commit": RetrieverDependency(
                DependencyAction.REFRESH, DependencyTarget("self", "unit_count"))
        },
    }

    def __init__(self, data=None, pieces=None):
        retrievers = [
            Retriever("unit_count", DataType("u32")),
            Retriever("units", DataType(UnitStruct))
        ]

        super().__init__("Player Units", retrievers, parser_obj, data, pieces=pieces)

    @staticmethod
    def defaults(pieces):
        defaults = {
            'unit_count': 0,
            'units': [],
        }
        return defaults
