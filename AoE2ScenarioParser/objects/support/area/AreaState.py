from __future__ import annotations

from enum import IntEnum


class AreaState(IntEnum):
    """Enum to show the state of the Area object"""
    RECT = 0
    EDGE = 1
    GRID = 2
    LINES = 3
    CORNERS = 4

    def is_chunkable(self: AreaState) -> bool:
        """Return if the state is chunkable or not"""
        return not self in {AreaState.RECT, AreaState.EDGE}
