class InvalidScenarioStructureError(Exception):
    pass


class UnknownScenarioStructureError(Exception):
    pass


class UnknownStructureError(Exception):
    pass


class EndOfFileError(Exception):
    pass


class UnsupportedAttributeError(Exception):
    pass


class WarningToError(Exception):
    pass


class UnsupportedVersionError(Exception):
    pass


def type_error_message(value, include_hint=True):
    return f"Expected int, found: {value.__class__}. " + (f"Maybe you meant: '{value}.ID'?" if include_hint else "")
