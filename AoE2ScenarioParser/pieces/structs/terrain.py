from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.aoe2_file_section import AoE2FileSection


class TerrainStruct(AoE2FileSection):
    def __init__(self):
        retrievers = [
            Retriever("terrain_id", DataType("u8")),
            Retriever("elevation", DataType("u8")),
            Retriever("unused", DataType("u8")),
            Retriever("separator", DataType("2")),
            Retriever("layer", DataType("s16"))
        ]

        super().__init__("Terrain", retrievers)

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
