from __future__ import annotations

from bfp_rs import RefStruct, ret, RetrieverRef

from AoE2ScenarioParser.sections import Diplomacy, GlobalVictory, Options, ScenarioSections, Settings
from AoE2ScenarioParser.datasets.trigger_data import SecondaryGameMode, VictoryCondition


class OptionManager(RefStruct):

    # @formatter:off
    _victory_type: int        = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.global_victory), ret(GlobalVictory.victory_type))
    min_score: int            = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.global_victory), ret(GlobalVictory.min_score))
    time_limit: int           = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.global_victory), ret(GlobalVictory.time_limit))
    meet_all_conditions: bool = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.global_victory), ret(GlobalVictory.meet_all_conditions))
    lock_teams_in_game: bool  = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.diplomacy), ret(Diplomacy.lock_teams_in_game))
    lock_teams_in_lobby: bool = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.diplomacy), ret(Diplomacy.lock_teams_in_lobby))
    random_start_points: bool = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.diplomacy), ret(Diplomacy.random_start_points))
    collide_and_correct: bool = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.options), ret(Options.collide_and_correct))
    villager_force_drop: bool = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.options), ret(Options.villager_force_drop))
    lock_coop_alliances: bool = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.options), ret(Options.lock_coop_alliances))
    _secondary_game_mode: int = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.options), ret(Options.secondary_game_mode))
    # @formatter:on

    @property
    def victory_type(self) -> VictoryCondition:
        return VictoryCondition(self._victory_type)

    @victory_type.setter
    def victory_type(self, value: VictoryCondition | int):
        self._victory_type = value

    @property
    def secondary_game_mode(self) -> SecondaryGameMode:
        return SecondaryGameMode(self._secondary_game_mode)

    @secondary_game_mode.setter
    def secondary_game_mode(self, value: SecondaryGameMode | int):
        self._secondary_game_mode = value
