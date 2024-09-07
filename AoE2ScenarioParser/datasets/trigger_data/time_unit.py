from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class TimeUnit(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the unit of time used in an effect. Used in the
    'Display Timer' effect.

    **Examples**

    >>> TimeUnit.YEARS
    <TimeUnit.YEARS: 0>
    """
    YEARS = 0
    """In-Game years. A year is 5 seconds in-game time."""
    MINUTES = 1
    """In-Game minutes."""
    SECONDS = 2
    """In-Game seconds."""
    MINUTES_AND_SECONDS = 3
    """In-Game Minutes abd seconds."""
