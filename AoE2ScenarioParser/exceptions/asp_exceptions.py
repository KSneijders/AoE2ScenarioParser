class AoE2ScenarioParserError(Exception):
    """
    The super class of all errors in the AoE2ScenarioParser.
    Can be used to act on all AoE2ScenarioParser Errors at the same time
    """


class InvalidScenarioStructureError(AoE2ScenarioParserError):
    pass


class UnknownErrorDuringReadingIterationError(AoE2ScenarioParserError):
    def __init__(self, iteration: int, *args):
        super().__init__(*args)

        self.iteration = iteration


class UnknownScenarioStructureError(AoE2ScenarioParserError):
    pass


class UnknownStructureError(AoE2ScenarioParserError):
    pass


class EndOfFileError(AoE2ScenarioParserError):
    pass


class UnsupportedAttributeError(AoE2ScenarioParserError):
    pass


class WarningToError(AoE2ScenarioParserError):
    pass


class UnsupportedVersionError(AoE2ScenarioParserError):
    pass


class ScenarioWritingError(AoE2ScenarioParserError):
    pass


def type_error_message(value, include_hint=True):
    return f"Expected int, found: {value.__class__}. " + (f"Maybe you meant: '{value}.ID'?" if include_hint else "")
