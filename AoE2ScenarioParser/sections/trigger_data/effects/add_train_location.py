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


class AddTrainLocation(Effect):
    """
    This effect can be used to add an additional building where a specific type of unit can be trained.
    """
    EFFECT_ID: int = 102

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    object_id: BuildingInfo | HeroInfo | OtherInfo | UnitInfo | int = RetrieverRef(Effect._object_id)
    """The type of unit to add an additional train location for"""

    source_player: Player | int = RetrieverRef(Effect._source_player)
    """The player for whom the additional train location will be added"""

    object2_id: UnitInfo | int = RetrieverRef(Effect._object2_id)
    """The type of building where the unit can now be trained"""

    button_location: ButtonLocation | int = RetrieverRef(Effect._button_location)
    """The location of the button to use. This number is given by the following formula: (row - 1) * 5 + column + 1"""

    train_time: int = RetrieverRef(Effect._train_time)
    """The train time used for the new train location"""

    hotkey: int = RetrieverRef(Effect._hotkey)
    """The hotkey ID to use for the train location"""

    def __init__(
        self,
        object_id: BuildingInfo | HeroInfo | OtherInfo | UnitInfo | int = -1,
        source_player: Player | int = -1,
        object2_id: UnitInfo | int = -1,
        button_location: ButtonLocation | int = -1,
        train_time: int = -1,
        hotkey: int = -1,
    ):
        super().__init__()

        self.object_id: BuildingInfo | HeroInfo | OtherInfo | UnitInfo | int = object_id
        self.source_player: Player | int = source_player
        self.object2_id: UnitInfo | int = object2_id
        self.button_location: ButtonLocation | int = button_location
        self.train_time: int = train_time
        self.hotkey: int = hotkey

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
