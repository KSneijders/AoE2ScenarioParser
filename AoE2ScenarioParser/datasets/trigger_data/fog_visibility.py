from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class FogVisibility(_DataSetIntEnums):
    """
    This enum class provides the integer values used to references the different fog visibility settings that can be
    used in the 'Modify Attribute' effect with the 'Fog Visibility' attribute.

    **Examples**

    >>> FogVisibility.VISIBLE_IF_ALIVE
    <FogVisibility.VISIBLE_IF_ALIVE: 2>
    """
    NOT_VISIBLE = 0
    ALWAYS_VISIBLE = 1
    VISIBLE_IF_ALIVE = 2
    INVERTED_VISIBILITY = 3
    CHECK_DOPPELGANGER = 4
