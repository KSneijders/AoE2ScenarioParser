from __future__ import annotations

from typing import TYPE_CHECKING

from AoE2ScenarioParser.managers import MapManager, MessageManager, PlayerManager, UnitManager
from AoE2ScenarioParser.sections import ScenarioSections

if TYPE_CHECKING:
    from typing import Self


class AoE2Scenario:

    def __init__(self, sections: ScenarioSections):
        super().__init__()

        self.sections = sections

        self.message_manager = MessageManager(sections)

        self.map_manager = MapManager(sections)
        # noinspection PyProtectedMember
        self.map_manager._initialize_properties()

        self.unit_manager = UnitManager(sections)
        # noinspection PyProtectedMember
        self.unit_manager._initialize_properties()

        self.player_manager = PlayerManager(sections)
        # noinspection PyProtectedMember
        self.player_manager._initialize_properties()

    @classmethod
    def from_file(cls, path: str) -> Self:
        sections = ScenarioSections.from_file(path, strict = True)

        return cls(sections)

    def to_file(self, path: str) -> None:
        self.sections.to_file(path)

    # Todo: Scenario variant switching
    # Todo: Resetting internal name on write
    # Todo: On-write callbacks
    # Todo: Document from_default() scenario changes (difference between pre-v1 and BFP default)
    # Todo: Prevent source overwrite (unless configured otherwise)
