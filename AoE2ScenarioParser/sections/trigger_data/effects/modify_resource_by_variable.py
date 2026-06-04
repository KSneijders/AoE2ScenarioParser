from __future__ import annotations

from bfp_rs import RetrieverRef

from AoE2ScenarioParser.datasets.trigger_data.operation import Operation
from AoE2ScenarioParser.datasets.player_data.player import Player
from AoE2ScenarioParser.datasets.trigger_data.player_attribute import PlayerAttribute
from AoE2ScenarioParser.sections import Variable
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ModifyResourceByVariable(Effect):
    """
    This effect can be used to modify the amount of a specific resource for the specified player using the value stored in a variable.
    """
    EFFECT_ID: int = 53

    resource: PlayerAttribute = RetrieverRef(Effect._resource)
    """The resource to modify"""

    source_player: Player = RetrieverRef(Effect._source_player)
    """The player whose resource will be modified"""

    operation: Operation = RetrieverRef(Effect._operation)
    """The operation to apply to the attribute using the variable."""

    variable1_id: Variable = RetrieverRef(Effect._variable1_id)
    """The variable whose value will be used to modify the resource"""

    def __init__(
        self,
        resource: PlayerAttribute | None = None,
        source_player: Player | None = None,
        operation: Operation | None = None,
        variable1_id: Variable | None = None,
    ):
        super().__init__()

        self.resource: PlayerAttribute | None = resource
        self.source_player: Player | None = source_player
        self.operation: Operation | None = operation
        self.variable1_id: Variable | None = variable1_id

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
