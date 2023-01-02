from __future__ import annotations

from typing import Dict, Type, TypeVar
from uuid import UUID

from AoE2ScenarioParser.helper.printers import s_print
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.managers.xs_manager import XsManager
from AoE2ScenarioParser.objects.managers.map_manager import MapManager
from AoE2ScenarioParser.objects.managers.message_manager import MessageManager
from AoE2ScenarioParser.objects.managers.player_manager import PlayerManager
from AoE2ScenarioParser.objects.managers.trigger_manager import TriggerManager
from AoE2ScenarioParser.objects.managers.unit_manager import UnitManager
from AoE2ScenarioParser.scenarios.scenario_store import getters

managers: Dict[str, Dict[str, Type[AoE2Object]]] = {
    'DE': {
        'Message': MessageManager,
        'Player': PlayerManager,
        'Map': MapManager,
        'Unit': UnitManager,
        'Trigger': TriggerManager,
        'Xs': XsManager,
    }
}

ManagerInstance = TypeVar('ManagerInstance', bound = AoE2Object)


class AoE2ObjectManager:
    def __init__(self, scenario_uuid: UUID):
        """
        Args:
            scenario_uuid: The universally unique identifier of the scenario
        """
        self.scenario_uuid: UUID = scenario_uuid
        self.managers: Dict[str, ManagerInstance] = {}

    def setup(self) -> None:
        """Sets up the managers by calling their construct functions"""
        s_print(f"Setting up managers ...", final=True, time=True, newline=True)
        gv = getters.get_game_version(self.scenario_uuid)

        for name, manager in managers[gv].items():
            s_print(f"\t🔄 Setting up {name}Manager...", color="yellow")
            self.managers[name] = manager.construct(self.scenario_uuid)
            s_print(f"\t✔ {name}Manager", final=True, color="green")

        s_print(f"Setting up managers finished successfully.", final=True, time=True)

    def reconstruct(self) -> None:
        """Reconstructs the file sections by calling the managers commit functions"""
        s_print("Reconstructing sections and structs from managers...", final=True, time=True, newline=True)

        for name, manager in self.managers.items():
            s_print(f"\t🔄 Reconstructing {name}Manager...", color = "yellow")
            manager.commit()
            s_print(f"\t✔ {name}Manager", final = True, color = "green")

        s_print("Reconstruction finished successfully.", final=True, time=True)
