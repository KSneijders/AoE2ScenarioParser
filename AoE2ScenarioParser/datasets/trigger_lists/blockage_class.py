from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class BlockageClass(_DataSetIntEnums):
    """
    This enum class provides the integer values for the different blockage classes that can be used in the 'Modify
    Attribute' effect with the 'BlockageClass' attribute.

    **Examples**:

    >>> BlockageClass.RESOURCE
    <BlockageClass.RESOURCE: 1>
    """
    DEFAULT = 0
    """Forces default obstruction type"""
    RESOURCE = 1
    UNIT = 2
    BUILDING = 3
    WALL = 4
    GATE = 5
    """Gate, allows trespassing"""
    CLIFF = 6
    """Cliff, blocks walling"""
