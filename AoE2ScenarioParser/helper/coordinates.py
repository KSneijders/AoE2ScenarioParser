from __future__ import annotations

from typing import Tuple, TYPE_CHECKING

from AoE2ScenarioParser.helper.helper import value_is_valid
from AoE2ScenarioParser.helper.printers import warn

if TYPE_CHECKING:
    from AoE2ScenarioParser.objects.support.tile import Tile


def xy_to_i(x, y, map_size) -> int:
    if max(x, y) >= map_size or min(x, y) < 0:
        raise ValueError("X and Y need to be: 0 <= n < map_size")
    return x + y * map_size


def i_to_xy(i, map_size) -> tuple[int, int]:
    if i < 0 or i >= pow(map_size, 2):
        raise ValueError(f"X and Y need to be: 0 <= n ({i}) < map_size ({map_size})")
    return int(i % map_size), int(i / map_size)


def validate_coords(
        x1: int = None,
        y1: int = None,
        x2: int = None,
        y2: int = None,
        corner1: Tile = None,
        corner2: Tile = None,
) -> Tuple[int, int, int, int]:
    """
    Validates given coordinates.

    - Swaps x/y1 with x/y2 if 1 is higher than it's 2 counterpart
    - Sets x/y2 to x/y1 if it's not been set.

    Args:
        x1: The X location of the left corner
        y1: The Y location of the left corner
        x2: The X location of the right corner
        y2: The Y location of the right corner
        corner1: The location of the left corner
        corner2: The location of the right corner

    Returns:
        The updated values through a tuple as (x1, y1, x2, y2)
    """
    if value_is_valid(corner1):
        x1, y1 = corner1.x, corner1.y
    if value_is_valid(corner2):
        x2, y2 = corner2.x, corner2.y
    if value_is_valid(x1) and not value_is_valid(x2):
        x2 = x1
    if value_is_valid(y1) and not value_is_valid(y2):
        y2 = y1
    if x1 > x2:
        x1, x2 = x2, x1
        warn("Swapping 'x1' and 'x2' values. Attribute 'x1' cannot be higher than 'x2'")
    if y1 > y2:
        y1, y2 = y2, y1
        warn("Swapping 'y1' and 'y2' values. Attribute 'y1' cannot be higher than 'y2'")
    return x1, y1, x2, y2
