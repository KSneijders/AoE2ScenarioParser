from AoE2ScenarioParser.managers import TriggerManager
from tests.managers.functions import create_trigger


def test_import_triggers_allows_unlinked_triggers(tm: TriggerManager):
    trigger1 = create_trigger("T1")
    trigger2 = create_trigger("T2")

    tm.import_triggers((trigger1, trigger2))

    assert trigger1 in tm.triggers
    assert trigger2 in tm.triggers


def test_import_triggers_allows_linked_triggers(tm: TriggerManager, tm2: TriggerManager):
    trigger1 = create_trigger("T1")
    trigger2 = create_trigger("T2")

    tm.add_triggers((trigger1, trigger2))

    assert tm._is_linked_to_same(trigger1)
    assert tm._is_linked_to_same(trigger2)

    tm2.import_triggers((trigger1, trigger2))

    assert tm._is_not_linked_to_same(trigger1)
    assert tm._is_not_linked_to_same(trigger2)
    assert tm2._is_linked_to_same(trigger1)
    assert tm2._is_linked_to_same(trigger1)
