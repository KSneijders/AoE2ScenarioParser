from __future__ import annotations

import pytest

from AoE2ScenarioParser.managers import MapManager, UnitManager
from AoE2ScenarioParser.sections import ScenarioSections


@pytest.fixture
def um():
    sections = ScenarioSections()

    um = UnitManager(sections)
    um._initialize_properties()

    return um


@pytest.fixture
def mm():
    sections = ScenarioSections()

    mm = MapManager(sections)
    mm._initialize_properties()
    mm.map_size = 5

    return mm


