from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class TechnologyState(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference technology state of a technology in the game. Used in
    the 'Technology State' condition.

    **Examples**

    >>> TechnologyState.NOT_READY
    <TechnologyState.NOT_READY: 0>
    """
    DISABLED = -1
    NOT_READY = 0
    """A tech that is not available to be researched (Bombard Tower is not ready before chemistry is researched)"""
    READY = 1
    """A tech that is available to be researched (Bombard Tower is ready after chemistry is researched)"""
    RESEARCHING = 2
    """A tech that is currently being researched"""
    DONE = 3
    """A Tech that has already been researched"""
    QUEUED = 4
    """A tech that is waiting in queue to be researched"""
