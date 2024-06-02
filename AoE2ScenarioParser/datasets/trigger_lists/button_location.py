from __future__ import annotations

import math

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class ButtonLocation(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the button locations in the game. These button
    locations are what determines where a unit's train button or a research's research button appears in a building's
    UI

    **Examples**

    >>> ButtonLocation.r2c2
    <ButtonLocation.r2c2: 7>
    >>> ButtonLocation.r3c1.attribute_presentation()
    'row_3_col_1'
    """
    _r1c1 = 0
    r1c1 = 1
    r1c2 = 2
    r1c3 = 3
    r1c4 = 4
    r1c5 = 5
    r2c1 = 6
    r2c2 = 7
    r2c3 = 8
    r2c4 = 9
    r2c5 = 10
    r3c1 = 11
    r3c2 = 12
    r3c3 = 13
    r3c4 = 14

    # r3c5 = 15  # Doesn't actually work in-game. Probably to make space for the arrow key.

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
