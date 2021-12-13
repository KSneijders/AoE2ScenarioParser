from typing import TYPE_CHECKING, Dict, Optional
from uuid import UUID
if TYPE_CHECKING:
    from AoE2ScenarioParser.scenarios.aoe2_scenario import AoE2Scenario
    from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

_scenarios: Dict[str, AoE2Scenario] = {}


def get_scenario(uuid: str) -> Optional[AoE2Scenario]:
    """
    Get scenario through uuid. Not intended to be called outside of the store itself.

    Args:
        uuid (UUID): The universally unique identifier of the scenario

    Returns:
        The scenario based on it's uuid
    """
    if uuid == "<<NO_HOST_UUID>>":
        return None
    return _scenarios[uuid]


def register_scenario(scenario: AoE2Scenario) -> None:
    """
    Register a scenario to the store

    Args:
        scenario (AoE2DEScenario): The scenario to register
    """
    if scenario.uuid in _scenarios:
        raise ValueError("Scenario with that UUID already present")
    _scenarios[scenario.uuid] = scenario
