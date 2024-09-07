from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntFlags


class SecondaryGameMode(_DataSetIntFlags):
    """
    This enum class provides the integer values for the different secondary game modes.

    **Examples**

    >>> SecondaryGameMode.EMPIRE_WARS
    <SecondaryGameMode.EMPIRE_WARS: 1>
    >>> SecondaryGameMode.SUDDEN_DEATH | SecondaryGameMode.REGICIDE
    <HeroStatusFlag.SUDDEN_DEATH|REGICIDE: 6>
    """

    # todo: we can probably add this to the base dataset int flags class, I have an idea on how to generic-ify this
    #  method although idk if its actually good - Alian
    @staticmethod
    def combine(
            empire_wars: bool = False,
            sudden_death: bool = False,
            regicide: bool = False,
            king_of_the_hill: bool = False,
    ) -> SecondaryGameMode:
        """
        This method combines the given hero status flags into an integer value

        Args:
            empire_wars: If empire wars should be enabled
            sudden_death: If sudden death should be enabled
            regicide: If regicide should be enabled
            king_of_the_hill: If king of the hill should be enabled

        Returns:
            An integer combining all the different hero status flags into one value
        """
        total = 1 if empire_wars else 0
        total += 2 if sudden_death else 0
        total += 4 if regicide else 0
        total += 8 if king_of_the_hill else 0
        return SecondaryGameMode(total)

    NONE = 0
    EMPIRE_WARS = 1
    SUDDEN_DEATH = 2
    REGICIDE = 4
    KING_OF_THE_HILL = 8
