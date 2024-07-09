from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int16
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class ViewI(BaseStruct):
    x: int = Retriever(int16, default = 60)
    y: int = Retriever(int16, default = 60)

    def __init__(self, struct_ver: Version = DE_LATEST, initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
