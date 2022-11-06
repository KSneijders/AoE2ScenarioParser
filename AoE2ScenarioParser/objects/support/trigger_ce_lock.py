from __future__ import annotations

from typing import List


class TriggerCELock:
    """Object used to identify which conditions and effects should be locked from change"""
    def __init__(
            self,
            lock_conditions: bool = False,
            lock_effects: bool = False,
            lock_condition_type: List[int] | None = None,
            lock_effect_type: List[int] | None = None,
            lock_condition_ids: List[int] | None = None,
            lock_effect_ids: List[int] | None = None
    ):
        """
        Args:
            lock_conditions: Lock all conditions
            lock_effects: Lock all effects
            lock_condition_type: Lock certain condition types. Example: `ConditionId.OWN_OBJECTS`
            lock_effect_type: Lock certain effect types. Example: `EffectId.CREATE_OBJECT`
            lock_condition_ids: Lock certain conditions by their id
            lock_effect_ids: Lock certain effects by their id
        """
        if lock_condition_type is None:
            lock_condition_type = []
        if lock_effect_type is None:
            lock_effect_type = []
        if lock_condition_ids is None:
            lock_condition_ids = []
        if lock_effect_ids is None:
            lock_effect_ids = []

        self.lock_conditions = lock_conditions
        self.lock_effects = lock_effects
        self.lock_condition_type = lock_condition_type
        self.lock_effect_type = lock_effect_type
        self.lock_condition_ids = lock_condition_ids
        self.lock_effect_ids = lock_effect_ids
