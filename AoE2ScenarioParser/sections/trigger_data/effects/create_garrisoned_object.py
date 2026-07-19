from __future__ import annotations

from bfp_rs import ret, RetrieverRef

from AoE2ScenarioParser.objects.support import Area, AreaT
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.other import OtherInfo
from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.sections import Unit
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class CreateGarrisonedObject(Effect):
    """
    This effect can be used to create a unit that is already garrisoned inside the specified units.
    """
    EFFECT_ID: int = 49

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    object_id: BuildingInfo | HeroInfo | OtherInfo | UnitInfo | int = RetrieverRef(Effect._object_id)
    """The type of unit to receive the new garrisoned unit"""

    source_player: Player | int = RetrieverRef(Effect._source_player)
    """The player for whom the garrisoned unit will be created"""

    @property
    def area(self) -> Area:
        """The area in which to create the garrisoned unit. When not set, units across the entire map receive the garrisoned unit"""
        return self._area

    @area.setter
    def area(self, value: AreaT) -> None:
        """The area in which to create the garrisoned unit. When not set, units across the entire map receive the garrisoned unit"""
        self._area = value

    object2_id: UnitInfo | int = RetrieverRef(Effect._object2_id)
    """The type of unit to create and garrison inside the affected units"""

    selected_unit_ref_ids: None | list[Unit] = RetrieverRef(ret(Effect._selected_unit_ref_ids))
    """The units to be affected by this effect. When defined, overwrites all other unit filters, like area selection, type of unit, object type etc."""

    max_units_affected: int = RetrieverRef(Effect._max_units_affected)
    """The maximum number of units affected by this effect"""

    disable_sound: bool = RetrieverRef(Effect._disable_sound)
    """When enabled, disable the sound during the creation of the object"""

    def __init__(
        self,
        object_id: BuildingInfo | HeroInfo | OtherInfo | UnitInfo | int = -1,
        source_player: Player | int = -1,
        area: Area | None = None,
        object2_id: UnitInfo | int = -1,
        selected_unit_ref_ids: None | list[Unit] = None,
        max_units_affected: int = -1,
        disable_sound: bool = False,
    ):
        super().__init__()

        self.object_id: BuildingInfo | HeroInfo | OtherInfo | UnitInfo | int = object_id
        self.source_player: Player | int = source_player
        self.area: Area = area or ((-1, -1), (-1, -1))
        self.object2_id: UnitInfo | int = object2_id
        self.selected_unit_ref_ids: list[Unit] = selected_unit_ref_ids or []
        self.max_units_affected: int = max_units_affected
        self.disable_sound: bool = disable_sound

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
