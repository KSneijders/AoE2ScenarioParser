from typing import List, overload, Union, TYPE_CHECKING

from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.scenarios.scenario_store import store

if TYPE_CHECKING:
    from AoE2ScenarioParser.objects.data_objects.unit import Unit


@overload
def unit_change_ownership(uuid: str, player: Union[int, PlayerId], unit: 'Unit') -> None:
    ...


@overload
def unit_change_ownership(uuid: str, player: Union[int, PlayerId], units: List['Unit']) -> None:
    ...


def unit_change_ownership(uuid: str, player: Union[int, PlayerId], *args) -> None:
    """
    Get the trigger manager of a scenario.

    Args:
        uuid (str): The UUID of the scenario
        player (Union[int, PlayerId]): The player to transfer the units to.
        args: Unit object or List of unit objects

    Returns:
        The trigger manager of a scenario.
    """
    def transfer_unit(scenario_, unit_, player_):
        scenario_.unit_manager.units[unit_.player].remove(unit_)
        scenario_.unit_manager.units[player_].append(unit_)

    scenario = store.get_scenario(uuid)
    for units in args:
        if isinstance(units, List):
            for unit in units:
                transfer_unit(scenario, unit, player)
        else:
            transfer_unit(scenario, units, player)
