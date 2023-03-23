from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import bool32, uint32


class PlayerDataBlock1(BaseStruct):
    # @formatter:off
    active: bool               = Retriever(bool32,                   default=False)
    human: bool                = Retriever(bool32,                   default=False)
    civilization_1_36: int     = Retriever(uint32, (1, 36), (1, 40), default=36)
    civilization_1_41: int     = Retriever(uint32, (1, 41), (1, 42), default=38)
    civilization_1_43: int     = Retriever(uint32, (1, 43), (1, 45), default=40)
    civilization_1_46: int     = Retriever(uint32, (1, 46),          default=43)
    architecture_set_1_40: int = Retriever(uint32, (1, 40), (1, 40), default=36)
    architecture_set_1_41: int = Retriever(uint32, (1, 41), (1, 42), default=38)
    architecture_set_1_43: int = Retriever(uint32, (1, 43), (1, 45), default=40)
    architecture_set_1_46: int = Retriever(uint32, (1, 46),          default=43)
    cty_mode: int              = Retriever(uint32,                   default=4)
    # @formatter:on

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)
