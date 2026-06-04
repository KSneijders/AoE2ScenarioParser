from __future__ import annotations

from bfp_rs import ret, RetrieverRef

from AoE2ScenarioParser.datasets.trigger_data.action_type import ActionType
from AoE2ScenarioParser.objects.support import Area, AreaT
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.trigger_data.object_class import ObjectClass
from AoE2ScenarioParser.datasets.trigger_data.object_type import ObjectType
from AoE2ScenarioParser.datasets.other import OtherInfo
from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.objects.support import Tile, TileT
from AoE2ScenarioParser.sections import Unit
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class TaskObject(Effect):
    """
    This effect can be used to order units to perform a specific action at a target location or on a target object.
    """
    EFFECT_ID: int = 12

    object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = RetrieverRef(Effect._object_id)
    """The type of unit to task"""

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player whose units will be tasked"""

    @property
    def location(self) -> Tile:
        """The tile to send the tasked units to"""
        return self._location

    @location.setter
    def location(self, value: TileT) -> None:
        """The tile to send the tasked units to"""
        self._location = value

    location_unit_ref: Unit = RetrieverRef(Effect._location_unit_ref)
    """The target unit (as if it was right clicked)"""

    @property
    def area(self) -> Area:
        """The area in which units will be tasked. When not set, units across the entire map are tasked"""
        return self._area

    @area.setter
    def area(self, value: AreaT) -> None:
        """The area in which units will be tasked. When not set, units across the entire map are tasked"""
        self._area = value

    object_group: ObjectClass = RetrieverRef(Effect._object_group)
    """The units with this class will be affected by this effect"""

    object_type: ObjectType = RetrieverRef(Effect._object_type)
    """The units of this type will be affected by this effect"""

    action_type: ActionType = RetrieverRef(Effect._action_type)
    """The type of action to perform on the affected units"""

    selected_unit_ref_ids: list[Unit] = RetrieverRef(ret(Effect._selected_unit_ref_ids))
    """The units to be affected by this effect. When defined, overwrites all other unit filters, like area selection, type of unit, object type etc."""

    disable_garrison_unload_sound: bool = RetrieverRef(Effect._disable_garrison_unload_sound)
    """When enabled, disables the sound that plays when unloading garrisoned units"""

    max_units_affected: int = RetrieverRef(Effect._max_units_affected)
    """The maximum number of units affected by this effect"""

    issue_group_command: bool = RetrieverRef(Effect._issue_group_command)
    """When enabled, will issue a task as a group formation task, instead of every unit individually"""

    queue_action: bool = RetrieverRef(Effect._queue_action)
    """When enabled, the set task will be shift-queued"""

    def __init__(
        self,
        object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = None,
        source_player: Player | None = None,
        location: Tile | None = None,
        location_unit_ref: Unit | None = None,
        area: Area | None = None,
        object_group: ObjectClass | None = None,
        object_type: ObjectType | None = None,
        action_type: ActionType | None = None,
        selected_unit_ref_ids: list[Unit] | None = None,
        disable_garrison_unload_sound: bool | None = None,
        max_units_affected: int | None = None,
        issue_group_command: bool | None = None,
        queue_action: bool | None = None,
    ):
        super().__init__()

        self.object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = object_id
        self.source_player: Player | None = source_player
        self.location: Tile | None = location
        self.location_unit_ref: Unit | None = location_unit_ref
        self.area: Area | None = area
        self.object_group: ObjectClass | None = object_group
        self.object_type: ObjectType | None = object_type
        self.action_type: ActionType | None = action_type
        self.selected_unit_ref_ids: list[Unit] | None = selected_unit_ref_ids
        self.disable_garrison_unload_sound: bool | None = disable_garrison_unload_sound
        self.max_units_affected: int | None = max_units_affected
        self.issue_group_command: bool | None = issue_group_command
        self.queue_action: bool | None = queue_action

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
