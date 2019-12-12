from src.pieces.scenario_piece import *
from src.helper.retriever import Retriever
from src.helper.datatype import DataType
from src.pieces.structs.terrain import TerrainStruct


class MapPiece(ScenarioPiece):

    def __init__(self, parser):
        retrievers = [
            Retriever("Separator", DataType("u32")),
            Retriever("Player 1 camera, Y", DataType("s32")),
            Retriever("Player 1 camera, X", DataType("s32")),
            Retriever("AI Type", DataType("s32")),
            Retriever("Map Width", DataType("u32"), save_as="map_width", log_value=True),
            Retriever("Map Height", DataType("u32"), save_as="map_height", log_value=True),
            Retriever("Terrain data", DataType("7"), set_repeat="{map_width}*{map_height}", on_success=lambda x: TerrainStruct(parser, x)),
        ]

        super().__init__(parser, "Map", retrievers)
