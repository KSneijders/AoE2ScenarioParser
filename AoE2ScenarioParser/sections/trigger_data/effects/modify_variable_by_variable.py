from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.datasets.trigger_data.operation import Operation
from AoE2ScenarioParser.sections import Variable
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ModifyVariableByVariable(Effect):
    """
    This effect can be used to modify a variable using the value of another variable.
    """
    EFFECT_ID: int = 100

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    variable1_id: Variable = RetrieverRef(Effect._variable1_id)
    """The variable that will be modified"""

    operation: Operation = RetrieverRef(Effect._operation)
    """The operation to apply to the variable using the second variable."""

    variable2_id: Variable = RetrieverRef(Effect._variable2_id)
    """The variable whose value will be used in the operation"""

    def __init__(
        self,
        variable1_id: Variable | None = None,
        operation: Operation | None = None,
        variable2_id: Variable | None = None,
    ):
        super().__init__()

        self.variable1_id: Variable | None = variable1_id
        self.operation: Operation | None = operation
        self.variable2_id: Variable | None = variable2_id

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
