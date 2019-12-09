from src.pieces.scenario_piece import ScenarioPiece
from src.helper.datatype import DataType
from src.helper.retriever import Retriever
from src.pieces.structs.player_data_one import PlayerDataOne


class DataHeaderPiece(ScenarioPiece):
    retrievers = [
        Retriever("Next unit ID to Place", DataType("u32")),
        Retriever("Version", DataType("f32")),
        Retriever("ASCII player names", DataType("c256", repeat=16)),
        Retriever("String table player names", DataType("u32", repeat=16)),
        Retriever("Player Data#1", DataType("16", repeat=16), on_success=lambda x: PlayerDataOne(x)),
        Retriever("Conquest Mode", DataType("u8")),
        Retriever("Mission Items Counter", DataType("u16"), save_as="mic"),
        Retriever("Mission Available", DataType("u16")),
        Retriever("Mission Timeline", DataType("f32")),
        Retriever("Mission Item", DataType("30"), set_repeat="{mic}"),
        Retriever("Original Filename at creation", DataType("str16"))
    ]

    def __init__(self):
        super().__init__("Data Header", self.retrievers)
