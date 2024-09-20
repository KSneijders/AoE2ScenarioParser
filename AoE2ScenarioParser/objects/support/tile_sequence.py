import abc
from typing import Callable

from ordered_set import OrderedSet
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from AoE2ScenarioParser.objects.support import Tile
    from AoE2ScenarioParser.objects.support.typedefs import T


class TileSequence:
    def map(self, callback: Callable[['Tile'], 'T']) -> dict['Tile', 'T']:
        """
        Map every tile inside this area. Applies the given callable to every tile in this pattern.
        Returns as a dict where the tile used in the callback is the key

        Args:
            callback: The callable to be applied to every tile

        Returns:
            A dict containing `{key: <return of callable>}` for each tile in this pattern
        """
        return {tile: callback(tile) for tile in self.to_tiles()}

    @abc.abstractmethod
    def to_tiles(self) -> OrderedSet['Tile']:
        ...
