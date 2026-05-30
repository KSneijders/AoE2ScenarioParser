from AoE2ScenarioParser.managers import MapManager


def test_get_tile(mm: MapManager):
    assert mm.get_tile(i = 0) is mm.terrain[0][0]
    assert mm.get_tile(tile = (0, 0)) is mm.terrain[0][0]

    assert mm.get_tile(i = 20) is mm.terrain[4][0]

    assert mm.get_tile(i = 20) is mm.terrain[4][0]
