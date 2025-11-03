from __future__ import annotations

from typing import Optional, List
from uuid import UUID

from AoE2ScenarioParser.scenarios.scenario_store import store

from AoE2ScenarioParser.datasets.dataset_enum import dataset_or_value, _DataSet
from AoE2ScenarioParser.datasets.object_support import StartingAge, Civilization, CivilizationOld
from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.datasets.trigger_lists import DiplomacyState
from AoE2ScenarioParser.helper.list_functions import listify
from AoE2ScenarioParser.helper.printers import warn
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object


class Player(AoE2Object):
    """A class for handling all player information."""

    _object_attributes = [
        'player_id',
        'starting_age',
        'lock_civ',
        'food',
        'wood',
        'gold',
        'stone',
        'color',
        'active',
        'human',
        'civilization',
        'architecture_set',
    ]
    _object_attributes_non_gaia = [
        'population_cap',
        'diplomacy',
        'initial_camera_x',
        'initial_camera_y',
        'allied_victory',
        'disabled_techs',
        'disabled_buildings',
        'disabled_units',
        'base_priority',
        'tribe_name',
        'string_table_name_id',
        'initial_player_view_x',
        'initial_player_view_y',
    ]

    def __init__(
            self,
            player_id: int,
            starting_age: int,
            lock_civ: int,
            lock_personality: int,
            food: int,
            wood: int,
            gold: int,
            stone: int,
            color: int,
            active: bool,
            human: bool,
            civilization: int,
            architecture_set: int,

            # Optionals due to GAIA not having such value
            population_cap: Optional[int] = None,
            diplomacy: Optional[List[int]] = None,
            initial_camera_x: Optional[int] = None,
            initial_camera_y: Optional[int] = None,
            allied_victory: Optional[int] = None,
            disabled_techs: Optional[List[int]] = None,
            disabled_buildings: Optional[List[int]] = None,
            disabled_units: Optional[List[int]] = None,
            tribe_name: Optional[str] = None,
            base_priority: Optional[int] = None,
            string_table_name_id: Optional[int] = None,
            initial_player_view_x: Optional[int] = None,
            initial_player_view_y: Optional[int] = None,
            **kwargs
    ):
        super().__init__(**kwargs)

        self._player_id: int = player_id
        self._active: bool = active
        self.starting_age: int = dataset_or_value(StartingAge, starting_age)
        self.lock_civ: bool = bool(lock_civ)
        self.lock_personality: bool = bool(lock_personality)
        self.food: int = food
        self.wood: int = wood
        self.gold: int = gold
        self.stone: int = stone
        self.color: int = color
        self.human: bool = human
        self.civilization: str | Civilization = dataset_or_value(Civilization, civilization)
        self.architecture_set: str | Civilization = dataset_or_value(Civilization, architecture_set)

        # Optionals due to GAIA not having such value
        self.population_cap: Optional[int] = population_cap
        self.diplomacy: Optional[List[int]] = diplomacy
        self._initial_camera_x: Optional[int] = initial_camera_x  # ← Deprecated
        self._initial_camera_y: Optional[int] = initial_camera_y  # ← Deprecated
        self.allied_victory: Optional[bool] = bool(allied_victory) if allied_victory is not None else None
        self.disabled_techs: Optional[List[int]] = disabled_techs
        self.disabled_buildings: Optional[List[int]] = disabled_buildings
        self.disabled_units: Optional[List[int]] = disabled_units
        self.tribe_name: Optional[str] = tribe_name
        self.base_priority: Optional[int] = base_priority
        self.string_table_name_id: Optional[int] = string_table_name_id
        self.initial_player_view_x: Optional[int] = initial_player_view_x
        self.initial_player_view_y: Optional[int] = initial_player_view_y

    @property
    def civilization(self) -> Civilization | str | int:
        return self._civilization

    @civilization.setter
    def civilization(self, value: int | str | Civilization | CivilizationOld):
        self._civilization = self._to_civilization_dataset(value)

    @property
    def architecture_set(self) -> Civilization | str | int:
        return self._architecture_set

    @architecture_set.setter
    def architecture_set(self, value: int | str | Civilization | CivilizationOld):
        self._architecture_set = self._to_civilization_dataset(value)

    @property
    def _civilization_for_writing(self) -> int | str:
        return self._get_civilization_value_for_writing(self.civilization)

    @property
    def _architecture_set_for_writing(self) -> int | str:
        return self._get_civilization_value_for_writing(self.architecture_set)

    @property
    def initial_camera_x(self):
        warn("Unused by scenario. Use: `initial_player_view_x` instead", DeprecationWarning)
        return self._initial_camera_x

    @initial_camera_x.setter
    def initial_camera_x(self, value):
        warn("Unused by scenario. Use: `initial_player_view_x` instead", DeprecationWarning)
        self._initial_camera_x = value

    @property
    def initial_camera_y(self):
        warn("Unused by scenario. Use: `initial_player_view_y` instead", DeprecationWarning)
        return self._initial_camera_y

    @initial_camera_y.setter
    def initial_camera_y(self, value):
        warn("Unused by scenario. Use: `initial_player_view_y` instead", DeprecationWarning)
        self._initial_camera_y = value

    @property
    def player_id(self) -> int:
        """Read-only value of the player ID"""
        return self._player_id

    @property
    def active(self) -> bool:
        """Read-only value if this player is active or not"""
        return self._active

    def set_player_diplomacy(self, players: PlayerId | int | List[PlayerId | int], diplomacy: DiplomacyState):
        """
        Set the diplomacy of this player to other players.

        Note: This sets the player diplomacy ONE WAY!
            This does NOT set the other player's diplomacy to this player to the same diplomacy

        Args:
            players: The player(s) to change
            diplomacy: The diplomacy setting to set the player to
        """
        players: List[PlayerId | int] = listify(players)

        if self.player_id in players:
            raise ValueError("Cannot set diplomacy from and to the same player")

        for player in players:
            self.diplomacy[player - 1] = diplomacy

    def _get_object_attrs(self) -> list:
        attrs = self._object_attributes
        if self.player_id != PlayerId.GAIA:
            attrs.extend(self._object_attributes_non_gaia)
        return super()._get_object_attrs() + attrs

    def _get_civilization_value_for_writing(self, value: Civilization | CivilizationOld | str | int):
        if isinstance(value, Civilization) or isinstance(value, CivilizationOld):
            value = value.name
        elif isinstance(value, int) or isinstance(value, str):
            return value

        if Player.is_using_old_civilization_dataset(self._uuid):
            return CivilizationOld[value].value
        else:
            return Civilization[value].value

    @staticmethod
    def _to_civilization_dataset(value: int | str | Civilization | CivilizationOld) -> Civilization | int | str:
        def to_civilization(val) -> Civilization:
            if isinstance(val, Civilization):
                return val
            elif isinstance(val, CivilizationOld):
                return Civilization[val.name]
            elif isinstance(val, int):
                return Civilization[CivilizationOld(val).name]
            elif isinstance(val, str):
                return Civilization[val]
            else:
                raise TypeError(f"Unexpected type {type(val)}")

        # Try Except allows custom civ values
        try:
            return to_civilization(value)
        except (ValueError,  KeyError):
            return value

    @staticmethod
    def is_using_old_civilization_dataset(uuid: UUID):
        return store.get_scenario(uuid).scenario_version_tuple <= (1, 55)
