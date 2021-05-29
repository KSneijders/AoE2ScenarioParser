from enum import Enum


class OtherInfo(Enum):
    @property
    def ID(self):
        return self.value[0]

    @classmethod
    def from_id(cls, value: int):
        if type(value) is not int:
            raise TypeError(f"from_id expected int, got {type(value)}")
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
    def from_icon_id(cls, value: int):
        if type(value) is not int:
            raise TypeError(f"from_icon_id expected int, got {type(value)}")
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
    def from_dead_id(cls, value: int):
        if type(value) is not int:
            raise TypeError(f"from_dead_id expected int, got {type(value)}")
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
        for x in OtherInfo:
            if x.IS_GAIA:
                result.append(x)
        return result

    @staticmethod
    def non_gaia():
        result = []
        for x in OtherInfo:
            if not x.IS_GAIA:
                result.append(x)
        return result

    SMALL_TEMP_MAP_REVEAL = 112, -1, -1, False
    LARGE_TEMP_MAP_REVEAL = 332, -1, -1, False
    FLARE = 274, -1, -1, False
    FLARE_PERMANENT = 1689, -1, -1, False
    FISH_PERCH = 53, 276, -1, True
    FORAGE_BUSH = 59, 6, -1, True
    GOLD_MINE = 66, 14, -1, True
    SHORE_FISH = 69, 280, -1, True
    STONE_MINE = 102, 9, -1, True
    CRACKS = 241, -1, -1, True
    TREE_TD = 284, 32, 415, True
    RELIC = 285, 26, -1, True
    BRITISH_RELIC = 287, 26, -1, True
    BYZANTINE_RELIC = 288, 26, -1, True
    CHINESE_RELIC = 289, 26, -1, True
    FRANKISH_RELIC = 290, 26, -1, True
    GOTHIC_RELIC = 292, 26, -1, True
    JAPANESE_RELIC = 294, 26, -1, True
    PERSIAN_RELIC = 295, 26, -1, True
    SARACEN_RELIC = 296, 26, -1, True
    TEUTONIC_RELIC = 297, 26, -1, True
    TURKISH_RELIC = 298, 26, -1, True
    GRASS_PATCH_GREEN = 301, -1, -1, True
    BUSH_A = 302, 32, 415, True
    BONFIRE = 304, -1, -1, False
    BLACK_TILE = 306, -1, -1, True
    MOUNTAIN_1 = 310, -1, -1, True
    MOUNTAIN_2 = 311, -1, -1, True
    FLOWERS_1 = 334, -1, -1, True
    FLOWERS_2 = 335, -1, -1, True
    FLOWERS_3 = 336, -1, -1, True
    FLOWERS_4 = 337, -1, -1, True
    PATH_4 = 338, -1, -1, True
    PATH_1 = 339, -1, -1, True
    PATH_2 = 340, -1, -1, True
    PATH_3 = 341, -1, -1, True
    TREE_BAMBOO_FOREST = 348, 32, 737, True
    TREE_OAK = 349, 32, 415, True
    TREE_PINE_FOREST = 350, 32, 415, True
    TREE_PALM_FOREST = 351, 32, 415, True
    SEA_ROCKS_1 = 389, -1, -1, True
    SEA_ROCKS_2 = 396, -1, -1, True
    TREE_A = 399, 32, 415, True
    TREE_B = 400, 32, 415, True
    TREE_C = 401, 32, 415, True
    TREE_D = 402, 32, 415, True
    TREE_E = 403, 32, 415, True
    TREE_F = 404, 32, 415, True
    TREE_G = 405, 32, 415, True
    TREE_H = 406, 32, 415, True
    TREE_I = 407, 32, 415, True
    TREE_J = 408, 32, 415, True
    TREE_K = 409, 32, 415, True
    TREE_L = 410, 32, 415, True
    TREE_OAK_FOREST = 411, 32, 415, True
    TREE_SNOW_PINE = 413, 32, 415, True
    TREE_JUNGLE = 414, 32, 415, True
    POENARI_CASTLE = 445, 7, 1488, True
    GREAT_FISH_MARLIN = 450, 281, -1, True
    FISH_DORADO = 455, 275, -1, True
    FISH_SALMON = 456, 277, -1, True
    FISH_TUNA = 457, 279, -1, True
    FISH_SNAPPER = 458, 278, -1, True
    TORCH_A = 499, -1, -1, False
    FLAG_A = 600, -1, -1, False
    FLAG_B = 601, -1, -1, False
    FLAG_C = 602, -1, -1, False
    FLAG_D = 603, -1, -1, False
    FLAG_E = 604, -1, -1, False
    ROCK_1 = 623, -1, -1, True
    PAVILION_A = 624, 43, 1476, True
    PAVILION_C = 625, 43, 1478, True
    PAVILION_B = 626, 43, 1477, True
    MOSQUE = 655, 12, 1496, True
    THE_ACCURSED_TOWER = 684, 45, 1494, True
    THE_TOWER_OF_FLIES = 685, 45, 1495, True
    PIECE_OF_THE_TRUE_CROSS = 688, -1, -1, True
    DOME_OF_THE_ROCK = 690, 37, 1482, True
    GREAT_PYRAMID = 696, 57, 1516, True
    CACTUS = 709, 32, -1, True
    SKELETON = 710, -1, -1, True
    RUGS = 711, -1, -1, True
    NINE_BANDS = 720, -1, -1, True
    SHIPWRECK_A = 721, -1, -1, True
    SHIPWRECK_B = 722, -1, -1, True
    CRATER = 723, -1, -1, True
    ICE_NAVIGABLE = 728, -1, -1, True
    MOUNTAIN_3 = 744, -1, -1, True
    MOUNTAIN_4 = 745, -1, -1, True
    BURNED_BUILDING = 758, -1, -1, True
    STUMP = 809, -1, -1, True
    PLANT = 818, -1, -1, True
    SIGN = 819, 189, -1, True
    GRAVE = 820, -1, -1, True
    HEAD = 821, -1, -1, True
    MAP_REVEALER = 837, -1, -1, True
    ES_FLAG = 851, -1, -1, True
    OLD_STONE_HEAD = 855, -1, -1, True
    ROMAN_RUINS = 856, -1, -1, True
    HAY_STACK = 857, -1, -1, True
    BROKEN_CART = 858, -1, -1, True
    FLOWER_BED = 859, -1, -1, True
    RUBBLE_1_X_1 = 863, -1, -1, False
    RUBBLE_2_X_2 = 864, -1, -1, False
    RUBBLE_3_X_3 = 865, -1, -1, False
    GRASS_PATCH_DRY = 1033, -1, -1, True
    MOUNTAIN_5 = 1041, -1, -1, True
    MOUNTAIN_6 = 1042, -1, -1, True
    MOUNTAIN_7 = 1043, -1, -1, True
    MOUNTAIN_8 = 1044, -1, -1, True
    SNOW_MOUNTAIN_1 = 1045, -1, -1, True
    SNOW_MOUNTAIN_2 = 1046, -1, -1, True
    SNOW_MOUNTAIN_3 = 1047, -1, -1, True
    ROCK_FORMATION_1 = 1048, -1, -1, True
    ROCK_FORMATION_2 = 1049, -1, -1, True
    ROCK_FORMATION_3 = 1050, -1, -1, True
    TREE_DRAGON = 1051, 32, 415, True
    TREE_BAOBAB = 1052, 32, 1634, True
    BUSH_B = 1053, 32, 415, True
    BUSH_C = 1054, 32, 415, True
    FRUIT_BUSH = 1059, 199, -1, True
    TREE_ACACIA = 1063, 32, 415, True
    GRANARY = 1089, 60, 1499, True
    BARRICADE_A = 1090, 54, 1472, True
    ANIMAL_SKELETON = 1091, -1, -1, True
    STELAE_A = 1092, -1, -1, True
    STELAE_B = 1093, -1, -1, True
    STELAE_C = 1094, -1, -1, True
    GALLOW = 1095, -1, -1, True
    BOX_TURTLES = 1141, 282, -1, True
    TREE_MANGROVE = 1144, 32, 415, True
    TREE_RAINFOREST = 1146, 32, 415, True
    ROCK_BEACH = 1148, -1, -1, True
    ROCK_JUNGLE = 1149, -1, -1, True
    FLAG_G = 1150, -1, -1, False
    FLAG_H = 1151, -1, -1, False
    FLAG_I = 1152, -1, -1, False
    FLAG_J = 1153, -1, -1, False
    BUDDHA_STATUE_A = 1171, -1, -1, True
    BUDDHA_STATUE_B = 1172, -1, -1, True
    BUDDHA_STATUE_C = 1173, -1, -1, True
    BUDDHA_STATUE_D = 1174, -1, -1, True
    FERN_PATCH = 1175, -1, -1, True
    TROWULAN_GATE = 1176, -1, -1, True
    VASES = 1177, -1, -1, True
    STUPA = 1191, -1, -1, True
    PAGODA_A = 1201, -1, -1, True
    PAGODA_B = 1202, -1, -1, True
    PAGODA_C = 1203, -1, -1, True
    BARRICADE_B = 1218, 54, 1473, True
    BARRICADE_C = 1219, 54, 1474, True
    BARRICADE_D = 1220, 54, 1475, True
    TREE_OAK_AUTUMN = 1248, 32, 415, True
    TREE_OAK_AUTUMN_SNOW = 1249, 32, 415, True
    TREE_DEAD = 1250, 32, 415, True
    DISMANTLED_CART = 1270, 271, -1, False
    STATUE_CIVILIZATION = 1279, -1, -1, False
    FLAG_K = 1282, -1, -1, False
    FLAG_L = 1283, -1, -1, False
    FLAG_M = 1284, -1, -1, False
    FE_FLAG = 1285, -1, -1, False
    FLAG_F = 1307, -1, -1, False
    SMOKE = 1308, -1, -1, False
    IMPALED_CORPSE = 1315, -1, -1, False
    STATUE_COLUMN = 1322, -1, -1, True
    ROCK_2 = 1323, -1, -1, True
    BARRELS = 1330, -1, -1, True
    STATUE_LEFT = 1343, -1, -1, True
    STATUE_RIGHT = 1345, -1, -1, True
    TREE_CYPRESS = 1347, 32, 415, True
    TREE_ITALIAN_PINE = 1348, 32, 415, True
    TREE_OLIVE = 1349, 32, 415, True
    TREE_REEDS = 1350, 32, 737, True
    PLANT_JUNGLE = 1351, -1, -1, True
    PLANT_UNDERBRUSH_TROPICAL = 1352, -1, -1, True
    PLANT_UNDERBRUSH = 1353, -1, -1, True
    PLANT_RAINFOREST = 1354, -1, -1, True
    GRASS_GREEN = 1358, -1, -1, True
    GRASS_DRY = 1359, -1, -1, True
    PLANT_BUSH_GREEN = 1360, -1, -1, True
    PLANT_SHRUB_GREEN = 1362, -1, -1, True
    PLANT_WEEDS = 1364, -1, -1, True
    PLANT_DEAD = 1365, -1, -1, True
    PLANT_FLOWERS = 1366, -1, -1, True
    TORCH_B = 1376, -1, -1, False
    RUBBLE_4_X_4 = 1497, -1, -1, False
    RUBBLE_8_X_8 = 1498, -1, -1, False
    PAIFANG_GATE = 1562, -1, -1, True
    NUBIAN_PYRAMID = 1563, -1, -1, True
    TARGET_A = 1564, -1, -1, False
    TARGET_B = 1565, -1, -1, False
    TEMPLE_RUIN = 1566, -1, -1, True
    WELL = 1567, -1, -1, True
