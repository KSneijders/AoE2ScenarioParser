from __future__ import annotations

from bfp_rs import ret, RetrieverRef

from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class DeleteKey(Effect):
    """
    This effect can be used to delete a key and its associated value from the key-value store. The key-value store is persistent across scenarios in a campaign, but these effects only function when the scenario is played as part of a campaign.
    """
    EFFECT_ID: int = 83

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    message: str = RetrieverRef(ret(Effect._message))
    """The name of the key to delete"""

    def __init__(
        self,
        message: str | None = None,
    ):
        super().__init__()

        self.message: str | None = message

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
