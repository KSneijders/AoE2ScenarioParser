from __future__ import annotations

from bfp_rs import BaseStruct, com, ret, Retriever, RetrieverCombiner, RetrieverRef, Version
from bfp_rs.types.le import str_array32

from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class LegacyAiFile(BaseStruct):
    """This struct is useless"""

    __default_ver__ = DE_LATEST

    # the ._0 is a PyO3 thing that would need a lot of refactoring to fix. Something for future me to do
    _strings1: list[str] = Retriever(str_array32._0[2], max_ver = Version(1, 7), default_factory = lambda _: [""] * 2)
    _strings2: list[str] = Retriever(str_array32._0[3], min_ver = Version(1, 8), default_factory = lambda _: [""] * 3)

    _strings: list[str] = RetrieverCombiner(ret(_strings2), ret(_strings1))

    # @formatter:off
    build_list: str = RetrieverRef(com(_strings), 0)
    """unused?"""
    city_plans: str = RetrieverRef(com(_strings), 1)
    """unused?"""
    ai_rules: str   = RetrieverRef(com(_strings), 2)
    """From the .per file of an AI"""
    # @formatter:on
