from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.objects.support import Area, AreaT
from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.trigger_data.object_class import ObjectClass
from AoE2ScenarioParser.datasets.other import OtherInfo
from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.sections import Variable
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class CountsUnitsIntoVariable(Effect):
    """
    This effect can be used to count units and store the result in a variable.
    """
    EFFECT_ID: int = 101

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = RetrieverRef(Effect._object_id)
    """The type of unit to count"""

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player whose units will be counted"""

    @property
    def area(self) -> Area:
        """The area in which units will be counted. When not set, units across the entire map are counted"""
        return self._area

    @area.setter
    def area(self, value: AreaT) -> None:
        """The area in which units will be counted. When not set, units across the entire map are counted"""
        self._area = value

    object_group: ObjectClass = RetrieverRef(Effect._object_group)
    """The units with this class will be affected by this effect"""

    variable2_id: Variable = RetrieverRef(Effect._variable2_id)
    """The variable in which the unit count will be stored"""

    def __init__(
        self,
        object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = None,
        source_player: Player | None = None,
        area: Area | None = None,
        object_group: ObjectClass | None = None,
        variable2_id: Variable | None = None,
    ):
        super().__init__()

        self.object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = object_id
        self.source_player: Player | None = source_player
        self.area: Area | None = area
        self.object_group: ObjectClass | None = object_group
        self.variable2_id: Variable | None = variable2_id

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
