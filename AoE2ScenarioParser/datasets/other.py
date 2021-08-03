from AoE2ScenarioParser.datasets.support.info_dataset_base import InfoDatasetBase


class OtherInfo(InfoDatasetBase):
    """
    **Description**

    This enum class provides information about the 'Other' units in the game in the game. Information about the
    following properties of a building is found in this class:
     - Unit ID
     - Icon ID
     - Dead Unit ID
     - HotKey ID
     - If the unit is a gaia only unit (eg. deer, boar, etc.)

    **Inherited Methods from class InfoDatasetBase**

    >>> InfoDatasetBase.from_id()
    >>> InfoDatasetBase.from_dead_id()
    >>> InfoDatasetBase.from_icon_id()
    >>> InfoDatasetBase.from_hotkey_id()
    >>> InfoDatasetBase.gaia_only()
    >>> InfoDatasetBase.non_gaia()

    **Examples**

    >>> OtherInfo.FLARE.ID
    >>> 274

    >>> OtherInfo.FLARE.ICON_ID
    >>> -1

    >>> OtherInfo.FLARE.DEAD_ID
    >>> -1

    >>> OtherInfo.FLARE.HOTKEY_ID
    >>> 16316

    >>> OtherInfo.FLARE.IS_GAIA_ONLY
    >>> False
    """
    SMALL_TEMP_MAP_REVEAL = 112, -1, -1, 16316, False
    LARGE_TEMP_MAP_REVEAL = 332, -1, -1, 16316, False
    FLARE = 274, -1, -1, 16316, False
    FLARE_PERMANENT = 1689, -1, -1, 16316, False
    FISH_PERCH = 53, 276, -1, 16072, True
    FORAGE_BUSH = 59, 6, -1, 16401, True
    GOLD_MINE = 66, 14, -1, 16400, True
    SHORE_FISH = 69, 280, -1, 16501, True
    STONE_MINE = 102, 9, -1, 16252, True
    CRACKS = 241, -1, -1, 16259, True
    TREE_TD = 284, 32, 415, 16348, True
    RELIC = 285, 26, -1, 16350, True
    BRITISH_RELIC = 287, 26, -1, 16352, True
    BYZANTINE_RELIC = 288, 26, -1, 16353, True
    CHINESE_RELIC = 289, 26, -1, 16354, True
    FRANKISH_RELIC = 290, 26, -1, 16355, True
    GOTHIC_RELIC = 292, 26, -1, 16356, True
    JAPANESE_RELIC = 294, 26, -1, 16357, True
    PERSIAN_RELIC = 295, 26, -1, 16358, True
    SARACEN_RELIC = 296, 26, -1, 16359, True
    TEUTONIC_RELIC = 297, 26, -1, 16360, True
    TURKISH_RELIC = 298, 26, -1, 16351, True
    GRASS_PATCH_GREEN = 301, -1, -1, 16385, True
    BUSH_A = 302, 32, 415, 16398, True
    BONFIRE = 304, -1, -1, 16768, False
    BLACK_TILE = 306, -1, -1, 16389, True
    MOUNTAIN_1 = 310, -1, -1, 16342, True
    MOUNTAIN_2 = 311, -1, -1, 16343, True
    FLOWERS_1 = 334, -1, -1, 16382, True
    FLOWERS_2 = 335, -1, -1, 16383, True
    FLOWERS_3 = 336, -1, -1, 16384, True
    FLOWERS_4 = 337, -1, -1, 16385, True
    PATH_4 = 338, -1, -1, 16386, True
    PATH_1 = 339, -1, -1, 16387, True
    PATH_2 = 340, -1, -1, 16388, True
    PATH_3 = 341, -1, -1, 16389, True
    TREE_BAMBOO_FOREST = 348, 32, 737, 16396, True
    TREE_OAK = 349, 32, 415, 16397, True
    TREE_PINE_FOREST = 350, 32, 415, 16399, True
    TREE_PALM_FOREST = 351, 32, 415, 16398, True
    SEA_ROCKS_1 = 389, -1, -1, 16253, True
    SEA_ROCKS_2 = 396, -1, -1, 16262, True
    TREE_A = 399, 32, 415, 16265, True
    TREE_B = 400, 32, 415, 16266, True
    TREE_C = 401, 32, 415, 16267, True
    TREE_D = 402, 32, 415, 16268, True
    TREE_E = 403, 32, 415, 16269, True
    TREE_F = 404, 32, 415, 16270, True
    TREE_G = 405, 32, 415, 16271, True
    TREE_H = 406, 32, 415, 16272, True
    TREE_I = 407, 32, 415, 16273, True
    TREE_J = 408, 32, 415, 16274, True
    TREE_K = 409, 32, 415, 16275, True
    TREE_L = 410, 32, 415, 16276, True
    TREE_OAK_FOREST = 411, 32, 415, 16277, True
    TREE_SNOW_PINE = 413, 32, 415, 16694, True
    TREE_JUNGLE = 414, 32, 415, 16693, True
    POENARI_CASTLE = 445, 7, 1488, 16318, True
    GREAT_FISH_MARLIN = 450, 281, -1, 16330, True
    FISH_DORADO = 455, 275, -1, 16335, True
    FISH_SALMON = 456, 277, -1, 16336, True
    FISH_TUNA = 457, 279, -1, 16337, True
    FISH_SNAPPER = 458, 278, -1, 16338, True
    TORCH_A = 499, -1, -1, 16423, False
    FLAG_A = 600, -1, -1, 16506, False
    FLAG_B = 601, -1, -1, 16507, False
    FLAG_C = 602, -1, -1, 16508, False
    FLAG_D = 603, -1, -1, 16509, False
    FLAG_E = 604, -1, -1, 16510, False
    ROCK_1 = 623, -1, -1, 16520, True
    PAVILION_A = 624, 43, 1476, 16521, True
    PAVILION_C = 625, 43, 1478, 16523, True
    PAVILION_B = 626, 43, 1477, 16522, True
    MOSQUE = 655, 12, 1496, 16552, True
    THE_ACCURSED_TOWER = 684, 45, 1494, 16566, True
    THE_TOWER_OF_FLIES = 685, 45, 1495, 16567, True
    PIECE_OF_THE_TRUE_CROSS = 688, -1, -1, 16570, True
    DOME_OF_THE_ROCK = 690, 37, 1482, 16572, True
    GREAT_PYRAMID = 696, 57, 1516, 16578, True
    CACTUS = 709, 32, -1, 16591, True
    SKELETON = 710, -1, -1, 16592, True
    RUGS = 711, -1, -1, 16593, True
    NINE_BANDS = 720, -1, -1, 16602, True
    SHIPWRECK_A = 721, -1, -1, 16603, True
    SHIPWRECK_B = 722, -1, -1, 16604, True
    CRATER = 723, -1, -1, 16605, True
    ICE_NAVIGABLE = 728, -1, -1, 16610, True
    MOUNTAIN_3 = 744, -1, -1, 16647, True
    MOUNTAIN_4 = 745, -1, -1, 16648, True
    BURNED_BUILDING = 758, -1, -1, 16393, True
    STUMP = 809, -1, -1, 16281, True
    PLANT = 818, -1, -1, 16718, True
    SIGN = 819, 189, -1, 16719, True
    GRAVE = 820, -1, -1, 16720, True
    HEAD = 821, -1, -1, 16721, True
    MAP_REVEALER = 837, -1, -1, 16737, True
    ES_FLAG = 851, -1, -1, 16751, True
    OLD_STONE_HEAD = 855, -1, -1, 16756, True
    ROMAN_RUINS = 856, -1, -1, 16757, True
    HAY_STACK = 857, -1, -1, 16761, True
    BROKEN_CART = 858, -1, -1, 16759, True
    FLOWER_BED = 859, -1, -1, 16385, True
    RUBBLE_1_X_1 = 863, -1, -1, 16001, False
    RUBBLE_2_X_2 = 864, -1, -1, 16002, False
    RUBBLE_3_X_3 = 865, -1, -1, 16003, False
    GRASS_PATCH_DRY = 1033, -1, -1, 16385, True
    MOUNTAIN_5 = 1041, -1, -1, 16772, True
    MOUNTAIN_6 = 1042, -1, -1, 16773, True
    MOUNTAIN_7 = 1043, -1, -1, 16774, True
    MOUNTAIN_8 = 1044, -1, -1, 16775, True
    SNOW_MOUNTAIN_1 = 1045, -1, -1, 16776, True
    SNOW_MOUNTAIN_2 = 1046, -1, -1, 16777, True
    SNOW_MOUNTAIN_3 = 1047, -1, -1, 16778, True
    ROCK_FORMATION_1 = 1048, -1, -1, 16789, True
    ROCK_FORMATION_2 = 1049, -1, -1, 16790, True
    ROCK_FORMATION_3 = 1050, -1, -1, 16791, True
    TREE_DRAGON = 1051, 32, 415, 16792, True
    TREE_BAOBAB = 1052, 32, 1634, 16793, True
    BUSH_B = 1053, 32, 415, 16794, True
    BUSH_C = 1054, 32, 415, 16795, True
    FRUIT_BUSH = 1059, 199, -1, 16401, True
    TREE_ACACIA = 1063, 32, 415, 16798, True
    GRANARY = 1089, 60, 1499, 16222, True
    BARRICADE_A = 1090, 54, 1472, 16223, True
    ANIMAL_SKELETON = 1091, -1, -1, 16224, True
    STELAE_A = 1092, -1, -1, 16225, True
    STELAE_B = 1093, -1, -1, 16226, True
    STELAE_C = 1094, -1, -1, 16227, True
    GALLOW = 1095, -1, -1, 16228, True
    BOX_TURTLES = 1141, 282, -1, 16173, True
    TREE_MANGROVE = 1144, 32, 415, 16177, True
    TREE_RAINFOREST = 1146, 32, 415, 16179, True
    ROCK_BEACH = 1148, -1, -1, 16180, True
    ROCK_JUNGLE = 1149, -1, -1, 16181, True
    FLAG_G = 1150, -1, -1, 16183, False
    FLAG_H = 1151, -1, -1, 16184, False
    FLAG_I = 1152, -1, -1, 16188, False
    FLAG_J = 1153, -1, -1, 16189, False
    BUDDHA_STATUE_A = 1171, -1, -1, 16756, True
    BUDDHA_STATUE_B = 1172, -1, -1, 16756, True
    BUDDHA_STATUE_C = 1173, -1, -1, 16756, True
    BUDDHA_STATUE_D = 1174, -1, -1, 16756, True
    FERN_PATCH = 1175, -1, -1, 16385, True
    TROWULAN_GATE = 1176, -1, -1, 16756, True
    VASES = 1177, -1, -1, 16385, True
    STUPA = 1191, -1, -1, 16756, True
    PAGODA_A = 1201, -1, -1, 16756, True
    PAGODA_B = 1202, -1, -1, 16756, True
    PAGODA_C = 1203, -1, -1, 16756, True
    BARRICADE_B = 1218, 54, 1473, 16223, True
    BARRICADE_C = 1219, 54, 1474, 16223, True
    BARRICADE_D = 1220, 54, 1475, 16223, True
    TREE_OAK_AUTUMN = 1248, 32, 415, 16277, True
    TREE_OAK_AUTUMN_SNOW = 1249, 32, 415, 16694, True
    TREE_DEAD = 1250, 32, 415, 16694, True
    DISMANTLED_CART = 1270, 271, -1, 16189, False
    STATUE_CIVILIZATION = 1279, -1, -1, 16403, False
    FLAG_K = 1282, -1, -1, 16183, False
    FLAG_L = 1283, -1, -1, 16183, False
    FLAG_M = 1284, -1, -1, 16183, False
    FE_FLAG = 1285, -1, -1, 16183, False
    FLAG_F = 1307, -1, -1, 16517, False
    SMOKE = 1308, -1, -1, 16517, False
    IMPALED_CORPSE = 1315, -1, -1, 16000, False
    STATUE_COLUMN = 1322, -1, -1, 16717, True
    ROCK_2 = 1323, -1, -1, 16520, True
    BARRELS = 1330, -1, -1, 16757, True
    STATUE_LEFT = 1343, -1, -1, 16717, True
    STATUE_RIGHT = 1345, -1, -1, 16717, True
    TREE_CYPRESS = 1347, 32, 415, 16399, True
    TREE_ITALIAN_PINE = 1348, 32, 415, 16399, True
    TREE_OLIVE = 1349, 32, 415, 16399, True
    TREE_REEDS = 1350, 32, 737, 16396, True
    PLANT_JUNGLE = 1351, -1, -1, 16718, True
    PLANT_UNDERBRUSH_TROPICAL = 1352, -1, -1, 16718, True
    PLANT_UNDERBRUSH = 1353, -1, -1, 16718, True
    PLANT_RAINFOREST = 1354, -1, -1, 16718, True
    GRASS_GREEN = 1358, -1, -1, 16718, True
    GRASS_DRY = 1359, -1, -1, 16718, True
    PLANT_BUSH_GREEN = 1360, -1, -1, 16718, True
    PLANT_SHRUB_GREEN = 1362, -1, -1, 16718, True
    PLANT_WEEDS = 1364, -1, -1, 16718, True
    PLANT_DEAD = 1365, -1, -1, 16718, True
    PLANT_FLOWERS = 1366, -1, -1, 16718, True
    TORCH_B = 1376, -1, -1, 16423, False
    RUBBLE_4_X_4 = 1497, -1, -1, 16004, False
    RUBBLE_8_X_8 = 1498, -1, -1, 16006, False
    PAIFANG_GATE = 1562, -1, -1, 16756, True
    NUBIAN_PYRAMID = 1563, -1, -1, 16756, True
    TARGET_A = 1564, -1, -1, 16000, False
    TARGET_B = 1565, -1, -1, 16000, False
    TEMPLE_RUIN = 1566, -1, -1, 16757, True
    WELL = 1567, -1, -1, 16756, True
