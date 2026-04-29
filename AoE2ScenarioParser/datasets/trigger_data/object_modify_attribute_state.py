from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class ObjectModifyAttributeState(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the modification state of a unit used in the
    modify object attribute effect.

    **Examples**

    >>> ObjectModifyAttributeState.NOT_MODIFIED
    <ObjectModifyAttributeState.NOT_MODIFIED: 1>
    """
    ALL = 0
    NOT_MODIFIED = 1
    MODIFIED = 2
