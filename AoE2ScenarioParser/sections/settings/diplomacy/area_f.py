from bfp_rs import BaseStruct, Retriever

from AoE2ScenarioParser.sections.scx_versions import DE_LATEST
from AoE2ScenarioParser.sections.settings.diplomacy.tile_f import TileF


class AreaF(BaseStruct):
    __default_ver__ = DE_LATEST

    corner1: TileF = Retriever(TileF, default_factory = TileF)
    corner2: TileF = Retriever(TileF, default_factory = TileF)
