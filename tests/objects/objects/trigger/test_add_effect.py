from AoE2ScenarioParser.sections import Trigger
from AoE2ScenarioParser.sections.trigger_data.effect import Effect


def test_add_effect_returns_effect():
    trigger = Trigger()
    result = trigger.add_effect(Effect())

    assert isinstance(result, Effect)


def test_add_effect_adds_effect():
    trigger = Trigger()
    assert len(trigger.effects) == 0

    trigger.add_effect(Effect())
    assert len(trigger.effects) == 1

    trigger.add_effect(Effect())
    assert len(trigger.effects) == 2


def test_add_effect_is_in_effects():
    trigger = Trigger()
    effect = Effect()
    trigger.add_effect(effect)

    assert effect in trigger.effects


def test_add_effect_updates_display_orders():
    trigger = Trigger()

    assert trigger.effect_display_orders == []

    trigger.add_effect(Effect())
    trigger.add_effect(Effect())

    assert trigger.effect_display_orders == [0, 1]


def test_add_effects_returns_effects():
    trigger = Trigger()
    result = trigger.add_effects([Effect(), Effect(), Effect()])

    assert isinstance(result, list)
    assert len(result) == 3
    assert all(isinstance(e, Effect) for e in result)


def test_add_effects_adds_effects():
    trigger = Trigger()
    assert len(trigger.effects) == 0

    trigger.add_effects([Effect(), Effect()])
    assert len(trigger.effects) == 2

    trigger.add_effects([Effect()])
    assert len(trigger.effects) == 3
