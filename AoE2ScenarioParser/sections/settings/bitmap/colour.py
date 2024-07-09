from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import uint8


class Colour(BaseStruct):
    red: int   = Retriever(uint8, default = 0)
    green: int = Retriever(uint8, default = 0)
    blue: int  = Retriever(uint8, default = 0)
    alpha: int = Retriever(uint8, default = 0)
    """unused"""

    def __init__(
        self,
        struct_ver: Version = Version((1, 47)),
        initialise_defaults = True,
        **retriever_inits
    ):
        super().__init__(struct_ver, initialise_defaults = initialise_defaults, **retriever_inits)