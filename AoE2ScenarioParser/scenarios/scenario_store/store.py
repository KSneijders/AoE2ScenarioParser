from __future__ import annotations

import time
from typing import TYPE_CHECKING, Dict, Optional
from uuid import UUID
from weakref import WeakValueDictionary

from AoE2ScenarioParser import settings
from AoE2ScenarioParser.helper.printers import warn
from AoE2ScenarioParser.objects.support.uuid_list import NO_UUID

if TYPE_CHECKING:
    from AoE2ScenarioParser.scenarios.aoe2_scenario import AoE2Scenario
    from AoE2ScenarioParser.objects.aoe2_object import AoE2Object

_scenarios: WeakValueDictionary[UUID, 'AoE2Scenario'] = WeakValueDictionary()
_scenarios_by_name: WeakValueDictionary[str, 'AoE2Scenario'] = WeakValueDictionary()


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
        scenario: The scenario to register
    """
    if scenario.uuid in _scenarios:
        raise ValueError("Scenario with that UUID already present")

    if settings.SHOW_SCENARIO_VERSION_WARNINGS:
        for other in _scenarios.values():
            if other.scenario_version == scenario.scenario_version:
                continue

            other_display = f"'{other.name}' [{other.scenario_version}]"
            display = f"'{scenario.name}' [{scenario.scenario_version}]"

            print('\n\n')
            time.sleep(.1)  # Prevent stacking the error inside other logs
            warn(
                message=f"Reading multiple scenarios with different versions ({other_display} vs {display}) can cause "
                        f"issues on assignment of values.\nWhen experiencing issues, please update scenarios to the "
                        f"same version.\nYou can do this by opening the scenarios in the editor and saving them (this "
                        f"updates them to the latest version).\nYou can disable this warnings using:\n"
                        f"settings.SHOW_SCENARIO_VERSION_WARNINGS = False",
                stack=3
            )
            time.sleep(.1)  # Prevent stacking the error inside other logs
            print('\n\n')

    _scenarios[scenario.uuid] = scenario
    _scenarios_by_name[scenario.name] = scenario


def remove_scenario(uuid: UUID) -> None:
    """
    force remove a scenario from the store. In general this is not necessary as the store stores references to the
    scenario weakly. This means, as soon as the user removes all hard references, it's gone from the store too.

    Args:
        uuid: The UUID of the scenario
    """
    del _scenarios[uuid]
