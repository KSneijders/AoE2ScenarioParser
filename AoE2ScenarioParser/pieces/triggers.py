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
            Retriever("number_of_triggers", DataType("s32")),
            # on_construct=(CallbackType.SAVE, 'number_of_triggers'),
            # on_commit=(CallbackType.SET_VALUE, '{number_of_triggers}')),
            Retriever("trigger_data", DataType(TriggerStruct)),
            # on_construct=(CallbackType.SET_REPEAT, '{number_of_triggers}'),
            # on_commit=(CallbackType.SAVE, 'number_of_triggers', 'len(x)')),
            Retriever("trigger_display_order_array", DataType("u32")),
            # on_construct=(CallbackType.SET_REPEAT, '{number_of_triggers}')),
            Retriever("unknown", DataType("1028")),
            Retriever("number_of_variables", DataType("u32")),
            # on_construct=(CallbackType.SAVE, 'number_of_vars'),
            # on_commit=(CallbackType.SET_VALUE, '{number_of_vars}')),
            Retriever("variable_data", DataType(VariableStruct))
            # on_construct=(CallbackType.SET_REPEAT, '{number_of_vars}'),
            # on_commit=(CallbackType.SAVE, 'number_of_vars', 'len(x)'))
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
