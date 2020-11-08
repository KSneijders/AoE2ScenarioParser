from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.helper.retriever_dependency import RetrieverDependency, DependencyAction, DependencyTarget, \
    DependencyEval
from AoE2ScenarioParser.pieces.structs.aoe2_struct import AoE2Struct
from AoE2ScenarioParser.pieces.structs.unit import UnitStruct


class PlayerUnitsStruct(AoE2Struct):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("unit_count", DataType("u32"),
                      on_refresh=RetrieverDependency(
                          DependencyAction.SET_VALUE, DependencyTarget("self", "units"),
                          DependencyEval("len(x)"))),
            Retriever("units", DataType(UnitStruct),
                      on_refresh=RetrieverDependency(
                          DependencyAction.SET_REPEAT, DependencyTarget("self", "unit_count")),
                      on_construct=RetrieverDependency(DependencyAction.REFRESH_SELF),
                      on_commit=RetrieverDependency(
                          DependencyAction.REFRESH, DependencyTarget("self", "unit_count")))
        ]

        super().__init__("Player Units", retrievers, parser_obj, data)

    @staticmethod
    def defaults():
        defaults = {
            'unit_count': 0,
            'units': [],
        }
        return defaults
