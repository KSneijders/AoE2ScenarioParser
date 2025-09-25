from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.managers import UnitManager
from AoE2ScenarioParser.sections import Unit


def test_clone_unit_returns_unit(um: UnitManager):
    original = um.add_unit(Unit(Player.ONE, 4, (1, 2), 3.5, 4, 3.44, 11, -1, 'caption', 12))
    original.garrisoned_in = Unit(Player.ONE, 4, (1, 2), reference_id = 12)

    clone = um.clone_unit(original)

    assert isinstance(clone, Unit)
    assert original is not clone
    assert clone.x == original.x
    assert clone.y == original.y
    assert clone.z == original.z
    assert clone.type == original.type
    assert clone.state == original.state
    assert clone.rotation == original.rotation
    assert clone.frame == original.frame
    assert clone._garrisoned_in_ref == original._garrisoned_in_ref
    assert clone.caption_string_id == original.caption_string_id
    assert clone.caption_string == original.caption_string
    assert clone.player == original.player

    assert clone.reference_id != original.reference_id


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
