from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct
from binary_file_parser.types import (
    bool8, Bytes, uint32, uint8, int16, uint16, int32,
    nt_str16, Array16, FixedLenArray, Array32, float32
)


class PlayerDataBlock4(BaseStruct):
    food: float = Retriever(float32, default=0.0)
    """duplicate"""
    wood: float = Retriever(float32, default=0.0)
    """duplicate"""
    gold: float = Retriever(float32, default=0.0)
    """duplicate"""
    stone: float = Retriever(float32, default=0.0)
    """duplicate"""
    ore_x: float = Retriever(float32, default=0.0)
    """duplicate"""
    trade_goods: float = Retriever(float32, default=0.0)
    population_limit: float = Retriever(float32, default=200.0)

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)


class ViewF(BaseStruct):
    x: float = Retriever(float32, default=60.0)
    y: float = Retriever(float32, default=60.0)

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)


class ViewI(BaseStruct):
    x: int = Retriever(int16, default=60)
    y: int = Retriever(int16, default=60)

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)


class PlayerDataBlock3(BaseStruct):
    @staticmethod
    def set_unknown2_repeat(_, instance: PlayerDataBlock3):
        Retriever.set_repeat(PlayerDataBlock3.unknown2, instance, 7 if instance.victory_version == 2.0 else -1)

    @staticmethod
    def set_num_wwc2_repeat(_, instance: PlayerDataBlock3):
        if instance.victory_version != 2.0:
            Retriever.set_repeat(PlayerDataBlock3.num_ww_campaign2, instance, -1)

    @staticmethod
    def set_gte_repeat(_, instance: PlayerDataBlock3):
        Retriever.set_repeat(PlayerDataBlock3.grand_theft_empires, instance, instance.num_grand_theft_empires)

    @staticmethod
    def set_wwc2_repeat(_, instance: PlayerDataBlock3):
        Retriever.set_repeat(PlayerDataBlock3.ww_campaign2, instance, instance.num_ww_campaign2)

    @staticmethod
    def update_num_gte(_, instance: PlayerDataBlock3):
        instance.num_grand_theft_empires = len(instance.grand_theft_empires)

    @staticmethod
    def update_num_wwc2(_, instance: PlayerDataBlock3):
        instance.num_ww_campaign2 = len(instance.ww_campaign2)

    # formatter:off
    constant_name: str                       = Retriever(nt_str16,                 default="Scenario Editor Phantom")
    editor_view: ViewF                       = Retriever(ViewF,                    default=ViewF())
    initial_view: ViewI                      = Retriever(ViewI,                    default=ViewI())
    aok_allied_victory: bool                 = Retriever(bool8,                    default=False)
    diplomacy_stances_interaction: list[int] = Retriever(Array16[uint8],           default=[3, 0, 3, 3, 3, 3, 3, 3, 3])
    diplomacy_stances_ai_system: list[int]   = Retriever(FixedLenArray[uint32, 9], default=[0, 1, 4, 4, 4, 4, 4, 4, 4])
    colour: int                              = Retriever(uint32,                   default=0)
    victory_version: float                   = Retriever(float32,                  default=2.0, on_set=[set_unknown2_repeat, set_num_wwc2_repeat])
    num_grand_theft_empires: int             = Retriever(uint16,                   default=0, on_set=[set_gte_repeat], on_write=[update_num_gte])
    unknown2: list[int]                      = Retriever(uint8,                    default=0, repeat=7)
    grand_theft_empires: list[bytes]         = Retriever(Bytes[44],                default=b"\x00" * 44)
    """unknown structure"""
    num_ww_campaign2: int                    = Retriever(uint8,                    default=0, on_set=[set_wwc2_repeat], on_write=[update_num_wwc2])
    unknown3: int                            = Retriever(uint8,                    default=0, repeat=7)
    ww_campaign2: list[bytes]                = Retriever(Bytes[32],                default=[], repeat=0)
    """unknown structure"""
    unknown4: int                            = Retriever(int32,                    default=-1)
    # formatter:on

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)


class Unit(BaseStruct):
    # formatter:off
    x: float                        = Retriever(float32, default=0.5)
    y: float                        = Retriever(float32, default=0.5)
    z: float                        = Retriever(float32, default=0)
    reference_id: int               = Retriever(int32, default=0)
    const: int                      = Retriever(uint16, default=4)
    status: int                     = Retriever(uint8, default=2)
    rotation: float                 = Retriever(float32, default=0)
    initial_animation_frame: int    = Retriever(uint16, default=0)
    garrisoned_in_reference_id: int = Retriever(int32, default=-1)
    # formatter:on

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)


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

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)
