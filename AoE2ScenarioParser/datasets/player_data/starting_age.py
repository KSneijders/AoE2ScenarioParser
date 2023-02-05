from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class StartingAge(_DataSetIntEnums):
    """
    **This is not the same as the "Age" dataset and should !!NOT!! be used in effects/conditions etc.**

    This enum class provides the integer values used to reference the starting ages in the game.
    This is used in the player objects to set a starting age.

    **Examples**

    >>> StartingAge.POST_IMPERIAL_AGE
    <StartingAge.POST_IMPERIAL_AGE: 6>
    """
    DARK_AGE = 2
    FEUDAL_AGE = 3
    CASTLE_AGE = 4
    IMPERIAL_AGE = 5
    POST_IMPERIAL_AGE = 6
