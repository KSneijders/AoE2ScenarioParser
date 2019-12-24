from src.helper.datatype import DataType
from src.helper.retriever import Retriever
import src.pieces.structs.aoe2_struct as structs
from src.pieces.structs.unit import UnitStruct


class PlayerUnitsStruct(structs.Struct):
    def __init__(self, parser_obj, data=None):
        retrievers = [
            Retriever("Unit count", DataType("u32"), save_as="unit_count"),
            Retriever("Units", DataType(UnitStruct), set_repeat="{unit_count}")
        ]

        super().__init__(parser_obj, "Player Units", retrievers, data)
