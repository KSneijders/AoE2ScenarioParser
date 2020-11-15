from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.structs.aoe2_struct import AoE2Struct


class TerrainStruct(AoE2Struct):
    def __init__(self, parser_obj=None, data=None, pieces=None):
        retrievers = [
            Retriever("terrain_id", DataType("u8")),
            Retriever("elevation", DataType("u8")),
            Retriever("unused", DataType("u8")),
            Retriever("separator", DataType("2")),
            Retriever("layer", DataType("s16"))
        ]

        super().__init__("Terrain", retrievers, parser_obj, data, pieces=pieces)

    @staticmethod
    def defaults(pieces):
        defaults = {
            'terrain_id': 0,
            'elevation': 0,
            'unused': 0,
            'separator': b'\xff\xff',
            'layer': -1,
        }
        return defaults
