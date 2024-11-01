from __future__ import annotations

from typing import List, Dict, Any

from AoE2ScenarioParser.datasets.object_support import Civilization
from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.datasets.trigger_lists import DiplomacyState
from AoE2ScenarioParser.exceptions.asp_exceptions import UnsupportedAttributeError
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.data_objects.player.player import Player
from AoE2ScenarioParser.objects.data_objects.player.player_data_four import PlayerDataFour
from AoE2ScenarioParser.objects.data_objects.player.player_data_three import PlayerDataThree
from AoE2ScenarioParser.objects.data_objects.player.player_diplomacy import PlayerDiplomacy
from AoE2ScenarioParser.objects.data_objects.player.player_initial_view import PlayerInitialView
from AoE2ScenarioParser.objects.data_objects.player.player_meta_data import PlayerMetaData
from AoE2ScenarioParser.objects.data_objects.player.player_resources import PlayerResources
from AoE2ScenarioParser.objects.support.uuid_list import UuidList
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink
from AoE2ScenarioParser.sections.retrievers.retriever_object_link_group import RetrieverObjectLinkGroup
from AoE2ScenarioParser.sections.retrievers.support import Support


class PlayerManager(AoE2Object):
    """Manager of everything player related."""

    # Todo: Implement a DE version separate of this.
    #  I'll be dealing with this IF support for other game versions will ever happen.

    _link_list = [
        RetrieverObjectLink("_player_count", "FileHeader", "player_count"),

        RetrieverObjectLinkGroup("DataHeader", group=[
            RetrieverObjectLink("_tribe_names", link="tribe_names"),
            RetrieverObjectLink("_string_table_player_names", link="string_table_player_names"),
            RetrieverObjectLink("_metadata", link="player_data_1", process_as_object=PlayerMetaData),
            RetrieverObjectLink("_lock_civilizations", link="per_player_lock_civilization"),
            RetrieverObjectLink("_lock_personalities", link="per_player_lock_personality", support=Support(since=1.53)),
        ]),

        RetrieverObjectLink("_resources", "PlayerDataTwo", "resources", process_as_object=PlayerResources),

        RetrieverObjectLinkGroup("Diplomacy", group=[
            RetrieverObjectLink("_diplomacy", link="per_player_diplomacy", process_as_object=PlayerDiplomacy),
            RetrieverObjectLink("_allied_victories", link="per_player_allied_victory"),
        ]),

        RetrieverObjectLinkGroup("Options", group=[
            *[
                RetrieverObjectLink(f"_disabled_{type_}_ids_player_{i}", link=f"disabled_{type_}_ids_player_{i}")
                for type_ in ["tech", "building", "unit"] for i in range(1, 9)
            ],
            RetrieverObjectLink("_starting_ages", link="per_player_starting_age"),
            RetrieverObjectLink("_base_priorities", link="per_player_base_priority"),
        ]),

        RetrieverObjectLink("_pop_caps", "Map", "per_player_population_cap", support=Support(since=1.44)),
        RetrieverObjectLink("_initial_player_views", "Map", "initial_player_views", support=Support(since=1.40), process_as_object=PlayerInitialView),

        RetrieverObjectLinkGroup("Units", group=[
            RetrieverObjectLink("_player_data_4", link="player_data_4", process_as_object=PlayerDataFour),
            RetrieverObjectLink("_player_data_3", link="player_data_3", process_as_object=PlayerDataThree),
        ]),
    ]

    def __init__(
            self,
            _player_count: int,
            _tribe_names: List[str],
            _string_table_player_names: List[int],
            _metadata: List[PlayerMetaData],
            _lock_civilizations: List[int],
            _lock_personalities: List[int],
            _resources: List[PlayerResources],
            _diplomacy: List[PlayerDiplomacy],
            _allied_victories: List[int],
            _starting_ages: List[int],
            _base_priorities: List[int],
            _pop_caps: List[int],
            _initial_player_views: List[PlayerInitialView],
            _player_data_4: List[PlayerDataFour],
            _player_data_3: List[PlayerDataThree],
            **kwargs
    ):
        super().__init__(**kwargs)

        disables = {}
        for type_ in ['tech', 'building', 'unit']:
            disables[type_] = [kwargs[f'_disabled_{type_}_ids_player_{p}'] for p in range(1, 9)]

        gaia_first_params = {
            'initial_player_view_x': [ipv.location_x for ipv in _initial_player_views or []],
            'initial_player_view_y': [ipv.location_y for ipv in _initial_player_views or []],
        }
        no_gaia_params = {
            'population_cap': [int(pd.population_limit) for pd in _player_data_4],
            'tribe_name': _tribe_names,
            'string_table_name_id': _string_table_player_names,
            'base_priority': _base_priorities,
            'allied_victory': _allied_victories,
            'disabled_techs': disables['tech'],
            'disabled_buildings': disables['building'],
            'disabled_units': disables['unit'],
            'initial_camera_x': [pd.initial_camera_x for pd in _player_data_3],
            'initial_camera_y': [pd.initial_camera_y for pd in _player_data_3],
            'diplomacy': [d.diplomacy_stance for d in _diplomacy],
        }
        gaia_last_params = {
            'starting_age': _starting_ages,
            'lock_civ': _lock_civilizations,
            'lock_personality': _lock_personalities,
            'food': [r.food for r in _resources],
            'wood': [r.wood for r in _resources],
            'gold': [r.gold for r in _resources],
            'stone': [r.stone for r in _resources],
            'color': [r.color for r in _resources],
            'active': [r.active for r in _metadata],
            'human': [r.human for r in _metadata],
            'civilization': [r.civilization for r in _metadata],
            'architecture_set': [r.architecture_set for r in _metadata],
        }

        param_sets = [(no_gaia_params, None), (gaia_first_params, True), (gaia_last_params, False)]
        player_attributes: Dict[int, Dict] = {i: {'player_id': PlayerId(i)} for i in range(9)}
        for param_set, gaia_first in param_sets:
            for key, lst in param_set.items():
                # If a property is not supported, fill it with Nones and skip it
                if lst is None or isinstance(lst, list) and len(lst) == 0:
                    _spread_player_attributes(player_attributes, key, [None] * 16, gaia_first)
                    continue
                _spread_player_attributes(player_attributes, key, lst, gaia_first)

        self.players = [Player(**player_attributes[p]) for p in PlayerId.all()]

    @property
    def active_players(self) -> int:
        """The amount of players that are active within the scenario"""
        return len([player for player in self.players if player.active])

    @active_players.setter
    def active_players(self, value: int):
        if not 1 <= value <= 8:
            raise ValueError("Active players value has to be between 1 and 8")
        for player_id in PlayerId.all(exclude_gaia=True):
            setattr(self.players[player_id], '_active', player_id <= value)

    @property
    def players(self) -> List[Player]:
        """Returns all player objects"""
        return self._players

    @players.setter
    def players(self, value: List[Player]) -> None:
        """Sets player objects"""
        self._players = UuidList(self._uuid, value)

    def set_default_starting_resources(self, players: List[PlayerId] = None) -> None:
        """
        Sets the default starting resources for all players

        Warning: Does NOT take civilizations into account
            This does not take the current selected civ of this player into account. For example, a player with the
            Chinese civ selected will still be set to 200 food. Generally speaking, it's recommended to not use this for
            competitive, normal play. You can select `low` resources in the lobby menu to get 'normal' resources for
            every civ.

        Args:
            players: A list of players, defaults to all players (incl GAIA) when left out
        """
        if players is None:
            players = PlayerId.all()
        for player in players:
            self.players[player].food = 200
            self.players[player].wood = 200
            self.players[player].gold = 100
            self.players[player].stone = 200

    def set_diplomacy_teams(self, *args: List[PlayerId | int], diplomacy: DiplomacyState = DiplomacyState.ALLY) \
            -> None:
        """
        Sets all players in list allied with all others in the same list.

        Args:
            *args: List(s) with player IDs that'll be set to the given diplomacy value
            diplomacy: The diplomacy to set the teams to. Defaults to ally.

        Examples:
            To set diplomacy like a 4v4 in ranked. Two teams of 4 with alternating IDs.

                set_diplomacy_teams([1,3,5,7], [2,4,6,8], diplomacy=DiplomacyState.ALLY)
        """
        for team in args:
            for player in team:
                if player == PlayerId.GAIA:
                    raise ValueError("Gaia cannot be in a team")
                self.players[player].set_player_diplomacy([p for p in team if p != player], diplomacy)

    # ###############################################################################################
    # ################################# Functions for reconstruction ################################
    # ###############################################################################################

    def __getattribute__(self, name: str) -> Any:
        if name.startswith('_disabled_'):
            type_ = name.split('_')[2]
            return getattr(self.players[int(name[-1])], f"disabled_{type_}s")

        return super().__getattribute__(name)

    @property
    def _player_count(self):
        """Returns number of active players to be stored in the FileHeader"""
        return self.active_players

    @property
    def _allied_victories(self):
        """Returns the allied victory of all players"""
        return self._player_attributes_to_list("allied_victory", None, default=0, fill_empty=8)

    @property
    def _starting_ages(self):
        """Returns the starting age of all players"""
        return self._player_attributes_to_list("starting_age", False, default=2, fill_empty=7)

    @property
    def _lock_civilizations(self):
        """Returns the civ lock bool of all players"""
        return self._player_attributes_to_list("lock_civ", False, default=0, fill_empty=7)

    @property
    def _lock_personalities(self):
        """Returns the civ lock bool of all players"""
        return self._player_attributes_to_list("lock_personality", False, default=0, fill_empty=7)

    @property
    def _pop_caps(self):
        """Returns the population cap of all players"""
        return self._player_attributes_to_list("population_cap", None, default=200, fill_empty=8)

    @property
    def _diplomacy(self):
        """Returns the diplomacy of all players"""
        diplomacies = self._player_attributes_to_list("diplomacy", None)

        player_diplomacies = UuidList(self._uuid, [
            PlayerDiplomacy(diplomacy_stance=diplomacies[i]) for i in range(8)
        ])
        player_diplomacies.extend([
            PlayerDiplomacy(diplomacy_stance=[3] * 16) for _ in range(8)
        ])
        return player_diplomacies

    @property
    def _player_data_4(self):
        """Returns the resource duplicates for all players"""
        population_limit = self._player_attributes_to_list("population_cap", None, default=200)
        food = self._player_attributes_to_list("food", None, default=0)
        wood = self._player_attributes_to_list("wood", None, default=0)
        gold = self._player_attributes_to_list("gold", None, default=0)
        stone = self._player_attributes_to_list("stone", None, default=0)

        return UuidList(self._uuid, [
            PlayerDataFour(
                population_limit=float(population_limit[i]),
                food_duplicate=float(food[i]),
                wood_duplicate=float(wood[i]),
                gold_duplicate=float(gold[i]),
                stone_duplicate=float(stone[i]),
            ) for i in range(8)
        ])

    @property
    def _player_data_3(self) -> List[PlayerDataThree]:
        """Returns the resource objects for all players"""
        original_map: Dict[int, str] = {0: 'ally', 1: 'neutral', 3: 'enemy'}
        mappings: Dict[str, Dict[str, int]] = {
            'diplomacy_for_interaction': {'self': 0, 'ally': 0, 'neutral': 1, 'enemy': 3, 'gaia': 3},
            'diplomacy_for_ai_system': {'self': 1, 'ally': 2, 'neutral': 3, 'enemy': 4, 'gaia': 0},
        }

        initial_camera_x = self._player_attributes_to_list("initial_camera_x", None, default=72)
        initial_camera_y = self._player_attributes_to_list("initial_camera_y", None, default=72)
        aok_allied_victory = self._player_attributes_to_list("allied_victory", None, default=0)
        color = self._player_attributes_to_list("color", False, default=1)
        diplomacies: List[List[int]] = self._player_attributes_to_list("diplomacy", None)

        other_diplomacies: Dict[str, List[List[int]]] = {}
        for player in range(8):
            diplomacy = diplomacies[player][:8]
            for key, mapping in mappings.items():
                lst = other_diplomacies.setdefault(key, [])
                temp_lst = [mapping['gaia']] + [mapping[original_map[n]] for n in diplomacy]
                temp_lst[player + 1] = mapping['self']
                lst.append(temp_lst)

        return UuidList(self._uuid, [
            PlayerDataThree(
                initial_camera_x[i],
                initial_camera_y[i],
                aok_allied_victory[i],
                other_diplomacies['diplomacy_for_interaction'][i],
                other_diplomacies['diplomacy_for_ai_system'][i],
                color[i],
            ) for i in range(len(initial_camera_x))
        ])

    @property
    def _resources(self) -> List[PlayerResources]:
        """Returns the resource objects for all players"""
        food = self._player_attributes_to_list("food", False, default=0, fill_empty=7)
        wood = self._player_attributes_to_list("wood", False, default=0, fill_empty=7)
        gold = self._player_attributes_to_list("gold", False, default=0, fill_empty=7)
        stone = self._player_attributes_to_list("stone", False, default=0, fill_empty=7)
        color = self._player_attributes_to_list("color", False, default=0)
        color.extend(range(9, 16))

        return UuidList(self._uuid, [
            PlayerResources(food[i], wood[i], gold[i], stone[i], color[i]) for i in range(len(food))
        ])

    @property
    def _metadata(self) -> List[PlayerMetaData]:
        """Returns the metadata objects for all players"""
        active = self._player_attributes_to_list("active", False, default=0, fill_empty=7)
        human = self._player_attributes_to_list("human", False, default=1, fill_empty=7)
        civilization = self._player_attributes_to_list("civilization", False, default=Civilization.RANDOM, fill_empty=7)
        architecture_set = self._player_attributes_to_list("architecture_set", False, default=Civilization.RANDOM, fill_empty=7)
        return UuidList(self._uuid, [
            PlayerMetaData(active[i], human[i], civilization[i], architecture_set[i]) for i in range(len(active))
        ])

    @property
    def _base_priorities(self) -> List[int]:
        """Returns the base priorities of all players"""
        return self._player_attributes_to_list("base_priority", None, default=0)

    @property
    def _tribe_names(self) -> List[str]:
        """Returns the tribe names of all players"""
        return self._player_attributes_to_list("tribe_name", None, default="", fill_empty=8)

    @property
    def _string_table_player_names(self) -> List[int]:
        """Returns the string table player names of all players"""
        return self._player_attributes_to_list("string_table_name_id", None, default=-2, fill_empty=8)

    @property
    def _initial_player_views(self):
        x = self._player_attributes_to_list("initial_player_view_x", gaia_first=True, default=-1, fill_empty=7)
        y = self._player_attributes_to_list("initial_player_view_y", gaia_first=True, default=-1, fill_empty=7)

        return UuidList(self._uuid, [PlayerInitialView(x[i], y[i]) for i in range(len(x))])

    def _player_attributes_to_list(
            self,
            attribute: str,
            gaia_first: bool | None = True,
            default: str | int = 0,
            fill_empty: int = 0
    ) -> List[Any]:
        """
        The list to store in the scenario structure with values from all players.

        Args:
            attribute: The attribute to get from the players
            gaia_first: If the list has gaia first, last or not at all
            default: The default value to fill the empty fields and what to end to an 16 field list
            fill_empty: How many empty elements have to be filled with the default value

        Returns:
            The list of values
        """
        players = _player_list(gaia_first)
        default_list = [default] * fill_empty
        values = []
        for p in players:
            try:
                v = getattr(self.players[p], attribute)
                if v is None and gaia_first is None:
                    v = default
            except UnsupportedAttributeError:
                v = None
            values.append(v)
        return values + default_list


def _player_list(gaia_first: None | bool = True) -> List[PlayerId]:
    """
    Construct a list of players where GAIA can be first, last or not in the list at all

    Args:
        gaia_first: If the list has gaia first, last or not at all

    Returns:
        The list of players
    """
    players = PlayerId.all(exclude_gaia=True)
    if gaia_first is not None:
        players.insert(0 if gaia_first else 8, PlayerId.GAIA)
    return players


def _spread_player_attributes(
        player_attributes: Dict,
        key: str,
        lst: List,
        gaia_first: None | bool = True
) -> None:
    """
    Spreads list values to player attribute dictionaries

    Args:
        player_attributes: Player attributes dict to save the values in
        key: The key to save the values under in the player dicts
        lst: The list of values
        gaia_first: If the list has gaia first, last or not at all.
    """
    for index, p in enumerate(_player_list(gaia_first)):
        player_attributes[p][key] = lst[index] if lst is not None else None
