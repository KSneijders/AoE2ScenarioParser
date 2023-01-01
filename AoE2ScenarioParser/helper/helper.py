from __future__ import annotations

import math
from enum import Enum
from typing import Tuple, Any

from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.other import OtherInfo
from AoE2ScenarioParser.datasets.support.info_dataset_base import InfoDatasetBase
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.exceptions import asp_exceptions
from AoE2ScenarioParser.helper.printers import warn
from AoE2ScenarioParser.objects.support.tile import Tile

""" =============================================================
============================ COORDS =============================
=============================================================="""


def xy_to_i(x: int, y: int, map_size: int) -> int:
    """
    Converts 2-dimensional map coordinates to 1-dimensional array index

    Args:
        x: The x coordinate on the map
        y: The y coordinate on the map
        map_size: The size of the map

    Returns:
        The 1-dimensional array index for the given 2-dimensional map coordinates and specified map size
    """
    if max(x, y) >= map_size or min(x, y) < 0:
        raise ValueError("X and Y need to be: 0 <= n < map_size")
    return x + y * map_size


def i_to_xy(i: int, map_size: int) -> Tuple[int, int]:
    """
    Converts 1-dimensional array index to 2-dimensional map coordinates

    Args:
        i: The index in the 1-dimensional array
        map_size: The size of the map

    Returns:
        A tuple containing the (x, y) coordinates for the given 1-dimensional array index and specified map size
    """
    if i < 0 or i >= pow(map_size, 2):
        raise ValueError(f"X and Y need to be: 0 <= n ({i}) < map_size ({map_size})")
    return Tile(int(i % map_size), int(i / map_size))


""" =============================================================
============================= OTHER =============================
=============================================================="""


def value_is_valid(value: Any) -> bool:
    """
    Check if value is valid by making sure it's neither -1 nor None

    Args:
        value:

    Returns:
        `True` if value is not None or -1. `False` if it is either of those.
    """
    return value not in [None, -1]


def values_are_valid(*args: Any) -> bool:
    """
    Check if value is valid by making sure it's not -1 nor None

    Returns:
        `True` if all values are not None or -1. `False` if any of them are either of those.
    """
    return any(map(lambda v: v not in [None, -1], args))


def get_enum_from_unit_const(const: int) -> InfoDatasetBase | None:
    """
    Get the enum value for the given unit constant

    Args:
        const: The unit ID

    Returns:
        The enum value for the given unit constant
    """
    enums = [UnitInfo, BuildingInfo, HeroInfo, OtherInfo]
    for enum in enums:
        try:
            return enum.from_id(const)
        except (ValueError, KeyError):
            continue
    return None


def get_int_len(num: int) -> int:
    """
    Get the length (in digits) of the given number

    Args:
        num: The number to find the length

    Returns:
        The length of the given number
    """
    if num > 0:
        return math.floor(math.log10(num))
    return 0


def mutually_exclusive(*args) -> bool:
    """
    `True` only if one of the entries is true, `False` otherwise.

    Args:
        *args: values that can be converted to booleans

    Returns:
        True/False
    """
    return sum(map(bool, args)) == 1


def raise_if_not_int_subclass(values):
    for v in values:
        if not issubclass(v.__class__, int):
            raise TypeError(asp_exceptions.type_error_message(v, issubclass(v.__class__, Enum)))


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


def typename(x: Any):
    """Get the name of the class of the given object"""
    return type(x).__name__
