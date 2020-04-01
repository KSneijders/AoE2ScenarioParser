beach = 2
beach_non_navigable = 79
beach_non_navigable_wet_gravel = 81
beach_non_navigable_wet_rock = 82
beach_non_navigable_wet_sand = 80
snow = 37
beach_vegetation = 52
beach_wet = 107
beach_wet_gravel = 108
beach_wet_rock = 109
beach_white = 53
beach_white_vegetation = 51
black = 47
desert_cracked = 45
desert_quicksand = 46
desert_sand = 14
dirt_1 = 6
dirt_2 = 11
dirt_3 = 3
dirt_4 = 42
dirt_mud = 76
dirt_savannah = 41
farm = 7
farm_0 = 29
farm_33 = 30
farm_67 = 31
farm_dead = 8
forest_acacia = 50
forest_autumn = 104
forest_autumn_snow = 105
forest_bamboo = 18
forest_baobab = 49
forest_bush = 89
forest_dead = 106
forest_dragon_tree = 48
forest_jungle = 17
forest_magrove = 55
forest_mediterranean = 88
forest_oak = 10
forest_oak_bush = 20
forest_palm_desert = 13
forest_pine = 19
forest_pine_snow = 21
forest_rainforest = 56
forest_reeds = 92
forest_reeds_beach = 91
forest_reeds_shallows = 90
grass_1 = 0
grass_2 = 12
grass_3 = 9
grass_dry = 100
grass_foundation = 27
grass_jungle = 60
grass_jungle_rainforest = 83
grass_other = 16
gravel_default = 70
gravel_desert = 102
ice = 35
rice_farm = 63
rice_farm_0 = 65
rice_farm_33 = 66
rice_farm_67 = 67
rice_farm_dead = 64
road = 24
road_broken = 25
road_fungus = 75
road_gravel = 78
rock_1 = 40
shallows = 4
shallows_azure = 59
shallows_mangrove = 54
snow_foundation = 36
snow_light = 73
snow_strong = 74
swamp_bogland = 101
underbush = 5
underbush_jungle = 77
underbush_leaves = 71
underbush_snow = 72
water_2d_bridge = 28
water_2d_shoreless = 15
water_azure = 58
water_brown = 96
water_deep = 22
water_deep_ocean = 57
water_green = 95
water_medium = 23
water_shallow = 1


def get_terrain_id_by_string(terrain):
    """
    Returns the ID of the given terrain. None otherwise.
    """
    try:
        return eval(terrain)
    except NameError:
        return None