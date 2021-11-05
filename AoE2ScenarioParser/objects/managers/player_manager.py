from typing import List, Dict, Union

from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.data_objects.player import Player
from AoE2ScenarioParser.objects.data_objects.player_meta_data import PlayerMetaData
from AoE2ScenarioParser.objects.data_objects.player_resources import PlayerResources
from AoE2ScenarioParser.objects.support.uuid_list import UuidList
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink


class PlayerManager(AoE2Object):
    """Manager of the everything player related."""

    _link_list = [
        RetrieverObjectLink("_starting_ages", "Options", "per_player_starting_age"),
        RetrieverObjectLink("_lock_civilizations", "DataHeader", "per_player_lock_civilization"),
        RetrieverObjectLink("_resources", "PlayerDataTwo", "resources", process_as_object=PlayerResources),
        RetrieverObjectLink("_metadata", "DataHeader", "player_data_1", process_as_object=PlayerMetaData),
        RetrieverObjectLink("_base_priorities", "Options", "per_player_base_priority"),
        RetrieverObjectLink("_pop_caps", "Map", "per_player_population_cap"),
        RetrieverObjectLink("_tribe_names", "DataHeader", "tribe_names"),
        RetrieverObjectLink("_string_table_player_names", "DataHeader", "string_table_player_names"),
    ]

    def __init__(self,
                 _starting_ages: List[int],
                 _lock_civilizations: List[int],
                 _resources: List[PlayerResources],
                 _metadata: List[PlayerMetaData],
                 _base_priorities: List[int],
                 _pop_caps: List[int],
                 _tribe_names: List[str],
                 _string_table_player_names: List[int],
                 **kwargs
                 ):
        super().__init__(**kwargs)

        gaia_first_params = {}
        no_gaia_params = {
            'tribe_name': _tribe_names,
            'string_table_name_id': _string_table_player_names,
            'base_priority': _base_priorities,
        }
        gaia_last_params = {
            'starting_age': _starting_ages,
            'lock_civ': _lock_civilizations,
            'population_cap': _pop_caps,
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
                spread_player_attributes(player_attributes, key, lst, gaia_first)

        player_objects = []
        for p in PlayerId.all():
            player_objects.append(
                Player(**player_attributes[p])
            )
        self.players = player_objects

    @property
    def players(self) -> List[Player]:
        """Returns all player objects"""
        return self._players

    @players.setter
    def players(self, value: List[Player]) -> None:
        """Sets player objects"""
        self._players = UuidList(self._host_uuid, value)

    def set_default_starting_resources(self, players: List[PlayerId] = None) -> None:
        """
        Sets the default starting resources for all players

        Args:
            players (List[PlayerId]): A list of players, defaults to all players (incl GAIA) when left out
        """
        if players is None:
            players = PlayerId.all()
        for player in players:
            self.players[player].food = 200
            self.players[player].wood = 200
            self.players[player].gold = 100
            self.players[player].stone = 200

    # ###############################################################################################
    # ################################# Functions for reconstruction ################################
    # ###############################################################################################

    @property
    def _starting_ages(self):
        """Returns the starting age of all players"""
        return self._player_attributes_to_list("starting_age", False, default=2, fill_empty=7)

    @property
    def _lock_civilizations(self):
        """Returns the civ lock bool of all players"""
        return self._player_attributes_to_list("lock_civ", False, default=0, fill_empty=7)

    @property
    def _pop_caps(self):
        """Returns the population cap of all players"""
        return self._player_attributes_to_list("population_cap", False, default=200, fill_empty=7)

    @property
    def _resources(self) -> List[PlayerResources]:
        """Returns the resource objects for all players"""
        food = self._player_attributes_to_list("food", False, default=0, fill_empty=7)
        wood = self._player_attributes_to_list("wood", False, default=0, fill_empty=7)
        gold = self._player_attributes_to_list("gold", False, default=0, fill_empty=7)
        stone = self._player_attributes_to_list("stone", False, default=0, fill_empty=7)
        color = self._player_attributes_to_list("color", False, default=0, fill_empty=7)
        return UuidList(self._host_uuid, [
            PlayerResources(food[i], wood[i], gold[i], stone[i], color[i]) for i in range(len(food))
        ])

    @property
    def _metadata(self) -> List[PlayerMetaData]:
        """Returns the metadata objects for all players"""
        active = self._player_attributes_to_list("active", False, default=0, fill_empty=7)
        human = self._player_attributes_to_list("human", False, default=0, fill_empty=7)
        civilization = self._player_attributes_to_list("civilization", False, default=40, fill_empty=7)
        architecture_set = self._player_attributes_to_list("architecture_set", False, default=40, fill_empty=7)
        return UuidList(self._host_uuid, [
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
        return self._player_attributes_to_list("string_table_name_id", None, default=0, fill_empty=8)

    def _player_attributes_to_list(
            self,
            attribute: str,
            gaia_first: Union[bool, None] = True,
            default: Union[str, int] = 0,
            fill_empty: int = 0
    ) -> List:
        """
        The list to store in the scenario structure with values from all players.

        Args:
            attribute (str): The attribute to get from the players
            gaia_first (Union[bool, None]): If the list has gaia first, last or not at all
            default (Union[str, int]): The default value to fill the empty fields and what to end to an 16 field list
            fill_empty (int): How many empty elements have to be filled with the default value

        Returns:
            The list of values
        """
        players = player_list(gaia_first)
        default_list = [default] * fill_empty
        values = []
        for p in players:
            v = getattr(self.players[p], attribute)
            if v is None and gaia_first is None:
                v = default
            values.append(v)
        return values + default_list


def player_list(gaia_first: Union[None, bool] = True) -> List[PlayerId]:
    """
    Construct a list of players where GAIA can be first, last or not in the list at all

    Args:
        gaia_first (Union[None, bool]): If the list has gaia first, last or not at all

    Returns:
        The list of players
    """
    players = PlayerId.all(exclude_gaia=True)
    if gaia_first is not None:
        players.insert(0 if gaia_first else 8, PlayerId.GAIA)
    return players


def spread_player_attributes(player_attributes: Dict, key: str, lst: List,
                             gaia_first: Union[None, bool] = True) -> None:
    """
    Spreads list values to player attribute dictionaries

    Args:
        player_attributes (dict): Player attributes dict to save the values in
        key (str): The key to save the values under in the player dicts
        lst (List): The list of values
        gaia_first (Union[None, bool]): If the list has gaia first, last or not at all.
    """
    for index, p in enumerate(player_list(gaia_first)):
        player_attributes[p][key] = lst[index]
