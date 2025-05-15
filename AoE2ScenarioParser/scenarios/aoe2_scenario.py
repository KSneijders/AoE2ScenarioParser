from __future__ import annotations

from typing import Type

from AoE2ScenarioParser.objects.support.typedefs import Scenario
from AoE2ScenarioParser.sections import ScenarioSections


class AoE2Scenario:
    """All scenario objects are derived from this class"""

    @classmethod
    def from_file_bfp(cls: Type[Scenario], path: str) -> ScenarioSections:
        scenario = ScenarioSections.from_file(path, strict=True)

        return scenario

    # Todo: Scenario variant switching
    # Todo: Resetting internal name on write
    # Todo: On-write callbacks
    # Todo: Document from_default() scenario changes (difference between pre-v1 and BFP default)
    # Todo: Prevent source overwrite (unless configured otherwise)