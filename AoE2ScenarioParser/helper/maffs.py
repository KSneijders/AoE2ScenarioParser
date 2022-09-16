"""
Don't hate the player, hate the g... name.
https://memeguy.com/photos/images/quick-maffs-288168.jpg
"""
from __future__ import annotations

import math


def sign(a: int | float, b: int | float) -> int:
    """
    Args:
        a: The first number
        b: The second number

    Returns:
        Returns 1 if a is higher than b, -1 if b is higher than a, and 0 when they're equal
    """
    return 0 if a == b else math.copysign(1, a - b)
