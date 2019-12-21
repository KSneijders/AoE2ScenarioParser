import src.pieces.scenario_piece as scenario_piece
from src.helper.retriever import Retriever
from src.helper.datatype import DataType
from src.pieces.structs.trigger import TriggerStruct


class TriggerPiece(scenario_piece.ScenarioPiece):
    def __init__(self, parser_obj):
        retrievers = [
            Retriever("Trigger Version", DataType("f64")),
            Retriever("Trigger instructions start", DataType("s8")),
            Retriever("Number of triggers", DataType("s32"), save_as="number_of_triggers"),
            Retriever("Trigger data", DataType(TriggerStruct), set_repeat="{number_of_triggers}"),
            Retriever("Trigger display order array", DataType("u32"), set_repeat="{number_of_triggers}"),
        ]

        super().__init__(parser_obj, "Triggers", retrievers)
