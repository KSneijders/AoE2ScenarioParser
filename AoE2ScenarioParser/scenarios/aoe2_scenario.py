from __future__ import annotations

from typing import Self

from AoE2ScenarioParser.managers import MapManager, UnitManager
from AoE2ScenarioParser.sections import ScenarioSections


class AoE2Scenario:

    def __init__(self, sections: ScenarioSections):
        super().__init__()

        self.sections = sections

        self.map_manager = MapManager(sections)
        self.unit_manager = UnitManager(sections)

    @classmethod
    def from_file(cls, path: str) -> Self:
        sections = ScenarioSections.from_file(path, strict = True)

        return cls(sections)

    def to_file(self, path: str) -> None:
        ScenarioSections.to_file(path, self.sections)


    # Todo: Scenario variant switching
    # Todo: Resetting internal name on write
    # Todo: On-write callbacks
    # Todo: Document from_default() scenario changes (difference between pre-v1 and BFP default)
    # Todo: Prevent source overwrite (unless configured otherwise)
