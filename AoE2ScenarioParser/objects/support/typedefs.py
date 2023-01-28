from typing import Union, Tuple

from AoE2ScenarioParser.objects.support.area import Area

TileT = Tuple[int, int]
AreaT = Union[Area, Tuple[TileT, TileT], Tuple[TileT]]
