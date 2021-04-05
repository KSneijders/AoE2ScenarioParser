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


def type_error_message(value):
    return f"Expected int, found: {value.__class__}. Maybe you meant: '{value}.ID'?"
