from binary_file_parser import BaseStruct, Retriever, Version
from binary_file_parser.types import int32


class TileStruct(BaseStruct):
    _x: int = Retriever(int32, default=-1)
    _y: int = Retriever(int32, default=-1)

    def __init__(self, struct_ver: Version = Version((3, 5, 1, 47)), parent: BaseStruct = None, initialise_defaults=True, **retriever_inits):
        super().__init__(struct_ver, parent, initialise_defaults=initialise_defaults, **retriever_inits)

    def map(self) -> BaseStruct:
        from AoE2ScenarioParser.objects.support import Tile
        return Tile(self._x, self._y)
