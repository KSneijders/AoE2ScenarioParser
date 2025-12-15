from __future__ import annotations

from bfp_rs import RefStruct, ret, RetrieverRef

from AoE2ScenarioParser.managers.support import XsCheck
from AoE2ScenarioParser.sections import Options, ScenarioSections, Settings
from sections import Trigger


class XsManager(RefStruct):

    xs_check: XsCheck
    xs_trigger_initialized: bool = False
    _xs_trigger: Trigger

    # @formatter:off
    script_name: str = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.options), ret(Options.script_name))
    # @formatter:on

    def _initialize_properties(self):
        self._setup_xs_check()

    def _setup_xs_check(self):
        self.xs_check = XsCheck()

    # @property
    # def xs_trigger(self):
    #     if not self.xs_trigger_initialized:
    #         self._xs_trigger = Trigger()
    #
    #     return self._xs_trigger
