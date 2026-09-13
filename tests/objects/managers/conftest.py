from __future__ import annotations

import pytest

from AoE2ScenarioParser.managers import MapManager, PlayerManager, TriggerManager, UnitManager
from AoE2ScenarioParser.sections import ScenarioSections
from AoE2ScenarioParser.sections.scx_initialization_data import ScenarioInitializationData


@pytest.fixture
def um():
    sections = ScenarioSections()
    sections.initialization_data = ScenarioInitializationData()

    um = UnitManager(sections)
    um._initialize_properties()

    return um


# Alias for when you need two trigger managers
um2 = um


@pytest.fixture
def mm():
    sections = ScenarioSections()
    sections.initialization_data = ScenarioInitializationData()

    mm = MapManager(sections)
    mm._initialize_properties()
    mm.map_size = 5

    return mm


@pytest.fixture
def tm():
    sections = ScenarioSections()
    sections.initialization_data = ScenarioInitializationData()

    tm = TriggerManager(sections)
    tm._initialize_properties()

    return tm


# Alias for when you need two trigger managers
tm2 = tm


@pytest.fixture
def pm():
    sections = ScenarioSections()
    sections.initialization_data = ScenarioInitializationData()

    pm = PlayerManager(sections)
    pm._initialize_properties()

    return pm
