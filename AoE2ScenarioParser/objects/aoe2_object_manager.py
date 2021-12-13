from __future__ import annotations

from typing import Dict, Type, Tuple

from AoE2ScenarioParser.helper.printers import s_print
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.managers.de.map_manager_de import MapManagerDE
from AoE2ScenarioParser.objects.managers.de.trigger_manager_de import TriggerManagerDE
from AoE2ScenarioParser.objects.managers.de.unit_manager_de import UnitManagerDE
from AoE2ScenarioParser.objects.managers.de.xs_manager_de import XsManagerDE
from AoE2ScenarioParser.objects.managers.player_manager import PlayerManager
from AoE2ScenarioParser.scenarios.scenario_store import getters

managers: Dict[str, Dict[str, Type[AoE2Object]]] = {
    'DE': {
        'Player': PlayerManager,
        'Map': MapManagerDE,
        'Unit': UnitManagerDE,
        'Trigger': TriggerManagerDE,
        'Xs': XsManagerDE,
    }
}


class AoE2ObjectManager:
    def __init__(self, scenario_uuid):
        self.scenario_uuid = scenario_uuid
        self.managers = {}

    def setup(self):
        s_print(f"\nSetting up managers ...", final=True)
        gv = getters.get_game_version(self.scenario_uuid)

        for name, manager in managers[gv].items():
            s_print(f"\t🔄 Setting up {name}Manager...", color="yellow")
            self.managers[name] = manager._construct(self.scenario_uuid)
            s_print(f"\t✔ {name}Manager", final=True, color="green")

        s_print(f"Setting up managers finished successfully.", final=True)

    def reconstruct(self):
        s_print("\nReconstructing sections and structs from managers...", final=True)

        for name, manager in self.managers.items(): #type: str, AoE2Object
            s_print(f"\t🔄 Reconstructing {name}Manager...", color="yellow")
            manager.commit()
            s_print(f"\t✔ {name}Manager", final=True, color="green")

        s_print("Reconstruction finished successfully.", final=True)
