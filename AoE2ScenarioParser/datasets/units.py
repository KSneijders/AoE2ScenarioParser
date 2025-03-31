from __future__ import annotations

from typing import List

from AoE2ScenarioParser.datasets.support.info_dataset_base import InfoDatasetBase


class UnitInfo(InfoDatasetBase):
    """
    This class provides information about most of the units in the game. Information about the following properties of
    a unit is found in this class:

     - Unit ID
     - Icon ID
     - Dead Unit ID
     - HotKey ID
     - If the unit is a gaia only unit (e.g. deer, boar, etc.)

    **Methods**

    >>> UnitInfo.vils()
    >>> UnitInfo.unique_units()

    **Inherited Methods from class InfoDatasetBase**

    >>> InfoDatasetBase.from_id()
    >>> InfoDatasetBase.from_dead_id()
    >>> InfoDatasetBase.from_icon_id()
    >>> InfoDatasetBase.from_hotkey_id()
    >>> InfoDatasetBase.gaia_only()
    >>> InfoDatasetBase.non_gaia()

    **Examples**

    >>> UnitInfo.VILLAGER_FEMALE.ID
    >>> 293

    >>> UnitInfo.PETARD.ICON_ID
    >>> 113

    >>> UnitInfo.PALADIN.DEAD_ID
    >>> 570

    >>> UnitInfo.VILLAGER_MALE.HOTKEY_ID
    >>> 16121

    >>> UnitInfo.DEER.IS_GAIA_ONLY
    >>> True
    """

    @staticmethod
    def vils(
            exclude_female: bool = False,
            exclude_male: bool = False,
            include_chronicles: bool = False,
    ) -> List[UnitInfo]:
        """
        Args:
            exclude_female: if set to true, exclude the female villagers
            exclude_male: if set to true, exclude the male villagers
            include_chronicles: if set to `True`, include chronicles villagers

        Returns:
            A list of villager UnitInfo objects
        """
        villagers = {
            "base": {
                "male": [
                    UnitInfo.VILLAGER_MALE,
                    UnitInfo.VILLAGER_MALE_MONASTERY,
                    UnitInfo.VILLAGER_MALE_BUILDER,
                    UnitInfo.VILLAGER_MALE_FARMER,
                    UnitInfo.VILLAGER_MALE_FISHERMAN,
                    UnitInfo.VILLAGER_MALE_FORAGER,
                    UnitInfo.VILLAGER_MALE_GOLD_MINER,
                    UnitInfo.VILLAGER_MALE_HUNTER,
                    UnitInfo.VILLAGER_MALE_LUMBERJACK,
                    UnitInfo.VILLAGER_MALE_REPAIRER,
                    UnitInfo.VILLAGER_MALE_SHEPHERD,
                    UnitInfo.VILLAGER_MALE_STONE_MINER,
                ],
                "female": [
                    UnitInfo.VILLAGER_FEMALE,
                    UnitInfo.VILLAGER_FEMALE_BUILDER,
                    UnitInfo.VILLAGER_FEMALE_FARMER,
                    UnitInfo.VILLAGER_FEMALE_FISHERMAN,
                    UnitInfo.VILLAGER_FEMALE_FORAGER,
                    UnitInfo.VILLAGER_FEMALE_GOLD_MINER,
                    UnitInfo.VILLAGER_FEMALE_HUNTER,
                    UnitInfo.VILLAGER_FEMALE_LUMBERJACK,
                    UnitInfo.VILLAGER_FEMALE_REPAIRER,
                    UnitInfo.VILLAGER_FEMALE_SHEPHERD,
                    UnitInfo.VILLAGER_FEMALE_STONE_MINER,
                ],
            },
            "chronicles": {
                "male": [
                    UnitInfo.VILLAGER_MALE_OYSTER_GATHERER,
                ],
                "female": [
                    UnitInfo.VILLAGER_FEMALE_OYSTER_GATHERER,
                ],
            },
        }

        units_to_return = []

        addons = ["base"]
        if include_chronicles:
            addons.append("chronicles")

        for addon in addons:
            if not exclude_female:
                units_to_return.extend(villagers[addon]["female"])
            if not exclude_male:
                units_to_return.extend(villagers[addon]["male"])

        return units_to_return

    @staticmethod
    def unique_units(
            exclude_elite_units: bool = False,
            exclude_non_elite_units: bool = False,
            exclude_castle_units: bool = False,
            exclude_non_castle_units: bool = False,
            include_chronicles: bool = False,
    ) -> List[UnitInfo]:
        """
        Args:
            exclude_elite_units: if set to `False`, exclude the elite unique units
            exclude_non_elite_units: if set to `False`, exclude the non elite unique units
            exclude_castle_units: if set to `False`, exclude the castle unique units
            exclude_non_castle_units: if set to `False`, excludes the unique units not trained at the castle
            include_chronicles: if set to `True`, will include all unique units added in the chronicles dlc

        Returns:
            A list of unique unit UniInfo objects
        """
        unique_units = {
            "base": {
                "castle": {
                    "non_elite": [
                        UnitInfo.ARAMBAI,
                        UnitInfo.BALLISTA_ELEPHANT,
                        UnitInfo.BERSERK,
                        UnitInfo.BOYAR,
                        UnitInfo.CAMEL_ARCHER,
                        UnitInfo.CAMEL_SCOUT,
                        UnitInfo.CATAPHRACT,
                        UnitInfo.CENTURION,
                        UnitInfo.CHAKRAM_THROWER,
                        UnitInfo.CHU_KO_NU,
                        UnitInfo.COMPOSITE_BOWMAN,
                        UnitInfo.CONQUISTADOR,
                        UnitInfo.COUSTILLIER,
                        UnitInfo.FLAMING_CAMEL,
                        UnitInfo.GBETO,
                        UnitInfo.GENOESE_CROSSBOWMAN,
                        UnitInfo.GHULAM,
                        UnitInfo.HUSKARL,
                        UnitInfo.HUSSITE_WAGON,
                        UnitInfo.JAGUAR_WARRIOR,
                        UnitInfo.JANISSARY,
                        UnitInfo.KAMAYUK,
                        UnitInfo.KARAMBIT_WARRIOR,
                        UnitInfo.KESHIK,
                        UnitInfo.KIPCHAK,
                        UnitInfo.KONNIK,
                        UnitInfo.LEITIS,
                        UnitInfo.LONGBOWMAN,
                        UnitInfo.MAGYAR_HUSZAR,
                        UnitInfo.MAMELUKE,
                        UnitInfo.MANGUDAI,
                        UnitInfo.MONASPA,
                        UnitInfo.OBUCH,
                        UnitInfo.ORGAN_GUN,
                        UnitInfo.PLUMED_ARCHER,
                        UnitInfo.RATHA_MELEE,
                        UnitInfo.RATHA_RANGED,
                        UnitInfo.RATTAN_ARCHER,
                        UnitInfo.SAMURAI,
                        UnitInfo.SERJEANT,
                        UnitInfo.SHOTEL_WARRIOR,
                        UnitInfo.TARKAN,
                        UnitInfo.TEUTONIC_KNIGHT,
                        UnitInfo.THROWING_AXEMAN,
                        UnitInfo.URUMI_SWORDSMAN,
                        UnitInfo.WAR_ELEPHANT,
                        UnitInfo.WAR_WAGON,
                        UnitInfo.WOAD_RAIDER,
                    ],
                    "elite": [
                        UnitInfo.ELITE_ARAMBAI,
                        UnitInfo.ELITE_BALLISTA_ELEPHANT,
                        UnitInfo.ELITE_BERSERK,
                        UnitInfo.ELITE_BOYAR,
                        UnitInfo.ELITE_CAMEL_ARCHER,
                        UnitInfo.ELITE_CATAPHRACT,
                        UnitInfo.ELITE_CENTURION,
                        UnitInfo.ELITE_CHAKRAM_THROWER,
                        UnitInfo.ELITE_CHU_KO_NU,
                        UnitInfo.ELITE_COMPOSITE_BOWMAN,
                        UnitInfo.ELITE_CONQUISTADOR,
                        UnitInfo.ELITE_COUSTILLIER,
                        UnitInfo.ELITE_GBETO,
                        UnitInfo.ELITE_GENOESE_CROSSBOWMAN,
                        UnitInfo.ELITE_GHULAM,
                        UnitInfo.ELITE_HUSKARL,
                        UnitInfo.ELITE_HUSSITE_WAGON,
                        UnitInfo.ELITE_JAGUAR_WARRIOR,
                        UnitInfo.ELITE_JANISSARY,
                        UnitInfo.ELITE_KAMAYUK,
                        UnitInfo.ELITE_KARAMBIT_WARRIOR,
                        UnitInfo.ELITE_KESHIK,
                        UnitInfo.ELITE_KIPCHAK,
                        UnitInfo.ELITE_KONNIK,
                        UnitInfo.ELITE_LEITIS,
                        UnitInfo.ELITE_LONGBOWMAN,
                        UnitInfo.ELITE_MAGYAR_HUSZAR,
                        UnitInfo.ELITE_MAMELUKE,
                        UnitInfo.ELITE_MANGUDAI,
                        UnitInfo.ELITE_MONASPA,
                        UnitInfo.ELITE_OBUCH,
                        UnitInfo.ELITE_ORGAN_GUN,
                        UnitInfo.ELITE_PLUMED_ARCHER,
                        UnitInfo.ELITE_RATHA_MELEE,
                        UnitInfo.ELITE_RATHA_RANGED,
                        UnitInfo.ELITE_RATTAN_ARCHER,
                        UnitInfo.ELITE_SAMURAI,
                        UnitInfo.ELITE_SERJEANT,
                        UnitInfo.ELITE_SHOTEL_WARRIOR,
                        UnitInfo.ELITE_TARKAN,
                        UnitInfo.ELITE_TEUTONIC_KNIGHT,
                        UnitInfo.ELITE_THROWING_AXEMAN,
                        UnitInfo.ELITE_URUMI_SWORDSMAN,
                        UnitInfo.ELITE_WAR_ELEPHANT,
                        UnitInfo.ELITE_WAR_WAGON,
                        UnitInfo.ELITE_WOAD_RAIDER,
                    ]
                },
                "non_elite": [
                    UnitInfo.CARAVEL,
                    UnitInfo.CAMEL_SCOUT,
                    UnitInfo.CONDOTTIERO,
                    UnitInfo.CONDOTTIERO_PLACEHOLDER,
                    UnitInfo.FLEMISH_MILITIA,
                    UnitInfo.FLEMISH_MILITIA_FEMALE,
                    UnitInfo.FLEMISH_MILITIA_MALE,
                    UnitInfo.GENITOUR,
                    UnitInfo.HOUFNICE,
                    UnitInfo.HUSKARL_BARRACKS,
                    UnitInfo.IMPERIAL_CAMEL_RIDER,
                    UnitInfo.IMPERIAL_SKIRMISHER,
                    UnitInfo.KONNIK_DISMOUNTED,
                    UnitInfo.KONNIK_KREPOST,
                    UnitInfo.LEGIONARY,
                    UnitInfo.LONGBOAT,
                    UnitInfo.MISSIONARY,
                    UnitInfo.SAVAR,
                    UnitInfo.SERJEANT_DONJON,
                    UnitInfo.SHRIVAMSHA_RIDER,
                    UnitInfo.SLINGER,
                    UnitInfo.TARKAN_STABLE,
                    UnitInfo.THIRISADAI,
                    UnitInfo.TURTLE_SHIP,
                    UnitInfo.WARRIOR_PRIEST,
                    UnitInfo.WARRIOR_PRIEST_WITH_RELIC,
                    UnitInfo.WINGED_HUSSAR,
                ],
                "elite": [
                    UnitInfo.ELITE_CARAVEL,
                    UnitInfo.ELITE_GENITOUR,
                    UnitInfo.ELITE_HUSKARL_BARRACKS,
                    UnitInfo.ELITE_KIPCHAK_CUMAN_MERCENARIES,
                    UnitInfo.ELITE_KONNIK_DISMOUNTED,
                    UnitInfo.ELITE_KONNIK_KREPOST,
                    UnitInfo.ELITE_LONGBOAT,
                    UnitInfo.ELITE_SERJEANT_DONJON,
                    UnitInfo.ELITE_SHRIVAMSHA_RIDER,
                    UnitInfo.ELITE_TARKAN_STABLE,
                    UnitInfo.ELITE_TURTLE_SHIP,
                ],
            },
            "chronicles": {
                "castle": {
                    "non_elite": [
                        UnitInfo.IMMORTAL_MELEE,
                        UnitInfo.IMMORTAL_RANGED,
                        UnitInfo.STRATEGOS,
                        UnitInfo.STRATEGOS_WITH_TAXIARCHS,
                        UnitInfo.HIPPEUS,
                        UnitInfo.HIPPEUS_WITH_AURA,
                    ],
                    "elite": [
                        UnitInfo.ELITE_IMMORTAL_MELEE,
                        UnitInfo.ELITE_IMMORTAL_RANGED,
                        UnitInfo.ELITE_STRATEGOS,
                        UnitInfo.ELITE_STRATEGOS_WITH_TAXIARCHS,
                        UnitInfo.ELITE_HIPPEUS,
                        UnitInfo.ELITE_HIPPEUS_WITH_AURA,
                    ]
                },
                "non_elite": [
                ],
                "elite": [
                ],
            },
        }

        units_to_return = []

        addons = ["base"]
        if include_chronicles:
            addons.append("chronicles")

        for addon in addons:
            if not exclude_non_elite_units:
                if not exclude_non_castle_units:
                    units_to_return.extend(unique_units[addon]["non_elite"])
                if not exclude_castle_units:
                    units_to_return.extend(unique_units[addon]["castle"]["non_elite"])
            if not exclude_elite_units:
                if not exclude_non_castle_units:
                    units_to_return.extend(unique_units[addon]["elite"])
                if not exclude_castle_units:
                    units_to_return.extend(unique_units[addon]["castle"]["elite"])

        return units_to_return

    BEAR = 486, 151, 489, 16712, True
    BUTTERFLY1 = 1608, -1, -1, 16716, True
    BUTTERFLY2 = 1609, -1, -1, 16716, True
    BUTTERFLY3 = 1610, -1, -1, 16716, True
    CROCODILE = 1031, 193, 1032, 16060, True
    DEER = 65, 3, 43, 16071, True
    DIRE_WOLF = 89, 7, 237, 16553, True
    ELEPHANT = 1301, 179, 1332, 16722, True
    FALCON = 1056, 5, -1, 16058, True
    HAWK = 96, 283, -1, 16073, True
    IBEX = 1239, 267, 1240, 16071, True
    IRON_BOAR = 810, 98, 356, 16710, True
    JAGUAR = 812, 111, 813, 16712, True
    JAVELINA = 822, 98, 356, 16722, True
    KOMODO_DRAGON = 1135, 226, 1136, 16163, True
    LION = 1029, 194, 1030, 16059, True
    MACAW = 816, 284, -1, 16716, True
    OSTRICH = 1026, 196, 1027, 16071, True
    RABID_WOLF = 202, 7, 237, 16652, True
    RHINOCEROS = 1139, 225, 1140, 16172, True
    SEAGULLS = 303, -1, -1, 16716, True
    SNOW_LEOPARD = 1241, 268, 1242, 16060, True
    STORK = 1028, 285, -1, 16058, True
    STORMY_DOG = 862, 159, -1, 16764, True
    TIGER = 1137, 227, 1138, 16170, True
    VULTURE = 1305, 286, -1, 16716, True
    WILD_BACTRIAN_CAMEL = 1247, 266, 1238, 16735, True
    WILD_BOAR = 48, 98, 356, 16406, True
    WILD_CAMEL = 884, 135, 898, 16735, True
    WILD_HORSE = 835, 112, 815, 16735, True
    WOLF = 126, 7, 237, 16075, True
    ZEBRA = 1019, 192, 1020, 16071, True
    MOVEABLE_MAP_REVEALER = 0, -1, -1, 16000, False
    ALFRED_THE_ALPACA = 1300, 177, 1331, 16469, False
    AMAZON_ARCHER = 850, 165, 1325, 16683, False
    AMAZON_WARRIOR = 825, 166, 1324, 16667, False
    ARAMBAI = 1126, 230, 1127, 16101, False
    ARBALESTER = 492, 90, 496, 16418, False
    ARCHER = 4, 17, 3, 16083, False
    BACTRIAN_CAMEL = 1237, 266, 1238, 16714, False
    BALLISTA_ELEPHANT = 1120, 231, 1121, 16101, False
    BANDIT = 299, 8, 152, 16098, False
    BATTERING_RAM = 1258, 74, 23, 16094, False
    BATTLE_ELEPHANT = 1132, 228, 1133, 16733, False
    BERSERK = 692, 38, 693, 16574, False
    BOMBARD_CANNON = 36, 30, 16, 16093, False
    BOYAR = 876, 114, 877, 16101, False
    CAMEL = 897, 135, 898, 16714, False
    CAMEL_ARCHER = 1007, 191, 1008, 16101, False
    CAMEL_RIDER = 329, 78, 113, 16416, False
    CANNON_GALLEON = 420, 55, -1, 16287, False
    CANOE = 778, 164, -1, 16106, False
    CAPPED_RAM = 422, 63, 423, 16289, False
    CARAVEL = 1004, 198, -1, 16106, False
    CART = 1338, 34, 205, 16100, False
    CATAPHRACT = 40, 35, 27, 16101, False
    CAVALIER = 283, 49, 139, 16070, False
    CAVALRY_ARCHER = 39, 19, 34, 16085, False
    IMPERIAL_CENTURION = 275, 138, 277, 16451, False
    CHAMPION = 567, 72, 568, 16469, False
    CHU_KO_NU = 73, 36, 28, 16102, False
    COBRA_CAR = 748, 142, -1, 16658, False
    CONDOTTIERO = 882, 134, 883, 16679, False
    CONQUISTADOR = 771, 106, 772, 16687, False
    COW_A = 705, 150, 843, 16498, False
    COW_B = 1596, 150, 1597, 16498, False
    COW_C = 1598, 150, 1599, 16498, False
    COW_D = 1600, 150, 1601, 16498, False
    CROSSBOWMAN = 24, 18, 26, 16084, False
    DEMOLITION_RAFT = 1104, 202, -1, 16424, False
    DEMOLITION_SHIP = 527, 84, -1, 16424, False
    DONKEY = 846, 158, 848, 16100, False
    DRAGON_SHIP = 1302, 178, -1, 16739, False
    EAGLE_SCOUT = 751, 109, 754, 16671, False
    EAGLE_WARRIOR = 753, 148, 1116, 16671, False
    EASTERN_SWORDSMAN = 894, 186, 895, 16081, False
    ELEPHANT_ARCHER = 873, 93, 874, 16101, False
    ELITE_ARAMBAI = 1128, 230, 1127, 16101, False
    ELITE_BALLISTA_ELEPHANT = 1122, 231, 1121, 16101, False
    ELITE_BATTLE_ELEPHANT = 1134, 246, 1154, 16733, False
    ELITE_BERSERK = 694, 38, 695, 16576, False
    ELITE_BOYAR = 878, 114, 877, 16101, False
    ELITE_CAMEL_ARCHER = 1009, 191, 1008, 16101, False
    ELITE_CANNON_GALLEON = 691, 298, -1, 16573, False
    ELITE_CARAVEL = 1006, 198, -1, 16106, False
    ELITE_CATAPHRACT = 553, 35, 27, 16451, False
    ELITE_CHU_KO_NU = 559, 36, 28, 16452, False
    ELITE_CONQUISTADOR = 773, 106, 772, 16689, False
    ELITE_EAGLE_WARRIOR = 752, 149, 1117, 16673, False
    ELITE_ELEPHANT_ARCHER = 875, 93, 874, 16101, False
    ELITE_GBETO = 1015, 197, 1014, 16101, False
    ELITE_GENITOUR = 1012, 201, 1011, 16417, False
    ELITE_GENOESE_CROSSBOWMAN = 868, 133, 867, 16101, False
    ELITE_HUSKARL = 555, 50, 62, 16454, False
    ELITE_JAGUAR_WARRIOR = 726, 110, 750, 16669, False
    ELITE_JANISSARY = 557, 39, 107, 16455, False
    ELITE_KAMAYUK = 881, 97, 880, 16460, False
    ELITE_KARAMBIT_WARRIOR = 1125, 233, 1124, 16101, False
    ELITE_KESHIK = 1230, 251, 1229, 16101, False
    ELITE_KIPCHAK = 1233, 252, 1232, 16108, False
    ELITE_KONNIK = 1227, 249, 1253, 16101, False
    ELITE_KONNIK_DISMOUNTED = 1253, 250, 1257, 16411, False
    ELITE_LEITIS = 1236, 253, 1235, 16101, False
    ELITE_LONGBOAT = 533, 40, -1, 16457, False
    ELITE_LONGBOWMAN = 530, 41, 115, 16456, False
    ELITE_MAGYAR_HUSZAR = 871, 99, 870, 16101, False
    ELITE_MAMELUKE = 556, 37, 44, 16453, False
    ELITE_MANGUDAI = 561, 42, 135, 16458, False
    ELITE_ORGAN_GUN = 1003, 190, 1002, 16101, False
    ELITE_PLUMED_ARCHER = 765, 108, 764, 16685, False
    ELITE_RATTAN_ARCHER = 1131, 232, 1130, 16101, False
    ELITE_SAMURAI = 560, 44, 151, 16460, False
    ELITE_SHOTEL_WARRIOR = 1018, 195, 1017, 16101, False
    ELITE_SKIRMISHER = 6, 21, 100, 16087, False
    ELITE_STEPPE_LANCER = 1372, 274, 1373, 16746, False
    ELITE_TARKAN = 757, 105, 756, 16677, False
    ELITE_TEUTONIC_KNIGHT = 554, 45, 181, 16462, False
    ELITE_THROWING_AXEMAN = 531, 46, 157, 16461, False
    ELITE_TURTLE_SHIP = 832, 116, -1, 16106, False
    ELITE_WAR_ELEPHANT = 558, 43, 136, 16459, False
    ELITE_WAR_WAGON = 829, 117, 828, 16729, False
    ELITE_WOAD_RAIDER = 534, 47, 233, 16463, False
    FAST_FIRE_SHIP = 532, 85, -1, 16429, False
    FIRE_GALLEY = 1103, 203, -1, 16426, False
    FIRE_SHIP = 529, 86, -1, 16426, False
    FISHING_SHIP = 13, 24, -1, 16090, False
    FLAMETHROWER = 188, 144, 189, 16109, False
    FLAMING_CAMEL = 1263, 270, -1, 16734, False
    FURIOUS_THE_MONKEY_BOY = 860, 132, 861, 16763, False
    GALLEON = 442, 60, -1, 16309, False
    GALLEY = 539, 87, -1, 16436, False
    GBETO = 1013, 197, 1014, 16101, False
    GENITOUR = 1010, 201, 1011, 16417, False
    GENOESE_CROSSBOWMAN = 866, 133, 867, 16101, False
    GOAT = 1060, 200, 1061, 16061, False
    GOOSE = 1243, 265, 1244, 16061, False
    HALBERDIER = 359, 104, 502, 16409, False
    HAND_CANNONEER = 5, 22, 98, 16086, False
    HEAVY_CAMEL_RIDER = 330, 79, 495, 16417, False
    HEAVY_CAVALRY_ARCHER = 474, 71, 631, 16412, False
    HEAVY_CROSSBOWMAN = 493, 133, 867, 16101, False
    HEAVY_DEMOLITION_SHIP = 528, 83, -1, 16425, False
    HEAVY_PIKEMAN = 892, 136, 893, 16410, False
    HEAVY_SCORPION = 542, 89, 543, 16439, False
    HEAVY_SWORDSMAN = 76, 184, 99, 16077, False
    HORSE_A = 814, 112, 815, 16714, False
    HORSE_B = 1356, 112, 1357, 16714, False
    HORSE_C = 1602, 112, 1603, 16714, False
    HORSE_D = 1604, 112, 1605, 16714, False
    HORSE_E = 1606, 112, 1607, 16714, False
    HUSKARL = 41, 50, 62, 16104, False
    HUSSAR = 441, 103, 480, 16661, False
    IMPERIAL_CAMEL_RIDER = 207, 185, 300, 16417, False
    IMPERIAL_SKIRMISHER = 1155, 229, 1156, 16087, False
    INVISIBLE_OBJECT = 1291, -1, -1, 16000, False
    IROQUOIS_WARRIOR = 1374, 297, 1375, 16113, False
    JAGUAR_WARRIOR = 725, 110, 750, 16667, False
    JANISSARY = 46, 39, 107, 16105, False
    JUNK = 15, 211, -1, 16092, False
    KAMAYUK = 879, 97, 880, 16110, False
    KARAMBIT_WARRIOR = 1123, 233, 1124, 16101, False
    KESHIK = 1228, 251, 1229, 16101, False
    KHAN = 1275, 258, 1277, 16458, False
    KING = 434, 48, 435, 16301, False
    KIPCHAK = 1231, 252, 1232, 16108, False
    KNIGHT = 38, 1, 111, 16068, False
    KONNIK = 1225, 249, 1252, 16101, False
    KONNIK_DISMOUNTED = 1252, 250, 1257, 16411, False
    IMPERIAL_LEGIONARY = 1, 139, 2, 16669, False
    LEITIS = 1234, 253, 1235, 16101, False
    LIGHT_CAVALRY = 546, 91, 547, 16444, False
    LLAMA = 305, 156, 780, 16498, False
    LONG_SWORDSMAN = 77, 13, 180, 16081, False
    LONGBOAT = 250, 40, -1, 16106, False
    LONGBOWMAN = 8, 41, 115, 16107, False
    MAGYAR_HUSZAR = 869, 99, 870, 16101, False
    MAMELUKE = 282, 37, 44, 16103, False
    MAN_AT_ARMS = 75, 10, 154, 16080, False
    MANGONEL = 280, 27, 121, 16095, False
    MANGUDAI = 11, 42, 135, 16108, False
    MERCHANT = 1572, 346, 1573, 16301, False
    MILITIA = 74, 8, 152, 16079, False
    MISSIONARY = 775, 107, 776, 16691, False
    MONK = 125, 33, 134, 16099, False
    MONK_WITH_RELIC = 286, 33, 134, 16380, False
    NINJA = 1145, 299, 1147, 16110, False
    NORSE_WARRIOR = 361, 140, 362, 16081, False
    ONAGER = 550, 101, 675, 16448, False
    ORGAN_GUN = 1001, 190, 1002, 16101, False
    OX_CART = 1271, 263, 1272, 16100, False
    OX_WAGON = 1273, 264, 1274, 16100, False
    PALADIN = 569, 2, 570, 16471, False
    PENGUIN = 639, 157, 641, 16469, False
    PETARD = 440, 113, -1, 16660, False
    PHOTONMAN = 1577, 300, 1578, 16043, False
    PIG = 1245, 269, 1246, 16061, False
    PIKEMAN = 358, 11, 501, 16408, False
    PLUMED_ARCHER = 763, 108, 764, 16683, False
    PRIEST = 1023, 294, 1024, 16120, False
    PRIEST_WITH_RELIC = 1400, 33, 1024, 16380, False
    QUEEN = 1292, 168, 1328, 16302, False
    RATTAN_ARCHER = 1129, 232, 1130, 16101, False
    RELIC_CART = 1304, 295, 285, 16082, False
    ROYAL_JANISSARY = 52, 296, 1576, 16455, False
    SAMURAI = 291, 44, 151, 16110, False
    SCORPION = 279, 80, 149, 16096, False
    SCOUT_CAVALRY = 448, 64, 449, 16326, False
    SHARKATZOR = 1222, 352, -1, 16458, False
    SHEEP = 594, 96, 595, 16498, False
    SHOTEL_WARRIOR = 1016, 195, 1017, 16101, False
    SIEGE_ONAGER = 588, 102, 589, 16493, False
    SIEGE_RAM = 548, 73, 549, 16446, False
    SIEGE_TOWER = 1105, 212, 1107, 16445, False
    SKIRMISHER = 7, 20, 238, 16088, False
    SLINGER = 185, 143, 186, 16743, False
    SPEARMAN = 93, 31, 140, 16078, False
    STEPPE_LANCER = 1370, 273, 1371, 16746, False
    TARKAN = 755, 105, 756, 16675, False
    TEUTONIC_KNIGHT = 25, 45, 181, 16112, False
    THROWING_AXEMAN = 281, 46, 157, 16111, False
    TORCH_A_CONVERTABLE = 854, -1, -1, 16753, False
    TORCH_B_CONVERTABLE = 1377, -1, -1, 16753, False
    TRADE_CART_EMPTY = 128, 34, 178, 16100, False
    TRADE_CART_FULL = 204, 34, 205, 16100, False
    TRADE_COG = 17, 23, -1, 16089, False
    TRANSPORT_SHIP = 545, 95, -1, 16443, False
    TREBUCHET = 42, 28, 194, 16097, False
    TREBUCHET_PACKED = 331, 29, 735, 16381, False
    TURKEY = 833, 115, 834, 16733, False
    TURTLE_SHIP = 831, 116, -1, 16106, False
    TWO_HANDED_SWORDSMAN = 473, 12, 500, 16411, False
    VILLAGER_MALE = 83, 15, 224, 16121, False
    VILLAGER_FEMALE = 293, 16, 211, 16121, False
    VILLAGER_MALE_BUILDER = 118, 330, 225, 16122, False
    VILLAGER_FEMALE_BUILDER = 212, 329, 213, 16122, False
    VILLAGER_MALE_FARMER = 259, 332, 226, 16123, False
    VILLAGER_FEMALE_FARMER = 214, 331, 215, 16123, False
    VILLAGER_MALE_FISHERMAN = 56, 332, 58, 16499, False
    VILLAGER_FEMALE_FISHERMAN = 57, 331, 60, 16499, False
    VILLAGER_MALE_FORAGER = 120, 332, 353, 16402, False
    VILLAGER_FEMALE_FORAGER = 354, 331, 355, 16402, False
    VILLAGER_MALE_GOLD_MINER = 579, 334, 229, 16482, False
    VILLAGER_FEMALE_GOLD_MINER = 581, 333, 221, 16482, False
    VILLAGER_MALE_HUNTER = 122, 332, 227, 16124, False
    VILLAGER_FEMALE_HUNTER = 216, 331, 217, 16124, False
    VILLAGER_MALE_LUMBERJACK = 123, 339, 228, 16125, False
    VILLAGER_FEMALE_LUMBERJACK = 218, 338, 219, 16125, False
    VILLAGER_MALE_REPAIRER = 156, 330, 225, 16127, False
    VILLAGER_FEMALE_REPAIRER = 222, 329, 213, 16127, False
    VILLAGER_MALE_SHEPHERD = 592, 332, 593, 16496, False
    VILLAGER_FEMALE_SHEPHERD = 590, 331, 591, 16496, False
    VILLAGER_MALE_STONE_MINER = 124, 336, 229, 16126, False
    VILLAGER_FEMALE_STONE_MINER = 220, 335, 221, 16126, False
    VILLAGER_MALE_OYSTER_GATHERER = 2333, 229, 334, 16482, False
    VILLAGER_FEMALE_OYSTER_GATHERER = 2334, 221, 333, 16482, False
    VMDL = 206, 337, -1, 16656, False
    WAR_ELEPHANT = 239, 43, 136, 16109, False
    WAR_GALLEY = 21, 25, -1, 16091, False
    WAR_WAGON = 827, 117, 828, 16727, False
    WATER_BUFFALO = 1142, 224, 1143, 16175, False
    WOAD_RAIDER = 232, 47, 233, 16113, False
    XOLOTL_WARRIOR = 1570, 351, 1571, 16326, False
    BOARDER_GALLEY = 536, 82, -1, 16703, False
    HUSKARL_BARRACKS = 759, 50, 62, 16748, False
    ELITE_HUSKARL_BARRACKS = 761, 50, 62, 16748, False
    TARKAN_STABLE = 886, 105, 756, 16741, False
    ELITE_TARKAN_STABLE = 887, 105, 756, 16741, False
    GENITOUR_ORIGINAL = 583, 19, 152, 16663, False
    ELITE_GENITOUR_ORIGINAL = 596, 19, 152, 16665, False
    COUSTILLIER = 1655, 355, 1656, 16101, False
    ELITE_COUSTILLIER = 1657, 355, 1656, 16101, False
    FLEMISH_MILITIA = 1699, 354, 1664, 16735, False
    FLEMISH_MILITIA_MALE = 1663, 354, 1664, 16469, False
    FLEMISH_MILITIA_FEMALE = 1697, 354, 1698, 16469, False
    SERJEANT = 1658, 356, 1662, 16104, False
    ELITE_SERJEANT = 1659, 356, 1662, 16454, False
    SERJEANT_DONJON = 1660, 356, 1662, 16101, False
    ELITE_SERJEANT_DONJON = 1661, 356, 1662, 16101, False
    CONDOTTIERO_PLACEHOLDER = 184, 134, 883, 16679, False
    KONNIK_KREPOST = 1254, 249, 1252, 16101, False
    ELITE_KONNIK_KREPOST = 1255, 249, 1253, 16101, False
    ELITE_KIPCHAK_CUMAN_MERCENARIES = 1260, 252, 1232, 16730, False
    FOOD_WOOD_GOLD_TRICKLE = 1654, -1, -1, 16737, False
    CUMAN_DISABLED = 1261, 114, 1232, 16108, False
    OUTLW = 158, 17, 3, 16074, True
    RFARC = 571, 17, 572, 16474, False
    MONUMENT_RESOURCE_ENABLER = 1639, 17, 572, 16464, False
    HUSSITE_WAGON = 1704, 370, 1705, 16101, False
    ELITE_HUSSITE_WAGON = 1706, 370, 1705, 16101, False
    OBUCH = 1701, 369, 1702, 16104, False
    ELITE_OBUCH = 1703, 369, 1702, 16104, False
    WINGED_HUSSAR = 1707, 371, 1708, 16661, False
    HOUFNICE = 1709, 372, 1710, 16093, False
    URUMI_SWORDSMAN = 1735, 386, 1736, 16104, False
    MONK_WITH_TURKISH_RELIC = 309, 33, 134, 16361, False
    CRUSADER_KNIGHT = 1723, 377, 1724, 16730, False
    ELITE_URUMI_SWORDSMAN = 1737, 386, 1736, 16454, False
    RATHA_MELEE = 1738, 388, 1739, 16101, False
    ELITE_RATHA_MELEE = 1740, 388, 1739, 16101, False
    CHAKRAM_THROWER = 1741, 390, 1742, 16111, False
    ELITE_CHAKRAM_THROWER = 1743, 390, 1742, 16461, False
    GHULAM = 1747, 385, 1748, 16101, False
    ELITE_GHULAM = 1749, 385, 1748, 16101, False
    THIRISADAI = 1750, 387, -1, 16106, False
    SHRIVAMSHA_RIDER = 1751, 391, 1752, 16737, False
    ELITE_SHRIVAMSHA_RIDER = 1753, 391, 1752, 16737, False
    CAMEL_SCOUT = 1755, 392, 1668, 16416, False
    RATHA_RANGED = 1759, 389, 1760, 16727, False
    ELITE_RATHA_RANGED = 1761, 389, 1760, 16729, False
    ARMORED_ELEPHANT = 1744, 394, 1745, 16494, False
    SIEGE_ELEPHANT = 1746, 395, 1757, 16494, False
    SOGDIAN_CATAPHRACT = 1299, 181, 1401, 1645, False
    SPEARMAN_DONJON = 1786, 31, 140, 16078, False
    PIKEMAN_DONJON = 1787, 11, 501, 16408, False
    HALBERDIER_DONJON = 1788, 104, 502, 16409, False
    CENTURION = 1790, 405, 1791, 16101, False
    ELITE_CENTURION = 1792, 405, 1791, 16101, False
    LEGIONARY = 1793, 139, 1794, 16469, False
    DROMON = 1795, 406, -1, 16738, False
    GAZELLE = 1796, 404, 1797, 16071, True
    COMPOSITE_BOWMAN = 1800, 407, 1801, 16107, False
    ELITE_COMPOSITE_BOWMAN = 1802, 407, 1801, 16456, False
    MONASPA = 1803, 408, 1804, 16101, False
    ELITE_MONASPA = 1805, 408, 1804, 16101, False
    VILLAGER_MALE_MONASTERY = 1810, 15, 224, 16691, False
    WARRIOR_PRIEST = 1811, 409, 1812, 16691, False
    WARRIOR_PRIEST_WITH_RELIC = 1831, 409, 1812, 16380, False
    SAVAR = 1813, 410, 1814, 16471, False
    QIZILBASH_WARRIOR = 1817, 412, 1818, 16101, False
    ELITE_QIZILBASH_WARRIOR = 1829, 412, 1818, 16101, False
    IMMORTAL_MELEE = 2101, 2103, 621, 16104, False
    ELITE_IMMORTAL_MELEE = 2102, 2103, 621, 16104, False
    STRATEGOS = 2104, 2106, 624, 16104, False
    ELITE_STRATEGOS = 2105, 2106, 624, 16104, False
    STRATEGOS_WITH_TAXIARCHS = 2227, 2106, 624, 16104, False
    ELITE_STRATEGOS_WITH_TAXIARCHS = 2228, 2106, 624, 16104, False
    HIPPEUS = 2107, 2109, 623, 16104, False
    ELITE_HIPPEUS = 2108, 2109, 623, 16104, False
    HIPPEUS_WITH_AURA = 2168, 2109, 623, -1, False
    ELITE_HIPPEUS_WITH_AURA = 2169, 2109, 623, -1, False
    HOPLITE = 2110, 2112, 625, 416013, False
    ELITE_HOPLITE = 2111, 2301, 626, 416013, False
    HOPLITE_WITH_XYPHOS = 2187, 2112, 625, 416013, False
    ELITE_HOPLITE_WITH_XYPHOS = 2188, 2301, 626, 416013, False
    LEMBOS = 2123, -1, 656, 416006, False
    WAR_LEMBOS = 2124, -1, 657, 416006, False
    HEAVY_LEMBOS = 2125, -1, 658, 416006, False
    ELITE_LEMBOS = 2126, -1, 659, 416006, False
    MONOREME = 2127, -1, 661, 416007, False
    BIREME = 2128, -1, 662, 416007, False
    TRIREME = 2129, -1, 663, 416007, False
    GALLEY_ANTIQUITY = 2130, -1, 664, 416008, False
    WAR_GALLEY_ANTIQUITY = 2131, -1, 666, 416008, False
    ELITE_GALLEY = 2132, -1, 665, 416008, False
    INCENDIARY_RAFT = 2133, -1, 667, 416009, False
    INCENDIARY_SHIP = 2134, -1, 668, 416009, False
    HEAVY_INCENDIARY_SHIP = 2135, -1, 669, 416009, False
    CATAPULT_SHIP = 2138, -1, 671, 416011, False
    ONAGER_SHIP = 2139, -1, 672, 416011, False
    LEVIATHAN = 2140, -1, 670, 416012, False
    TRANSPORT_SHIP_ANTIQUITY = 2148, -1, 655, 416005, False
    MERCHANT_SHIP = 2149, -1, 660, 416004, False
    WAR_CHARIOT = 2150, 2302, 627, 416015, False
    ELITE_WAR_CHARIOT = 2151, 2303, 628, 416015, False
    IMMORTAL_RANGED = 2174, 2304, 630, 16101, False
    ELITE_IMMORTAL_RANGED = 2175, 2304, 630, 16101, False
    RHODIAN_SLINGER = 2320, 2367, 693, 16743, False
    MERCENARY_HOPLITE = 2321, 2361, 691, 416013, False
    GREEK_NOBLE_CAVALRY = 2322, 2369, 684, 416016, False
    SCYTHIAN_AXE_CAVALRY = 2323, 2374, 687, 416016, False
    BACTRIAN_ARCHER = 2324, 2366, 686, 416016, False
    EKDROMOS = 2325, 2357, 685, 416016, False
    CRETAN_ARCHER = 2326, 2365, 683, 416016, False
    CAMEL_RAIDER = 2327, 2368, 681, 16416, False
    TARANTINE_CAVALRY = 2328, 2375, 689, 16417, False
    SPARABARA = 2329, 2372, 692, 16101, False
    SAKAN_AXEMAN = 2330, 2358, 688, 416016, False
    SICKLE_WARRIOR = 2331, 2362, 690, 16101, False
    MERCENARY_PELTAST = 2332, 2377, 694, 16087, False
    LYSANDERS_RAIDER = 2349, 2361, 691, 416016, False
    HINT_OBJECT = 2238, -1, -1, 16000, False
    MOUFLON = 2340, 2341, 267, 16071, True
    GOAT_UNCONVERTIBLE = 2381, 1061, 200, 16061, False
