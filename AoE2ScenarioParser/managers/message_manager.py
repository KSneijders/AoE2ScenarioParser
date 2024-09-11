from __future__ import annotations

from binary_file_parser import Manager, RetrieverRef

from AoE2ScenarioParser.helper.support import r
from AoE2ScenarioParser.sections import Messages, ScenarioSections, Settings


class MessageManager(Manager):
    # @formatter:off
    instructions: str        = RetrieverRef(r(ScenarioSections.settings), r(Settings.messages), r(Messages.instructions))
    hints: str               = RetrieverRef(r(ScenarioSections.settings), r(Settings.messages), r(Messages.hints))
    victory: str             = RetrieverRef(r(ScenarioSections.settings), r(Settings.messages), r(Messages.victory))
    loss: str                = RetrieverRef(r(ScenarioSections.settings), r(Settings.messages), r(Messages.loss))
    history: str             = RetrieverRef(r(ScenarioSections.settings), r(Settings.messages), r(Messages.history))
    scouts: str              = RetrieverRef(r(ScenarioSections.settings), r(Settings.messages), r(Messages.scouts))

    instructions_str_id: int = RetrieverRef(r(ScenarioSections.settings), r(Settings.messages), r(Messages.instructions_str_id))
    hints_str_id: int        = RetrieverRef(r(ScenarioSections.settings), r(Settings.messages), r(Messages.hints_str_id))
    victory_str_id: int      = RetrieverRef(r(ScenarioSections.settings), r(Settings.messages), r(Messages.victory_str_id))
    loss_str_id: int         = RetrieverRef(r(ScenarioSections.settings), r(Settings.messages), r(Messages.loss_str_id))
    history_str_id: int      = RetrieverRef(r(ScenarioSections.settings), r(Settings.messages), r(Messages.history_str_id))
    scouts_str_id: int       = RetrieverRef(r(ScenarioSections.settings), r(Settings.messages), r(Messages.scouts_str_id))
    # @formatter:on
