from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.managers import UnitManager
from AoE2ScenarioParser.sections import Unit
from tests.objects.managers.functions import create_unit


def test_add_unit_returns_unit(um: UnitManager):
    result = um.add_unit(Unit(Player.THREE, 4, (1, 2)))

    assert isinstance(result, Unit)
    assert result.type == 4
    assert result.x == 1
    assert result.y == 2


def test_add_unit_adds_unit(um: UnitManager):
    assert len(list(um.get_all_units())) == 0

    um.add_unit(create_unit(Player.ONE))
    assert len(list(um.get_all_units())) == 1
    assert len(um.units[Player.ONE]) == 1

    um.add_unit(create_unit(Player.TWO))
    assert len(list(um.get_all_units())) == 2
    assert len(um.units[Player.TWO]) == 1


def test_add_unit_places_unit_in_right_player_units(um: UnitManager):
    unit = create_unit(Player.TWO)
    assert unit.player is Player.TWO
    um.add_unit(unit)
    assert unit.player == Player.TWO
    assert unit in um.units[Player.TWO]


def test_add_units_returns_units(um: UnitManager):
    result = um.add_units(
        [
            Unit(Player.ONE, 4, (1, 2)),
            Unit(Player.ONE, 4, (3, 4)),
            Unit(Player.ONE, 4, (5, 6))
        ]
    )

    assert isinstance(result, list)
    assert len(result) == 3

    for i in range(3):
        assert isinstance(result[i], Unit)
        assert result[i].x == 1 + (i * 2)
        assert result[i].y == 2 + (i * 2)


def test_add_units_adds_units(um: UnitManager):
    assert len(list(um.get_all_units())) == 0

    um.add_units([create_unit(Player.ONE), create_unit(Player.ONE), create_unit(Player.ONE)])
    assert len(list(um.get_all_units())) == 3
    assert len(um.units[Player.ONE]) == 3

    um.add_units([create_unit(Player.TWO), create_unit(Player.TWO)])
    assert len(list(um.get_all_units())) == 5
    assert len(um.units[Player.TWO]) == 2


def test_add_units_places_units_in_right_player_units(um: UnitManager):
    unit1, unit2 = create_unit(Player.FOUR), create_unit(Player.THREE)
    assert unit1.player is Player.FOUR
    assert unit2.player is Player.THREE
    um.add_units((unit1, unit2))
    assert unit1.player == Player.FOUR
    assert unit1 in um.units[Player.FOUR]
    assert unit2.player == Player.THREE
    assert unit2 in um.units[Player.THREE]
