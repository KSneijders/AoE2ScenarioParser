from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.managers import UnitManager
from AoE2ScenarioParser.sections import Unit


def test_clone_garrisoned_unit(um: UnitManager):
    child = um.add_unit(Unit(Player.ONE, 4, (1, 2), 3.5, 4, 3.44, 11, -1, 'caption', reference_id = 12))

    clone = um.clone_unit(child)

    assert isinstance(clone, Unit)
    assert child is not clone
    assert clone.x == child.x
    assert clone.y == child.y
    assert clone.z == child.z
    assert clone.object_id == child.object_id
    assert clone.state == child.state
    assert clone.rotation == child.rotation
    assert clone.frame == child.frame
    assert clone._garrisoned_in_unit_ref == child._garrisoned_in_unit_ref
    assert clone.caption_string_id == child.caption_string_id
    assert clone.caption_string == child.caption_string
    assert clone.player == child.player

    assert clone.reference_id != child.reference_id


def test_clone_garrisoned_unit_clone_also_garrisoned(um: UnitManager):
    parent = Unit(Player.ONE, 4, (1, 2))

    child = um.add_unit(Unit(Player.ONE, 4, (1, 2), 3.5, 4, 3.44, 11, -1, 'caption'))
    child.garrisoned_in = parent

    clone = um.clone_unit(child)

    assert clone._garrisoned_in_unit_ref == child._garrisoned_in_unit_ref


def test_clone_unit_with_diff_player(um: UnitManager):
    original = um.add_unit(Unit(Player.ONE, 4, (1, 2)))
    clone = um.clone_unit(original, Player.TWO)

    assert original.player == Player.ONE
    assert clone.player == Player.TWO


def test_clone_unit_with_no_player(um: UnitManager):
    original = Unit(Player.ONE, 4, (1, 2))
    clone = um.clone_unit(original, Player.TWO)

    assert original.player == Player.ONE
    assert clone.player == Player.TWO
