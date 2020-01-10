import src.pieces.aoe2_piece as scenario_piece
from src.helper.retriever import Retriever
from src.helper.datatype import DataType
from src.pieces.structs.terrain import TerrainStruct


class MapPiece(scenario_piece.ScenarioPiece):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("Separator??", DataType("2")),
            Retriever("Unknown String", DataType("str16")),
            Retriever("Separator?? (2)", DataType("2")),
            Retriever("Map color mood", DataType("str16")),
            Retriever("Collide and Correcting", DataType("u8")),
            # Retriever("Separator", DataType("u8")),
            Retriever("Player 1 camera, Y", DataType("s32")),
            Retriever("Player 1 camera, X", DataType("s32")),
            Retriever("AI Type", DataType("s8")),
            Retriever("Map Width", DataType("s32"), save_as="map_width"),
            # Retriever("Unknown", DataType("u16")),
            Retriever("Map Height", DataType("s32"), save_as="map_height"),
            # Retriever("Unknown2", DataType("u16")),
            Retriever("Terrain data", DataType(TerrainStruct), set_repeat="{map_width}*{map_height}"),
        ]

        super().__init__("Map", retrievers, parser_obj)
