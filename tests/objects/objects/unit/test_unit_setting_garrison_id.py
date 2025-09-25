from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.sections import Unit


def test_create_unit_with_identical_children():
    unit = Unit(
        player = Player.ONE,
        type = 4,
        location = (1, 4),
        garrisoned_units = [
            Unit.garrisoned(player = Player.ONE, type = 4),
            Unit.garrisoned(player = Player.ONE, type = 4)
        ]
    )

    assert len(unit.garrisoned_units) == 2


def test_create_unit_with_children():
    unit = Unit(
        player = Player.ONE,
        type = 4,
        location = (1, 4),
        reference_id = 1,
        garrisoned_units = [
            Unit.garrisoned(player = Player.ONE, type = 5, reference_id = 2),
            Unit.garrisoned(player = Player.ONE, type = 6, reference_id = 3)
        ]
    )

    assert len(unit.garrisoned_units) == 2
    assert unit.garrisoned_units[0].reference_id == 2
    assert unit.garrisoned_units[1].reference_id == 3

    assert unit.garrisoned_units[0].garrisoned_in is unit
    assert unit.garrisoned_units[0]._garrisoned_in_ref == unit.reference_id

    assert unit.garrisoned_units[1].garrisoned_in is unit
    assert unit.garrisoned_units[1]._garrisoned_in_ref == unit.reference_id


def test_set_through_child():
    unit = Unit.garrisoned(player = Player.ONE, type = 4, reference_id = 1)
    parent = Unit(
        player = Player.ONE,
        type = 5,
        location = (3, 5),
        reference_id = 2,
    )
    unit.garrisoned_in = parent

    assert unit.garrisoned_in is parent
    assert unit._garrisoned_in_ref == parent.reference_id

    assert parent.garrisoned_units[0] is unit


def test_set_through_parent():
    unit = Unit.garrisoned(player = Player.ONE, type = 4, reference_id = 1)
    parent = Unit(
        player = Player.ONE,
        type = 8,
        location = (5, 6),
        reference_id = 2,
    )
    parent.garrisoned_units = tuple([unit])

    assert unit.garrisoned_in is parent
    assert unit._garrisoned_in_ref == parent.reference_id

    assert parent.garrisoned_units[0] is unit


def test_parent_add_garrisoned_unit():
    unit1 = Unit.garrisoned(player = Player.ONE, type = 4, reference_id = 1)
    unit2 = Unit.garrisoned(player = Player.ONE, type = 4, reference_id = 2)
    parent = Unit(
        player = Player.ONE,
        type = 8,
        location = (5, 6),
        reference_id = 3,
    )
    parent.add_garrisoned_units(unit1, unit2)

    assert unit1.garrisoned_in is parent
    assert unit1._garrisoned_in_ref == parent.reference_id
    assert unit2.garrisoned_in is parent
    assert unit2._garrisoned_in_ref == parent.reference_id

    assert parent.garrisoned_units[0] is unit1
    assert parent.garrisoned_units[1] is unit2


def test_parent_remove_garrisoned_unit():
    unit1 = Unit.garrisoned(player = Player.ONE, type = 4, reference_id = 1)
    unit2 = Unit.garrisoned(player = Player.ONE, type = 4, reference_id = 2)

    parent = Unit(
        player = Player.ONE,
        type = 8,
        location = (5, 6),
        reference_id = 3,
        garrisoned_units = [unit1, unit2],
    )

    assert len(parent.garrisoned_units) == 2
    assert parent.garrisoned_units[0] is unit1

    parent.remove_garrisoned_units(unit1)

    assert len(parent.garrisoned_units) == 1
    assert parent.garrisoned_units[0] is unit2

    parent.remove_garrisoned_units(unit2)

    assert len(parent.garrisoned_units) == 0

    # Allow removal of units not garrisoned in parent
    parent.remove_garrisoned_units(unit2)


def test_remove_from_child():
    unit = Unit.garrisoned(player = Player.ONE, type = 4, reference_id = 1)
    parent = Unit(
        player = Player.ONE,
        type = 8,
        location = (5, 6),
        reference_id = 3,
        garrisoned_units = [unit],
    )

    assert len(parent.garrisoned_units) == 1
    assert parent.garrisoned_units[0] is unit

    unit.garrisoned_in = None

    assert len(parent.garrisoned_units) == 0
    assert unit._garrisoned_in_ref == -1

    # Allow setting to None when already no parent
    unit.garrisoned_in = None


def test_cannot_garrison_more_than_once():
    unit = Unit.garrisoned(player = Player.ONE, type = 4, reference_id = 1)
    parent = Unit(
        player = Player.ONE,
        type = 8,
        location = (5, 6),
        reference_id = 3,
        garrisoned_units = [unit],
    )

    assert len(parent.garrisoned_units) == 1
    assert parent.garrisoned_units[0] is unit

    parent.add_garrisoned_units(unit)

    assert len(parent.garrisoned_units) == 1


def test_is_garrisoned():
    unit = Unit.garrisoned(player = Player.ONE, type = 4, reference_id = 1)
    parent = Unit(
        player = Player.ONE,
        type = 8,
        location = (5, 6),
        reference_id = 2,
    )

    assert unit.is_garrisoned is False
    assert unit.is_not_garrisoned is True
    assert parent.is_garrisoned is False
    assert parent.is_not_garrisoned is True

    parent.add_garrisoned_units(unit)

    assert unit.is_garrisoned is True
    assert unit.is_not_garrisoned is False
    assert parent.is_garrisoned is False
    assert parent.is_not_garrisoned is True
