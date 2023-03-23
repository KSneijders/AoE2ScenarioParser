from __future__ import annotations

from binary_file_parser import Retriever, BaseStruct
from binary_file_parser.types import bool32, Bytes, uint32, uint8, StackedArray32s

from AoE2ScenarioParser.sections.bfp.map_data import View


class Options(BaseStruct):
    @staticmethod
    def update_num_triggers(_, instance: Options):
        instance.num_triggers = len(instance.parent.trigger_data.triggers)

    # formatter:off
    disabled_tech_ids: list[list[int]]     = Retriever(StackedArray32s[uint32, 16], default=[[] for _ in range(16)])
    disabled_unit_ids: list[list[int]]     = Retriever(StackedArray32s[uint32, 16], default=[[] for _ in range(16)])
    disabled_building_ids: list[list[int]] = Retriever(StackedArray32s[uint32, 16], default=[[] for _ in range(16)])
    combat_mode: bool                      = Retriever(bool32,                      default=False)
    naval_mode: bool                       = Retriever(bool32,                      default=False)
    all_techs: bool                        = Retriever(bool32,                      default=False)
    starting_ages: list[int]               = Retriever(uint32,                      default=2, repeat=16)
    separator: bytes                       = Retriever(Bytes[4],                    default=b"\x9d\xff\xff\xff")
    player1_view: View                     = Retriever(View,                        default=View())
    ai_map_type_unused_1_45: int           = Retriever(uint32, max_ver=(1, 45),     default=2, )
    ai_map_type_unused_1_46: int           = Retriever(uint32, (1, 46), (1, 46),    default=22)
    ai_map_type: int                       = Retriever(uint32, (1, 47),             default=0)
    unknown3: bytes                        = Retriever(Bytes[1],                    default=b"\x00")
    base_priorities: list[int]             = Retriever(uint8,                       default=0, repeat=8)
    unknown2: bytes                        = Retriever(Bytes[7],                    default=b"\x00" * 7)
    num_triggers: int                      = Retriever(uint32,                      default=0, on_write=[update_num_triggers])
    # formatter:on

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)
