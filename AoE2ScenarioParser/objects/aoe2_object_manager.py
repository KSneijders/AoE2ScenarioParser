from __future__ import annotations

from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.objects.managers.de.map_manager_de import MapManagerDE
from AoE2ScenarioParser.objects.managers.de.trigger_manager_de import TriggerManagerDE
from AoE2ScenarioParser.objects.managers.de.unit_manager_de import UnitManagerDE

managers = {
    'DE': {
        'Map': MapManagerDE,
        'Trigger': TriggerManagerDE,
        'Unit': UnitManagerDE,
    }
}


class AoE2ObjectManager:
    def __init__(self, sections, game_version):
        self.sections = sections
        self.game_version = game_version
        self.managers = {}

    def setup(self):
        helper.rprint(f"Setting up managers ...", final=True)

        for name, manager in managers[self.game_version].items():
            helper.rprint(f"\t🔄 Setting up {name}Manager...")
            self.managers[name] = manager._construct(self.sections)
            helper.rprint(f"\t✔ {name}Manager", final=True)

        helper.rprint(f"Setting up managers finished successfully.", final=True)

    def reconstruct(self):
        helper.rprint("\nReconstructing sections and structs from managers...", final=True)

        for name, manager in managers[self.game_version].items():
            helper.rprint(f"\t🔄 Reconstructing {name}Manager...")
            self.managers[name].commit(self.sections)
            helper.rprint(f"\t✔ {name}Manager", final=True)

        helper.rprint("Reconstruction finished successfully.", final=True)
