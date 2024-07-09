from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import bool32, uint32
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST


class GlobalVictory(BaseStruct):
    # @formatter:off
    conquest: bool                       = Retriever(bool32, default = True)
    capture_min_monuments: int           = Retriever(uint32, default = 0)
    """Ruins in aoe1"""
    collect_min_relics: int              = Retriever(uint32, default = 0)
    """Artifacts in aoe1"""
    make_min_remarkable_discoveries: int = Retriever(uint32, default = 0)
    """Only in aoe1"""
    explore_map_percent: int             = Retriever(uint32, default = 0)
    collect_gold: int                    = Retriever(uint32, default = 0)
    meet_all_conditions: bool            = Retriever(bool32, default = False)
    victory_type: int                    = Retriever(uint32, default = 4,    min_ver = Version((1, 13)))
    min_score: int                       = Retriever(uint32, default = 900,  min_ver = Version((1, 13)))
    time_limit: int                      = Retriever(uint32, default = 9000, min_ver = Version((1, 13)))
    """in 10ths of a year"""
    # @formatter:on

    def __init__(self, struct_ver: Version = DE_LATEST, initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
