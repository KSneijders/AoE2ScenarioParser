from typing import Optional

from AoE2ScenarioParser.datasets.object_support import StartingAge
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object


class Player(AoE2Object):
    """Object for handling all player information."""

    _object_attributes = [
        'player_id',
        'starting_age',
        'lock_civ',
        'food',
        'wood',
        'gold',
        'stone',
        'color',
        'tribe_name',
        'string_table_name_id'
    ]

    def __init__(
            self,
            player_id: int,
            starting_age: int,
            lock_civ: int,
            food: int,
            wood: int,
            gold: int,
            stone: int,
            color: int,
            tribe_name: Optional[str] = None,  # Optional due to GAIA not having such value
            string_table_name_id: Optional[int] = None,  # Optional due to GAIA not having such value
            **kwargs
    ):
        super().__init__(**kwargs)

        self.player_id: int = player_id
        self.starting_age: int = StartingAge(starting_age)
        self.lock_civ: bool = bool(lock_civ)
        self.food: int = food
        self.wood: int = wood
        self.gold: int = gold
        self.stone: int = stone
        self.color: int = color
        self.tribe_name: Optional[str] = tribe_name
        self.string_table_name_id: Optional[int] = string_table_name_id

    def _get_object_attrs(self):
        return super()._get_object_attrs() + self._object_attributes
