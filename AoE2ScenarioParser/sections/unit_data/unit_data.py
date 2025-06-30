from __future__ import annotations

from bfp_rs import BaseStruct, ret, Retriever, RetrieverCombiner, Version
from bfp_rs.combinators import get, get_len, set_, set_repeat
from bfp_rs.types.le import (
    Array32, u32,
)

from AoE2ScenarioParser.sections.scx_versions import DE_LATEST
from AoE2ScenarioParser.sections.unit_data.scenario_player_data import ScenarioPlayerData
from AoE2ScenarioParser.sections.unit_data.unit import Unit
from AoE2ScenarioParser.sections.unit_data.world_player_data import WorldPlayerData


def world_player_data_repeat():
    return [
        set_repeat(ret(UnitData.world_player_data)).by(get(ret(UnitData._num_world_players)) - 1)
    ]


def sync_num_world_players():
    return [
        set_(ret(UnitData._num_world_players)).by(get_len(ret(UnitData.world_player_data)) + 1)
    ]


def scx_player_data_repeat():
    return [
        set_repeat(ret(UnitData.scenario_player_data)).by(get(ret(UnitData._num_scenario_players)) - 1)
    ]


def sync_num_scx_players():
    return [
        set_(ret(UnitData._num_scenario_players)).by(get_len(ret(UnitData.scenario_player_data)) + 1)
    ]


class UnitData(BaseStruct):
    # @formatter:off
    # these lists can't be Array32s because the length is -1 the num_value. yES
    _num_world_players: int                        = Retriever(u32,                                          default = 9,                                     on_read = world_player_data_repeat, on_write = sync_num_world_players)
    world_player_data: list[WorldPlayerData]       = Retriever(WorldPlayerData,    min_ver = Version(1,  7), default_factory = WorldPlayerData,    repeat = 8)

    _units_aoc: list[list[Unit]]                   = Retriever(Array32[Unit],      max_ver = Version(1, 33), default_factory = lambda _: [],       repeat = 9)
    _num_scenario_players: int                     = Retriever(u32,                                          default = 9,                                     on_read = scx_player_data_repeat,   on_write = sync_num_scx_players)
    scenario_player_data: list[ScenarioPlayerData] = Retriever(ScenarioPlayerData,                           default_factory = ScenarioPlayerData, repeat = 8)
    _units_de: list[list[Unit]]                    = Retriever(Array32[Unit],      min_ver = Version(1, 36), default_factory = lambda _: [],       repeat = 9)

    units: list[list[Unit]]                        = RetrieverCombiner(ret(_units_de), ret(_units_aoc))
    # @formatter:on

    def __new__(cls, ver: Version = DE_LATEST, init_defaults = True, **retriever_inits):
        return super().__new__(cls, ver, init_defaults, **retriever_inits)
