import pytest

from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.managers import UnitManager
from AoE2ScenarioParser.sections import Unit


def test_clone_unit_returns_unit(um: UnitManager):
    original = um.add_unit(Player.ONE, Unit(x = 1, y = 2, z = 3.5))
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
    assert clone.garrisoned_in_ref == original.garrisoned_in_ref
    assert clone.caption_string_id == original.caption_string_id
    assert clone.caption_string == original.caption_string
    assert clone.player == original.player

    assert clone.reference_id != original.reference_id


def test_clone_unit_with_diff_player(um: UnitManager):
    original = um.add_unit(Player.ONE, Unit(x = 1, y = 2, z = 3.5))
    clone = um.clone_unit(original, Player.TWO)

    assert original.player == Player.ONE
    assert clone.player == Player.TWO


def test_clone_unit_with_no_player(um: UnitManager):
    original = Unit(x = 1, y = 2, z = 3.5)
    clone = um.clone_unit(original, Player.TWO)

    assert original.player is None
    assert clone.player == Player.TWO


def test_clone_unit_with_no_player_no_reassignment(um: UnitManager):
    original = Unit(x = 1, y = 2, z = 3.5)

    with pytest.raises(ValueError):
        um.clone_unit(original)
