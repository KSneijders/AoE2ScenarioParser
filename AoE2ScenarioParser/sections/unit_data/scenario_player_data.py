from __future__ import annotations

from bfp_rs import BaseStruct, Retriever, Version
from bfp_rs.types.le import (Array, Array16, bool8, nt_str16, u32, u8)

from AoE2ScenarioParser.sections.scx_versions import DE_LATEST
from AoE2ScenarioParser.sections.unit_data.victory_options import VictoryOptions
from AoE2ScenarioParser.sections.unit_data.view import ViewF, ViewI


class ScenarioPlayerData(BaseStruct):
    __default_ver__ = DE_LATEST

    # @formatter:off
    name: str                                = Retriever(nt_str16,                                 default = "Scenario Editor Phantom")
    editor_view: ViewF                       = Retriever(ViewF,                                    default_factory = ViewF)
    """The location the editor starts at when viewing this map"""
    initial_view: ViewI                      = Retriever(ViewI,                                    default_factory = ViewI)
    """Written when clicking "Go to View" - Unused in editor & game"""
    aok_allied_victory: bool                 = Retriever(bool8,                                    default = False)
    diplomacy_stances_interaction: list[int] = Retriever(Array16[u8],                              default_factory = lambda _: [3, 0, 3, 3, 3, 3, 3, 3, 3])
    """aka relations"""
    # :prayge:
    diplomacy_stances_ai_system: list[int]   = Retriever(Array[9][u32],  min_ver = Version(1,  9), default_factory = lambda _: [0, 1, 4, 4, 4, 4, 4, 4, 4])
    """aka unit_diplomacy"""
    color: int                               = Retriever(u32,            min_ver = Version(1, 17), default = 0)
    victory_options: VictoryOptions          = Retriever(VictoryOptions,                           default_factory = lambda _ver: VictoryOptions())
    # @formatter:on
