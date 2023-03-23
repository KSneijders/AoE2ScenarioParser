from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct
from binary_file_parser.types import uint8, uint32, str16

from AoE2ScenarioParser.sections.bfp.player_data_block_2.ai_file import AiFile
from AoE2ScenarioParser.sections.bfp.player_data_block_2.resources import Resources


class PlayerDataBlock2(BaseStruct):
    # formatter:off
    strings: list[str]         = Retriever(str16, default="", repeat=32)
    ai_names: list[str]        = Retriever(str16, default="", repeat=16)
    ai_files: list[AiFile]     = Retriever(AiFile, default=AiFile(), repeat=16)
    ai_types: list[int]        = Retriever(uint8, default=1, repeat=16)
    separator: int             = Retriever(uint32, default=4294967197)
    resources: list[Resources] = Retriever(Resources, default=Resources(), repeat=16)
    # formatter:on

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)
