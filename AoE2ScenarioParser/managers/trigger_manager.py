from __future__ import annotations

from typing import Iterable

from bfp_rs import RefStruct, ret, RetrieverRef, set_mut
from bfp_rs.bfp_rs import borrow_mut

import AoE2ScenarioParser.sections.trigger_data.effects as effects_module
from AoE2ScenarioParser.concerns import CanBeLinked
from AoE2ScenarioParser.sections import Condition, ScenarioSections, Trigger, TriggerDataSection
from AoE2ScenarioParser.sections.trigger_data.effect import Effect


class TriggerManager(RefStruct, CanBeLinked):
    _effect_mapping: dict[int, type[Effect]]
    _condition_mapping: dict[int, type[Condition]]

    # @formatter:off
    legacy_execution_order: bool = RetrieverRef(ret(ScenarioSections.trigger_data), ret(TriggerDataSection.is_legacy_execution_order))
    triggers: list[Trigger]     = RetrieverRef(ret(ScenarioSections.trigger_data), ret(TriggerDataSection.triggers))
    # @formatter:on

    def _initialize_properties(self):
        self._effect_mapping = {}
        self._condition_mapping = {}

        self._do_ce_conversions()

    def _do_ce_conversions(self):
        effect_map: dict[int, type[Effect]] = self._get_effect_mapping()
        for trigger in self.triggers:
            for i in range(len(trigger.effects)):
                # noinspection PyProtectedMember
                if trigger.effects[i]._type in effect_map:
                    # noinspection PyProtectedMember
                    trigger.effects[i].__class__ = effect_map[trigger.effects[i]._type]

            set_mut(trigger.effects, False)
            set_mut(trigger.conditions, False)
        set_mut(self.triggers, False)

    def _get_effect_mapping(self):
        if self._effect_mapping == {}:
            modules: list[type[Effect]] = list(vars(effects_module).values())

            self._effect_mapping = {
                cls.EFFECT_ID: cls
                for cls in modules
                if isinstance(cls, type) and issubclass(cls, Effect) and cls is not Effect
            }
        return self._effect_mapping

    def add_trigger(self, trigger: Trigger) -> Trigger:
        """
        Adds a trigger to the scenario

        Args:
            trigger: The trigger to add

        Returns:
            The added trigger
        """
        self._validate_linkable_can_be_linked(trigger)

        with borrow_mut(self.triggers):
            self.triggers.append(trigger)

        trigger._struct = self._struct  # Link the unit to this scenario

        return trigger

    def add_triggers(self, triggers: Iterable[Trigger]) -> list[Trigger]:
        """
        Adds triggers to the scenario

        Args:
            triggers: The triggers to add

        Returns:
            The added triggers
        """
        return [self.add_trigger(trigger) for trigger in triggers]

    def import_triggers(self, triggers: Iterable[Trigger]) -> list[Trigger]:
        # Todo: Update once effects and conditions have been implemented.
        for trigger in triggers:
            trigger._struct = None  # Unlink

        return self.add_triggers(triggers)

        # Todo: Add clone_trigger (instead of copy)
