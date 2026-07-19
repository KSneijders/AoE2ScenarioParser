from __future__ import annotations

from typing import Iterable

from bfp_rs import RefStruct, ret, RetrieverRef, set_mut
from bfp_rs.bfp_rs import borrow_mut

import AoE2ScenarioParser.sections.trigger_data.effects as effects_module
from AoE2ScenarioParser.concerns import CanBeLinked, CanHoldUnits
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
        # noinspection PyTypeChecker
        struct: ScenarioSections = self._struct

        effect_map: dict[int, type[Effect]] = self._get_effect_mapping()
        for trigger in self.triggers:
            for effect in trigger.effects:
                if effect._type in effect_map:
                    effect.__class__ = effect_map[effect._type]

                    if hasattr(effect, 'selected_units'):
                        unit_mapping = struct.initialization_data._unit_reference_mapping

                        selected_units = []
                        for ref_id in effect._selected_unit_ref_ids:
                            unit = unit_mapping[ref_id]

                            selected_units.append(unit)
                            unit._add_trigger_artifact_reference(effect)

                        effect.selected_units = selected_units

            # Todo: Copy for conditions as well

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

        for effect in trigger.effects:
            self._validate_linkable_can_be_linked(effect)
        for condition in trigger.conditions:
            self._validate_linkable_can_be_linked(condition)

        self._link_other(trigger)

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
            trigger._unlink()

        return self.add_triggers(triggers)

        # Todo: Add clone_trigger (instead of copy)
