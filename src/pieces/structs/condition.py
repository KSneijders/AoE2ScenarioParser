from src.helper.datatype import DataType
from src.helper.retriever import Retriever
import src.pieces.structs.struct as structs


class ConditionStruct(structs.Struct):
    def __init__(self, parser_obj, data=None):
        retrievers = [
            Retriever("Condition Type", DataType("s32")),
            Retriever("Amount of condition attributes? Always 0x15", DataType("s32")),  # Was always: 0x10
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
            Retriever("Target player (diplo state)", DataType("s32")),
        ]

        super().__init__(parser_obj, "Condition", retrievers, data)
