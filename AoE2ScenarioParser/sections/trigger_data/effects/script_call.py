from __future__ import annotations

from bfp_rs import ret, RetrieverRef

from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class ScriptCall(Effect):
    """
    This effect can be used to (define and) call an XS function.
    """
    EFFECT_ID: int = 55

    str_id: int = RetrieverRef(Effect._str_id)
    """The string ID of the XS script function name to call"""

    message: str = RetrieverRef(ret(Effect._message))
    """The name of the XS function to call or a function definition which will be called"""

    def __init__(
        self,
        str_id: int | None = None,
        message: str | None = None,
    ):
        super().__init__()

        self.str_id: int | None = str_id
        self.message: str | None = message

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
