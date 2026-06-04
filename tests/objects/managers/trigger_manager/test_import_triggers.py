from AoE2ScenarioParser.managers import TriggerManager
from AoE2ScenarioParser.sections import ScenarioSections
from tests.objects.managers.functions import create_trigger


def test_import_triggers_allows_unlinked_triggers(tm: TriggerManager):
    trigger1 = create_trigger("T1")
    trigger2 = create_trigger("T2")

    tm.import_triggers((trigger1, trigger2))

    assert trigger1 in tm.triggers
    assert trigger2 in tm.triggers


def test_import_triggers_allows_linked_triggers():
    trigger1 = create_trigger("T1")
    trigger2 = create_trigger("T2")

    tm1 = TriggerManager(ScenarioSections())
    tm1._initialize_properties()
    tm1.add_triggers((trigger1, trigger2))

    assert tm1._is_linked_to_same(trigger1)

    tm2 = TriggerManager(ScenarioSections())
    tm2._initialize_properties()
    tm2.import_triggers((trigger1, trigger2))

    assert tm1._is_not_linked_to_same(trigger1)
    assert tm2._is_linked_to_same(trigger1)
