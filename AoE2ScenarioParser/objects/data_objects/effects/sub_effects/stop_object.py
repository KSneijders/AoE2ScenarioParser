from binary_file_parser.retrievers import RetrieverRef

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.datasets.support.info_dataset_base import InfoDatasetBase
from AoE2ScenarioParser.datasets.trigger_data import ObjectClass, ObjectType
from AoE2ScenarioParser.datasets.triggers import EffectType
from AoE2ScenarioParser.objects.data_objects.effects.effect import Effect
from AoE2ScenarioParser.objects.support import Area
from AoE2ScenarioParser.sections.bfp.triggers import EffectStruct


class StopObject(Effect):
    _type_ = EffectType.STOP_OBJECT

    object: InfoDatasetBase = RetrieverRef(EffectStruct._object_list_unit_id)  # type:ignore
    """The specific TYPE of unit to be affected by the effect (NOT a specific unit)"""
    source_player: Player = RetrieverRef(EffectStruct._source_player)  # type:ignore
    """The player owning the object to be affected, ignored when `selected_object_ids` is used"""
    area: Area = RetrieverRef(EffectStruct._area)  # type:ignore
    """The area in which all matching units are affected. If left empty, the entire map is used. Ignored when `selected_object_ids` is used"""
    object_group: ObjectClass = RetrieverRef(EffectStruct._object_group)  # type:ignore
    """The unit group to be affected (e.g. Cavalry or Preditor Animal)."""
    object_type: ObjectType = RetrieverRef(EffectStruct._object_type)  # type:ignore
    """The broad unit type to be affected (Civilian, Military, Other or Building)."""
    selected_object_ids: list[int] = RetrieverRef(
        EffectStruct._selected_object_ids  # type:ignore 
    )  # Todo: [Object vs Int]
    """The specific existing units to be affected by this effect. If set, ignores any other type of selection including player, type, group and area"""

    def __init__(
        self,
        quantity: int = -1,
        source_player: Player = Player.ONE,
        area: Area = Area((-1, -1)),
        object_group = -1,
        object_type = -1,
        selected_object_ids = None,
        **kwargs,
    ):
        """
        Stop all actions on objects that are affected by this effect.

        Args:
            object: The specific TYPE of unit to be affected by the effect (NOT a specific unit)
            source_player: The player owning the object to be affected, ignored when `selected_object_ids` is used
            area: The area in which all matching units are affected. If left empty, the entire map is used. Ignored when `selected_object_ids` is used
            object_group: The unit group to be affected (e.g. Cavalry or Preditor Animal).
            object_type: The broad unit type to be affected (Civilian, Military, Other or Building).
            selected_object_ids: The specific existing units to be affected by this effect. If set, ignores any other type of selection including player, type, group and area
        """
        if area:
            area = Area.from_value(area)

        selected_object_ids = selected_object_ids or []
        super().__init__(local_vars = locals(), **kwargs)
