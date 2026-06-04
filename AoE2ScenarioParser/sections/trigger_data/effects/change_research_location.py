from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.datasets.trigger_data.button_location import ButtonLocation
from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.datasets.techs import TechInfo
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ChangeResearchLocation(Effect):
    """
    This effect can be used to change the type of building where a specific technology can be researched.
    """
    EFFECT_ID: int = 47

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player for whom the research location will be changed"""

    technology_id: TechInfo = RetrieverRef(Effect._technology_id)
    """The technology whose research location will be changed"""

    object2_id: UnitInfo = RetrieverRef(Effect._object2_id)
    """The type of building where the technology will now be researched"""

    button_location: ButtonLocation = RetrieverRef(Effect._button_location)
    """The location of the button to use. This number is given by the following formula: (row - 1) * 5 + column + 1"""

    def __init__(
        self,
        source_player: Player | None = None,
        technology_id: TechInfo | None = None,
        object2_id: UnitInfo | None = None,
        button_location: ButtonLocation | None = None,
    ):
        super().__init__()

        self.source_player: Player | None = source_player
        self.technology_id: TechInfo | None = technology_id
        self.object2_id: UnitInfo | None = object2_id
        self.button_location: ButtonLocation | None = button_location

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
