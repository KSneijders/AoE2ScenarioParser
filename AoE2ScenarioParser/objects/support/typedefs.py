from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Union, Tuple, TypeVar

from typing_extensions import Iterable

if TYPE_CHECKING:
    from AoE2ScenarioParser.objects.support import AreaPattern, Tile
    from AoE2ScenarioParser.objects.support import Area
    from AoE2ScenarioParser.objects.data_objects.trigger import Trigger
    from typing import TypeAlias
    var = Trigger, TypeAlias, AreaPattern, Tile, Area
    # These are functionally redundant, but they tell PyCharm to not remove the 2 imports above
    # It considers the imports unused even though they DO actually help PyCharm understand types in other files...

TriggerIdentifier: 'TypeAlias' = Union[int, 'Trigger']
TileT = Union[Tuple[int, int], 'Tile']
AreaT = Union['Area', Tuple[TileT, TileT], Tuple[TileT]]

Scenario: TypeVar = TypeVar('Scenario', bound='AoE2Scenario')
"""A type variable (generic) that represents an instance of the AoE2Scenario class or any of its subclasses"""

T = TypeVar('T')

Func: TypeVar = TypeVar('Func', bound='Callable[[Any], Any]')
"""A type variable (generic) that represents a function"""
