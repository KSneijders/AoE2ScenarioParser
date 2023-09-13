from binary_file_parser.retrievers import RetrieverRef

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.datasets.support.info_dataset_base import InfoDatasetBase
from AoE2ScenarioParser.datasets.trigger_data import ObjectClass, ObjectType, ActionType
from AoE2ScenarioParser.datasets.triggers import EffectType
from AoE2ScenarioParser.objects.support import Tile, Area, TileT
from AoE2ScenarioParser.sections.bfp.triggers import EffectStruct

from AoE2ScenarioParser.objects.data_objects.effects.effect import Effect

class TaskObject(Effect):
    _type_ = EffectType.TASK_OBJECT

    source_player: Player = RetrieverRef(EffectStruct._source_player)  # type:ignore
    """The player to create the object for"""
    object: InfoDatasetBase = RetrieverRef(EffectStruct._object_list_unit_id)  # type:ignore
    """The specific TYPE of unit to be affected by the effect (NOT a specific unit)"""
    location: Tile = RetrieverRef(EffectStruct._location)  # type:ignore
    """The location of the task; Where a unit should walk to, or shoot at, or go to work etc."""
    location_object: int = RetrieverRef(EffectStruct._location_object_reference)  # type:ignore
    """The location of the task but referencing a specific existing unit's location. (e.g. a tree for a villager to chop)"""
    area: Area = RetrieverRef(EffectStruct._area)  # type:ignore
    """The area in which all matching units are affected by this effect. If left empty, the entire map is used."""
    object_group: ObjectClass = RetrieverRef(EffectStruct._object_group)  # type:ignore
    """The unit group to be affected (e.g. Cavalry or Preditor Animal)."""
    object_type: ObjectType = RetrieverRef(EffectStruct._object_type)  # type:ignore
    """The broad unit type to be affected (Civilian, Military, Other or Building)."""
    action_type: ActionType = RetrieverRef(EffectStruct._action_type)  # type:ignore
    """The type of action to be executed by the effected units (e.g. Guard, Attack Ground or Drop Relic)"""
    selected_object_ids: list[int] = RetrieverRef(EffectStruct._selected_object_ids)  # type:ignore # Todo: [Object vs Int]
    """The specific existing units to be affected by this effect. If set, ignores all types, groups and area selections"""

    def __init__(
        self,
        source_player: Player = Player.ONE,
        object: InfoDatasetBase = -1,
        location: TileT = Tile(-1, -1),
        location_object: int = -1,
        area: Area = Area((-1, -1)),
        object_group: ObjectClass = -1,
        object_type: ObjectType = -1,
        action_type: ActionType = ActionType.DEFAULT,
        selected_object_ids: list[int] = None,
        **kwargs,
    ):
        """
        Task specific objects or a group of objects based on type, group and location to a set or dynamic destination.

        Args:
            source_player: The player to create the object for
            object: The specific TYPE of unit to be affected by the effect (NOT a specific unit)
            location: The location of the task; Where a unit should walk to, or shoot at, or go to work etc.
            location_object: The location of the task but referencing a specific existing unit's location. (e.g. a tree for a villager to chop)
            area: The area in which all matching units are affected by this effect. If left empty, the entire map is used.
            object_group: The unit group to be affected (e.g. Cavalry or Preditor Animal).
            object_type: The broad unit type to be affected (Civilian, Military, Other or Building).
            action_type: The type of action to be executed by the effected units (e.g. Guard, Attack Ground or Drop Relic)
            selected_object_ids: The specific existing units to be affected by this effect. If set, ignores all types, groups and area selections
        """
        if location:
            location = Tile.from_value(location)
        if area:
            area = Area.from_value(area)

        selected_object_ids = selected_object_ids or []

        super().__init__(local_vars = locals(), **kwargs)
