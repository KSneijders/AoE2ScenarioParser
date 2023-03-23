from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import nt_str16, bool8, Array16, uint8, FixedLenArray, uint32, float32, uint16, Bytes, \
    int32

from AoE2ScenarioParser.sections.bfp.units.view_i import ViewI
from AoE2ScenarioParser.sections.bfp.units.view_f import ViewF


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
