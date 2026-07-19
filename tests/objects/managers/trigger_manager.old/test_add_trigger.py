from AoE2ScenarioParser.managers import TriggerManager
from AoE2ScenarioParser.sections import Trigger
from tests.objects.managers.functions import create_trigger


def test_add_trigger_returns_trigger(tm: TriggerManager):
    result = tm.add_trigger(Trigger(name="Test"))

    assert isinstance(result, Trigger)
    assert result.name == "Test"


def test_add_trigger_adds_trigger(tm: TriggerManager):
    assert len(tm.triggers) == 0

    tm.add_trigger(create_trigger("T1"))
    assert len(tm.triggers) == 1

    tm.add_trigger(create_trigger("T2"))
    assert len(tm.triggers) == 2


def test_add_trigger_is_in_triggers(tm: TriggerManager):
    trigger = create_trigger("T1")
    tm.add_trigger(trigger)
    assert trigger in tm.triggers


def test_add_triggers_returns_triggers(tm: TriggerManager):
    result = tm.add_triggers([
        Trigger(name="T1"),
        Trigger(name="T2"),
        Trigger(name="T3"),
    ])

    assert isinstance(result, list)
    assert len(result) == 3
    for i, t in enumerate(result):
        assert isinstance(t, Trigger)
        assert t.name == f"T{i + 1}"


def test_add_triggers_adds_triggers(tm: TriggerManager):
    assert len(tm.triggers) == 0

    tm.add_triggers([create_trigger("T1"), create_trigger("T2")])
    assert len(tm.triggers) == 2

    tm.add_triggers([create_trigger("T3")])
    assert len(tm.triggers) == 3
