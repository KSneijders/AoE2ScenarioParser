from __future__ import annotations

from bfp_rs import ret, RetrieverRef

from AoE2ScenarioParser.sections import Variable
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class StoreKeyValue(Effect):
    """
    This effect can be used to store the value of a variable into the key-value store. The key-value store is persistent across scenarios in a campaign, but these effects only function when the scenario is played as part of a campaign.
    """
    EFFECT_ID: int = 82

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    variable1_id: Variable = RetrieverRef(Effect._variable1_id)
    """The variable whose value will be stored"""

    message: str = RetrieverRef(ret(Effect._message))
    """The name of the key to store the value in"""

    def __init__(
        self,
        variable1_id: Variable | None = None,
        message: str | None = None,
    ):
        super().__init__()

        self.variable1_id: Variable | None = variable1_id
        self.message: str | None = message

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
