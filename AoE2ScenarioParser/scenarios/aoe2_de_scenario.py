from __future__ import annotations

from typing import Type

from AoE2ScenarioParser.objects.managers.de.map_manager_de import MapManagerDE
from AoE2ScenarioParser.objects.managers.de.trigger_manager_de import TriggerManagerDE
from AoE2ScenarioParser.objects.managers.de.unit_manager_de import UnitManagerDE
from AoE2ScenarioParser.objects.managers.de.xs_manager_de import XsManagerDE
from AoE2ScenarioParser.objects.managers.message_manager import MessageManager
from AoE2ScenarioParser.objects.managers.option_manager import OptionManager
from AoE2ScenarioParser.objects.managers.player_manager import PlayerManager
from AoE2ScenarioParser.scenarios.aoe2_scenario import AoE2Scenario, S


class AoE2DEScenario(AoE2Scenario):
    """
    Used to represent a scenario with version >= 1.36 (DE). It is the main class that is exposed to the user of the API.
    """

    @property
    def trigger_manager(self) -> TriggerManagerDE:
        """The trigger manager of the scenario"""
        return self._object_manager.managers['Trigger']

    @property
    def unit_manager(self) -> UnitManagerDE:
        """The unit manager of the scenario"""
        return self._object_manager.managers['Unit']

    @property
    def map_manager(self) -> MapManagerDE:
        """The map manager of the scenario"""
        return self._object_manager.managers['Map']

    @property
    def xs_manager(self) -> XsManagerDE:
        """The XS manager of the scenario"""
        return self._object_manager.managers['Xs']

    @property
    def player_manager(self) -> PlayerManager:
        """The player manager of the scenario"""
        return self._object_manager.managers['Player']

    @property
    def message_manager(self) -> MessageManager:
        return self._object_manager.managers['Message']

    @property
    def option_manager(self) -> OptionManager:
        return self._object_manager.managers['Option']

    @classmethod
    def from_file(cls: Type[S], path: str, game_version: str = "DE", name: str = "") -> S:
        """
        Creates and returns an instance of the AoE2DEScenario class from the given scenario file

        Args:
            path: The path to the scenario file to create the object from
            game_version: The version of the game to create the object for
            name: The name given to this scenario (defaults to the filename without extension)

        Returns:
            An instance of the AoE2DEScenario class which is the object representation of the given scenario file
        """
        return super().from_file(path=path, game_version=game_version, name=name)
