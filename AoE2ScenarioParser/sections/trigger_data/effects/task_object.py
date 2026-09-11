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

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = RetrieverRef(Effect._object_id)
    """The type of unit to task"""

    source_player: Player | int = RetrieverRef(Effect._source_player)
    """The player whose units will be tasked"""

    @property
    def location(self) -> Tile:
        """The tile to send the tasked units to"""
        return self._location

    @location.setter
    def location(self, value: TileT) -> None:
        """The tile to send the tasked units to"""
        self._location = Tile.from_value(value)

    location_unit_ref: Unit | int = RetrieverRef(Effect._location_unit_ref)
    """The target unit (as if it was right clicked)"""

    @property
    def area(self) -> Area:
        """The area in which units will be tasked. When not set, units across the entire map are tasked"""
        return self._area

    @area.setter
    def area(self, value: AreaT) -> None:
        """The area in which units will be tasked. When not set, units across the entire map are tasked"""
        self._area = Area.from_value(value)

    object_group: ObjectClass | int = RetrieverRef(Effect._object_group)
    """The units with this class will be affected by this effect"""

    object_type: ObjectType | int = RetrieverRef(Effect._object_type)
    """The units of this type will be affected by this effect"""

    action_type: ActionType | int = RetrieverRef(Effect._action_type)
    """The type of action to perform on the affected units"""

    selected_unit_ref_ids: list[Unit] | None = RetrieverRef(ret(Effect._selected_unit_ref_ids))
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
        object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = -1,
        source_player: Player | int = -1,
        location: TileT | None = None,
        location_unit_ref: Unit | int = -1,
        area: AreaT | None = None,
        object_group: ObjectClass | int = -1,
        object_type: ObjectType | int = -1,
        action_type: ActionType | int = -1,
        selected_unit_ref_ids: list[Unit] | None = None,
        disable_garrison_unload_sound: bool = False,
        max_units_affected: int = -1,
        issue_group_command: bool = False,
        queue_action: bool = False,
    ):
        super().__init__()

        self.object_id: BuildingInfo | HeroInfo | OtherInfo | UnitInfo | int = object_id
        self.source_player: Player | int = source_player
        self.location: TileT = location or Tile(-1, -1)
        self.location_unit_ref: Unit | int = location_unit_ref
        self.area: AreaT = area or Area((-1, -1), (-1, -1))
        self.object_group: ObjectClass | int = object_group
        self.object_type: ObjectType | int = object_type
        self.action_type: ActionType | int = action_type
        self.selected_unit_ref_ids: list[Unit] = selected_unit_ref_ids or []
        self.disable_garrison_unload_sound: bool = disable_garrison_unload_sound
        self.max_units_affected: int = max_units_affected
        self.issue_group_command: bool = issue_group_command
        self.queue_action: bool = queue_action

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
