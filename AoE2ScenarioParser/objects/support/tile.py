from __future__ import annotations

from collections import namedtuple
from typing import Type

Tile: Type[Tile] = namedtuple('Tile', ['x', 'y'])
"""NamedTuple for tiles. use tile.x or tile.y for coord access"""
