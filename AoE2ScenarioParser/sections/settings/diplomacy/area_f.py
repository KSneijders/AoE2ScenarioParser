from bfp_rs import BaseStruct, Context, Retriever, Version

from AoE2ScenarioParser.sections.scx_versions import DE_LATEST
from AoE2ScenarioParser.sections.settings.diplomacy.tile_f import TileF


class AreaF(BaseStruct):
    corner1: TileF = Retriever(TileF, default_factory = TileF)
    corner2: TileF = Retriever(TileF, default_factory = TileF)

    def __new__(cls, ver: Version = DE_LATEST, ctx: Context = Context(), init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, ctx, init_defaults, **retriever_inits)