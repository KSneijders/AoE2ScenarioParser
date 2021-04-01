from enum import Enum


class UnitInfo(Enum):
    @property
    def ID(self):
        return self.value[0]

    @classmethod
    def from_id(cls, value):
        if value == -1:
            raise ValueError("-1 is not a valid id value")
        for x in cls._member_map_.values():
            if x.value[0] == value:
                return x
        raise ValueError(f"{value} is not a valid id value")

    @property
    def ICON_ID(self):
        return self.value[1]

    @classmethod
    def from_icon_id(cls, value):
        if value == -1:
            raise ValueError("-1 is not a valid icon_id value")
        for x in cls._member_map_.values():
            if x.value[1] == value:
                return x
        raise ValueError(f"{value} is not a valid icon_id value")

    @property
    def DEAD_ID(self):
        return self.value[2]

    @classmethod
    def from_dead_id(cls, value):
        if value == -1:
            raise ValueError("-1 is not a valid dead_id value")
        for x in cls._member_map_.values():
            if x.value[2] == value:
                return x
        raise ValueError(f"{value} is not a valid dead_id value")

    @property
    def IS_GAIA_ONLY(self):
        return self.value[3]

    @staticmethod
    def gaia_only():
        result = []
        for x in UnitInfo:
            if x.IS_GAIA:
                result.append(x)
        return result

    @staticmethod
    def non_gaia():
        result = []
        for x in UnitInfo:
            if not x.IS_GAIA:
                result.append(x)
        return result

    BEAR = 486, 151, 489, True
    BUTTERFLY1 = 1608, -1, -1, True
    BUTTERFLY2 = 1609, -1, -1, True
    BUTTERFLY3 = 1610, -1, -1, True
    CROCODILE = 1031, 193, 1032, True
    DEER = 65, 3, 43, True
    DIRE_WOLF = 89, 7, 237, True
    ELEPHANT = 1301, 179, 1332, True
    FALCON = 1056, 5, -1, True
    HAWK = 96, 283, -1, True
    IBEX = 1239, 267, 1240, True
    IRON_BOAR = 810, 98, 356, True
    JAGUAR = 812, 111, 813, True
    JAVELINA = 822, 98, 356, True
    KOMODO_DRAGON = 1135, 226, 1136, True
    LION = 1029, 194, 1030, True
    MACAW = 816, 284, -1, True
    OSTRICH = 1026, 196, 1027, True
    RABID_WOLF = 202, 7, 237, True
    RHINOCEROS = 1139, 225, 1140, True
    SEAGULLS = 303, -1, -1, True
    SNOW_LEOPARD = 1241, 268, 1242, True
    STORK = 1028, 285, -1, True
    STORMY_DOG = 862, 159, -1, True
    TIGER = 1137, 227, 1138, True
    VULTURE = 1305, 286, -1, True
    WILD_BACTRIAN_CAMEL = 1247, 266, 1238, True
    WILD_BOAR = 48, 98, 356, True
    WILD_CAMEL = 884, 135, 898, True
    WILD_HORSE = 835, 112, 815, True
    WOLF = 126, 7, 237, True
    ZEBRA = 1019, 192, 1020, True
    MOVEABLE_MAP_REVEALER = 0, -1, -1, False
    ALFRED_THE_ALPACA = 1300, 177, 1331, False
    AMAZON_ARCHER = 850, 165, 1325, False
    AMAZON_WARRIOR = 825, 166, 1324, False
    ARAMBAI = 1126, 230, 1127, False
    ARBALESTER = 492, 90, 496, False
    ARCHER = 4, 17, 3, False
    BACTRIAN_CAMEL = 1237, 266, 1238, False
    BALLISTA_ELEPHANT = 1120, 231, 1121, False
    BANDIT = 299, 8, 152, False
    BATTERING_RAM = 1258, 74, 23, False
    BATTLE_ELEPHANT = 1132, 228, 1133, False
    BERSERK = 692, 38, 693, False
    BOMBARD_CANNON = 36, 30, 16, False
    BOYAR = 876, 114, 877, False
    CAMEL = 897, 135, 898, False
    CAMEL_ARCHER = 1007, 191, 1008, False
    CAMEL_RIDER = 329, 78, 113, False
    CANNON_GALLEON = 420, 55, -1, False
    CANOE = 778, 164, -1, False
    CAPPED_RAM = 422, 63, 423, False
    CARAVEL = 1004, 198, -1, False
    CART = 1338, 34, 205, False
    CATAPHRACT = 40, 35, 27, False
    CAVALIER = 283, 49, 139, False
    CAVALRY_ARCHER = 39, 19, 34, False
    CENTURION = 275, 138, 277, False
    CHAMPION = 567, 72, 568, False
    CHU_KO_NU = 73, 36, 28, False
    COBRA_CAR = 748, 142, -1, False
    CONDOTTIERO = 882, 134, 883, False
    CONQUISTADOR = 771, 106, 772, False
    COW_A = 705, 150, 843, False
    COW_B = 1596, 150, 1597, False
    COW_C = 1598, 150, 1599, False
    COW_D = 1600, 150, 1601, False
    CROSSBOWMAN = 24, 18, 26, False
    DEMOLITION_RAFT = 1104, 202, -1, False
    DEMOLITION_SHIP = 527, 84, -1, False
    DONKEY = 846, 158, 848, False
    DRAGON_SHIP = 1302, 178, -1, False
    EAGLE_SCOUT = 751, 109, 754, False
    EAGLE_WARRIOR = 753, 148, 1116, False
    EASTERN_SWORDSMAN = 894, 186, 895, False
    ELEPHANT_ARCHER = 873, 93, 874, False
    ELITE_ARAMBAI = 1128, 230, 1127, False
    ELITE_BALLISTA_ELEPHANT = 1122, 231, 1121, False
    ELITE_BATTLE_ELEPHANT = 1134, 246, 1154, False
    ELITE_BERSERK = 694, 38, 695, False
    ELITE_BOYAR = 878, 114, 877, False
    ELITE_CAMEL_ARCHER = 1009, 191, 1008, False
    ELITE_CANNON_GALLEON = 691, 298, -1, False
    ELITE_CARAVEL = 1006, 198, -1, False
    ELITE_CATAPHRACT = 553, 35, 27, False
    ELITE_CHU_KO_NU = 559, 36, 28, False
    ELITE_CONQUISTADOR = 773, 106, 772, False
    ELITE_EAGLE_WARRIOR = 752, 149, 1117, False
    ELITE_ELEPHANT_ARCHER = 875, 93, 874, False
    ELITE_GBETO = 1015, 197, 1014, False
    ELITE_GENITOUR = 1012, 201, 1011, False
    ELITE_GENOESE_CROSSBOWMAN = 868, 133, 867, False
    ELITE_HUSKARL = 555, 50, 62, False
    ELITE_JAGUAR_WARRIOR = 726, 110, 750, False
    ELITE_JANISSARY = 557, 39, 107, False
    ELITE_KAMAYUK = 881, 97, 880, False
    ELITE_KARAMBIT_WARRIOR = 1125, 233, 1124, False
    ELITE_KESHIK = 1230, 251, 1229, False
    ELITE_KIPCHAK = 1233, 252, 1232, False
    ELITE_KONNIK = 1227, 249, 1253, False
    ELITE_KONNIK_DISMOUNTED = 1253, 250, 1257, False
    ELITE_LEITIS = 1236, 253, 1235, False
    ELITE_LONGBOAT = 533, 40, -1, False
    ELITE_LONGBOWMAN = 530, 41, 115, False
    ELITE_MAGYAR_HUSZAR = 871, 99, 870, False
    ELITE_MAMELUKE = 556, 37, 44, False
    ELITE_MANGUDAI = 561, 42, 135, False
    ELITE_ORGAN_GUN = 1003, 190, 1002, False
    ELITE_PLUMED_ARCHER = 765, 108, 764, False
    ELITE_RATTAN_ARCHER = 1131, 232, 1130, False
    ELITE_SAMURAI = 560, 44, 151, False
    ELITE_SHOTEL_WARRIOR = 1018, 195, 1017, False
    ELITE_SKIRMISHER = 6, 21, 100, False
    ELITE_STEPPE_LANCER = 1372, 274, 1373, False
    ELITE_TARKAN = 757, 105, 756, False
    ELITE_TEUTONIC_KNIGHT = 554, 45, 181, False
    ELITE_THROWING_AXEMAN = 531, 46, 157, False
    ELITE_TURTLE_SHIP = 832, 116, -1, False
    ELITE_WAR_ELEPHANT = 558, 43, 136, False
    ELITE_WAR_WAGON = 829, 117, 828, False
    ELITE_WOAD_RAIDER = 534, 47, 233, False
    FAST_FIRE_SHIP = 532, 85, -1, False
    FIRE_GALLEY = 1103, 203, -1, False
    FIRE_SHIP = 529, 86, -1, False
    FISHING_SHIP = 13, 24, -1, False
    FLAMETHROWER = 188, 144, 189, False
    FLAMING_CAMEL = 1263, 270, -1, False
    FURIOUS_THE_MONKEY_BOY = 860, 132, 861, False
    GALLEON = 442, 60, -1, False
    GALLEY = 539, 87, -1, False
    GBETO = 1013, 197, 1014, False
    GENITOUR = 1010, 201, 1011, False
    GENOESE_CROSSBOWMAN = 866, 133, 867, False
    GOAT = 1060, 200, 1061, False
    GOOSE = 1243, 265, 1244, False
    HALBERDIER = 359, 104, 502, False
    HAND_CANNONEER = 5, 22, 98, False
    HEAVY_CAMEL_RIDER = 330, 79, 495, False
    HEAVY_CAVALRY_ARCHER = 474, 71, 631, False
    HEAVY_CROSSBOWMAN = 493, 133, 867, False
    HEAVY_DEMOLITION_SHIP = 528, 83, -1, False
    HEAVY_PIKEMAN = 892, 136, 893, False
    HEAVY_SCORPION = 542, 89, 543, False
    HEAVY_SWORDSMAN = 76, 184, 99, False
    HORSE_A = 814, 112, 815, False
    HORSE_B = 1356, 112, 1357, False
    HORSE_C = 1602, 112, 1603, False
    HORSE_D = 1604, 112, 1605, False
    HORSE_E = 1606, 112, 1607, False
    HUSKARL = 41, 50, 62, False
    HUSSAR = 441, 103, 480, False
    IMPERIAL_CAMEL_RIDER = 207, 185, 300, False
    IMPERIAL_SKIRMISHER = 1155, 229, 1156, False
    INVISIBLE_OBJECT = 1291, -1, -1, False
    IROQUOIS_WARRIOR = 1374, 297, 1375, False
    JAGUAR_WARRIOR = 725, 110, 750, False
    JANISSARY = 46, 39, 107, False
    JUNK = 15, 211, -1, False
    KAMAYUK = 879, 97, 880, False
    KARAMBIT_WARRIOR = 1123, 233, 1124, False
    KESHIK = 1228, 251, 1229, False
    KHAN = 1275, 258, 1277, False
    KING = 434, 48, 435, False
    KIPCHAK = 1231, 252, 1232, False
    KNIGHT = 38, 1, 111, False
    KONNIK = 1225, 249, 1252, False
    KONNIK_DISMOUNTED = 1252, 250, 1257, False
    LEGIONARY = 1, 139, 2, False
    LEITIS = 1234, 253, 1235, False
    LIGHT_CAVALRY = 546, 91, 547, False
    LLAMA = 305, 156, 780, False
    LONG_SWORDSMAN = 77, 13, 180, False
    LONGBOAT = 250, 40, -1, False
    LONGBOWMAN = 8, 41, 115, False
    MAGYAR_HUSZAR = 869, 99, 870, False
    MAMELUKE = 282, 37, 44, False
    MAN_AT_ARMS = 75, 10, 154, False
    MANGONEL = 280, 27, 121, False
    MANGUDAI = 11, 42, 135, False
    MERCHANT = 1572, 346, 1573, False
    MILITIA = 74, 8, 152, False
    MISSIONARY = 775, 107, 776, False
    MONK = 125, 33, 134, False
    MONK_WITH_RELIC = 286, 33, 134, False
    NINJA = 1145, 299, 1147, False
    NORSE_WARRIOR = 361, 140, 362, False
    ONAGER = 550, 101, 675, False
    ORGAN_GUN = 1001, 190, 1002, False
    OX_CART = 1271, 263, 1272, False
    OX_WAGON = 1273, 264, 1274, False
    PALADIN = 569, 2, 570, False
    PENGUIN = 639, 157, 641, False
    PETARD = 440, 113, -1, False
    PHOTONMAN = 1577, 300, 1578, False
    PIG = 1245, 269, 1246, False
    PIKEMAN = 358, 11, 501, False
    PLUMED_ARCHER = 763, 108, 764, False
    PRIEST = 1023, 294, 1024, False
    PRIEST_WITH_RELIC = 1400, 33, 1024, False
    QUEEN = 1292, 168, 1328, False
    RATTAN_ARCHER = 1129, 232, 1130, False
    RELIC_CART = 1304, 295, 285, False
    ROYAL_JANISSARY = 52, 296, 1576, False
    SAMURAI = 291, 44, 151, False
    SCORPION = 279, 80, 149, False
    SCOUT_CAVALRY = 448, 64, 449, False
    SHARKATZOR = 1222, 352, -1, False
    SHEEP = 594, 96, 595, False
    SHOTEL_WARRIOR = 1016, 195, 1017, False
    SIEGE_ONAGER = 588, 102, 589, False
    SIEGE_RAM = 548, 73, 549, False
    SIEGE_TOWER = 1105, 212, 1107, False
    SKIRMISHER = 7, 20, 238, False
    SLINGER = 185, 143, 186, False
    SPEARMAN = 93, 31, 140, False
    STEPPE_LANCER = 1370, 273, 1371, False
    TARKAN = 755, 105, 756, False
    TEUTONIC_KNIGHT = 25, 45, 181, False
    THROWING_AXEMAN = 281, 46, 157, False
    TORCH_A_CONVERTABLE = 854, -1, -1, False
    TORCH_B_CONVERTABLE = 1377, -1, -1, False
    TRADE_CART_EMPTY = 128, 34, 178, False
    TRADE_CART_FULL = 204, 34, 205, False
    TRADE_COG = 17, 23, -1, False
    TRANSPORT_SHIP = 545, 95, -1, False
    TREBUCHET = 42, 28, 194, False
    TREBUCHET_PACKED = 331, 29, 735, False
    TURKEY = 833, 115, 834, False
    TURTLE_SHIP = 831, 116, -1, False
    TWO_HANDED_SWORDSMAN = 473, 12, 500, False
    VILLAGER_MALE = 83, 15, 224, False
    VILLAGER_FEMALE = 293, 16, 211, False
    VILLAGER_MALE_BUILDER = 118, 330, 225, False
    VILLAGER_FEMALE_BUILDER = 212, 329, 213, False
    VILLAGER_MALE_FARMER = 259, 332, 226, False
    VILLAGER_FEMALE_FARMER = 214, 331, 215, False
    VILLAGER_MALE_FISHERMAN = 56, 332, 58, False
    VILLAGER_FEMALE_FISHERMAN = 57, 331, 60, False
    VILLAGER_MALE_FORAGER = 120, 332, 353, False
    VILLAGER_FEMALE_FORAGER = 354, 331, 355, False
    VILLAGER_MALE_GOLD_MINER = 579, 334, 229, False
    VILLAGER_FEMALE_GOLD_MINER = 581, 333, 221, False
    VILLAGER_MALE_HUNTER = 122, 332, 227, False
    VILLAGER_FEMALE_HUNTER = 216, 331, 217, False
    VILLAGER_MALE_LUMBERJACK = 123, 339, 228, False
    VILLAGER_FEMALE_LUMBERJACK = 218, 338, 219, False
    VILLAGER_MALE_REPAIRER = 156, 330, 225, False
    VILLAGER_FEMALE_REPAIRER = 222, 329, 213, False
    VILLAGER_MALE_SHEPHERD = 592, 332, 593, False
    VILLAGER_FEMALE_SHEPHERD = 590, 331, 591, False
    VILLAGER_MALE_STONE_MINER = 124, 336, 229, False
    VILLAGER_FEMALE_STONE_MINER = 220, 335, 221, False
    VMDL = 206, 337, -1, False
    WAR_ELEPHANT = 239, 43, 136, False
    WAR_GALLEY = 21, 25, -1, False
    WAR_WAGON = 827, 117, 828, False
    WATER_BUFFALO = 1142, 224, 1143, False
    WOAD_RAIDER = 232, 47, 233, False
    XOLOTL_WARRIOR = 1570, 351, 1571, False
    SMALL_TEMP_MAP_REVEAL = 112, -1, -1, False
    LARGE_TEMP_MAP_REVEAL = 332, -1, -1, False
    BOARDER_GALLEY = 536, 82, -1, False
    HUSKARL_BARRACKS = 759, 50, 62, False
    ELITE_HUSKARL_BARRACKS = 761, 50, 62, False
    TARKAN_STABLE = 886, 105, 756, False
    ELITE_TARKAN_STABLE = 887, 105, 756, False
    GENITOUR_ORIGINAL = 583, 19, 152, False
    ELITE_GENITOUR_ORIGINAL = 596, 19, 152, False
    COUSTILLIER = 1655, 355, 1656, False
    ELITE_COUSTILLIER = 1657, 355, 1656, False
    FLEMISH_MILITIA = 1699, 354, 1664, False
    FLEMISH_MILITIA_MALE = 1663, 354, 1664, False
    FLEMISH_MILITIA_FEMALE = 1697, 354, 1698, False
    SERJEANT = 1658, 356, 1662, False
    ELITE_SERJEANT = 1659, 356, 1662, False
    SERJEANT_DONJON = 1660, 356, 1662, False
    ELITE_SERJEANT_DONJON = 1661, 356, 1662, False
    CONDOTTIERO_PLACEHOLDER = 184, 134, 883, False
    KONNIK_KREPOST = 1254, 249, 1252, False
    ELITE_KONNIK_KREPOST = 1255, 249, 1253, False
    ELITE_KIPCHAK_CUMAN_MERCENARIES = 1260, 252, 1232, False
    FOOD_WOOD_GOLD_TRICKLE = 1654, -1, -1, False
