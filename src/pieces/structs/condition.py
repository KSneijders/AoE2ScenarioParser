from src.helper.datatype import DataType
from src.helper.retriever import Retriever
import src.pieces.structs.struct as structs


class ConditionStruct(structs.Struct):
    def __init__(self, parser, data=None):
        retrievers = [
            Retriever("Condition Type", DataType("s32")),
            Retriever("Check, always = 0x10", DataType("s32")),
            Retriever("Amount (of Object, Difficulty)", DataType("s32")),
            Retriever("Resource Type", DataType("s32")),
            Retriever("Unit object", DataType("s32")),
            Retriever("Unit ID", DataType("s32")),
            Retriever("Unit Name", DataType("s32")),
            Retriever("Player", DataType("s32")),
            Retriever("Technology", DataType("s32")),
            Retriever("Timer", DataType("s32")),
            Retriever("Unknown", DataType("s32")),
            Retriever("Area 1 X", DataType("s32")),
            Retriever("Area 1 Y", DataType("s32")),
            Retriever("Area 2 X", DataType("s32")),
            Retriever("Area 2 Y", DataType("s32")),
            Retriever("AI Signal", DataType("s32")),
        ]

        super().__init__(parser, "Condition", retrievers, data)
