from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import uint32, str16


class Messages(BaseStruct):
    # formatter:off
    instructions_str_id: int = Retriever(uint32, default=4294967294)
    hints_str_id: int        = Retriever(uint32, default=4294967294)
    victory_str_id: int      = Retriever(uint32, default=4294967294)
    loss_str_id: int         = Retriever(uint32, default=4294967294)
    history_str_id: int      = Retriever(uint32, default=4294967294)
    scouts_str_id: int       = Retriever(uint32, default=4294967294)
    instructions: str        = Retriever(str16,  default="")
    hints: str               = Retriever(str16,  default="")
    victory: str             = Retriever(str16,  default="This scenario was created using AoE2ScenarioParser! Hopefully you enjoyed!")
    loss: str                = Retriever(str16,  default="This scenario was created using AoE2ScenarioParser! Hopefully you enjoyed!")
    history: str             = Retriever(str16,  default="")
    scouts: str              = Retriever(str16,  default="")
    # formatter:on

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)
