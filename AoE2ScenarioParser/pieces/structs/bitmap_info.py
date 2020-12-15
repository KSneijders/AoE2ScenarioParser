from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.helper.retriever_dependency import RetrieverDependency, DependencyAction, DependencyTarget
from AoE2ScenarioParser.pieces.structs.aoe2_struct import AoE2Struct


class BitMapInfoStruct(AoE2Struct):
    dependencies = {
        'colors_used': {
            "on_construct": RetrieverDependency(
                DependencyAction.SET_REPEAT, DependencyTarget("self", "number_of_colors_used"),
            )
        },
        'image': {
            "on_construct": RetrieverDependency(
                DependencyAction.SET_REPEAT, DependencyTarget("self", "image_size"),
            )
        }
    }

    def __init__(self, data=None, pieces=None):
        retrievers = [
            Retriever("size", DataType("s32")),
            Retriever("width", DataType("u32")),
            Retriever("height", DataType("s32")),
            Retriever("planes", DataType("s16")),
            Retriever("bit_count", DataType("s16")),
            Retriever("compression", DataType("u32")),
            Retriever("image_size", DataType("u32")),
            Retriever("x_pels", DataType("u32")),
            Retriever("y_pels", DataType("u32")),
            Retriever("number_of_colors_used", DataType("u32")),
            Retriever("important_colors", DataType("u32")),
            Retriever("colors_used", DataType("u32")),
            Retriever("image", DataType("u8")),
        ]

        super().__init__("BitMap Info", retrievers, parser_obj, data=data, pieces=pieces)

    @staticmethod
    def defaults(pieces):
        defaults = {}
        return defaults
