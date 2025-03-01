from __future__ import annotations

from typing import Type, Union, Tuple, Optional

from AoE2ScenarioParser.exceptions.asp_exceptions import XsCheckValidationError
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

    LATEST_VERSION: Tuple[int, int] = (1, 54)

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
    def from_default(cls: Type[S], scenario_version: Optional[Union[str, Tuple[int, int]]] = None, **kwargs) -> S:
        """
        Creates and returns a default instance of the AoE2DEScenario class

        Args:
            scenario_version: The scenario version to generate

        Returns:
            An instance of the AoE2DEScenario class which is the object representation of the default scenario
        """
        return super().from_default(scenario_version or cls.LATEST_VERSION, "DE")

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

    def _internal_on_write(self, filename: str):
        super()._internal_on_write(filename)

        try:
            self.xs_manager.validate_scenario_xs()
        except XsCheckValidationError as e:
            raise XsCheckValidationError(str(e), xs_check_errors=e.xs_check_errors) from None

    def _write_as_default_scenario(self):
        """Create an empty default scenario. Meant for internal use only."""
        self.map_manager.map_size = 80

        for tile in self.map_manager.terrain:
            tile.elevation = 0
            tile.terrain_id = 0  # Grass
            tile.layer = -1

        self.unit_manager.units = []
        self.trigger_manager.triggers = []

        self.player_manager.active_players = 2

        for player in self.player_manager.players:
            player.food = 0
            player.wood = 0
            player.stone = 0
            player.gold = 0
            player.population_cap = 200

        for pdata3 in self.sections['Units'].player_data_3:
            pdata3.editor_camera_x = 40
            pdata3.editor_camera_y = 40
            pdata3.initial_camera_x = 40
            pdata3.initial_camera_y = 40

        self.sections['FileHeader'].creator_name = 'AoE2ScenarioParser'
        self.sections['DataHeader'].next_unit_id_to_place = 0

        self.write_to_file(f"default.aoe2scenario")
