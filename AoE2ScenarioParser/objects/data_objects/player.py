from typing import Optional, List

from AoE2ScenarioParser.datasets.object_support import StartingAge
from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.objects.aoe2_object import AoE2Object


class Player(AoE2Object):
    """Object for handling all player information."""

    _object_attributes = [
        'player_id',
        'starting_age',
        'lock_civ',
        'population_cap',
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
    ]

    def __init__(
            self,
            player_id: int,
            starting_age: int,
            lock_civ: int,
            population_cap: int,
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
            **kwargs
    ):
        super().__init__(**kwargs)

        self.player_id: int = player_id
        self.starting_age: int = StartingAge(starting_age)
        self.lock_civ: bool = bool(lock_civ)
        self.population_cap: int = population_cap
        self.food: int = food
        self.wood: int = wood
        self.gold: int = gold
        self.stone: int = stone
        self.color: int = color
        self.active: bool = active
        self.human: bool = human
        self.civilization = civilization
        self.architecture_set = architecture_set

        # Optionals due to GAIA not having such value
        self.diplomacy: Optional[List[int]] = diplomacy
        self.initial_camera_x: Optional[int] = initial_camera_x
        self.initial_camera_y: Optional[int] = initial_camera_y
        self.allied_victory: Optional[bool] = bool(allied_victory) if allied_victory is not None else None
        self.disabled_techs: Optional[List[int]] = disabled_techs
        self.disabled_buildings: Optional[List[int]] = disabled_buildings
        self.disabled_units: Optional[List[int]] = disabled_units
        self.tribe_name: Optional[str] = tribe_name
        self.base_priority: int = base_priority
        self.string_table_name_id: Optional[int] = string_table_name_id

    def _get_object_attrs(self):
        attrs = self._object_attributes
        if self.player_id != PlayerId.GAIA:
            attrs.extend(self._object_attributes_non_gaia)
        return super()._get_object_attrs() + attrs
