from AoE2ScenarioParser.datasets.player_data import Player
from AoE2ScenarioParser.sections.trigger_data.effects import TaskObject
from managers.functions import create_unit


def test_set_selected_units():
    unit = create_unit(Player.ONE, ref = 3)
    unit2 = create_unit(Player.ONE, ref = 4)

    assert len(unit._get_trigger_artifact_references()) == 0
    assert len(unit2._get_trigger_artifact_references()) == 0

    effect = TaskObject(selected_units = [unit, unit2])

    assert effect.selected_units == (unit, unit2)
    assert effect._get_unit_references() == (unit, unit2)

    assert effect._selected_unit_ref_ids[0] == 3
    assert effect._selected_unit_ref_ids[1] == 4

    assert len(unit._get_trigger_artifact_references()) == 1
    assert len(unit2._get_trigger_artifact_references()) == 1
    assert unit._get_trigger_artifact_references()[0] == effect
    assert unit2._get_trigger_artifact_references()[0] == effect
