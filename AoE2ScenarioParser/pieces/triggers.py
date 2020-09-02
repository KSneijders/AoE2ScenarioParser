from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces import aoe2_piece
from AoE2ScenarioParser.pieces.structs.trigger import TriggerStruct
from AoE2ScenarioParser.pieces.structs.variable import VariableStruct


class TriggerPiece(aoe2_piece.AoE2Piece):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("trigger_version", DataType("f64")),
            Retriever("trigger_instruction_start", DataType("s8")),
            Retriever("number_of_triggers", DataType("s32"), save_as="number_of_triggers"),
            Retriever("trigger_data", DataType(TriggerStruct), set_repeat="{number_of_triggers}"),
            Retriever("trigger_display_order_array", DataType("u32"), set_repeat="{number_of_triggers}"),
            Retriever("unknown", DataType("1028")),
            Retriever("number_of_variables", DataType("u32"), save_as="number_of_vars"),
            Retriever("variable_data", DataType(VariableStruct), set_repeat="{number_of_vars}")
        ]

        super().__init__("Triggers", retrievers, parser_obj, data=data)
