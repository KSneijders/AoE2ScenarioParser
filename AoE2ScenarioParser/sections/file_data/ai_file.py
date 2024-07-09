from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import nt_str32
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class AiFile(BaseStruct):
    # @formatter:off
    file_name: str = Retriever(nt_str32, default = "")
    ai_rules: str  = Retriever(nt_str32, default = "")
    """From the .per file of an AI"""
    # @formatter:on

    def __init__(self, struct_ver: Version = DE_LATEST, initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
