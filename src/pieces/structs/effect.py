from src.helper.datatype import DataType
from src.helper.retriever import Retriever
import src.pieces.structs.struct as structs


class EffectStruct(structs.Struct):
    def __init__(self, parser, data=None):
        retrievers = [
            Retriever("Effect type", DataType("s32")),
            Retriever("Check, ", DataType("s32")),  # always 0x17
            Retriever("AI script goal", DataType("s32")),
            Retriever("Amount, used for hp and attack", DataType("s32")),
            Retriever("Resource type", DataType("s32")),
            Retriever("Diplomacy, state for change", DataType("s32")),
            Retriever("Number of units selected", DataType("s32"), save_as="number_of_units_selected"),
            Retriever("Unit ID", DataType("s32")),
            Retriever("Unit Name", DataType("s32")),
            Retriever("Player Source", DataType("s32")),
            Retriever("Player Target", DataType("s32")),
            Retriever("Technology", DataType("s32")),
            Retriever("String ID", DataType("s32")),
            Retriever("Sound resource ID", DataType("s32")),
            Retriever("Display Time (display instructions)", DataType("s32")),
            Retriever("Trigger ID (activate/deactivate)", DataType("s32")),
            Retriever("Location X", DataType("s32")),
            Retriever("Location Y", DataType("s32")),
            Retriever("Area 1 X", DataType("s32")),
            Retriever("Area 1 Y", DataType("s32")),
            Retriever("Area 2 X", DataType("s32")),
            Retriever("Area 2 Y", DataType("s32")),
            Retriever("Unit Group", DataType("s32")),
            Retriever("Unit Type (Civilian, Military, Building, Other)", DataType("s32")),
            Retriever("Instruction Panel", DataType("s32")),
            Retriever("Instruction Text", DataType("str32")),
            Retriever("Sound filename", DataType("str32")),
            Retriever("Selected units IDs", DataType("s32"), set_repeat="{number_of_units_selected}"),
        ]

        super().__init__(parser, "Effect", retrievers, data)
