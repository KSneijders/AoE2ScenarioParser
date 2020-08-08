from AoE2ScenarioParser.pieces import aoe2_piece
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.pieces.structs.terrain import TerrainStruct


class MapPiece(aoe2_piece.AoE2Piece):
    def __init__(self, parser_obj=None, data=None):
        retrievers = [
            Retriever("Separator??", DataType("2")),
            Retriever("Unknown String", DataType("str16")),
            Retriever("Separator?? (2)", DataType("2")),
            Retriever("Map color mood", DataType("str16")),
            Retriever("Collide and Correcting", DataType("u8")),
            # [VERSION CHANGE] ADDED in 1.36 > 1.37
            Retriever("Villager Force Drop", DataType("u8"), set_repeat="1 if '{scenario_version}' == '1.37' else 0"),
            Retriever("Player 1 camera, Y", DataType("s32")),
            Retriever("Player 1 camera, X", DataType("s32")),
            Retriever("AI Type", DataType("s8")),
            Retriever("Map Width", DataType("s32"), save_as="map_width"),
            Retriever("Map Height", DataType("s32"), save_as="map_height"),
            Retriever("Terrain data", DataType(TerrainStruct), set_repeat="{map_width}*{map_height}"),
        ]

        super().__init__("Map", retrievers, parser_obj, data=data)
