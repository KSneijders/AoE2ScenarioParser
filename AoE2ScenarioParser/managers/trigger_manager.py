from __future__ import annotations

from bfp_rs import RefStruct, ret, RetrieverRef

from AoE2ScenarioParser.sections import ScenarioSections
from sections import TriggerData


class TriggerManager(RefStruct):

    # @formatter:off
    legacy_execution_order: bool         = RetrieverRef(ret(ScenarioSections.trigger_data), ret(TriggerData.is_legacy_execution_order))
    # @formatter:on
