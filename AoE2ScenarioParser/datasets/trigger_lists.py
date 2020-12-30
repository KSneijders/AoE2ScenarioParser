from enum import IntEnum


class DiplomacyState(IntEnum):
    ALLY = 0
    NEUTRAL = 1
    ENEMY = 3


class Operation(IntEnum):
    SET = 1
    ADD = 2
    SUBTRACT = 3
    MULTIPLY = 4
    DIVIDE = 5


class AttackStance(IntEnum):
    AGGRESSIVE_STANCE = 0
    DEFENSIVE_STANCE = 1
    STAND_GROUND = 2
    NO_ATTACK_STANCE = 3


class UnitAIAction(IntEnum):
    ANY = 0
    ATTACK = 1
    BUILD = 3
    CONVERT = 5
    DEFEND = 2
    ENTER = 18
    EVADE = 17
    EXPLORE = 6
    FOLLOW = 13
    GATHER = 10
    HEAL = 4
    HUNT = 14
    IDLE = 24
    MOVE = 11
    PATROL = 12
    RELIC = 23
    REPAIR = 19
    RESEARCH = 21
    RETREAT = 9
    RUNAWAY = 8
    STOP = 7
    TRADE = 16
    TRAIN = 20
    TRANSPORT = 15
    UNLOAD = 22


class ButtonLocation(IntEnum):
    LOCATION_0_0 = 0
    LOCATION_1_0 = 2
    LOCATION_2_0 = 3
    LOCATION_3_0 = 4
    LOCATION_4_0 = 5
    LOCATION_0_1 = 6
    LOCATION_1_1 = 7
    LOCATION_2_1 = 8
    LOCATION_3_1 = 9
    LOCATION_4_1 = 10
    LOCATION_0_2 = 11
    LOCATION_1_2 = 12
    LOCATION_2_2 = 13
    LOCATION_3_2 = 14
    # LOCATION_4_2 = 15?  # Probably disabled for the arrow key if present


class PanelLocation(IntEnum):
    TOP = 0
    """Panel at the top of the screen. ~13% from the top"""
    BETWEEN = 1
    """Panel between the top and the center of the screen. ~33% from the top"""
    CENTER = 2
    """Panel close to the center of the screen. ~45% from the top"""


class TimeUnit(IntEnum):
    YEARS = 2
    """In-Game years. A year is 5 seconds in-game time."""
    MINUTES = 1
    """In-Game minutes."""
    SECONDS = 0
    """In-Game seconds."""


class VisibilityState(IntEnum):
    VISIBLE = 0
    EXPLORED = 1
    INVISIBLE = 2


class DifficultyLevel(IntEnum):
    EASIEST = 4
    STANDARD = 3
    MODERATE = 2
    HARD = 1
    HARDEST = 0
    # EXTREME = 5  # ???


class TechnologyState(IntEnum):
    DISABLED = -1
    NOT_READY = 0
    READY = 1
    RESEARCHING = 2
    DONE = 3
    QUEUED = 4


class Comparison(IntEnum):
    EQUAL = 0
    LESS = 1
    LARGER = 2
    LESS_OR_EQUAL = 3
    LARGER_OR_EQUAL = 4


class ObjectAttribute(IntEnum):
    HIT_POINTS = 0
    LINE_OF_SIGHT = 1
    GARRISON_CAPACITY = 2
    UNIT_SIZE_X = 3
    UNIT_SIZE_Y = 4
    MOVEMENT_SPEED = 5
    ROTATION_SPEED = 6
    ARMOR = 8
    ATTACK = 9
    ATTACK_RELOAD_TIME = 10
    ACCURACY_PERCENT = 11
    MAX_RANGE = 12
    WORK_RATE = 13
    CARRY_CAPACITY = 14
    BASE_ARMOR = 15
    PROJECTILE_UNIT = 16
    ICON_GRAPHICS_ANGLE = 17
    TERRAIN_DEFENSE_BONUS = 18
    ENABLE_SMART_PROJECTILES = 19
    MINIMUM_RANGE = 20
    ARNOUNT_OF_1ST_RESOURCES = 21
    BLAST_WIDTH = 22
    SEARCH_RADIUS = 23
    HERO_STATUS = 40
    FRAME_DELAY = 41
    TRAIN_LOCATION = 42
    TRAIN_BUTTON = 43
    BLAST_LEVEL = 44
    OBJECT_NAME_ID = 50
    SHORT_DESCRIPTION_ID = 51
    TERRAIN_RESTRICTION_ID = 53
    DEAD_UNIT_ID = 57
    RESOURCE_COSTS = 100
    TRAIN_TIME = 101
    TOTAL_MISSILES = 102
    FOOD_COSTS = 103
    WOOD_COSTS = 104
    GOLD_COSTS = 105
    STONE_COSTS = 106
    MAX_TOTAL_MISSILES = 107
    GARRISON_HEAL_RATE = 108
    """Hidden in the editor, but does work! Do not open effect in editor. Will cause it to reset"""
    REGENERATION_RATE = 109


class Attribute(IntEnum):
    FOOD = 0
    """Food Amount of the Source Player"""
    WOOD = 1
    """Wood Amount of the Source Player"""
    STONE = 2
    """Stone Amount of the Source Player"""
    GOLD = 3
    """Gold Amount of the Source Player"""
    POPULATION_CAP = 4
    """Current Max Pop of the Source Player"""
    CONVERSION_RANGE = 5
    """Unknown: Amount of the Source Player"""
    CURRENT_AGE = 6
    """
    Age Name and Icon At the Top of the Screen of the Source Player:

    - 0: Dark Age
    - 1: Feudal Age
    - 2: Castle Age
    - 3: Imperial Age
    """
    RELICS = 7
    """Number of Relics Held by the Source Player"""
    TRADE_BONUS = 8
    """Unused: Amount of the Source Player"""
    TRADE_GOODS = 9
    """Unused: Amount of the Source Player"""
    TRADE_PRODUCTION = 10
    """Unused: Amount of the Source Player"""
    CURRENT_POPULATION = 11
    """Current Pop of the Source Player"""
    CORPSE_DECAY_TIME = 12
    """Time Taken by Corpses to Decay for the Source Player"""
    REMARKABLE_DISCOVERY = 13
    """Unknown: Amount of the Source Player"""
    MONUMENTS_CAPTURED = 14
    """Number of Monuments Owned by the Source Player"""
    MEAT_STORAGE = 15
    """Unknown: Amount of the Source Player"""
    BERRY_STORAGE = 16
    """Unknown: Amount of the Source Player"""
    FISH_STORAGE = 17
    """Unknown: Amount of the Source Player"""
    UNUSED_RESOURCE_018 = 18
    """Unused: Amount of the Source Player"""
    TOTAL_UNITS_OWNED = 19
    """Total Units Owned by the Source Player"""
    KILLS = 20
    """Total Units Killed of the Source Player"""
    RESEARCH_COUNT = 21
    """Research Count of the Source Player"""
    EXPLORATION = 22
    """Percent Map Explored of the Source Player"""
    CASTLE_AGE_TECH_ID = 23
    """Always 102"""
    IMPERIAL_AGE_TECH_ID = 24
    """Always 103"""
    FEUDAL_AGE_TECH_ID = 25
    """Always 101"""
    ATTACK_SOUND_EFFECT_ID = 26
    """Always 0"""
    ENABLE_MONK_CONVERSION = 27
    """
    Boolean: Allow Enemy Monk Conversions by the Source Player:

    - 0: Don't Allow
    - >= 1: Allow
    """
    ENABLE_BUILDING_CONVERSIONS = 28
    """
    Boolean: Allow Enemy Building Conversions by the Source Player:

    - 0: Don't Allow
    - 1: Allow
    - >=2: Monks Can Convert Buildings from Range
    """
    UNUSED_RESOURCE_029 = 29
    """Unused: Amount of the Source Player"""
    BUILDING_LIMIT = 30
    """Unused: Amount of the Source Player"""
    FOOD_LIMIT = 31
    """Unused: Amount of the Source Player"""
    BONUS_POPULATION_CAP = 32
    """Additional Max Pop Space of the Source Player"""
    FOOD_MAINTENANCE = 33
    """Unknown: Amount of the Source Player"""
    FAITH = 34
    """Boolean: Faith Researched by the Source Player"""
    FAITH_RECHARGE_RATE = 35
    """Monk Faith Recovery Rate of the Source Player"""
    FARM_FOOD = 36
    """Max Farm Food of the Source Player"""
    CIVILIAN_POPULATION = 37
    """Civilian Pop of the Source Player"""
    UNUSED_RESOURCE_038 = 38
    """Unused: Amount of the Source Player"""
    ALL_TECHS_ACHIEVED = 39
    """
    Boolean: Researched All Enabled Techs by the Source Player:

    - 0: When All Techs not Researched
    - 1: When All Techs Are Researched
    """
    MILITARY_POPULATION = 40
    """Military Pop of the Source Player"""
    CONVERSIONS = 41
    """Number of Units Converted by the Source Player"""
    WONDER = 42
    """Number of Standing Wonders of the Source Player"""
    RAZINGS = 43
    """Number of Buildings Destroyed by the Source Player"""
    KILL_RATIO = 44
    """Ceil of Kills/deaths of the Source Player"""
    PLAYER_KILLED = 45
    """
    Boolean: Survival to Finish of the Source Player:

    - 0: No
    - 1: Yes
    """
    TRIBUTE_INEFFICIENCY = 46
    """Tribute Tax Fraction Imposed On the Source Player"""
    GOLD_MINING_PRODUCTIVITY = 47
    """
    Longer Lasting Gold Percent of the Source Player:

    - 0: Generic
    - 10: Mayans
    """
    TOWN_CENTER_UNAVAILABLE = 48
    """
    Boolean: Allow Building Tcs for the Source Player:

    - 0: No (sudden Death)
    - 1: Yes
    """
    GOLD_COUNTER = 49
    """Total Gold Collected by the Source Player"""
    REVEAL_ALLY = 50
    """
    Boolean: Show Ally Los for the Source Player:

    - 0: No Allied Vision
    - 1: Allied Vision
    """
    HOUSES = 51
    """Unused: Amount of the Source Player"""
    MONASTERIES = 52
    """Number of Monasteries of the Source Player"""
    TRIBUTE_SENT = 53
    """Amount Tributed by the Source Player"""
    ALL_MONUMENTS_CAPTURED = 54
    """Boolean: All Monuments Captured by the Source Player"""
    ALL_RELICS_CAPTURED = 55
    """Boolean: All Relics Captured by the Source Player"""
    ORE = 56
    """Swbg Ore Amount of the Source Player"""
    CAPTURED_UNIT = 57
    """Number of Units Kidnapped by the Source Player"""
    DARK_AGE_TECH_ID = 58
    """Always 104"""
    TRADE_GOOD_QUALITY = 59
    """Unused: Amount of the Source Player"""
    TRADE_MARKET_LEVEL = 60
    """Unused: Amount of the Source Player"""
    FORMATIONS = 61
    """Unused: Amount of the Source Player"""
    BUILDING_HOUSE_RATE = 62
    """Unknown: Amount of the Source Player"""
    GATHER_TAX_RATE = 63
    """Unknown: Amount of the Source Player"""
    GATHER_ACCUMULATION = 64
    """Unknown: Amount of the Source Player"""
    SALVAGE_DECAY_RATE = 65
    """Boat Corpse Decay Rate of the Source Player"""
    ALLOW_FORMATIONS = 66
    """Unused: Amount of the Source Player"""
    CAN_CONVERT = 67
    """
    Boolean: Allow Enemy Object Conversions Amount of the Source Player:

    - 0: Don't Allow Even Regular Unit Conversion
    - 1: Allows Regular Unit Conversion
    """
    HITPOINTS_KILLED = 68
    """Cumulative Hp of All Units Killed by the Source Player"""
    PLAYER1_KILLS = 69
    """Number of Player1 Units Killed by the Source Player"""
    PLAYER2_KILLS = 70
    """Number of Player2 Units Killed by the Source Player"""
    PLAYER3_KILLS = 71
    """Number of Player3 Units Killed by the Source Player"""
    PLAYER4_KILLS = 72
    """Number of Player4 Units Killed by the Source Player"""
    PLAYER5_KILLS = 73
    """Number of Player5 Units Killed by the Source Player"""
    PLAYER6_KILLS = 74
    """Number of Player6 Units Killed by the Source Player"""
    PLAYER7_KILLS = 75
    """Number of Player7 Units Killed by the Source Player"""
    PLAYER8_KILLS = 76
    """Number of Player8 Units Killed by the Source Player"""
    CONVERSION_RESISTANCE = 77
    """Coefficient of Conversion Resistance of the Source Player"""
    TRADE_VIG_RATE = 78
    """
    Market Exhange Rate Fraction for the Source Player:

    - 0.3: Generic Rate
    - 0.15: After Guilds
    - 0.05: for Saracens
    """
    STONE_MINING_PRODUCTIVITY = 79
    """
    Longer Lasting Stone Percent of the Source Player:

    - 0: Generic
    - 10: Mayans
    """
    QUEUED_COUNT = 80
    """Amount of Units in Queue of the Source Player"""
    TRAINING_COUNT = 81
    """Amount of Units Being Trained of the Source Player"""
    START_WITH_PACKED_TOWN_CENTRE = 82
    """Boolean: Started With Ptwc of the Source Player"""
    BOARDING_RECHARGE_RATE = 83
    """Abgal Faith Recharge Rate Amount of the Source Player"""
    STARTING_VILLAGERS = 84
    """
    Number of Starting Villagers of the Source Player:

    - 3 for Generic Civs
    - 4 for Mayans
    - 6 for Chinese
    """
    RESEARCH_COST_MODIFIER = 85
    """Reduce Tech Cost to Fraction for the Source Player"""
    RESEARCH_TIME_MODIFIER = 86
    """Reduce Tech Research Time to Fraction for the Source Player"""
    CONVERT_BOATS = 87
    """Boolean: Allow Monks to Convert Boats Amount of the Source Player"""
    FISH_TRAP_FOOD = 88
    """Max Fishtrap Food of the Source Player"""
    HEAL_RATE_MODIFIER = 89
    """Monk Healing Rate of the Source Player"""
    HEAL_RANGE = 90
    """Monk Heal Range of the Source Player"""
    STARTING_FOOD = 91
    """Starting Food Amount of the Source Player"""
    STARTING_WOOD = 92
    """Starting Wood Amount of the Source Player"""
    STARTING_STONE = 93
    """Starting Stone Amount of the Source Player"""
    STARTING_GOLD = 94
    """Starting Gold Amount of the Source Player"""
    ENABLE_PTWC_OR_KIDNAP_OR_LOOT = 95
    """
    Enable Town Centre Packing for the Source Player:

    - 0: Normal
    - 1: Enables Pack Button On Tc But It is Bugged, if You Click It Then Tc Goes Berserk
    - >=2: No Noticeable Effect
    """
    BERSERKER_HEAL_TIMER = 96
    """Time Difference Between Berserker Heal Rate for Source Player"""
    DOMINANT_SHEEP_CONTROL = 97
    """
    Boolean: Force Sheep Conversion of the Source Player:

    - 0: Normal Sheep Conversion Behaviour
    - >=1: if Another Player does not also have this set to a Non Zero Value, Their Sheep will Force Convert to Source 
        Player
    """
    OBJECT_COST_SUMMATION = 98
    """Total Cost of All Units and Buildings Owned by the Source Player"""
    RESEARCH_COST_SUMMATION = 99
    """Total Cost of All Researches Researched by the Source Player"""
    RELIC_INCOME_SUMMATION = 100
    """Total Relic Gold Generated by the Source Player"""
    TRADE_INCOME_SUMMATION = 101
    """Total Trade Gold Generated by the Source Player"""
    PLAYER1_TRIBUTE = 102
    """Amount of Resources Tributed to Player1 by the Source Player"""
    PLAYER2_TRIBUTE = 103
    """Amount of Resources Tributed to Player2 by the Source Player"""
    PLAYER3_TRIBUTE = 104
    """Amount of Resources Tributed to Player3 by the Source Player"""
    PLAYER4_TRIBUTE = 105
    """Amount of Resources Tributed to Player4 by the Source Player"""
    PLAYER5_TRIBUTE = 106
    """Amount of Resources Tributed to Player5 by the Source Player"""
    PLAYER6_TRIBUTE = 107
    """Amount of Resources Tributed to Player6 by the Source Player"""
    PLAYER7_TRIBUTE = 108
    """Amount of Resources Tributed to Player7 by the Source Player"""
    PLAYER8_TRIBUTE = 109
    """Amount of Resources Tributed to Player8 by the Source Player"""
    PLAYER1_KILL_VALUE = 110
    """Cost of Units of Player1 Killed by the Source Player"""
    PLAYER2_KILL_VALUE = 111
    """Cost of Units of Player2 Killed by the Source Player"""
    PLAYER3_KILL_VALUE = 112
    """Cost of Units of Player3 Killed by the Source Player"""
    PLAYER4_KILL_VALUE = 113
    """Cost of Units of Player4 Killed by the Source Player"""
    PLAYER5_KILL_VALUE = 114
    """Cost of Units of Player5 Killed by the Source Player"""
    PLAYER6_KILL_VALUE = 115
    """Cost of Units of Player6 Killed by the Source Player"""
    PLAYER7_KILL_VALUE = 116
    """Cost of Units of Player7 Killed by the Source Player"""
    PLAYER8_KILL_VALUE = 117
    """Cost of Units of Player8 Killed by the Source Player"""
    PLAYER1_RAZINGS = 118
    """Number of Buildings Destroyed of Player1 by the Source Player"""
    PLAYER2_RAZINGS = 119
    """Number of Buildings Destroyed of Player2 by the Source Player"""
    PLAYER3_RAZINGS = 120
    """Number of Buildings Destroyed of Player3 by the Source Player"""
    PLAYER4_RAZINGS = 121
    """Number of Buildings Destroyed of Player4 by the Source Player"""
    PLAYER5_RAZINGS = 122
    """Number of Buildings Destroyed of Player5 by the Source Player"""
    PLAYER6_RAZINGS = 123
    """Number of Buildings Destroyed of Player6 by the Source Player"""
    PLAYER7_RAZINGS = 124
    """Number of Buildings Destroyed of Player7 by the Source Player"""
    PLAYER8_RAZINGS = 125
    """Number of Buildings Destroyed of Player8 by the Source Player"""
    PLAYER1_RAZING_VALUE = 126
    """Cost of Buildings Destroyed of Player1 by the Source Player"""
    PLAYER2_RAZING_VALUE = 127
    """Cost of Buildings Destroyed of Player2 by the Source Player"""
    PLAYER3_RAZING_VALUE = 128
    """Cost of Buildings Destroyed of Player3 by the Source Player"""
    PLAYER4_RAZING_VALUE = 129
    """Cost of Buildings Destroyed of Player4 by the Source Player"""
    PLAYER5_RAZING_VALUE = 130
    """Cost of Buildings Destroyed of Player5 by the Source Player"""
    PLAYER6_RAZING_VALUE = 131
    """Cost of Buildings Destroyed of Player6 by the Source Player"""
    PLAYER7_RAZING_VALUE = 132
    """Cost of Buildings Destroyed of Player7 by the Source Player"""
    PLAYER8_RAZING_VALUE = 133
    """Cost of Buildings Destroyed of Player8 by the Source Player"""
    CASTLE = 134
    """Number of Standing Castles by the Source Player"""
    HIT_POINT_RAZINGS = 135
    """Cumulative Hp of All Buildings Destroyed by the Source Player"""
    KILLS_BY_PLAYER1 = 136
    """Number of Units Killed by Player1 of the Source Player"""
    KILLS_BY_PLAYER2 = 137
    """Number of Units Killed by Player2 of the Source Player"""
    KILLS_BY_PLAYER3 = 138
    """Number of Units Killed by Player3 of the Source Player"""
    KILLS_BY_PLAYER4 = 139
    """Number of Units Killed by Player4 of the Source Player"""
    KILLS_BY_PLAYER5 = 140
    """Number of Units Killed by Player5 of the Source Player"""
    KILLS_BY_PLAYER6 = 141
    """Number of Units Killed by Player6 of the Source Player"""
    KILLS_BY_PLAYER7 = 142
    """Number of Units Killed by Player7 of the Source Player"""
    KILLS_BY_PLAYER8 = 143
    """Number of Units Killed by Player8 of the Source Player"""
    RAZINGS_BY_PLAYER1 = 144
    """Number of Buildings Destroyed by Player1 of the Source Player"""
    RAZINGS_BY_PLAYER2 = 145
    """Number of Buildings Destroyed by Player2 of the Source Player"""
    RAZINGS_BY_PLAYER3 = 146
    """Number of Buildings Destroyed by Player3 of the Source Player"""
    RAZINGS_BY_PLAYER4 = 147
    """Number of Buildings Destroyed by Player4 of the Source Player"""
    RAZINGS_BY_PLAYER5 = 148
    """Number of Buildings Destroyed by Player5 of the Source Player"""
    RAZINGS_BY_PLAYER6 = 149
    """Number of Buildings Destroyed by Player6 of the Source Player"""
    RAZINGS_BY_PLAYER7 = 150
    """Number of Buildings Destroyed by Player7 of the Source Player"""
    RAZINGS_BY_PLAYER8 = 151
    """Number of Buildings Destroyed by Player8 of the Source Player"""
    VALUE_KILLED_BY_OTHERS = 152
    """Cumulative Cost of Units Lost by the Source Player"""
    VALUE_RAZED_BY_OTHERS = 153
    """Cumulative Cost of Buildings Lost by the Source Player"""
    KILLED_BY_OTHERS = 154
    """Number of Units Killed by Other Players of the Source Player"""
    RAZED_BY_OTHERS = 155
    """Number of Buildings Destroyed by Other Players Amount of the Source Player"""
    TRIBUTE_FROM_PLAYER1 = 156
    """Tribute Received from Player1 of the Source Player"""
    TRIBUTE_FROM_PLAYER2 = 157
    """Tribute Received from Player2 of the Source Player"""
    TRIBUTE_FROM_PLAYER3 = 158
    """Tribute Received from Player3 of the Source Player"""
    TRIBUTE_FROM_PLAYER4 = 159
    """Tribute Received from Player4 of the Source Player"""
    TRIBUTE_FROM_PLAYER5 = 160
    """Tribute Received from Player5 of the Source Player"""
    TRIBUTE_FROM_PLAYER6 = 161
    """Tribute Received from Player6 of the Source Player"""
    TRIBUTE_FROM_PLAYER7 = 162
    """Tribute Received from Player7 of the Source Player"""
    TRIBUTE_FROM_PLAYER8 = 163
    """Tribute Received from Player8 of the Source Player"""
    VALUE_CURRENT_UNITS = 164
    """Cumulative Cost of Alive Untis of the Source Player"""
    VALUE_CURRENT_BUILDINGS = 165
    """Cumulative Cost of Standing Buildings of the Source Player"""
    FOOD_TOTAL = 166
    """Total Food Collected by the Source Player"""
    WOOD_TOTAL = 167
    """Total Wood Collected by the Source Player"""
    STONE_TOTAL = 168
    """Total Stone Collected by the Source Player"""
    GOLD_TOTAL = 169
    """Total Gold Collected by the Source Player"""
    TOTAL_VALUE_OF_KILLS = 170
    """Cumulative Cost of All Units Killed by the Source Player"""
    TOTAL_TRIBUTE_RECEIVED = 171
    """Total Amount of Resources Received in Tribute by the Source Player"""
    TOTAL_VALUE_OF_RAZINGS = 172
    """Cumulative Cost of All Buildings Destroyed by of the Source Player"""
    TOTAL_CASTLES_BUILT = 173
    """Number of Total Castles Built by the Source Player"""
    TOTAL_WONDERS_BUILT = 174
    """Number of Total Wonders Built by the Source Player"""
    TRIBUTE_SCORE = 175
    """Tribute Score of the Source Player"""
    CONVERT_MIN_ADJ = 176
    """Additional Monk Seconds Needed Before Conversion Starts for the Source Player"""
    CONVERT_MAX_ADJ = 177
    """Additional Monk Seconds Needed Before Forced Conversion for the Source Player"""
    CONVERT_RESIST_MIN_ADJ = 178
    """Additional Monk Seconds Needed Before Conversion Starts Against the Source Player"""
    CONVERT_RESIST_MAX_ADJ = 179
    """Additional Monk Seconds Needed Before Forced Conversion for the Source Player"""
    CONVERT_BUILDING_MIN = 180
    """Building Conversion Min Time of the Source Player"""
    CONVERT_BUILDING_MAX = 181
    """Building Conversion Max Time of the Source Player"""
    CONVERT_BUILDING_CHANCE = 182
    """Percent Chance for Monks to Convert Buildings by the Source Player"""
    SPIES = 183
    """Boolean: Show Enemy Los for the Source Player"""
    VALUE_WONDERS_CASTLES = 184
    """Total Cost of All Wonders and Castles of the Source Player"""
    FOOD_SCORE = 185
    """Unknown: Amount of the Source Player"""
    WOOD_SCORE = 186
    """Unknown: Amount of the Source Player"""
    STONE_SCORE = 187
    """Unknown: Amount of the Source Player"""
    GOLD_SCORE = 188
    """Unknown: Amount of the Source Player"""
    WOOD_BONUS = 189
    """
    Longer Lasting Wood Percent of the Source Player:

    - 0: Generic
    - 10: Mayans
    """
    FOOD_BONUS = 190
    """
    Longer Lasting Food Percent of the Source Player:

    - 0: Generic
    - 10: Mayans
    """
    RELIC_RATE = 191
    """
    Relic Gold Generation Rate for the Source Player:

    - 0.5 by Default
    """
    HERESY = 192
    """Boolean: Converted Units Die for the Source Player"""
    THEOCRACY = 193
    """Boolean: Only One Monk Needs to Regen Faith After Group Conversion for the Source Player"""
    CRENELLATIONS = 194
    """Boolean: Researched Crenellations Amount of the Source Player"""
    CONSTRUCTION_RATE_MOD = 195
    """
    Construction Rate Multiplier for the Source Player:

    - 1.0: Generic
    - 1.3: Spanish
    """
    HUN_WONDER_BONUS = 196
    """Additional Time for Relic/wonder Victories in One Tenth of an Year by Any Player"""
    SPIES_DISCOUNT = 197
    """Boolean: Give Discount On Spies for the Source Player"""
    UNKNOWN_RESOURCE_198 = 198
    """Unknown: Amount of Source Player"""
    UNKNOWN_RESOURCE_199 = 199
    """Unknown: Amount of Source Player"""
    UNKNOWN_RESOURCE_200 = 200
    """Unknown: Amount of Source Player"""
    UNKNOWN_RESOURCE_201 = 201
    """Unknown: Amount of Source Player"""
    UNKNOWN_RESOURCE_202 = 202
    """Unknown: Amount of Source Player"""
    UNKNOWN_RESOURCE_203 = 203
    """Unknown: Amount of Source Player"""
    UNKNOWN_RESOURCE_204 = 204
    """Unknown: Amount of Source Player"""
    FEITORIA_FOOD_PRODUCTIVITY = 205
    """Feitoria Food Production Multiplier for the Source Player"""
    FEITORIA_WOOD_PRODUCTIVITY = 206
    """Feitoria Wood Production Multiplier for the Source Player"""
    FEITORIA_STONE_PRODUCTIVITY = 207
    """Feitoria Stone Production Multiplier for the Source Player"""
    FEITORIA_GOLD_PRODUCTIVITY = 208
    """Feitoria Gold Production Multiplier for the Source Player"""
    REVEAL_ENEMY_TOWN_CENTRE = 209
    """
    Boolean: Reveal Enemy Town Centre Location for the Source Player:

    - 0: Generic
    - 5: Vietnamese
    """
    REVEAL_RELICS = 210
    """
    Boolean: Reveal Relics On Map Amount of the Source Player:

    - -1: Generic
    - 42: Burmese
    """
    ELEVATION_BONUS_HIGHER = 211
    """
    High Elevation Damage Bonus Fraction Amount of the Source Player:

    - 0.25: Generic
    - 0.5: Tatars
    """
    ELEVATION_BONUS_LOWER = 212
    """
    Low Elevation Damage Bonus Fraction Amount of the Source Player:

    - -0.25: Generic
    """
    RAIDING_PRODUCTIVITY = 213
    """Keshik Gold Generation Multiplier Percent for the Source Player"""
    MERCENARY_KIPCHAK_COUNT = 214
    """Total Number of Merc Kipchak Creatable by the Source Player"""
    MERCENARY_KIPCHAK_LIMIT = 215
    """Number of Merc Kipchak Created by the Source Player"""
    SHEPHERD_PRODUCTIVITY = 216
    """Longer Lasting Sheep Percent of the Source Player"""
    TRIGGER_SHARED_LOS = 217
    """
    Boolean: Reveal Ally for the Source Player:

    - 0: No Allied Vision
    - 1: Allied Vision
    """
    UNKNOWN_RESOURCE_218 = 218
    """Unknown: Amount of the Source Player"""
    UNKNOWN_RESOURCE_219 = 219
    """Unknown: Amount of the Source Player"""
    UNKNOWN_RESOURCE_220 = 220
    """Unknown: Amount of the Source Player"""
    FOOD_TRICKLE_FROM_MONUMENT = 221
    """Give 0.7925*value Food per Second if a Monument is Owned by the Source Player"""
    WOOD_TRICKLE_FROM_MONUMENT = 222
    """Give 0.7925*value Wood per Second if a Monument is Owned by the Source Player"""
    STONE_TRICKLE_FROM_MONUMENT = 223
    """Give 0.7925*value Stone per Second if a Monument is Owned by the Source Player"""
    GOLD_TRICKLE_FROM_MONUMENT = 224
    """Give 0.7925*value Gold per Second if a Monument is Owned by the Source Player"""
    UNKNOWN_RESOURCE_225 = 225
    """Unknown: Amount of the Source Player"""
    VILLAGERS_KILLED_BY_GAIA = 226
    """Villagers Lost to Gaia by the Source Player"""
    VILLAGERS_KILLED_BY_ANIMALS_INCLUDED_IN_GAIA = 227
    """Villagers Lost to Wild Animals by the Source Player"""
    VILLAGERS_KILLED_BY_AI_PLAYER = 228
    """Villagers Lost to Ais by the Source Player"""
    VILLAGERS_KILLED_BY_HUMAN_PLAYER = 229
    """Villagers Lost to Humans by the Source Player"""
    FOOD_TRICKLE = 230
    """Food Given per Minute to the Source Player"""
    WOOD_TRICKLE = 231
    """Wood Given per Minute to the Source Player"""
    STONE_TRICKLE = 232
    """Stone Given per Minute to the Source Player"""
    GOLD_TRICKLE = 233
    """Gold Given per Minute to the Source Player"""
