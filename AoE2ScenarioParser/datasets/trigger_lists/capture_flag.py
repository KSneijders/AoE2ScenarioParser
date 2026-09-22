from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class CaptureFlag(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the capture flag values used in the game for units.
    Used when placing new objects

    **Examples**

    >>> CaptureFlag.DEFAULT
    <CaptureFlag.DEFAULT: -1>
    """
    DEFAULT = -1
    NEVER = 0
    ONCE = 1
    MULTIPLE_TIMES = 2
    NEVER_GAIA_AGGRESSIVE = 3
