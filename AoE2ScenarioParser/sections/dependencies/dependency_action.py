from enum import Enum


class DependencyAction(Enum):
    """This is an enum class containing the values for the different retriever dependency actions"""
    REFRESH = 0
    REFRESH_SELF = 1
    SET_REPEAT = 2
    SET_VALUE = 3
