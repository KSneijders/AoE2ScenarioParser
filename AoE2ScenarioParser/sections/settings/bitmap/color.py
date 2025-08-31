from bfp_rs import BaseStruct, Retriever, Version
from bfp_rs.types.le import u8

from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class Color(BaseStruct):
    __default_ver__ = DE_LATEST

    blue: int = Retriever(u8, default = 0)
    green: int = Retriever(u8, default = 0)
    red: int = Retriever(u8, default = 0)
    reversed: int = Retriever(u8, default = 0)
    """unused"""
