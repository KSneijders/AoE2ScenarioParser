from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import (
    Array16, bool8, FixedLenArray, nt_str16, uint32,
    uint8,
)
from AoE2ScenarioParser.sections.scx_versions import DE_LATEST
from AoE2ScenarioParser.sections.unit_data.victory_options import VictoryOptions
from AoE2ScenarioParser.sections.unit_data.view import ViewF, ViewI


class ScenarioPlayerData(BaseStruct):
    # @formatter:off
    name: str                                = Retriever(nt_str16,                                             default = "Scenario Editor Phantom")
    editor_view: ViewF                       = Retriever(ViewF,                                                default_factory = lambda sv: ViewF(sv))
    initial_view: ViewI                      = Retriever(ViewI,                                                default_factory = lambda sv: ViewI(sv))
    aok_allied_victory: bool                 = Retriever(bool8,                                                default = False)
    diplomacy_stances_interaction: list[int] = Retriever(Array16[uint8],                                       default_factory = lambda _: [3, 0, 3, 3, 3, 3, 3, 3, 3])
    """aka relations"""
    diplomacy_stances_ai_system: list[int]   = Retriever(FixedLenArray[uint32, 9], min_ver = Version((1,  9)), default_factory = lambda _: [0, 1, 4, 4, 4, 4, 4, 4, 4])
    """aka unit_diplomacy"""
    colour: int                              = Retriever(uint32,                   min_ver = Version((1, 18)), default = 0)
    victory_options: VictoryOptions          = Retriever(VictoryOptions,                                       default_factory = lambda sv: VictoryOptions(sv))
    # @formatter:on

    def __init__(self, struct_ver: Version = DE_LATEST, initialise_defaults = True, **retriever_inits):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)
