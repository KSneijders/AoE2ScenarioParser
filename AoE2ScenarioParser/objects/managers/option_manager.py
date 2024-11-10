from __future__ import annotations

from math import floor

from AoE2ScenarioParser.datasets.trigger_lists import VictoryCondition, SecondaryGameMode
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.sections.retrievers.retriever_object_link_group import RetrieverObjectLinkGroup
from AoE2ScenarioParser.sections.retrievers.support import Support


class OptionManager(AoE2Object):
    _link_list = [
        RetrieverObjectLinkGroup("GlobalVictory", group=[
            RetrieverObjectLink("victory_condition", link='mode'),
            RetrieverObjectLink("victory_score", link='required_score_for_score_victory'),
            RetrieverObjectLink("_victory_years_10ths", link='time_for_timed_game_in_10ths_of_a_year'),
            RetrieverObjectLink("victory_custom_conditions_required", link='all_custom_conditions_required'),
        ]),

        RetrieverObjectLinkGroup("Diplomacy", group=[
            RetrieverObjectLink("lock_teams"),
            RetrieverObjectLink("random_start_points"),
            RetrieverObjectLink("allow_players_choose_teams"),
        ]),

        RetrieverObjectLinkGroup("Map", group=[
            RetrieverObjectLink("collide_and_correct"),
            RetrieverObjectLink("villager_force_drop", support=Support(since=1.37)),
            RetrieverObjectLink("lock_coop_alliances", support=Support(since=1.42)),
            RetrieverObjectLink("secondary_game_modes", support=Support(since=1.42)),
        ]),
    ]

    def __init__(
            self,
            victory_condition: int,
            victory_score: int,
            _victory_years_10ths: int,
            victory_custom_conditions_required: bool,
            secondary_game_modes: int,
            lock_teams: bool,
            random_start_points: bool,
            allow_players_choose_teams: bool,
            collide_and_correct: bool,
            villager_force_drop: bool,
            lock_coop_alliances: bool,
            **kwargs
    ):
        super().__init__(**kwargs)

        if victory_condition in VictoryCondition:
            victory_condition = VictoryCondition(victory_condition)
        if secondary_game_modes in SecondaryGameMode:
            secondary_game_modes = SecondaryGameMode(secondary_game_modes)

        self.victory_condition: int | VictoryCondition = victory_condition
        self.victory_score: int = victory_score
        self._victory_years_10ths: int = _victory_years_10ths
        self.victory_custom_conditions_required: bool = bool(victory_custom_conditions_required)
        self.secondary_game_modes: int | SecondaryGameMode = secondary_game_modes

        self.lock_teams: bool = bool(lock_teams)
        self.random_start_points: bool = bool(random_start_points)
        self.allow_players_choose_teams: bool = bool(allow_players_choose_teams)
        self.collide_and_correct: bool = bool(collide_and_correct)
        self.villager_force_drop: bool = bool(villager_force_drop) if villager_force_drop is not None else None
        self.lock_coop_alliances: bool = bool(lock_coop_alliances) if lock_coop_alliances is not None else None

    @property
    def victory_years(self) -> float:
        return self._victory_years_10ths / 10

    @victory_years.setter
    def victory_years(self, value: float):
        self._victory_years_10ths = floor(value * 10)
