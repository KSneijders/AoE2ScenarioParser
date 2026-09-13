import pytest

from AoE2ScenarioParser.exceptions.asp_exceptions import ObjectAlreadyLinkedError
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


def test_add_trigger_links_trigger(tm: TriggerManager):
    trigger = create_trigger("T1")
    tm.add_trigger(trigger)

    assert trigger._is_linked()
    assert tm._is_linked_to_same(trigger)


def test_add_trigger_cannot_add_already_linked_trigger(tm: TriggerManager, tm2: TriggerManager):
    trigger = create_trigger("T1")
    tm.add_trigger(trigger)

    with pytest.raises(ObjectAlreadyLinkedError):
        tm2.add_trigger(trigger)
