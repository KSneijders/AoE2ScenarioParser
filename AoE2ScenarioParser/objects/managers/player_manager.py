from typing import List, Dict, Union

from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.helper.pretty_format import pretty_format_dict, pretty_format_list
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object
from AoE2ScenarioParser.objects.data_objects.player import Player
from AoE2ScenarioParser.objects.data_objects.player_resources import PlayerResources
from AoE2ScenarioParser.objects.support.uuid_list import UuidList
from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink


class PlayerManager(AoE2Object):
    """Manager of the everything player related."""

    _link_list = [
        RetrieverObjectLink("starting_ages", "Options", "per_player_starting_age"),
        RetrieverObjectLink("per_player_lock_civilization", "DataHeader", "per_player_lock_civilization"),
        RetrieverObjectLink("resources", "PlayerDataTwo", "resources", process_as_object=PlayerResources),
        RetrieverObjectLink("tribe_names", "DataHeader", "tribe_names"),
        RetrieverObjectLink("string_table_player_names", "DataHeader", "string_table_player_names"),
    ]

    def __init__(self,
                 starting_ages: List[int],
                 per_player_lock_civilization: List[int],
                 resources: List[PlayerResources],
                 tribe_names: List[str],
                 string_table_player_names: List[int],
                 **kwargs
                 ):
        super().__init__(**kwargs)

        no_gaia_params = {
            'tribe_name': tribe_names,
            'string_table_name_id': string_table_player_names,
        }
        gaia_first_params = {

        }
        gaia_last_params = {
            'starting_age': starting_ages,
            'lock_civ': per_player_lock_civilization,
            'food': [r.food for r in resources],
            'wood': [r.wood for r in resources],
            'gold': [r.gold for r in resources],
            'stone': [r.stone for r in resources],
            'color': [r.color for r in resources],
        }
        param_sets = [
            (no_gaia_params, None),
            (gaia_first_params, True),
            (gaia_last_params, False)
        ]

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

        print(pretty_format_list(self.players))

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, value):
        self._players = UuidList(self._host_uuid, value)


def spread_player_attributes(player_attributes: Dict, key: str, lst: List, gaia_first: Union[None, bool] = True):
    players = PlayerId.all(exclude_gaia=True)
    if gaia_first is not None:
        players.insert(0 if gaia_first else 8, PlayerId.GAIA)

    for index, p in enumerate(players):
        player_attributes[p][key] = lst[index]
