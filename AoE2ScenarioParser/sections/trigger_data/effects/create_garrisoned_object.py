from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.sections.trigger_data import Effect
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.other import OtherInfo
from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.objects.support import Area, AreaT
from AoE2ScenarioParser.sections import Unit
from AoE2ScenarioParser.sections.trigger_data.concerns import HasSelectedUnitsAttribute
from AoE2ScenarioParser.concerns import CanHoldUnits

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class CreateGarrisonedObject(Effect, HasSelectedUnitsAttribute, CanHoldUnits):
    """
    This effect can be used to create a unit that is already garrisoned inside the specified units.
    """
    EFFECT_ID: int = 49

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = RetrieverRef(Effect._object_id)
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
        self._area = Area.from_value(value)

    object2_id: UnitInfo | int = RetrieverRef(Effect._object2_id)
    """The type of unit to create and garrison inside the affected units"""

    max_units_affected: int = RetrieverRef(Effect._max_units_affected)
    """The maximum number of units affected by this effect"""

    disable_sound: bool = RetrieverRef(Effect._disable_sound)
    """When enabled, disable the sound during the creation of the object"""

    def __init__(
        self,
        object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = -1,
        source_player: Player | int = -1,
        area: AreaT | None = None,
        object2_id: UnitInfo | int = -1,
        selected_units: list[Unit] | None = None,
        max_units_affected: int = -1,
        disable_sound: bool = False,
    ):
        super().__init__()

        self.object_id: BuildingInfo | HeroInfo | OtherInfo | UnitInfo | int = object_id
        self.source_player: Player | int = source_player
        self.area: AreaT = area or Area((-1, -1), (-1, -1))
        self.object2_id: UnitInfo | int = object2_id
        self._selected_unit_ref_ids: list[int] = []
        self._selected_units: tuple[Unit, ...] = ()
        self.selected_units: list[Unit] = selected_units or []
        self.max_units_affected: int = max_units_affected
        self.disable_sound: bool = disable_sound

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
