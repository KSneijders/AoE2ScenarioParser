from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.managers import UnitManager
from AoE2ScenarioParser.sections import Unit


def test_get_first_player_unit_returning_none_when_unit_not_found(um: UnitManager):
    um.add_unit(Unit(Player.ONE, UnitInfo.ARCHER.ID, (1, 2)))

    result = um.get_first_player_unit(Player.ONE, UnitInfo.CROSSBOWMAN.ID)

    assert result is None

    result = um.get_first_player_unit(Player.TWO, UnitInfo.ARCHER.ID)

    assert result is None


def test_get_first_player_unit_returning_unit_when_unit_found(um: UnitManager):
    unit = Unit(Player.ONE, UnitInfo.ARCHER.ID, (1, 2))

    um.add_unit(unit)

    result = um.get_first_player_unit(Player.ONE, UnitInfo.ARCHER.ID)

    assert result is unit


def test_get_first_player_unit_returning_first_unit_when_unit_found(um: UnitManager):
    unit1 = Unit(Player.ONE, UnitInfo.ARCHER.ID, (1, 2))
    unit2 = Unit(Player.ONE, UnitInfo.ARCHER.ID, (3, 4))

    um.add_units((unit1, unit2))

    result = um.get_first_player_unit(Player.ONE, UnitInfo.ARCHER.ID)

    assert result is unit1


def test_get_first_player_unit_returning_only_right_player_unit(um: UnitManager):
    unit1 = Unit(Player.ONE, UnitInfo.ARCHER.ID, (1, 2))
    unit2 = Unit(Player.TWO, UnitInfo.ARCHER.ID, (3, 4))

    um.add_units((unit1, unit2))

    result = um.get_first_player_unit(Player.TWO, UnitInfo.ARCHER.ID)

    assert result is unit2
