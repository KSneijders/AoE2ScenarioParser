from binary_file_parser.retrievers import RetrieverRef

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.datasets.support.info_dataset_base import InfoDatasetBase
from AoE2ScenarioParser.datasets.trigger_data import ObjectType, ObjectClass
from AoE2ScenarioParser.datasets.triggers import EffectType
from AoE2ScenarioParser.objects.data_objects.effects.effect import Effect
from AoE2ScenarioParser.objects.support import Area
from AoE2ScenarioParser.sections.bfp.triggers import EffectStruct


class KillObject(Effect):
    _type_ = EffectType.KILL_OBJECT

    source_player: Player = RetrieverRef(EffectStruct._source_player)  # type:ignore
    """The player to create the object for"""
    object: InfoDatasetBase = RetrieverRef(EffectStruct._object_list_unit_id)  # type:ignore
    """The specific TYPE of unit to be affected by the effect (NOT a specific unit)"""
    area: Area = RetrieverRef(EffectStruct._area)  # type:ignore
    """The area in which all matching units are killed. If left empty, the entire map is used."""
    object_group: ObjectClass = RetrieverRef(EffectStruct._object_group)  # type:ignore
    """The unit group to be affected (e.g. Cavalry or Preditor Animal)."""
    object_type: ObjectType = RetrieverRef(EffectStruct._object_type)  # type:ignore
    """The broad unit type to be affected (Civilian, Military, Other or Building)."""
    selected_object_ids: list[int] = RetrieverRef(EffectStruct._selected_object_ids)  # type:ignore # Todo: [Object vs Int]
    """The specific existing units to be affected by this effect. If set, ignores all types, groups and area selections"""

    def __init__(
        self,
        source_player: Player,
        object: InfoDatasetBase = -1,
        area: Area = Area((-1, -1)),
        object_group: ObjectClass = -1,
        object_type: ObjectType = -1,
        selected_object_ids: list[int] = None,
        **kwargs,
    ):
        """
        Kill units selected through area, type, group or their object directly

        Args:
            source_player: The player to create the object for
            object: The specific TYPE of unit to be affected by the effect (NOT a specific unit)
            area: The area in which all matching units are killed. If left empty, the entire map is used.
            object_group: The unit group to be affected (e.g. Cavalry or Preditor Animal).
            object_type: The broad unit type to be affected (Civilian, Military, Other or Building).
            selected_object_ids: The specific existing units to be affected by this effect. If set, ignores all types, groups and area selections
        """
        if area:
            area = Area.from_value(area)

        selected_object_ids = selected_object_ids or []

        super().__init__(local_vars = locals(), **kwargs)
