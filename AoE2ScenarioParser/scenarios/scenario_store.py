from typing import TYPE_CHECKING, Dict, Optional, List, Union, Type, Tuple

if TYPE_CHECKING:
    from AoE2ScenarioParser.objects.data_objects.unit import Unit
    from AoE2ScenarioParser.objects.managers.trigger_manager import TriggerManager
    from AoE2ScenarioParser.scenarios.aoe2_scenario import AoE2Scenario
    from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
    from AoE2ScenarioParser.sections.aoe2_file_section import AoE2FileSection

_scenarios: Dict[str, 'AoE2Scenario'] = {}


def _get_scenario(uuid: str) -> Optional[Union['AoE2Scenario', Type['AoE2Scenario']]]:
    """
    Get scenario through uuid. Not intended to be called outside of the store itself.

    Args:
        uuid (str): The UUID of the scenario

    Returns:
        The scenario based on it's uuid
    """
    if uuid == "<<NO_HOST_UUID>>":
        return None
    return _scenarios[uuid]


def register_scenario(scenario: 'AoE2Scenario') -> None:
    """
    Register a scenario to the store

    Args:
        scenario (AoE2DEScenario): The scenario to register
    """
    if scenario.uuid in _scenarios:
        raise ValueError("Scenario with that UUID already present")
    _scenarios[scenario.uuid] = scenario


def get_unit(uuid: str, unit_reference_id: int) -> Optional['Unit']:
    """
    Get a placed unit based on it's reference id in a scenario.

    Args:
        uuid (str): The UUID of the scenario
        unit_reference_id (int): The reference_id of the unit

    Returns:
        The Unit Object
    """
    units, _ = get_units(uuid, [unit_reference_id])
    if units:
        return units[0]
    return None


def get_units(uuid: str, unit_reference_ids: List[int]) -> Optional[Tuple[List['Unit'], List[int]]]:
    """
    Get a placed unit based on it's reference id in a scenario.

    Args:
        uuid (str): The UUID of the scenario
        unit_reference_ids (List[int]): The reference_ids of the units

    Returns:
        A tuple with a list of the found unit objects and a list of the IDs that weren't found.
    """
    unit_reference_ids = unit_reference_ids.copy()
    scenario = _get_scenario(uuid)
    if scenario:
        result = []
        for unit in scenario.unit_manager.get_all_units():
            if unit.reference_id in unit_reference_ids:
                unit_reference_ids.remove(unit.reference_id)
                result.append(unit)
        return result, unit_reference_ids
    return None


def get_sections(uuid: str) -> Optional[Dict[str, 'AoE2FileSection']]:
    """
    Get the section dict of a scenario.

    Args:
        uuid (str): The UUID of the scenario

    Returns:
        The sections of the selected scenario
    """
    scenario = _get_scenario(uuid)
    if scenario:
        return scenario.sections
    return None


def get_scenario_version(uuid: str) -> Optional[str]:
    """
    Get the scenario version.

    Args:
        uuid (str): The UUID of the scenario

    Returns:
        The scenario version of the selected scenario (e.g. '1.43')
    """
    scenario = _get_scenario(uuid)
    if scenario:
        return scenario.scenario_version
    return None


def get_game_version(uuid: str) -> Optional[str]:
    """
    Get the game version.

    Args:
        uuid (str): The UUID of the scenario

    Returns:
        The game version of the selected scenario (e.g. 'DE')
    """
    scenario = _get_scenario(uuid)
    if scenario:
        return scenario.game_version
    return None


def get_map_size(uuid: str) -> Optional[int]:
    """
    Get the map size of a scenario. Scenario is selected based on the given UUID.

    Args:
        uuid (str): The UUID of the scenario

    Returns:
        The map size of the scenario
    """
    scenario = _get_scenario(uuid)
    if scenario:
        return scenario.map_manager.map_size
    return None


def get_trigger_name(uuid: str, trigger_index: int) -> Optional[str]:
    """
    Get the trigger name of a trigger in a scenario.

    Args:
        uuid (str): The UUID of the scenario
        trigger_index (int): The index of the trigger

    Returns:
        The name of the trigger with the given ID
    """
    scenario = _get_scenario(uuid)
    if scenario and trigger_index < len(scenario.trigger_manager.triggers):
        return scenario.trigger_manager.triggers[trigger_index].name
    return None


def get_variable_name(uuid: str, variable_index: int) -> Optional[str]:
    """
    Get the variable name in a scenario.

    Args:
        uuid (str): The UUID of the scenario
        variable_index (int): The index of the variable

    Returns:
        The name of the variable with the given ID
    """
    scenario: 'AoE2DEScenario' = _get_scenario(uuid)
    if scenario:
        if gv := get_game_version(uuid) == "DE":
            variable = scenario.trigger_manager.get_variable(variable_index)
            if variable:
                return variable.name
            elif 0 <= variable_index <= 255:
                return f"Variable {variable_index}"
        else:
            raise ValueError(f"Scenarios with the game version: {gv} do not support variables.")
    return None


def get_trigger_manager(uuid: str) -> Optional['TriggerManager']:
    """
    Get the trigger manager of a scenario.

    Args:
        uuid (str): The UUID of the scenario

    Returns:
        The trigger manager of a scenario.
    """
    scenario = _get_scenario(uuid)
    if scenario:
        return scenario.trigger_manager
    return None
