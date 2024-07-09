from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import bool32, int32, uint32
from AoE2ScenarioParser.sections.settings.diplomacy.area_f import AreaF
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class LegacyVictoryInfo(BaseStruct):
    # @formatter:off
    unit_type: int                = Retriever(int32,   default = 0)
    all: bool                     = Retriever(bool32,  default = 0)
    player: int                   = Retriever(int32,   default = 0)
    destination_object_ref: int   = Retriever(int32,   default = 0)
    area: AreaF                   = Retriever(AreaF,   default_factory = AreaF)
    victory_type: int             = Retriever(int32,   default = 0)
    quantity: int                 = Retriever(int32,   default = 0)
    resource: int                 = Retriever(int32,   default = 0)
    object_ref: int               = Retriever(int32,   default = 0)
    destination_object_ref2: int  = Retriever(int32,   default = 0)
    object: int                   = Retriever(uint32,  default = 0)
    """unused"""
    destination_object: int       = Retriever(uint32,  default = 0)
    """unused"""
    # @formatter:on

    def __init__(self, struct_ver: Version = DE_LATEST, initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
