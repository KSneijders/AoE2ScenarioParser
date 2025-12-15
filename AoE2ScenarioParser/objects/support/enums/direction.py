from enum import auto, Enum


class Direction(Enum):
    """
    Enum used to indicate the direction on the map. Where EAST means, the left corner when looking at the mini map
    """
    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()
    CENTER = auto()
