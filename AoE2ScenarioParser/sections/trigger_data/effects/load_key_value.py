from __future__ import annotations

from bfp_rs import ret, RetrieverRef

from AoE2ScenarioParser.sections import Variable
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class LoadKeyValue(Effect):
    """
    This effect can be used to load a value from the key-value store into a variable. The key-value store is persistent across scenarios in a campaign, but these effects only function when the scenario is played as part of a campaign.
    """
    EFFECT_ID: int = 81

    variable1_id: Variable = RetrieverRef(Effect._variable1_id)
    """The variable in which the loaded value will be stored"""

    message: str = RetrieverRef(ret(Effect._message))
    """The name of the key to load"""

    quantity: int = RetrieverRef(Effect._quantity)
    """The default value to use if the key is not found"""

    def __init__(
        self,
        variable1_id: Variable | None = None,
        message: str | None = None,
        quantity: int | None = None,
    ):
        super().__init__()

        self.variable1_id: Variable | None = variable1_id
        self.message: str | None = message
        self.quantity: int | None = quantity

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
