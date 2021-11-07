from __future__ import annotations

from AoE2ScenarioParser.objects.managers.de.map_manager_de import MapManagerDE
from AoE2ScenarioParser.objects.managers.de.trigger_manager_de import TriggerManagerDE
from AoE2ScenarioParser.objects.managers.de.unit_manager_de import UnitManagerDE
from AoE2ScenarioParser.objects.managers.de.xs_manager_de import XsManagerDE
from AoE2ScenarioParser.scenarios.aoe2_scenario import AoE2Scenario


class AoE2DEScenario(AoE2Scenario):
    """
    This class is used to represent a scenario with version >= 1.36 (DE). It is the main class that is exposed to the
    user of the API.
    """
    @property
    def trigger_manager(self) -> TriggerManagerDE:
        return self._object_manager.managers['Trigger']

    @property
    def unit_manager(self) -> UnitManagerDE:
        return self._object_manager.managers['Unit']

    @property
    def map_manager(self) -> MapManagerDE:
        return self._object_manager.managers['Map']

    @property
    def xs_manager(self) -> XsManagerDE:
        return self._object_manager.managers['Xs']

    @classmethod
    def from_file(cls, filename: str, game_version: str="DE") -> AoE2DEScenario:
        """
        This function creates and returns an instance of the AoE2DEScenario class from the given scenario file

        Args:
            filename (str): The path to the scenario file to create the object from
            game_version (str): (Default: 'DE') The version of the game to create the object for

        Returns:
            An instance of the AoE2DEScenario class which is the object representation of the given scenario file
        """
        return super().from_file(filename, game_version)
