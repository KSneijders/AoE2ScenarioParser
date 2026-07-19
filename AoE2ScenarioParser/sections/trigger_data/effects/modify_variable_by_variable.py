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

    variable1_id: Variable | int = RetrieverRef(Effect._variable1_id)
    """The variable that will be modified"""

    operation: Operation | int = RetrieverRef(Effect._operation)
    """The operation to apply to the variable using the second variable."""

    variable2_id: Variable | int = RetrieverRef(Effect._variable2_id)
    """The variable whose value will be used in the operation"""

    def __init__(
        self,
        variable1_id: Variable | int = -1,
        operation: Operation | int = -1,
        variable2_id: Variable | int = -1,
    ):
        super().__init__()

        self.variable1_id: Variable | int = variable1_id
        self.operation: Operation | int = operation
        self.variable2_id: Variable | int = variable2_id

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
