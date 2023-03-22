from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct
from binary_file_parser.types import Bytes, uint8, uint32, int32, str16, str32


class AiFile(BaseStruct):
    unknown: bytes = Retriever(Bytes[8], default=b"\x00" * 8)
    per_content: list[str] = Retriever(str32, default="")

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)


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


class PlayerDataBlock2(BaseStruct):
    # formatter:off
    strings: list[str]         = Retriever(str16, default="", repeat=32)
    ai_names: list[str]        = Retriever(str16, default="", repeat=16)
    ai_files: list[AiFile]     = Retriever(AiFile, default=AiFile(), repeat=16)
    ai_types: list[int]        = Retriever(uint8, default=1, repeat=16)
    separator: int             = Retriever(uint32, default=4294967197)
    resources: list[Resources] = Retriever(Resources, default=Resources(), repeat=16)
    # formatter:on

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)
