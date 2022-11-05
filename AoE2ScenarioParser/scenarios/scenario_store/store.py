from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Optional
from uuid import UUID

from AoE2ScenarioParser.objects.support.uuid_list import NO_UUID

if TYPE_CHECKING:
    from AoE2ScenarioParser.scenarios.aoe2_scenario import AoE2Scenario
    from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
    from AoE2ScenarioParser.objects.aoe2_object import AoE2Object

_scenarios: Dict[UUID, 'AoE2Scenario'] = {}
_scenarios_by_name: Dict[str, 'AoE2Scenario'] = {}


def get_scenario(
        uuid: UUID = None,
        obj: 'AoE2Object' = None,
        name: str = None
) -> Optional['AoE2Scenario']:
    """
    Get scenario through a UUID, a related object or the name of a scenario.
    Not intended to be called outside the store itself.

    Use the wrapper instead: `AoE2Scenario.get_scenario()`

    Args:
        uuid: The UUID of the scenario
        obj: An object related to a scenario
        name: The name of a scenario

    Raises

    Returns:
        The scenario based on the given identifier, or `None`
    """
    if uuid == NO_UUID:
        return None

    key, dict_ = "", {}
    if uuid is not None:
        key, dict_ = uuid, _scenarios
    elif obj is not None:
        key, dict_ = obj._uuid, _scenarios
    elif name is not None:
        key, dict_ = name, _scenarios_by_name

    if key in dict_:
        return dict_[key]
    else:
        raise ValueError("Unable to find scenario based on the given identifier")


def register_scenario(scenario: 'AoE2Scenario') -> None:
    """
    Register a scenario to the store

    Args:
        scenario (AoE2DEScenario): The scenario to register
    """
    if scenario.uuid in _scenarios:
        raise ValueError("Scenario with that UUID already present")
    _scenarios[scenario.uuid] = scenario
    _scenarios_by_name[scenario.name] = scenario


def remove_scenario(uuid: UUID) -> None:
    """
    Remove a scenario from the store

    Args:
        uuid (UUID): The UUID of the scenario
    """
    del _scenarios[uuid]
