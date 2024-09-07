from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntFlags


class UnitTrait(_DataSetIntFlags):
    """
    This enum class provides the integer values used to references the different unit trait flags that can be used in
    the 'Modify Attribute' effect with the 'Unit Trait' attribute.

    **Examples**

    >>> UnitTrait.TRANSFORMABLE
    <UnitTrait.TRANSFORMABLE: 8>
    """
    GARRISONABLE = 1
    SHIP = 2
    BUILD_BUILDING = 4
    TRANSFORMABLE = 8
    AUTO_SCOUT = 16
