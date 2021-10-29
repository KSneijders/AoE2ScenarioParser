"""
Don't hate the player, hate the g... name.
https://memeguy.com/photos/images/quick-maffs-288168.jpg
"""
import math
from typing import Union


def sign(a: Union[int, float], b: Union[int, float]) -> int:
    """
    Args:
        a (int|float): The first number
        b (int|float): The second number

    Returns:
        Returns 1 if a is higher than b, -1 if b is higher than a, and 0 when they're equal
    """
    return 0 if a == b else math.copysign(1, a - b)
