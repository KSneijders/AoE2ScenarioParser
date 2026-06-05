from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.trigger_data.button_location import ButtonLocation
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.other import OtherInfo
from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ChangeTrainLocation(Effect):
    """
    This effect can be used to change the type of building where a specific type of unit can be trained.
    """
    EFFECT_ID: int = 46

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = RetrieverRef(Effect._object_id)
    """The type of unit whose change train location will be changed"""

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player for whom the train location will be changed"""

    object2_id: UnitInfo = RetrieverRef(Effect._object2_id)
    """The type of building where the unit will now be trained"""

    button_location: ButtonLocation = RetrieverRef(Effect._button_location)
    """The location of the button to use. This number is given by the following formula: (row - 1) * 5 + column + 1"""

    def __init__(
        self,
        object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = None,
        source_player: Player | None = None,
        object2_id: UnitInfo | None = None,
        button_location: ButtonLocation | None = None,
    ):
        super().__init__()

        self.object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = object_id
        self.source_player: Player | None = source_player
        self.object2_id: UnitInfo | None = object2_id
        self.button_location: ButtonLocation | None = button_location

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
