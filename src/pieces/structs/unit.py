from src.helper.datatype import DataType
from src.helper.retriever import Retriever
import src.pieces.structs.aoe2_struct as structs


class UnitStruct(structs.Struct):
    def __init__(self, parser_obj, data=None):
        retrievers = [
            Retriever("X position", DataType("f32")),
            Retriever("Y position", DataType("f32")),
            Retriever("Z position", DataType("f32")),
            Retriever("ID", DataType("u32")),
            Retriever("Unit 'constant'", DataType("u16")),
            Retriever("Status", DataType("u8")),
            Retriever("Rotation, in radians", DataType("f32")),
            Retriever("Initial animation frame", DataType("u16")),
            Retriever("Garrisoned in: ID", DataType("s32")),
        ]

        super().__init__(parser_obj, "Unit", retrievers, data)
