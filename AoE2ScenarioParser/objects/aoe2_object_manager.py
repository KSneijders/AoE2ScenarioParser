from __future__ import annotations

from typing import Dict, Type

from AoE2ScenarioParser.helper.printers import s_print
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.managers.de.map_manager_de import MapManagerDE
from AoE2ScenarioParser.objects.managers.de.trigger_manager_de import TriggerManagerDE
from AoE2ScenarioParser.objects.managers.de.unit_manager_de import UnitManagerDE

managers: Dict[str, Dict[str, Type[AoE2Object]]] = {
    'DE': {
        'Map': MapManagerDE,
        'Unit': UnitManagerDE,
        'Trigger': TriggerManagerDE,
    }
}


class AoE2ObjectManager:
    def __init__(self, sections, game_version, scenario_version):
        self.sections = sections
        self.game_version = game_version
        self.scenario_version = scenario_version
        self.managers = {}

    def setup(self):
        s_print(f"\nSetting up managers ...", final=True)

        for name, manager in managers[self.game_version].items():
            s_print(f"\t🔄 Setting up {name}Manager...")
            self.managers[name] = manager._construct(self.sections, self.scenario_version)
            s_print(f"\t✔ {name}Manager", final=True)

        s_print(f"Setting up managers finished successfully.", final=True)

    def reconstruct(self):
        s_print("\nReconstructing sections and structs from managers...", final=True)

        manager: AoE2Object
        for name, manager in self.managers.items():
            s_print(f"\t🔄 Reconstructing {name}Manager...")
            manager.commit(self.sections)
            s_print(f"\t✔ {name}Manager", final=True)

        s_print("Reconstruction finished successfully.", final=True)
