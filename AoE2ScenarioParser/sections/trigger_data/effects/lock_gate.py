from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.sections.trigger_data import Effect
from AoE2ScenarioParser.sections import Unit
from AoE2ScenarioParser.sections.trigger_data.concerns import HasSelectedUnitsAttribute
from AoE2ScenarioParser.concerns import CanHoldUnits

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class LockGate(Effect, HasSelectedUnitsAttribute, CanHoldUnits):
    """
    This effect can be used to lock specific gates.
    """
    EFFECT_ID: int = 7

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    def __init__(
        self,
        selected_units: list[Unit] | None = None,
    ):
        super().__init__()

        self._selected_unit_ref_ids: list[int] = []
        self._selected_units: tuple[Unit, ...] = ()
        self.selected_units: list[Unit] = selected_units or []

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
