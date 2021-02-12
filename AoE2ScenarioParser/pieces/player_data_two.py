from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.pieces.aoe2_file_section import AoE2FileSection
from AoE2ScenarioParser.pieces.structs.ai import AIStruct
from AoE2ScenarioParser.pieces.structs.resources import ResourcesStruct


class PlayerDataTwoPiece(AoE2FileSection):
    def __init__(self):
        retrievers = [
            Retriever("strings", DataType("str16", repeat=32)),
            Retriever("ai_names", DataType("str16", repeat=16)),
            Retriever("ai_files", DataType(AIStruct, repeat=16)),
            Retriever("ai_type", DataType("u8", repeat=16)),
            Retriever("separator", DataType("u32")),
            Retriever("resources", DataType(ResourcesStruct, repeat=16))
        ]

        super().__init__("PlayerDataTwoPiece", retrievers)

    @staticmethod
    def defaults(pieces):
        defaults = {
            'strings': [''] * 32,
            'ai_names': [''] * 16,
            # 'ai_files': [AIStruct(data=list(AIStruct.defaults(pieces).values()), pieces=pieces) for _ in range(16)],
            'ai_type': [1] * 16,
            'separator': 4294967197,
            # 'resources': PlayerDataTwoPiece._get_resource_struct_default(pieces),
        }
        return defaults

    @staticmethod
    def _get_resource_struct_default(pieces):
        data = [list(ResourcesStruct.defaults(pieces).values()) for _ in range(16)]
        for i in range(len(data)):
            data[i][5] = i
        return [ResourcesStruct(data=x, pieces=pieces) for x in data]
