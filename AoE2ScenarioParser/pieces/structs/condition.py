from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.structs.aoe2_struct import AoE2Struct


class ConditionStruct(AoE2Struct):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("Condition type", DataType("s32")),
            Retriever("Check, (21)", DataType("s32")),  # Was always: 0x10
            Retriever("Amount (Quantity)", DataType("s32")),  # Also technology state, also Difficulty
            Retriever("Resource Type/Tribute list", DataType("s32")),
            Retriever("Unit object", DataType("s32")),
            Retriever("Next object", DataType("s32")),  # Old: Unit ID
            Retriever("Object list", DataType("s32")),
            Retriever("Player", DataType("s32")),
            Retriever("Technology", DataType("s32")),
            Retriever("Timer", DataType("s32")),
            Retriever("Unknown", DataType("s32")),
            Retriever("Area 1 X", DataType("s32")),
            Retriever("Area 1 Y", DataType("s32")),
            Retriever("Area 2 X", DataType("s32")),
            Retriever("Area 2 Y", DataType("s32")),
            Retriever("Object Group", DataType("s32")),
            Retriever("Object Type", DataType("s32")),  # -1: None, 1: Other, 2: Building, 3: Civilian, 4: Military
            Retriever("AI Signal", DataType("s32")),
            Retriever("Inverted", DataType("s32")),
            Retriever("Unknown (3)", DataType("s32")),
            Retriever("Variable", DataType("s32")),  # Number == VariableX
            Retriever("Comparison", DataType("s32")),  # 0: ==, 1: <, 2: >, 3: <=, 4 >=
            Retriever("Target player", DataType("s32")),
        ]

        super().__init__("Condition", retrievers, parser_obj, data)
