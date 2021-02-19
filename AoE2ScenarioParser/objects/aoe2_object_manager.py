from __future__ import annotations

from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.objects.managers.de.map_manager_de import MapManagerDE
from AoE2ScenarioParser.objects.managers.de.trigger_manager_de import TriggerManagerDE
from AoE2ScenarioParser.objects.managers.unit_manager import UnitManager

managers = {
    'DE': {
        'Map': MapManagerDE,
        'Trigger': TriggerManagerDE,
        'Unit': UnitManager,
    }
}


class AoE2ObjectManager:
    def __init__(self, pieces, game_version):
        self.pieces = pieces
        self.game_version = game_version
        self.managers = {}

    def setup(self):
        helper.rprint(f"Setting up managers ...", final=True)

        for name, manager in managers[self.game_version].items():
            helper.rprint(f"\t🔄 Setting up {name}Manager...")
            self.managers[name] = manager._construct(self.pieces)
            helper.rprint(f"\t✔ {name}Manager", final=True)

        helper.rprint(f"Setting up managers finished successfully.", final=True)

    def reconstruct(self):
        helper.rprint("\nReconstructing pieces and structs from managers...")

        for name, manager in managers[self.game_version].items():
            helper.rprint("\tReconstructing " + manager.__name__ + "...", replace=True)
            self.managers[name].commit(self.pieces)
            helper.rprint("\tReconstructing " + manager.__name__ + " finished successfully.", replace=True)
            helper.rprint()

        helper.rprint("Reconstruction finished successfully.")
