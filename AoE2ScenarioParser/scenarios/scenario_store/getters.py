from typing import Optional, List, Tuple, Dict, TYPE_CHECKING
from uuid import UUID
from AoE2ScenarioParser.scenarios.scenario_store import store

if TYPE_CHECKING:
    from AoE2ScenarioParser.objects.data_objects.unit import Unit
    from AoE2ScenarioParser.objects.managers.trigger_manager import TriggerManager
    from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
    from AoE2ScenarioParser.objects.data_objects.terrain_tile import TerrainTile
    from AoE2ScenarioParser.sections.aoe2_file_section import AoE2FileSection


def get_unit(uuid: UUID, unit_reference_id: int) -> Optional[Unit]:
    """
    Get a placed unit based on it's reference id in a scenario.

    Args:
        uuid (UUID): The universally unique identifier of the scenario
        unit_reference_id (int): The reference_id of the unit

    Returns:
        The Unit Object
    """
    units, _ = get_units(uuid, [unit_reference_id])
    if units:
        return units[0]
    return None


def get_units(uuid: UUID, unit_reference_ids: List[int]) -> Optional[Tuple[List[Unit], List[int]]]:
    """
    Get a placed unit based on it's reference id in a scenario.

    Args:
        uuid (UUID): The universally unique identifier of the scenario
        unit_reference_ids (List[int]): The reference_ids of the units

    Returns:
        A tuple with a list of the found unit objects and a list of the IDs that weren't found.
    """
    unit_reference_ids = unit_reference_ids.copy()
    scenario = store.get_scenario(uuid)
    if scenario:
        result = []
        for unit in scenario.unit_manager.get_all_units():
            if unit.reference_id in unit_reference_ids:
                unit_reference_ids.remove(unit.reference_id)
                result.append(unit)
        return result, unit_reference_ids
    return None


def get_sections(uuid: UUID) -> Optional[Dict[str, AoE2FileSection]]:
    """
    Get the section dict of a scenario.

    Args:
        uuid (UUID): The universally unique identifier of the scenario

    Returns:
        The sections of the selected scenario
    """
    scenario = store.get_scenario(uuid)
    if scenario:
        return scenario.sections
    return None


def get_scenario_version(uuid: UUID) -> Optional[str]:
    """
    Get the scenario version.

    Args:
        uuid (UUID): The universally unique identifier of the scenario

    Returns:
        The scenario version of the selected scenario (e.g. '1.43')
    """
    scenario = store.get_scenario(uuid)
    if scenario:
        return scenario.scenario_version
    return None


def get_game_version(uuid: UUID) -> Optional[str]:
    """
    Get the game version.

    Args:
        uuid (UUID): The universally unique identifier of the scenario

    Returns:
        The game version of the selected scenario (e.g. 'DE')
    """
    scenario = store.get_scenario(uuid)
    if scenario:
        return scenario.game_version
    return None


def get_map_size(uuid: UUID) -> Optional[int]:
    """
    Get the map size of a scenario. Scenario is selected based on the given UUID.

    Args:
        uuid (UUID): The universally unique identifier of the scenario

    Returns:
        The map size of the scenario
    """
    scenario = store.get_scenario(uuid)
    if scenario:
        return scenario.map_manager.map_size
    return None


def get_terrain(uuid: UUID) -> Optional[List[TerrainTile]]:
    """
    Get the map size of a scenario. Scenario is selected based on the given UUID.

    Args:
        uuid (UUID): The universally unique identifier of the scenario

    Returns:
        The map size of the scenario
    """
    scenario = store.get_scenario(uuid)
    if scenario:
        return scenario.map_manager.terrain
    return None


def get_trigger_name(uuid: UUID, trigger_index: int) -> Optional[str]:
    """
    Get the trigger name of a trigger in a scenario.

    Args:
        uuid (UUID): The universally unique identifier of the scenario
        trigger_index (int): The index of the trigger

    Returns:
        The name of the trigger with the given ID
    """
    scenario = store.get_scenario(uuid)
    if scenario and trigger_index < len(scenario.trigger_manager.triggers):
        return scenario.trigger_manager.triggers[trigger_index].name
    return None


def get_variable_name(uuid: UUID, variable_index: int) -> Optional[str]:
    """
    Get the variable name in a scenario.

    Args:
        uuid (UUID): The universally unique identifier of the scenario
        variable_index (int): The index of the variable

    Returns:
        The name of the variable with the given ID

    Raises:
        ValueError: if variables are not supported in the scenario whose ID was provided
    """
    scenario: Optional[AoE2DEScenario] = store.get_scenario(uuid)
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


def get_trigger_version(uuid: UUID) -> Optional[float]:
    """
    Get the trigger version of the scenario.

    Args:
        uuid (UUID): The universally unique identifier of the scenario

    Returns:
        The trigger version.
    """
    scenario = store.get_scenario(uuid)
    if scenario:
        return scenario.sections['Triggers'].trigger_version
    return None


def get_trigger_manager(uuid: UUID) -> Optional[TriggerManager]:
    """
    Get the trigger manager of a scenario.

    Args:
        uuid (UUID): The universally unique identifier of the scenario

    Returns:
        The trigger manager of a scenario.
    """
    scenario = store.get_scenario(uuid)
    if scenario:
        return scenario.trigger_manager
    return None
