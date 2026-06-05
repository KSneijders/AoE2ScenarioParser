from __future__ import annotations

from bfp_rs import ret, RetrieverRef

from AoE2ScenarioParser.sections import Unit
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class LockGate(Effect):
    """
    This effect can be used to lock specific gates.
    """
    EFFECT_ID: int = 7

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    selected_unit_ref_ids: list[Unit] = RetrieverRef(ret(Effect._selected_unit_ref_ids))
    """The gates to be locked."""

    def __init__(
        self,
        selected_unit_ref_ids: list[Unit] | None = None,
    ):
        super().__init__()

        self.selected_unit_ref_ids: list[Unit] | None = selected_unit_ref_ids

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
