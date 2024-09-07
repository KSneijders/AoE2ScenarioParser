from __future__ import annotations

import math

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class ButtonLocation(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the button locations in the game. These button
    locations are what determines where a unit's train button or a research's research button appears in a building's
    UI

    **Examples**

    >>> ButtonLocation.R2C2
    <ButtonLocation.R2C2: 7>
    >>> ButtonLocation.R3C1.attribute_presentation()
    'row_3_col_1'
    """
    _R1C1 = 0
    R1C1 = 1
    R1C2 = 2
    R1C3 = 3
    R1C4 = 4
    R1C5 = 5
    R2C1 = 6
    R2C2 = 7
    R2C3 = 8
    R2C4 = 9
    R2C5 = 10
    R3C1 = 11
    R3C2 = 12
    R3C3 = 13
    R3C4 = 14
    # R3C5 = 15  # Doesn't actually work in-game. Probably to make space for the arrow key.

    def attribute_presentation(self):
        val = self.value or 1  # Change VAL 0 to 1
        row = math.ceil(val / 5)
        col = val - (row - 1) * 5
        return f"row_{row}_col_{col}"

    @classmethod
    def row_col(cls, row: int, col: int) -> int:
        """
        Get the button location ID of the row, column specified

        Args:
            row: The number of the row starting from the top (1-5)
            col: The number of the column starting from the left (1-3)

        Returns:
            The button location ID of the (row, column) location specified
        """
        return cls((row - 1) * 5 + col)
