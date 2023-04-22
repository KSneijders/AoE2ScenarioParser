from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct, Version
from binary_file_parser.types import (
    uint32, Array32
)

from AoE2ScenarioParser.sections.bfp.units.player_data_block_3 import PlayerDataBlock3
from AoE2ScenarioParser.sections.bfp.units.player_data_block_4 import PlayerDataBlock4
from AoE2ScenarioParser.sections.bfp.units.unit import Unit


class UnitData(BaseStruct):
    @staticmethod
    def set_units_repeat(_, instance: UnitData):
        Retriever.set_repeat(UnitData.units, instance, instance.num_unit_lists)

    @staticmethod
    def update_num_unit_lists(_, instance: UnitData):
        instance.num_unit_lists = len(instance.units)
        instance.num_players = len(instance.units)

    # formatter:off
    num_unit_lists: int                  = Retriever(uint32,           default=9, on_set=[set_units_repeat], on_write=[update_num_unit_lists])
    player_data4: list[PlayerDataBlock4] = Retriever(PlayerDataBlock4, default=PlayerDataBlock4(), repeat=8)
    num_players: int                     = Retriever(uint32,           default=9)
    player_data3: list[PlayerDataBlock3] = Retriever(PlayerDataBlock3, default=PlayerDataBlock3(), repeat=8)
    units: list[list[Unit]]              = Retriever(Array32[Unit],    default=[])
    # formatter:on

    def __init__(self, struct_ver: Version = Version((1, 47)), parent: BaseStruct = None, initialise_defaults=True, **retriever_inits):
        super().__init__(struct_ver, parent, initialise_defaults=initialise_defaults, **retriever_inits)
