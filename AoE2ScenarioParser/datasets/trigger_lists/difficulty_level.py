from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class DifficultyLevel(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference difficulty level of the game. Used in the 'Difficulty
    Level' condition.

    **Examples**

    >>> DifficultyLevel.HARD
    <DifficultyLevel.HARD: 1>
    """
    EASIEST = 4
    STANDARD = 3
    MODERATE = 2
    HARD = 1
    HARDEST = 0
    EXTREME = -1
    """
    The only exception in the entire scenario where the value -1 is NOT an unselected/invalid value. 
    This might cause issues in the parser, please report them if you find any.
    """
