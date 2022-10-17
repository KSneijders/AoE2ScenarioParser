from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Optional
from uuid import UUID

from AoE2ScenarioParser.objects.support.uuid_list import NO_UUID
from helper.helper import exclusive_if

if TYPE_CHECKING:
    from AoE2ScenarioParser.scenarios.aoe2_scenario import AoE2Scenario
    from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

_scenarios: Dict[UUID, 'AoE2Scenario'] = {}
_scenarios_by_name: Dict[str, 'AoE2Scenario'] = {}


def get_scenario(uuid: UUID | None = None, name: str | None = None) -> Optional['AoE2Scenario']:
    """
    Get scenario through uuid. Not intended to be called outside the store itself.

    Args:
        uuid (UUID): The UUID of the scenario
        name:

    Returns:
        The scenario based on it's uuid
    """
    if not exclusive_if(uuid, name):
        raise ValueError("Unable to locate scenario without either a uuid or a name")

    if uuid == NO_UUID:
        return None

    key, dict_ = "", {}
    if uuid:
        key, dict_ = uuid, _scenarios
    elif name:
        key, dict_ = name, _scenarios_by_name
    if key in dict_:
        return dict_[key]
    else:
        raise ValueError("Unable to find scenario based on the given name or uuid")


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
