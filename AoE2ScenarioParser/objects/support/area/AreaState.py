from __future__ import annotations

from enum import IntEnum


class AreaState(IntEnum):
    """Enum to show the state of the Area object"""
    FULL = 0
    EDGE = 1
    GRID = 2
    LINES = 3
    CORNERS = 4

    @staticmethod
    def unchunkables() -> set[AreaState]:
        """Returns the states that cannot be split into chunks"""
        return {AreaState.FULL, AreaState.EDGE}
