from bfp_rs import BaseStruct, Retriever, Version
from bfp_rs.types.le import i32

from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class Resources(BaseStruct):
    __default_ver__ = DE_LATEST

    # todo: corresponding index to be accessed/updated for individual structs in list
    # @formatter:off
    gold: int          = Retriever(i32, default = 0)
    wood: int          = Retriever(i32, default = 0)
    food: int          = Retriever(i32, default = 0)
    stone: int         = Retriever(i32, default = 0)
    ore_x: int         = Retriever(i32, default = 0, min_ver = Version(1, 17))
    """unused"""
    trade_goods: int   = Retriever(i32, default = 0, min_ver = Version(1, 17))
    """unused"""
    player_color: int  = Retriever(i32, default = 0, min_ver = Version(1, 24))
    # @formatter:on
