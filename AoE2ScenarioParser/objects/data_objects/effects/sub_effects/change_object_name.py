

from binary_file_parser.retrievers import RetrieverRef

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.datasets.support.info_dataset_base import InfoDatasetBase
from AoE2ScenarioParser.datasets.triggers import EffectType
from AoE2ScenarioParser.objects.support import Area
from AoE2ScenarioParser.sections.bfp.triggers import EffectStruct

from AoE2ScenarioParser.objects.data_objects.effects.effect import Effect


class ChangeObjectName(Effect):
    _type_ = EffectType.CHANGE_OBJECT_NAME

    object: InfoDatasetBase = RetrieverRef(EffectStruct._object_list_unit_id)  # type:ignore
    """The specific TYPE of unit to be affected by the effect (NOT a specific unit)"""
    source_player: Player = RetrieverRef(EffectStruct._source_player)  # type:ignore
    """The player owning the object to be renamed, ignored when `selected_object_ids` is used"""
    string_id: int = RetrieverRef(EffectStruct._string_id)  # type:ignore
    """The string ID used for the name. Using this will override the name filed"""
    area: Area = RetrieverRef(EffectStruct._area)  # type:ignore
    """The area in which all matching units are killed. If left empty, the entire map is used. Ignored when `selected_object_ids` is used"""
    name: str = RetrieverRef(EffectStruct._message)  # type:ignore
    """The name to give to the affected unit(s)"""
    selected_object_ids: list[int] = RetrieverRef(
        EffectStruct._selected_object_ids  # type:ignore 
    )  # Todo: [Object vs Int]
    """The specific existing units to be affected by this effect. If set, ignores any other type of selection including player, type, group and area"""

    def __init__(
        self,
        object: InfoDatasetBase = -1,
        source_player: Player = Player.ONE,
        string_id: int = -1,
        area: Area = Area((-1, -1)),
        name: str = '',
        selected_object_ids: list[int] = None,
        **kwargs,
    ):
        """
        Change the name of all objects that are affected by this effect.

        Args:
            object: The specific TYPE of unit to be affected by the effect (NOT a specific unit)
            source_player: The player owning the object to be renamed, ignored when `selected_object_ids` is used
            string_id: The string ID used for the name. Using this will override the name filed
            area: The area in which all matching units are killed. If left empty, the entire map is used. Ignored when `selected_object_ids` is used
            name: The name to give to the affected unit(s)
            selected_object_ids: The specific existing units to be affected by this effect. If set, ignores any other type of selection including player, type, group and area
        """
        if area:
            area = Area.from_value(area)

        selected_object_ids = selected_object_ids or []

        super().__init__(local_vars = locals(), **kwargs)
