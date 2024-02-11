from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import str16, uint32, uint8

from AoE2ScenarioParser.sections.bfp.player_data_block_2.ai_file import AiFile
from AoE2ScenarioParser.sections.bfp.player_data_block_2.resources import Resources


class PlayerDataBlock2(BaseStruct):
    # @formatter:off
    strings: list[str]         = Retriever(str16,     default = "",          repeat=32)
    ai_names: list[str]        = Retriever(str16,     default = "",          repeat=16)
    ai_files: list[AiFile]     = Retriever(AiFile,    default_factory = lambda sv, p: AiFile(sv, p),    repeat=16)
    ai_types: list[int]        = Retriever(uint8,     default = 1,           repeat=16)
    separator: int             = Retriever(uint32,    default = 4294967197)
    resources: list[Resources] = Retriever(Resources, default_factory = lambda sv, p: Resources(sv, p), repeat=16)
    # @formatter:on

    def __init__(
        self, struct_ver: Version = Version((1, 47)), parent: BaseStruct = None, initialise_defaults = True,
        **retriever_inits
    ):
        super().__init__(struct_ver, parent, initialise_defaults = initialise_defaults, **retriever_inits)