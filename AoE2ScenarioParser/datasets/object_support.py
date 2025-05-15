from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


class StartingAge(_DataSetIntEnums):
    """
    **This is not the same as the "Age" dataset and should !!NOT!! be used in effects/conditions etc.**

    This enum class provides the integer values used to reference the starting ages in the game.
    This is used in the player objects to set a starting age.

    **Examples**

    >>> StartingAge.POST_IMPERIAL_AGE
    <StartingAge.POST_IMPERIAL_AGE: 6>
    """
    DARK_AGE = 2
    FEUDAL_AGE = 3
    CASTLE_AGE = 4
    IMPERIAL_AGE = 5
    POST_IMPERIAL_AGE = 6


class Civilization(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the civilizations in the game.
    This can be used in research tech conditions to check civ or set a players civ in the player manager.

    **Examples**

    >>> Civilization.VIKINGS
    <Civilization.VIKINGS: 11>
    """
    GAIA = 0
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
    HINDUSTANIS = 20
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
    POLES = 38
    BOHEMIANS = 39
    DRAVIDIANS = 40
    BENGALIS = 41
    GURJARAS = 42
    ROMANS = 43
    ARMENIANS = 44
    GEORGIANS = 45
    ACHAEMENIDS = 46
    ATHENIANS = 47
    SPARTANS = 48
    SHU = 49
    WU = 50
    WEI = 51
    JURCHENS = 52
    KHITANS = 53

    RANDOM = 65537
    FULL_RANDOM = 65539
