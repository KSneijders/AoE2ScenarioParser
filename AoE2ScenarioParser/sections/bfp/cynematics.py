from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import str16


class Cinematics(BaseStruct):
    # @formatter:off
    pregame: str = Retriever(str16, default="")
    victory: str = Retriever(str16, default="")
    loss: str    = Retriever(str16, default="")
    # @formatter:on

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)
