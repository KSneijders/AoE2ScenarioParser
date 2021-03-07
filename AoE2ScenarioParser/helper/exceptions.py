# Todo: Add 'exception' or 'error' to the names for clarity


class InvalidScenarioStructure(Exception):
    pass


class UnknownScenarioStructure(Exception):
    pass


class EndOfFileError(Exception):
    pass


class UnsupportedAttributeError(Exception):
    pass
