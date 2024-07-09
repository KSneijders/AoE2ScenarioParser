from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int32
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class Resources(BaseStruct):
    # todo: corresponding index to be accessed/updated for individual structs in list
    # @formatter:off
    gold: int          = Retriever(int32, default = 0)
    wood: int          = Retriever(int32, default = 0)
    food: int          = Retriever(int32, default = 0)
    stone: int         = Retriever(int32, default = 0)
    ore_x: int         = Retriever(int32, default = 0, min_ver = Version((1, 17)))
    """unused"""
    trade_goods: int   = Retriever(int32, default = 0, min_ver = Version((1, 17)))
    """unused"""
    player_colour: int = Retriever(int32, default = 0, min_ver = Version((1, 24)))
    # @formatter:on

    def __init__(self, struct_ver: Version = DE_LATEST, initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
