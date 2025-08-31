from bfp_rs import BaseStruct, Retriever
from bfp_rs.types.le import bool32, i32, u32

from AoE2ScenarioParser.sections.scx_versions import DE_LATEST
from AoE2ScenarioParser.sections.settings.diplomacy.area_f import AreaF


class LegacyVictoryInfo(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    unit_type: int                = Retriever(i32,    default = 0)
    all: bool                     = Retriever(bool32, default = False)
    player: int                   = Retriever(i32,    default = 0)
    destination_object_ref: int   = Retriever(i32,    default = 0)
    area: AreaF                   = Retriever(AreaF,  default_factory = AreaF)
    victory_type: int             = Retriever(i32,    default = 0)
    quantity: int                 = Retriever(i32,    default = 0)
    resource: int                 = Retriever(i32,    default = 0)
    object_ref: int               = Retriever(i32,    default = 0)
    destination_object_ref2: int  = Retriever(i32,    default = 0)
    object: int                   = Retriever(u32,    default = 0)
    """unused"""
    destination_object: int       = Retriever(u32,    default = 0)
    """unused"""
    # @formatter:on
