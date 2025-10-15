from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums, _DataSet


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


class CivilizationOld(_DataSetIntEnums):
    """Legacy enum class used to reference the civilizations in the game."""
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

    MACEDONIANS = 54
    THRACIANS = 55
    PURU = 56

    RANDOM = 65537
    FULL_RANDOM = 65539


class Civilization(_DataSet):
    """
    This enum class provides the integer values used to reference the civilizations in the game.
    This can be used in research tech conditions to check civ or set a player's civ in the player manager.

    **Examples**

    >>> Civilization.HUNS
    <Civilization.HUNS: HUN-CIV>
    """
    GAIA = "GAIA"
    BRITONS = "BRITON-CIV"
    FRANKS = "FRANKISH-CIV"
    GOTHS = "GOTHIC-CIV"
    TEUTONS = "TEUTONIC-CIV"
    JAPANESE = "JAPANESE-CIV"
    CHINESE = "CHINESE-CIV"
    BYZANTINES = "BYZANTINE-CIV"
    PERSIANS = "PERSIAN-CIV"
    SARACENS = "SARACEN-CIV"
    TURKS = "TURKISH-CIV"
    VIKINGS = "VIKING-CIV"
    MONGOLS = "MONGOL-CIV"
    CELTS = "CELTIC-CIV"

    SPANISH = "SPANISH-CIV"
    AZTECS = "AZTEC-CIV"
    MAYANS = "MAYAN-CIV"
    HUNS = "HUN-CIV"
    KOREANS = "KOREAN-CIV"

    ITALIANS = "ITALIAN-CIV"
    HINDUSTANIS = "INDIAN-CIV"
    INCAS = "INCAN-CIV"
    MAGYARS = "MAGYAR-CIV"
    SLAVS = "SLAVIC-CIV"

    PORTUGUESE = "PORTUGUESE-CIV"
    ETHIOPIANS = "ETHIOPIAN-CIV"
    MALIANS = "MALIAN-CIV"
    BERBERS = "BERBERS-CIV"

    KHMER = "KHMER-CIV"
    MALAY = "MALAY-CIV"
    BURMESE = "BURMESE-CIV"
    VIETNAMESE = "VIETNAMESE-CIV"

    BULGARIANS = "BULGARIANS-CIV"
    TATARS = "TATARS-CIV"
    CUMANS = "CUMANS-CIV"
    LITHUANIANS = "LITHUANIANS-CIV"

    BURGUNDIANS = "BURGUNDIANS-CIV"
    SICILIANS = "SICILIANS-CIV"

    POLES = "POLES-CIV"
    BOHEMIANS = "BOHEMIANS-CIV"

    DRAVIDIANS = "DRAVIDIANS-CIV"
    BENGALIS = "BENGALIS-CIV"
    GURJARAS = "GURJARAS-CIV"

    ROMANS = "ROMANS-CIV"

    ARMENIANS = "ARMENIANS-CIV"
    GEORGIANS = "GEORGIANS-CIV"

    ACHAEMENIDS = "ACHAEMENIDS-CIV"
    ATHENIANS = "ATHENIANS-CIV"
    SPARTANS = "SPARTANS-CIV"

    SHU = "SHU-CIV"
    WU = "WU-CIV"
    WEI = "WEI-CIV"
    JURCHENS = "JURCHENS-CIV"
    KHITANS = "KHITANS-CIV"

    MACEDONIANS = "MACEDONIANS-CIV";
    THRACIANS = "THRACIANS-CIV";
    PURU = "PURU-CIV";

    RANDOM = "RANDOM-CIV"
    MIRROR_RANDOM = "MIRROR-RANDOM-CIV"
    FULL_RANDOM = "FULL-RANDOM-CIV"
    CUSTOM_RANDOM = "CUSTOM-RANDOM-CIV"

    def encode(self, c):
        return self.value.encode(c)