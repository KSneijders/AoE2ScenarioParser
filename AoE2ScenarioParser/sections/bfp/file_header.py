from __future__ import annotations

from binary_file_parser import BaseStruct
from binary_file_parser.retrievers import Retriever
from binary_file_parser.types import FixedLenStr, uint32, int32, nt_str32, bool32, Array32


class FileHeader(BaseStruct):
    # @staticmethod
    # def update_num_triggers(retriever: Retriever, instance: FileHeader):
    #     instance.num_triggers = len(instance.parent.trigger_data.triggers)

    @staticmethod
    def set_timestamp_of_last_save_repeat(retriever: Retriever, instance: FileHeader):
        if instance.savable < 2:
            FileHeader.timestamp_of_last_save.set_repeat(instance, 0)

    file_version: str = Retriever(FixedLenStr[4], default="1.47")
    header_len: int = Retriever(uint32, default=0)
    savable: int = Retriever(int32, default=6, on_set=[set_timestamp_of_last_save_repeat])
    timestamp_of_last_save: int = Retriever(uint32, default=1610675127)
    scenario_instructions: str = Retriever(nt_str32, default="")
    individual_victories_used: bool = Retriever(bool32, default=False, max_ver=(1, 37))
    num_players: int = Retriever(uint32, default=2)
    unknown1: int = Retriever(uint32, default=1000)
    """always (?) 1k"""
    unknown2: int = Retriever(uint32, default=1)
    """always (?) 1"""
    required_dats: list[int] = Retriever(Array32[uint32], default=[2, 3, 4, 5, 6, 7])
    """2 = AoK; 3 = AoC; 4 = FE; 5 = AK; 6 = RoR; 7 = TLK; 8 = LotW; 9 = DotD; 10 = DI;"""
    creator: str = Retriever(nt_str32, default="AoE2SP")
    num_triggers: int = Retriever(uint32, default=0)  # on_write = [update_num_triggers])

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)
