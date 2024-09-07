from __future__ import annotations

from typing import List, overload, TYPE_CHECKING, Optional
from uuid import UUID

from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.scenarios.scenario_store import store

if TYPE_CHECKING:
    from AoE2ScenarioParser.objects.data_objects.unit import Unit
    from AoE2ScenarioParser.objects.support.area import Area
    from AoE2ScenarioParser.objects.data_objects.trigger import Trigger


@overload
def unit_change_ownership(uuid: UUID, player: int | PlayerId, unit: 'Unit') -> None:
    ...


@overload
def unit_change_ownership(uuid: UUID, player: int | PlayerId, units: List['Unit']) -> None:
    ...


def unit_change_ownership(uuid: UUID, player: int | PlayerId, *args) -> None:
    """
    Change the unit(s) ownership.

    Args:
        uuid: The universally unique identifier of the scenario
        player: The player to transfer the units to.
        args: Unit object or List of unit objects
    """

    def transfer_unit(scenario_, unit_, player_):
        scenario_.unit_manager.units[unit_.player].remove(unit_)
        scenario_.unit_manager.units[player_].append(unit_)

    scenario = store.get_scenario(uuid)
    if scenario:
        for units in args:
            if isinstance(units, List):
                for unit in units:
                    transfer_unit(scenario, unit, player)
            else:
                transfer_unit(scenario, units, player)


def import_triggers(uuid: UUID, triggers: List['Trigger'], insert_index: int = -1, deepcopy=True) -> None:
    """
    Import triggers into the scenario using the trigger manager.

    Args:
        uuid: The UUID of the scenario
        triggers: The trigger to import.
        insert_index: The insert index used in import triggers function
        deepcopy: If the given triggers need to be deep copied or not when importing. Can be useful to keep the
            reference alive between the source and target trigger the same when setting this to `False`.
    """
    scenario = store.get_scenario(uuid)
    if scenario:
        scenario.trigger_manager.import_triggers(triggers, insert_index, deepcopy)


def remove_triggers(uuid: UUID, trigger_ids: List[int]) -> None:
    """
    Import triggers into the scenario using the trigger manager.

    Args:
        uuid: The UUID of the scenario
        trigger_ids: A list of trigger ids to remove.
    """
    scenario = store.get_scenario(uuid)
    if scenario:
        trigger_ids.sort(reverse=True)
        scenario.trigger_manager.remove_triggers(trigger_ids)


def new_area_object(uuid: UUID) -> Optional['Area']:
    """
    Creates a new area object.

    Args:
        uuid: The UUID of the scenario
    """
    scenario = store.get_scenario(uuid)
    if scenario:
        return scenario.new.area()
