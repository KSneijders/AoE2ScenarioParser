from enum import Enum


class DependencyAction(Enum):
    REFRESH = 0
    REFRESH_SELF = 1
    SET_REPEAT = 2
    SET_VALUE = 3
