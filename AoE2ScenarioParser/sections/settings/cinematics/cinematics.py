from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import str16
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class Cinematics(BaseStruct):
    # @formatter:off
    pregame: str = Retriever(str16, default = "")
    victory: str = Retriever(str16, default = "")
    loss: str    = Retriever(str16, default = "")
    # @formatter:on

    def __init__(self, struct_ver: Version = DE_LATEST, initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
