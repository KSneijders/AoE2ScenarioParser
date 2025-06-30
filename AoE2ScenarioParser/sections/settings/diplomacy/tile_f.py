from bfp_rs import BaseStruct, Retriever, Version
from bfp_rs.types.le import f32

from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class TileF(BaseStruct):
    x: float = Retriever(f32, default = 0)
    y: float = Retriever(f32, default = 0)

    def __new__(cls, ver: Version = DE_LATEST, init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, init_defaults, **retriever_inits)
