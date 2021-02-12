from AoE2ScenarioParser.helper.datatype import DataType
from AoE2ScenarioParser.helper.retriever import Retriever
from AoE2ScenarioParser.helper.retriever_dependency import RetrieverDependency, DependencyAction, DependencyTarget, \
    DependencyEval
from AoE2ScenarioParser.pieces.aoe2_file_section import AoE2FileSection
from AoE2ScenarioParser.pieces.structs.bitmap_info import BitMapInfoStruct


class BackgroundImagePiece(AoE2FileSection):
    dependencies = {
        'bitmap_info': {
            "on_construct": RetrieverDependency(
                DependencyAction.SET_REPEAT, DependencyTarget("self", "picture_orientation"),
                DependencyEval("1 if x in [-1, 2] else 0")
            )
        },
    }

    def __init__(self):
        retrievers = [
            Retriever("ascii_filename", DataType("str16")),
            Retriever("picture_version", DataType("u32")),
            Retriever("bitmap_width", DataType("u32")),
            Retriever("bitmap_height", DataType("s32")),
            Retriever("picture_orientation", DataType("s16")),
            Retriever("bitmap_info", DataType(BitMapInfoStruct), possibly_list=False),
        ]

        super().__init__("BackgroundImagePiece", retrievers)

    @staticmethod
    def defaults(pieces):
        defaults = {
            'ascii_filename': '',
            'picture_version': 3,
            'bitmap_width': 0,
            'bitmap_height': 0,
            'picture_orientation': 1,
            'bitmap_info': []
        }
        return defaults
