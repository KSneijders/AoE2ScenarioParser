from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import nt_str32, uint32
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST, TRIGGER_LATEST


class Variable(BaseStruct):
    # @formatter:off
    id: int   = Retriever(uint32, default = 0)
    name: str = Retriever(nt_str32, default = "_Variable")
    # @formatter:on

    def __init__(self, struct_ver: Version = TRIGGER_LATEST, initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
