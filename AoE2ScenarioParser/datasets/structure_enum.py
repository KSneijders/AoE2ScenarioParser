"""For parsing scenario structures and showing data from file sections"""

from __future__ import annotations

from enum import Enum, IntEnum


class PlayerStructIndex(IntEnum):
    """Used in some 8x, 9x or 16x structs(not for all). Different from `PlayerId`."""
    ONE = 0
    TWO = 1
    THREE = 2
    FOUR = 3
    FIVE = 4
    SIX = 5
    SEVEN = 6
    EIGHT = 7
    GAIA = 8
    UNKNOWN_9 = 9
    UNKNOWN_10 = 10
    UNKNOWN_11 = 11
    UNKNOWN_12 = 12
    UNKNOWN_13 = 13
    UNKNOWN_14 = 14
    UNKNOWN_15 = 15
    UNKNOWN_16 = 16


class PlayerColorStructId(IntEnum):
    """
    In section `PlayerDataTwo` - `Resources` - `player_color`, and `Units` - `PlayerDataThree` - `color`.
    Different from `PlayerColorId` of Effect.
    """
    BLUE = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    AQUA = 4
    PURPLE = 5
    GREY = 6
    ORANGE = 7
    WHITE_GAIA = 8


class InternalAINameDE(Enum):
    """
    In section `PlayerDataTwo` - `ai_names`.
    Edited by `Editor -> Players -> Personality`.
    Related to `InternalAITypeDE`.
    """
    STANDARD = 'PromiDE'
    NONE = 'NoneAi'
    CD_VERSION = 'RandomGame'
    HD_VERSION = 'AI (HD version).ai'


class InternalAITypeDE(IntEnum):
    """
    In section `PlayerDataTwo` - `ai_types`.
    Edited by `Editor -> Players -> Personality`.
    Related to `InternalAINameDE`.
    """
    STANDARD = 1
    NONE = 2
    CD_VERSION = 3
    HD_VERSION = 0
    CUSTOM = 0


class GlobalVictoryMode(IntEnum):
    STANDARD = 0
    CONQUEST = 1
    SCORE = 2
    TIME_LIMIT = 3
    CUSTOM = 4


class MaxNumberOfTeams(IntEnum):
    """In principle it can only be 2, 3, 4."""
    TWO = 2
    THREE = 3
    FOUR = 4


class AgeId(IntEnum):
    DARK_AGE = 2
    FEUDAL_AGE = 3
    CASTLE_AGE = 4
    IMPERIAL_AGE = 5
    POST_IMPERIAL_AGE = 6


class CivilizationId(IntEnum):
    GAIA = 0
    """Never seen in scenario structure, not sure whether it makes sense or not."""
    BRITONS = 1
    FRANKS = 2
    GOTHS = 3
    TEUTONS = 4
    JAPANESE = 5
    CHINESE = 6
    BYZANTINES = 7
    PERSIANS = 8
    SARACENS = 9
    TURKS = 10
    VIKINGS = 11
    MONGOLS = 12
    CELTS = 13
    SPANISH = 14
    AZTECS = 15
    MAYANS = 16
    HUNS = 17
    KOREANS = 18
    ITALIANS = 19
    INDIANS = 20
    INCAS = 21
    MAGYARS = 22
    SLAVS = 23
    PORTUGUESE = 24
    ETHIOPIANS = 25
    MALIANS = 26
    BERBERS = 27
    KHMER = 28
    MALAY = 29
    BURMESE = 30
    VIETNAMESE = 31
    BULGARIANS = 32
    TATARS = 33
    CUMANS = 34
    LITHUANIANS = 35
    BURGUNDIANS = 36
    SICILIANS = 37
    RANDOM = 38
    UKNOWN_39 = 39
    """Never seen in scenario structure, not sure whether it makes sense or not."""
    FULL_RANDOM = 40
