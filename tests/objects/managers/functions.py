from __future__ import annotations

from AoE2ScenarioParser.sections import Unit


def create_unit():
    return Unit(
        type = 4,
        location = (.5, .5)
    )
