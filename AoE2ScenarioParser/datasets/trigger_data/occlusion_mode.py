from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntFlags


class OcclusionMode(_DataSetIntFlags):
    """
    This enum class provides the integer values for the different occlusion mode flags that can be used in the 'Modify
    Attribute' effect with the 'OcclusionMode' attribute. This is a combinable bit field.

    **Examples**

    >>> OcclusionMode.NO_OCCLUSION
    <OcclusionMode.NO_OCCLUSION: 0>
    """
    NO_OCCLUSION = 0
    """
    No outline
    """
    DISPLAY_OUTLINE = 1
    """
    Display outline when behind other units that have flag 2
    """
    OCCLUDES_OTHERS = 2
    """
    Other units' outlines are rendered when they are behind this unit
    """
    DISPLAY_OUTLINE_FOR_FOUNDATION = 4
    """
    Display outline on this unit's foundation when behind other units that have flag 
    """
