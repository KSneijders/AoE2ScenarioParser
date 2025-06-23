from __future__ import annotations

from typing import List

from AoE2ScenarioParser.datasets.support.info_dataset_base import InfoDatasetBase


class OtherInfo(InfoDatasetBase):
    """
    This enum class provides information about the 'Other' units in the game in the game. Information about the
    following properties of a building is found in this class:

     - Unit ID
     - Icon ID
     - Dead Unit ID
     - HotKey ID
     - If the unit is a gaia only unit (e.g. deer, boar, etc.)

    **Methods**

    >>> OtherInfo.trees()

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

    @staticmethod
    def trees() -> List[OtherInfo]:
        """
        Returns:
            A list of all tree objects
        """
        return [
            OtherInfo.BLUE_TREE,
            OtherInfo.BUSH_A,
            OtherInfo.BUSH_B,
            OtherInfo.BUSH_C,
            OtherInfo.TREE_A,
            OtherInfo.TREE_ACACIA,
            OtherInfo.TREE_B,
            OtherInfo.TREE_BAMBOO_FOREST,
            OtherInfo.TREE_BAOBAB,
            OtherInfo.TREE_BIRCH,
            OtherInfo.TREE_C,
            OtherInfo.TREE_CYPRESS,
            OtherInfo.TREE_D,
            OtherInfo.TREE_DEAD,
            OtherInfo.TREE_DRAGON,
            OtherInfo.TREE_E,
            OtherInfo.TREE_F,
            OtherInfo.TREE_G,
            OtherInfo.TREE_H,
            OtherInfo.TREE_I,
            OtherInfo.TREE_ITALIAN_PINE,
            OtherInfo.TREE_J,
            OtherInfo.TREE_JUNGLE,
            OtherInfo.TREE_K,
            OtherInfo.TREE_L,
            OtherInfo.TREE_MANGROVE,
            OtherInfo.TREE_OAK,
            OtherInfo.TREE_OAK_AUTUMN,
            OtherInfo.TREE_OAK_AUTUMN_SNOW,
            OtherInfo.TREE_OAK_FOREST,
            OtherInfo.TREE_OLIVE,
            OtherInfo.TREE_PALM_FOREST,
            OtherInfo.TREE_PINE_FOREST,
            OtherInfo.TREE_RAINFOREST,
            OtherInfo.TREE_REEDS,
            OtherInfo.TREE_SNOW_PINE,
            OtherInfo.TREE_TD,
            OtherInfo.TREE_LUSH_BAMBOO_FOREST,
            OtherInfo.TREE_ASIAN_PINE,
            OtherInfo.TREE_PEACH_BLOSSOM,
            OtherInfo.TREE_WILLOW,
            OtherInfo.TREE_ASIAN_MAPLE_GREEN,
            OtherInfo.TREE_ASIAN_MAPLE_AUTUMN,
        ]

    ANIMAL_SKELETON = 1091, -1, -1, 16224, True
    BARRELS = 1330, -1, -1, 16757, True
    BLACK_TILE = 306, -1, -1, 16389, True
    BLUE_TREE = 768, 32, 415, 16277, True
    BONFIRE = 304, -1, -1, 16768, False
    BOX_TURTLES = 1141, 282, -1, 16173, True
    BRITISH_RELIC = 287, 26, -1, 16352, True
    BROKEN_CART = 858, -1, -1, 16759, True
    BUDDHA_STATUE_A = 1171, -1, -1, 16756, True
    BUDDHA_STATUE_B = 1172, -1, -1, 16756, True
    BUDDHA_STATUE_C = 1173, -1, -1, 16756, True
    BUDDHA_STATUE_D = 1174, -1, -1, 16756, True
    BURNED_BUILDING_A = 758, -1, -1, 16393, True
    BUSH_A = 302, 32, 415, 16398, True
    BUSH_B = 1053, 32, 415, 16794, True
    BUSH_C = 1054, 32, 415, 16795, True
    BYZANTINE_RELIC = 288, 26, -1, 16353, True
    CACTUS = 709, 32, -1, 16591, True
    CHINESE_RELIC = 289, 26, -1, 16354, True
    CRACKS = 241, -1, -1, 16259, True
    CRATER = 723, -1, -1, 16605, True
    DISMANTLED_CART = 1270, 271, -1, 16189, False
    ES_FLAG = 851, -1, -1, 16751, False
    FE_FLAG = 1285, -1, -1, 16183, False
    FERN_PATCH = 1175, -1, -1, 16385, True
    FISH_DORADO = 455, 275, -1, 16335, True
    FISH_PERCH = 53, 276, -1, 16072, True
    FISH_SALMON = 456, 277, -1, 16336, True
    FISH_SNAPPER = 458, 278, -1, 16338, True
    FISH_TUNA = 457, 279, -1, 16337, True
    FLAG_A = 600, -1, -1, 16506, False
    FLAG_B = 601, -1, -1, 16507, False
    FLAG_C = 602, -1, -1, 16508, False
    FLAG_D = 603, -1, -1, 16509, False
    FLAG_E = 604, -1, -1, 16510, False
    FLAG_F = 1307, -1, -1, 16517, False
    FLAG_G = 1150, -1, -1, 16183, False
    FLAG_H = 1151, -1, -1, 16184, False
    FLAG_I = 1152, -1, -1, 16188, False
    FLAG_J = 1153, -1, -1, 16189, False
    FLAG_K = 1282, -1, -1, 16183, False
    FLAG_L = 1283, -1, -1, 16183, False
    FLAG_M = 1284, -1, -1, 16183, False
    FLAG_N = 2010, -1, -1, 16517, False
    FLAG_O = 2011, -1, -1, 16517, False
    FLAG_P = 2012, -1, -1, 16517, False
    FLARE = 274, -1, -1, 16316, False
    FLARE_A_PERMANENT = 1689, -1, -1, 16316, False
    FLARE_B_PERMANENT = 1785, -1, -1, 16316, False
    FLOWER_BED = 859, -1, -1, 16385, True
    FLOWERS_1 = 334, -1, -1, 16382, True
    FLOWERS_2 = 335, -1, -1, 16383, True
    FLOWERS_3 = 336, -1, -1, 16384, True
    FLOWERS_4 = 337, -1, -1, 16385, True
    FORAGE_BUSH = 59, 6, -1, 16401, True
    FRANKISH_RELIC = 290, 26, -1, 16355, True
    FRUIT_BUSH = 1059, 199, -1, 16401, True
    GALLOW = 1095, -1, -1, 16228, True
    GOLD_MINE = 66, 14, -1, 16400, True
    GOTHIC_RELIC = 292, 26, -1, 16356, True
    GRANARY = 1089, 60, 1499, 16222, False
    GRASS_DRY = 1359, -1, -1, 16718, True
    GRASS_GREEN = 1358, -1, -1, 16718, True
    GRASS_PATCH_DRY = 1033, -1, -1, 16385, True
    GRASS_PATCH_GREEN = 301, -1, -1, 16385, True
    GRAVE = 820, -1, -1, 16720, True
    GREAT_FISH_MARLIN = 450, 281, -1, 16330, True
    HAY_STACK = 857, -1, -1, 16761, True
    HEAD = 821, -1, -1, 16721, True
    ICE_NAVIGABLE = 728, -1, -1, 16610, True
    IMPALED_CORPSE = 1315, -1, -1, 16721, False
    JAPANESE_RELIC = 294, 26, -1, 16357, True
    LARGE_TEMP_MAP_REVEAL = 332, -1, -1, 16316, False
    MAP_REVEALER = 837, -1, -1, 16737, False
    MAP_REVEALER_MEDIUM = 1774, -1, -1, 16737, False
    MAP_REVEALER_GIANT = 1775, -1, -1, 16737, False
    MOUNTAIN_1 = 310, -1, -1, 16342, True
    MOUNTAIN_2 = 311, -1, -1, 16343, True
    MOUNTAIN_3 = 744, -1, -1, 16647, True
    MOUNTAIN_4 = 745, -1, -1, 16648, True
    MOUNTAIN_5 = 1041, -1, -1, 16772, True
    MOUNTAIN_6 = 1042, -1, -1, 16773, True
    MOUNTAIN_7 = 1043, -1, -1, 16774, True
    MOUNTAIN_8 = 1044, -1, -1, 16775, True
    NINE_BANDS = 720, -1, -1, 16602, False
    NUBIAN_PYRAMID = 1563, -1, -1, 16756, True
    OLD_STONE_HEAD = 855, -1, -1, 16756, True
    PAGODA_A = 1201, -1, -1, 16756, True
    PAGODA_B = 1202, -1, -1, 16756, True
    PAGODA_C = 1203, -1, -1, 16756, True
    TORII_GATE = 1562, -1, -1, 16756, True
    PATH_1 = 339, -1, -1, 16387, True
    PATH_2 = 340, -1, -1, 16388, True
    PATH_3 = 341, -1, -1, 16389, True
    PATH_4 = 338, -1, -1, 16386, True
    PERSIAN_RELIC = 295, 26, -1, 16358, True
    PIECE_OF_THE_TRUE_CROSS = 688, -1, -1, 16570, True
    PLANT = 818, -1, -1, 16718, True
    PLANT_BUSH_GREEN = 1360, -1, -1, 16718, True
    PLANT_DEAD = 1365, -1, -1, 16718, True
    PLANT_FLOWERS = 1366, -1, -1, 16718, True
    PLANT_JUNGLE = 1351, -1, -1, 16718, True
    PLANT_RAINFOREST = 1354, -1, -1, 16718, True
    PLANT_SHRUB_GREEN = 1362, -1, -1, 16718, True
    PLANT_UNDERBRUSH = 1353, -1, -1, 16718, True
    PLANT_UNDERBRUSH_TROPICAL = 1352, -1, -1, 16718, True
    PLANT_WEEDS = 1364, -1, -1, 16718, True
    RELIC = 285, 26, -1, 16350, True
    ROCK_1 = 623, -1, -1, 16520, True
    ROCK_2 = 1323, -1, -1, 16520, True
    ROCK_BEACH = 1148, -1, -1, 16180, True
    ROCK_FORMATION_1 = 1048, -1, -1, 16789, True
    ROCK_FORMATION_2 = 1049, -1, -1, 16790, True
    ROCK_FORMATION_3 = 1050, -1, -1, 16791, True
    ROCK_JUNGLE = 1149, -1, -1, 16181, True
    ROMAN_RUINS = 856, -1, -1, 16757, True
    RUBBLE_1_X_1 = 863, -1, -1, 16001, False
    RUBBLE_2_X_2 = 864, -1, -1, 16002, False
    RUBBLE_3_X_3 = 865, -1, -1, 16003, False
    RUBBLE_4_X_4 = 1497, -1, -1, 16004, False
    RUBBLE_8_X_8 = 1498, -1, -1, 16006, False
    RUGS = 711, -1, -1, 16593, True
    SARACEN_RELIC = 296, 26, -1, 16359, True
    SEA_ROCKS_1 = 389, -1, -1, 16253, True
    SEA_ROCKS_2 = 396, -1, -1, 16262, True
    SHIPWRECK_A = 721, -1, -1, 16603, False
    SHIPWRECK_B = 722, -1, -1, 16604, False
    SHORE_FISH = 69, 280, -1, 16501, True
    SIGN = 819, 189, -1, 16719, True
    SKELETON = 710, -1, -1, 16592, True
    SMALL_TEMP_MAP_REVEAL = 112, -1, -1, 16316, False
    SMOKE = 1308, -1, -1, 16517, False
    SNOW_MOUNTAIN_1 = 1045, -1, -1, 16776, True
    SNOW_MOUNTAIN_2 = 1046, -1, -1, 16777, True
    SNOW_MOUNTAIN_3 = 1047, -1, -1, 16778, True
    STATUE_CIVILIZATION = 1279, -1, -1, 16403, False
    STATUE_COLUMN = 1322, -1, -1, 16717, True
    STATUE_LEFT = 1343, -1, -1, 16717, True
    STATUE_RIGHT = 1345, -1, -1, 16717, True
    STELAE_A = 1092, -1, -1, 16225, False
    STELAE_B = 1093, -1, -1, 16226, False
    STELAE_C = 1094, -1, -1, 16227, False
    STONE_MINE = 102, 9, -1, 16252, True
    STUMP = 809, -1, -1, 16281, True
    STUPA = 1191, -1, -1, 16756, True
    TARGET_A = 1564, -1, -1, 16721, False
    TARGET_B = 1565, -1, -1, 16721, False
    TEMPLE_RUIN = 1566, -1, -1, 16757, True
    TEUTONIC_RELIC = 297, 26, -1, 16360, True
    TORCH_A = 499, -1, -1, 16423, False
    TORCH_B = 1376, -1, -1, 16423, False
    TREE_A = 399, 32, 415, 16265, True
    TREE_ACACIA = 1063, 32, 415, 16798, True
    TREE_B = 400, 32, 415, 16266, True
    TREE_BAMBOO_FOREST = 348, 32, 737, 16396, True
    TREE_BAOBAB = 1052, 32, 1634, 16793, True
    TREE_BIRCH = 1717, 32, 415, 16399, True
    TREE_C = 401, 32, 415, 16267, True
    TREE_CYPRESS = 1347, 32, 415, 16399, True
    TREE_D = 402, 32, 415, 16268, True
    TREE_DEAD = 1250, 32, 415, 16694, True
    TREE_DRAGON = 1051, 32, 415, 16792, True
    TREE_E = 403, 32, 415, 16269, True
    TREE_F = 404, 32, 415, 16270, True
    TREE_G = 405, 32, 415, 16271, True
    TREE_H = 406, 32, 415, 16272, True
    TREE_I = 407, 32, 415, 16273, True
    TREE_ITALIAN_PINE = 1348, 32, 415, 16399, True
    TREE_J = 408, 32, 415, 16274, True
    TREE_JUNGLE = 414, 32, 415, 16693, True
    TREE_K = 409, 32, 415, 16275, True
    TREE_L = 410, 32, 415, 16276, True
    TREE_MANGROVE = 1144, 32, 415, 16177, True
    TREE_OAK = 349, 32, 415, 16397, True
    TREE_OAK_AUTUMN = 1248, 32, 415, 16277, True
    TREE_OAK_AUTUMN_SNOW = 1249, 32, 415, 16694, True
    TREE_OAK_FOREST = 411, 32, 415, 16277, True
    TREE_OLIVE = 1349, 32, 415, 16399, True
    TREE_PALM_FOREST = 351, 32, 415, 16398, True
    TREE_PINE_FOREST = 350, 32, 415, 16399, True
    TREE_RAINFOREST = 1146, 32, 415, 16179, True
    TREE_REEDS = 1350, 32, 737, 16396, True
    TREE_SNOW_PINE = 413, 32, 415, 16694, True
    TREE_TD = 284, 32, 415, 16348, True
    TROWULAN_GATE = 1176, -1, -1, 16756, True
    TURKISH_RELIC = 298, 26, -1, 16351, True
    VASES = 1177, -1, -1, 16385, True
    WELL = 1567, -1, -1, 16756, True
    DOLPHIN = 61, 141, -1, 16330, True
    LOOT = 472, -1, -1, 16717, True
    WATERFALL_OVERLAY = 896, -1, -1, 16756, True
    QUARRY = 1319, -1, -1, 16717, True
    LUMBER = 1320, -1, -1, 16717, True
    GOODS = 1321, -1, -1, 16717, True
    FLAME1 = 1333, -1, -1, 16517, True
    FLAME2 = 1334, -1, -1, 16517, True
    FLAME3 = 1335, -1, -1, 16517, True
    FLAME4 = 1336, -1, -1, 16517, True
    WATERFALL_BACKGROUND = 1635, -1, -1, 16756, True
    BLOCKER = 1776, -1, -1, 16756, True
    INDIAN_STATUES = 1777, -1, -1, 16717, True
    REKHA_DEUL_TEMPLE = 1778, -1, -1, 16756, True
    INDIAN_RUINS = 1784, -1, -1, 16757, True
    SVAN_TOWER = 1807, -1, -1, 16756, True
    CLIFF_DEFAULT_1 = 264, -1, -1, 16249, True
    CLIFF_DEFAULT_2 = 265, -1, -1, 16249, True
    CLIFF_DEFAULT_3 = 266, -1, -1, 16249, True
    CLIFF_DEFAULT_4 = 267, -1, -1, 16249, True
    CLIFF_DEFAULT_5 = 268, -1, -1, 16249, True
    CLIFF_DEFAULT_6 = 269, -1, -1, 16249, True
    CLIFF_DEFAULT_7 = 270, -1, -1, 16249, True
    CLIFF_DEFAULT_8 = 271, -1, -1, 16249, True
    CLIFF_DEFAULT_9 = 272, -1, -1, 16249, True
    CLIFF_DESERT_1 = 1849, -1, -1, 16249, True
    CLIFF_DESERT_2 = 1850, -1, -1, 16249, True
    CLIFF_DESERT_3 = 1851, -1, -1, 16249, True
    CLIFF_DESERT_4 = 1852, -1, -1, 16249, True
    CLIFF_DESERT_5 = 1853, -1, -1, 16249, True
    CLIFF_DESERT_6 = 1854, -1, -1, 16249, True
    CLIFF_DESERT_7 = 1855, -1, -1, 16249, True
    CLIFF_DESERT_8 = 1856, -1, -1, 16249, True
    CLIFF_DESERT_9 = 1857, -1, -1, 16249, True
    CLIFF_SNOW_1 = 1858, -1, -1, 16249, True
    CLIFF_SNOW_2 = 1859, -1, -1, 16249, True
    CLIFF_SNOW_3 = 1860, -1, -1, 16249, True
    CLIFF_SNOW_4 = 1861, -1, -1, 16249, True
    CLIFF_SNOW_5 = 1862, -1, -1, 16249, True
    CLIFF_SNOW_6 = 1863, -1, -1, 16249, True
    CLIFF_SNOW_7 = 1864, -1, -1, 16249, True
    CLIFF_SNOW_8 = 1865, -1, -1, 16249, True
    CLIFF_SNOW_9 = 1866, -1, -1, 16249, True
    OYSTERS = 2170, 701, -1, 16400, True
    MEDITERRANEAN_RUINS = 2234, -1, -1, 16757, True
    MEDITERRANEAN_COURTYARD_WALLS = 2235, -1, -1, 16757, True
    MESOPOTAMIAN_PILLAR = 2251, -1, -1, 16757, True
    MESOPOTAMIAN_GARDEN = 2252, -1, -1, 16757, True
    STATUE_ATHENA_MARBLE = 2264, -1, -1, 16717, True
    STATUE_ATHENA_PAINTED = 2265, -1, -1, 16717, True
    ARCHAIC_FENCE = 2274, -1, -1, 16757, True
    GARDEN_HEDGE = 2278, -1, -1, 16757, True
    STATUE_ARES_MARBLE = 2279, -1, -1, 16717, True
    STATUE_ARES_PAINTED = 2280, -1, -1, 16717, True
    SIEGE_CAMP_EQUIPMENT = 2282, -1, -1, 16757, True
    SIEGE_CAMP_WEAPONS = 2283, -1, -1, 16757, True
    MARKET_STALL = 2284, -1, -1, 16717, True
    STAKE_BARRICADE = 2285, -1, -1, 16717, True
    TROPAION = 2286, -1, -1, 16717, True
    MESOPOTAMIAN_TOMB = 2287, -1, -1, 16717, True
    FIRE_SHRINE = 2288, -1, -1, 16717, True
    TREASURE_CHEST = 2289, -1, -1, 16717, True
    GRAPEVINE = 2290, -1, -1, 16717, True
    LEATHERWORKING_EQUIPMENT = 2291, -1, -1, 16717, True
    WEAPON_RACK = 2293, -1, -1, 16757, True
    SACRED_TREE = 2294, -1, -1, 16717, True
    HERO_SHRINE = 2306, -1, -1, 16717, True
    MESOPOTAMIAN_RUINS = 2350, -1, -1, 16757, True
    THOLOS_SHRINE = 2351, -1, -1, 16757, True
    AURA_QUEST_INDICATOR_LAVENDER = 2373, -1, -1, 16385, True
    AURA_QUEST_INDICATOR_SEASHELLS = 2378, -1, -1, 16385, True
    AURA_QUEST_INDICATOR_COINS = 2379, -1, -1, 16385, True
    AURA_QUEST_INDICATOR_GOLD_AND_SHELLS = 2380, -1, -1, 16385, True
    FLAG_ACHAEMENIDS_1 = 2253, -1, -1, 16506, False
    FLAG_ACHAEMENIDS_2 = 2254, -1, -1, 16506, False
    FLAG_ACHAEMENIDS_3 = 2255, -1, -1, 16506, False
    FLAG_ATHENIANS_1 = 2256, -1, -1, 16506, False
    FLAG_ATHENIANS_2 = 2257, -1, -1, 16506, False
    FLAG_ATHENIANS_3 = 2258, -1, -1, 16506, False
    FLAG_SPARTANS_1 = 2259, -1, -1, 16506, False
    FLAG_SPARTANS_2 = 2260, -1, -1, 16506, False
    FLAG_SPARTANS_3 = 2261, -1, -1, 16506, False
    ANTIQUITY_TRANSPORT_SHIPWRECK = 2352, -1, -1, 16603, False
    LEVIATHAN_SHIPWRECK = 2353, -1, -1, 16603, False
    GALLEY_SHIPWRECK = 2354, -1, -1, 16603, False
    CATAPULT_SHIPWRECK = 2355, -1, -1, 16603, False
    BAMBOO_STUMP = 1536, -1, -1, 16281, True
    BAOBAB_STUMP = 1537, -1, -1, 16281, True
    LUSH_BAMBOO_STUMP = 1538, -1, -1, 16281, True
    FELLED_TREE = 1539, 32, 415, 16265, True
    FELLED_TREE_BAMBOO = 1540, 32, 737, 16396, True
    FELLED_TREE_BAOBAB = 1541, 32, 1634, 16793, True
    FELLED_TREE_LUSH_BAMBOO = 1542, 32, 1985, 16396, True
    CHAPEL = 1836, -1, -1, 16225, False
    CASTLE_RUINS = 1837, -1, -1, 16757, True
    CHURCH_RUINS = 1838, -1, -1, 16757, True
    TREE_LUSH_BAMBOO_FOREST = 1984, 32, 1985, 16396, True
    PAPER_LANTERN = 1986, -1, -1, 16721, False
    CHINESE_RUINS = 1987, -1, -1, 16717, True
    PAIFANG_GATE_SMALL = 1989, -1, -1, 16756, True
    PAIFANG_GATE_LARGE = 1990, -1, -1, 16756, True
    FOUNTAIN = 1991, -1, -1, 16756, True
    PAGODA_D = 2005, -1, -1, 16756, True
    PAGODA_E = 2006, -1, -1, 16756, True
    GARDEN_PAVILION = 2007, -1, -1, 16756, True
    ROCK_PILLAR = 2008, -1, -1, 16181, True
    ROCK_LIMESTONE = 2009, -1, -1, 16181, True
    FLAG_RITUAL_A = 2013, -1, -1, 16517, False
    FLAG_RITUAL_B = 2014, -1, -1, 16517, False
    FLAG_RITUAL_C = 2015, -1, -1, 16517, False
    TREE_ASIAN_PINE = 2016, 32, 415, 16396, True
    TREE_PEACH_BLOSSOM = 2017, 32, 415, 16396, True
    ASIAN_CARTS = 2018, -1, -1, 16756, True
    WEAPON_STACKS = 2019, -1, -1, 16756, True
    GARDEN_BRIDGE = 2020, -1, -1, 16756, True
    SIEGE_PROPS = 2021, -1, -1, 16756, True
    ASIAN_LANTERNS = 2022, -1, -1, 16756, True
    BURNED_BUILDING_B = 2023, -1, -1, 16756, True
    ASIAN_MARKET_STALLS = 2024, -1, -1, 16756, True
    TREE_WILLOW = 2025, 32, 415, 16396, True
    TREE_ASIAN_MAPLE_GREEN = 2027, 32, 415, 16396, True
    TREE_ASIAN_MAPLE_AUTUMN = 2028, 32, 415, 16396, True
    FALLEN_LEAVES_PEACH_BLOSSOM = 2029, -1, -1, 16718, True
    FALLEN_LEAVES_MAPLE = 2030, -1, -1, 16718, True
    FALLEN_LEAVES_MAPLE_AUTUMN = 2031, -1, -1, 16718, True
    HUABIAO_TOTEM = 2058, -1, -1, 16756, True
    QUE_TOWER = 2059, -1, -1, 16717, True
    PANDA_ROCK = 2082, -1, -1, 16181, True
