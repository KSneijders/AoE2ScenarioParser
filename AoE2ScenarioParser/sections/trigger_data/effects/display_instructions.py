from __future__ import annotations

from bfp_rs import ret, RetrieverRef

from AoE2ScenarioParser.datasets.buildings import BuildingInfo
from AoE2ScenarioParser.datasets.heroes import HeroInfo
from AoE2ScenarioParser.datasets.other import OtherInfo
from AoE2ScenarioParser.datasets.trigger_data.panel_location import PanelLocation
from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class DisplayInstructions(Effect):
    """
    This effect can be used to display a message in a panel for all players
    """
    EFFECT_ID: int = 20

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int = RetrieverRef(Effect._object_id)
    """The unit whose icon to the display in the panel"""

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player whose color to use in the icon"""

    str_id: int = RetrieverRef(Effect._str_id)
    """The string ID to use as the instruction message instead of the message field"""

    display_time: int = RetrieverRef(Effect._display_time)
    """The number of real-life seconds to display the instructions panel for"""

    instruction_panel_position: PanelLocation = RetrieverRef(Effect._instruction_panel_position)
    """The position on the screen where the instruction panel will be displayed"""

    play_sound: bool = RetrieverRef(Effect._play_sound)
    """When enabled, plays the message notification"""

    message: str = RetrieverRef(ret(Effect._message))
    """The instruction message to display in the panel"""

    sound_name: str = RetrieverRef(ret(Effect._sound_name))
    """The name of the sound to play when the instruction panel is shown"""

    def __init__(
        self,
        object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = None,
        source_player: Player | None = None,
        str_id: int | None = None,
        display_time: int | None = None,
        instruction_panel_position: PanelLocation | None = None,
        play_sound: bool | None = None,
        message: str | None = None,
        sound_name: str | None = None,
    ):
        super().__init__()

        self.object_id: UnitInfo | BuildingInfo | HeroInfo | OtherInfo | int | None = object_id
        self.source_player: Player | None = source_player
        self.str_id: int | None = str_id
        self.display_time: int | None = display_time
        self.instruction_panel_position: PanelLocation | None = instruction_panel_position
        self.play_sound: bool | None = play_sound
        self.message: str | None = message
        self.sound_name: str | None = sound_name

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
