from bfp_rs import BaseStruct, Retriever, Version

from AoE2ScenarioParser.sections.settings.diplomacy.tile_f import TileF
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class AreaF(BaseStruct):
    corner1: TileF = Retriever(TileF, default_factory = TileF)
    corner2: TileF = Retriever(TileF, default_factory = TileF)

    def __new__(cls, ver: Version = DE_LATEST, init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, init_defaults, **retriever_inits)
