from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import float32
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class WorldPlayerData(BaseStruct):
    """All data here is duplicated except pop limit"""

    # @formatter:off
    food: float             = Retriever(float32,                             default = 200)
    wood: float             = Retriever(float32,                             default = 200)
    gold: float             = Retriever(float32,                             default = 200)
    stone: float            = Retriever(float32,                             default = 200)
    ore_x: float            = Retriever(float32, min_ver = Version((1, 18)), default = 100)
    trade_goods: float      = Retriever(float32, min_ver = Version((1, 18)), default = 0.0)
    population_limit: float = Retriever(float32, min_ver = Version((1, 20)), default = 200.0)
    # @formatter:on

    def __init__(self, struct_ver: Version = DE_LATEST, initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
