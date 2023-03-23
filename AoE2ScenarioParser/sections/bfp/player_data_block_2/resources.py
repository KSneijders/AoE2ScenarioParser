from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import int32


class Resources(BaseStruct):
    # todo: parents on list structs
    # todo: corresponding index to be accessed/updated for individual structs in list
    @staticmethod
    def update_player_data4_attr(instance: Resources, attr: str):
        unit_data = instance.parent.parent.unit_data
        for i in range(8):
            setattr(unit_data.player_data4[i], attr, getattr(instance.parent.resources[i], attr))

    @staticmethod
    def update_player_data4_gold(_, instance: Resources):
        Resources.update_player_data4_attr(instance, 'gold')

    @staticmethod
    def update_player_data4_wood(_, instance: Resources):
        Resources.update_player_data4_attr(instance, 'wood')

    @staticmethod
    def update_player_data4_food(_, instance: Resources):
        Resources.update_player_data4_attr(instance, 'food')

    @staticmethod
    def update_player_data4_stone(_, instance: Resources):
        Resources.update_player_data4_attr(instance, 'stone')

    @staticmethod
    def update_player_data4_ore_x(_, instance: Resources):
        Resources.update_player_data4_attr(instance, 'ore_x')

    @staticmethod
    def update_player_data4_trade_goods(_, instance: Resources):
        Resources.update_player_data4_attr(instance, 'trade_goods')

    # formatter:off
    gold: int          = Retriever(int32, default=0, on_write=[update_player_data4_gold])
    wood: int          = Retriever(int32, default=0, on_write=[update_player_data4_wood])
    food: int          = Retriever(int32, default=0, on_write=[update_player_data4_food])
    stone: int         = Retriever(int32, default=0, on_write=[update_player_data4_stone])
    ore_x: int         = Retriever(int32, default=0, on_write=[update_player_data4_ore_x])
    trade_goods: int   = Retriever(int32, default=0, on_write=[update_player_data4_trade_goods])
    player_colour: int = Retriever(int32, default=0)
    # formatter:on

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)
