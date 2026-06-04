from __future__ import annotations

from bfp_rs import ret, RetrieverRef

from AoE2ScenarioParser.datasets.trigger_data.operation import Operation
from AoE2ScenarioParser.sections import Variable
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ChangeVariable(Effect):
    """
    This effect can be used to change the value of a trigger variable.
    """
    EFFECT_ID: int = 56

    quantity: int = RetrieverRef(Effect._quantity)
    """The value to use in the operation on the variable"""

    operation: Operation = RetrieverRef(Effect._operation)
    """The operation to apply to the variable using the quantity."""

    variable1_id: Variable = RetrieverRef(Effect._variable1_id)
    """The variable whose value will be changed"""

    message: str = RetrieverRef(ret(Effect._message))
    """The display name of the variable in the scenario editor. Setting this via ASP has no effect."""

    def __init__(
        self,
        quantity: int | None = None,
        operation: Operation | None = None,
        variable1_id: Variable | None = None,
        message: str | None = None,
    ):
        super().__init__()

        self.quantity: int | None = quantity
        self.operation: Operation | None = operation
        self.variable1_id: Variable | None = variable1_id
        self.message: str | None = message

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
