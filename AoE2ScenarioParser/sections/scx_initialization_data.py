from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from AoE2ScenarioParser.sections import Unit


class ScenarioInitializationData:
    """
    An object holding data while a scenario is being read initialized.
    This object will be removed from the struct once the initialization is completed.

    The primary use for this object is caching of computationally heavy properties which
    are necessary for linking objects together.
    """

    _unit_reference_mapping: dict[int, 'Unit']
