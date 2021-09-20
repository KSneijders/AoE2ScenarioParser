from typing import TYPE_CHECKING, Dict

if TYPE_CHECKING:
    from AoE2ScenarioParser.scenarios.aoe2_scenario import AoE2Scenario
    from AoE2ScenarioParser.sections.aoe2_file_section import AoE2FileSection

_scenarios: Dict[str, 'AoE2Scenario'] = {}


def register_scenario(scenario: 'AoE2Scenario') -> None:
    """
    Register a scenario to the store

    Args:
        scenario (AoE2DEScenario): The scenario to register
    """
    if scenario.uuid in _scenarios:
        raise ValueError("Scenario with that UUID already present")
    _scenarios[scenario.uuid] = scenario


def get_sections(uuid: str) -> Dict[str, 'AoE2FileSection']:
    """
    Get the section dict of a scenario.

    Args:
        uuid (str): The UUID of the scenario

    Returns:
        The sections of the selected scenario
    """
    return _scenarios[uuid].sections


def get_scenario_version(uuid: str) -> str:
    """
    Get the scenario version.

    Args:
        uuid (str): The UUID of the scenario

    Returns:
        The scenario version of the selected scenario (e.g. '1.43')
    """
    return _scenarios[uuid].scenario_version


def get_game_version(uuid: str) -> str:
    """
    Get the game version.

    Args:
        uuid (str): The UUID of the scenario

    Returns:
        The game version of the selected scenario (e.g. 'DE')
    """
    return _scenarios[uuid].game_version


def get_map_size(uuid: str) -> int:
    """
    Get the map size of a scenario. Scenario is selected based on the given UUID.

    Args:
        uuid (str): The UUID of the scenario

    Returns:
        The map size of the scenario
    """
    return _scenarios[uuid].map_manager.map_size


def get_trigger_name(uuid: str, trigger_index: int) -> str:
    """
    Get the trigger name of a trigger in a scenario.

    Args:
        uuid (str): The UUID of the scenario
        trigger_index (int): The index of the trigger

    Returns:
        A list of all names in order of trigger_manager.triggers
    """
    return _scenarios[uuid].trigger_manager.triggers[trigger_index].name
