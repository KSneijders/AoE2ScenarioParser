from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, RetrieverCombiner, RetrieverRef, Version
from binary_file_parser.types import StrArray32
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class LegacyAiFile(BaseStruct):
    """This struct is useless"""

    _strings1: list[str] = Retriever(StrArray32[2], max_ver = Version((1, 7)), default_factory = lambda _: [""] * 2)
    _strings2: list[str] = Retriever(StrArray32[3], min_ver = Version((1, 8)), default_factory = lambda _: [""] * 3)

    # refs
    _strings: list[str] = RetrieverCombiner(_strings2, _strings1)

    # @formatter:off
    build_list: str = RetrieverRef(_strings, 0)
    """unused?"""
    city_plans: str = RetrieverRef(_strings, 1)
    """unused?"""
    ai_rules: str   = RetrieverRef(_strings, 2)
    """From the .per file of an AI"""
    # @formatter:on

    def __init__(self, struct_ver: Version = DE_LATEST, initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
