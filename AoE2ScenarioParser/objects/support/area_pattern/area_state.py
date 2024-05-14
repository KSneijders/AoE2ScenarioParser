from __future__ import annotations

from enum import auto, IntEnum


class AreaState(IntEnum):
    """Enum to show the state of the AreaPattern object"""
    RECT = auto()
    EDGE = auto()
    GRID = auto()
    LINES = auto()
    CORNERS = auto()

    def is_chunkable(self: AreaState) -> bool:
        """Return if the state is chunkable or not"""
        return self not in {AreaState.RECT, AreaState.EDGE}
