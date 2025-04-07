import pytest

from AoE2ScenarioParser.managers import MapManager
from objects.support import AreaState
from tests.objects import MockScenarioSections


@pytest.fixture
def mm():
    return MapManager(MockScenarioSections())


def test_terrain_getter_area(mm: MapManager):
    area = mm.new_area()

    assert area == ((0, 0), (mm.map_size - 1, mm.map_size - 1))
    assert area.width == mm.map_size
    assert area.height == mm.map_size


def test_terrain_getter_area_pattern(mm: MapManager):
    area_pattern = mm.new_area_pattern()

    assert area_pattern.state == AreaState.RECT
    assert area_pattern.area == ((0, 0), (mm.map_size - 1, mm.map_size - 1))
    assert area_pattern.area.width == mm.map_size
    assert area_pattern.area.height == mm.map_size
    
