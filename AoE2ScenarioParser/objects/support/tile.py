from typing import NamedTuple


class Tile(NamedTuple):
    """NamedTuple for tiles. use tile.x or tile.y for coord access"""
    x: int
    y: int
