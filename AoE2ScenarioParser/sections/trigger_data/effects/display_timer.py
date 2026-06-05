from __future__ import annotations

from bfp_rs import ret, RetrieverRef

from AoE2ScenarioParser.datasets.trigger_data.time_unit import TimeUnit
from AoE2ScenarioParser.sections.trigger_data.effect import Effect

if True:
    # ====== CUSTOM IMPORTS START ======
    pass
    # ====== CUSTOM IMPORTS END ======


class DisplayTimer(Effect):
    """
    This effect can be used to display a countdown timer on the screen.
    """
    EFFECT_ID: int = 37

    __slots__ = ()
    # Keeps the memory layout identical to Effect, required for __class__ reassignment.
    # Adding new instance attributes in a subclass will break this.

    str_id: int = RetrieverRef(Effect._str_id)
    """The string ID to use as the timer label instead of the message field"""

    display_time: int = RetrieverRef(Effect._display_time)
    """The initial value of the timer"""

    time_unit: TimeUnit = RetrieverRef(Effect._time_unit)
    """The unit of time to use (In game seconds, minutes or years (One year being 5 seconds))"""

    timer_id: int = RetrieverRef(Effect._timer_id)
    """The ID of the timer to display (multiple timers can be shown simultaneously)"""

    reset_timer: bool = RetrieverRef(Effect._reset_timer)
    """Removes the old timer if it exists, when disabled it will create multiple timers with the same ID, disable with caution"""

    message: str = RetrieverRef(ret(Effect._message))
    """The message to display for the timer. Use '<TIMER>' to show the timer in your message"""

    def __init__(
        self,
        str_id: int | None = None,
        display_time: int | None = None,
        time_unit: TimeUnit | None = None,
        timer_id: int | None = None,
        reset_timer: bool | None = None,
        message: str | None = None,
    ):
        super().__init__()

        self.str_id: int | None = str_id
        self.display_time: int | None = display_time
        self.time_unit: TimeUnit | None = time_unit
        self.timer_id: int | None = timer_id
        self.reset_timer: bool | None = reset_timer
        self.message: str | None = message

    # ====== CUSTOM LOGIC START ======
    # ====== CUSTOM LOGIC END ======
