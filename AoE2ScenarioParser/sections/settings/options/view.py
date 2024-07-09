from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int32
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class View(BaseStruct):
    x: int = Retriever(int32, default = -1)
    y: int = Retriever(int32, default = -1)

    def __init__(self, struct_ver: Version = DE_LATEST, initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
