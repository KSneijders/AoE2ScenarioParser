from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums
from AoE2ScenarioParser.datasets.techs import TechInfo


class LocalTechnology(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference local technologies of the game.
    Used in the 'Research Local Technologies' effect and 'Local Technology Researched' condition.

    It indirectly uses the TechInfo enum class as that's where the values are stored. This is a narrow selection
    created for convienience.

    **Examples**

    >>> LocalTechnology.DEFENSIVE_TOWN_CENTER
    <LocalTechnology.DEFENSIVE_TOWN_CENTER: 1197>
    """
    DEFENSIVE_TOWN_CENTER = TechInfo.DEFENSIVE_TOWN_CENTER.ID
    ECONOMIC_TOWN_CENTER = TechInfo.ECONOMIC_TOWN_CENTER.ID
    MILITARY_TOWN_CENTER = TechInfo.MILITARY_TOWN_CENTER.ID
