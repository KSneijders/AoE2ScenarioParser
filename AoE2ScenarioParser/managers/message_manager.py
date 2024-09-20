from __future__ import annotations

from binary_file_parser import Manager, ret, RetrieverRef

from AoE2ScenarioParser.sections import Messages, ScenarioSections, Settings


class MessageManager(Manager):
    # @formatter:off
    instructions: str        = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.messages), ret(Messages.instructions))
    hints: str               = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.messages), ret(Messages.hints))
    victory: str             = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.messages), ret(Messages.victory))
    loss: str                = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.messages), ret(Messages.loss))
    history: str             = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.messages), ret(Messages.history))
    scouts: str              = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.messages), ret(Messages.scouts))

    instructions_str_id: int = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.messages), ret(Messages.instructions_str_id))
    hints_str_id: int        = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.messages), ret(Messages.hints_str_id))
    victory_str_id: int      = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.messages), ret(Messages.victory_str_id))
    loss_str_id: int         = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.messages), ret(Messages.loss_str_id))
    history_str_id: int      = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.messages), ret(Messages.history_str_id))
    scouts_str_id: int       = RetrieverRef(ret(ScenarioSections.settings), ret(Settings.messages), ret(Messages.scouts_str_id))
    # @formatter:on
