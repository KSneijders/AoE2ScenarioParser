from __future__ import annotations

import re
from typing import Optional, List, Tuple, Dict, TYPE_CHECKING, AnyStr
from uuid import UUID

from AoE2ScenarioParser.scenarios.scenario_store import store

if TYPE_CHECKING:
    from AoE2ScenarioParser.objects.data_objects.unit import Unit
    from AoE2ScenarioParser.objects.data_objects.trigger import Trigger
    from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
    from AoE2ScenarioParser.objects.data_objects.terrain_tile import TerrainTile
    from AoE2ScenarioParser.sections.aoe2_file_section import AoE2FileSection


def get_unit(uuid: UUID, unit_reference_id: int) -> Optional['Unit']:
    """
    Get a placed unit based on it's reference id in a scenario.

    Args:
        uuid: The universally unique identifier of the scenario
        unit_reference_id: The reference_id of the unit

    Returns:
        The Unit Object
    """
    units, _ = get_units(uuid, [unit_reference_id])
    if units:
        return units[0]
    return None


def get_units_in_area(uuid: UUID, x1: int, y1: int, x2: int, y2: int) -> Optional[List['Unit']]:
    """
    Get a placed unit based on it's reference id in a scenario.

    Args:
        uuid: The UUID of the scenario
        x1: The X location of the left corner
        y1: The Y location of the left corner
        x2: The X location of the right corner
        y2: The Y location of the right corner

    Returns:
        The Unit Object
    """
    scenario = store.get_scenario(uuid)
    if scenario:
        return scenario.unit_manager.get_units_in_area(x1, y1, x2, y2)
    return None


def get_units(uuid: UUID, unit_reference_ids: List[int]) -> Tuple[List['Unit'], List[int]] | None:
    """
    Get a placed unit based on it's reference id in a scenario.

    Args:
        uuid: The universally unique identifier of the scenario
        unit_reference_ids: The reference_ids of the units

    Returns:
        A tuple with a list of the found unit objects and a list of the IDs that weren't found.
    """
    unit_reference_ids = unit_reference_ids.copy()
    scenario = store.get_scenario(uuid)
    if scenario:
        units = scenario.unit_manager.filter_units_by_reference_id(unit_reference_ids)
        found = [unit.reference_id for unit in units]
        return units, [id_ for id_ in unit_reference_ids if id_ not in found]
    return None


def get_sections(uuid: UUID) -> Optional[Dict[str, 'AoE2FileSection']]:
    """
    Get the section dict of a scenario.

    Args:
        uuid: The universally unique identifier of the scenario

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
        uuid: The universally unique identifier of the scenario

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
        uuid: The universally unique identifier of the scenario

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
        uuid: The universally unique identifier of the scenario

    Returns:
        The map size of the scenario
    """
    scenario = store.get_scenario(uuid)
    if scenario:
        return scenario.map_manager.map_size
    return None


def get_terrain(uuid: UUID) -> Optional[List['TerrainTile']]:
    """
    Get the map size of a scenario. Scenario is selected based on the given UUID.

    Args:
        uuid: The universally unique identifier of the scenario

    Returns:
        The map size of the scenario
    """
    scenario = store.get_scenario(uuid)
    if scenario:
        return scenario.map_manager.terrain
    return None


def get_trigger(uuid: UUID, trigger_index: int) -> Optional['Trigger']:
    """
    Get a trigger in a scenario.

    Args:
        uuid: The universally unique identifier of the scenario
        trigger_index: The index of the trigger

    Returns:
        The trigger with the given ID
    """
    scenario = store.get_scenario(uuid)
    if scenario and trigger_index < len(scenario.trigger_manager.triggers):
        return scenario.trigger_manager.triggers[trigger_index]
    return None


def get_triggers_by_regex(uuid: UUID, pattern: re.Pattern[AnyStr]) -> Optional[List[Tuple['Trigger', str, str]]]:
    """
    Get any triggers whose names match the data triggers syntax ``TYPE : KEY``

    Args:
        uuid: The UUID of the scenario
        pattern: A regex pattern which must capture two groups: a type_ and a key

    Returns:
        A list of tuples containing a Trigger, it's type_, and the key
    """
    scenario = store.get_scenario(uuid)
    if not scenario:
        return None

    return [
        (trigger, match.group(1).lower(), match.group(2))
        for trigger in scenario.trigger_manager.triggers
        if (match := re.match(pattern, trigger.name))
    ]


def get_variable_name(uuid: UUID, variable_index: int) -> Optional[str]:
    """
    Get the variable name in a scenario.

    Args:
        uuid: The universally unique identifier of the scenario
        variable_index: The index of the variable

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
        uuid: The universally unique identifier of the scenario

    Returns:
        The trigger version.
    """
    scenario = store.get_scenario(uuid)
    if scenario:
        return scenario.sections['Triggers'].trigger_version
    return None
