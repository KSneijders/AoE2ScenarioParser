from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.helper.retriever_dependency import RetrieverDependency, DependencyAction, DependencyTarget, \
    DependencyEval
from AoE2ScenarioParser.pieces.aoe2_file_part import AoE2FilePart


class BitMapInfoStruct(AoE2FilePart):
    dependencies = {
        'colors_used': {
            "on_construct": RetrieverDependency(
                DependencyAction.SET_REPEAT, DependencyTarget("self", "number_of_colors_used"),
            )
        },
        'image': {
            "on_construct": RetrieverDependency(
                DependencyAction.SET_REPEAT, DependencyTarget(["self"] * 2, ["width", "height"]),
                DependencyEval("width * height", values_as_variable=['width', 'height'])
            )
        },
    }

    def __init__(self):
        retrievers = [
            Retriever("size", DataType("s32")),
            Retriever("width", DataType("u32")),
            Retriever("height", DataType("u32")),
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

        super().__init__("BitMap Info", retrievers)

    @staticmethod
    def defaults(pieces):
        defaults = {}
        return defaults
