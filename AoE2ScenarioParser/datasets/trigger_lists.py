from __future__ import annotations
from enum import IntEnum


class DiplomacyState(IntEnum):
    """
    This enum class provides the integer values used to reference the diplomacy states in the game. Used in the 'Change
    Diplomacy' effect and the 'Diplomacy State' condition

    **Examples**

    >>> DiplomacyState.ALLY
    >>> 0
    """
    ALLY = 0
    NEUTRAL = 1
    ENEMY = 3


class Operation(IntEnum):
    """
    This enum class provides the integer values used to reference the operations in the game. Used in a lot of effects
    like 'Modify Attribute' to control whether an attribute is set, added to, multiplied or divided by a value.

    **Examples**

    >>> Operation.MULTIPLY
    >>> 4
    """
    SET = 1
    ADD = 2
    SUBTRACT = 3
    MULTIPLY = 4
    DIVIDE = 5


class AttackStance(IntEnum):
    """
    This enum class provides the integer values used to reference the different unit stances in the game. Used in the
    'Change Object Stance' effect

    **Examples**

    >>> AttackStance.AGGRESSIVE_STANCE
    >>> 0
    """
    AGGRESSIVE_STANCE = 0
    DEFENSIVE_STANCE = 1
    STAND_GROUND = 2
    NO_ATTACK_STANCE = 3


class UnitAIAction(IntEnum):
    """
    This enum class provides the integer values used to reference the unit AI actions in the game. Used in the 'Object
    Has Action' condition.

    **Examples**

    >>> UnitAIAction.ATTACK
    >>> 1
    """
    ANY = 0
    """Fires if the unit has any action"""
    ATTACK = 1
    """Fires when the unit is attacking any unit"""
    BUILD = 3
    """Unknown"""
    CONVERT = 5
    """Fires when a monk or missionary is converting any unit"""
    DEFEND = 2
    """Unknown"""
    ENTER = 18
    """Unknown"""
    EVADE = 17
    """Unknown"""
    EXPLORE = 6
    """Unknown"""
    FOLLOW = 13
    """Fires when a unit is following any unit"""
    GATHER = 10
    """Fires when a villager or fishing ship is gathering resources"""
    HEAL = 4
    """Fires when a monk or missionary is healing another unit"""
    HUNT = 14
    """
    Fires when a hunter is gathering from a corpse of a hunted animal. Does **NOT** fire when the hunter is chasing the
    animal
    """
    IDLE = 24
    """Fires when a unit is standing still"""
    MOVE = 11
    """Fires when a unit is moving"""
    PATROL = 12
    """Fires when a unit is patrolling"""
    RELIC = 23
    """Unknown"""
    REPAIR = 19
    """Fires when a villager is repairing any other unit"""
    RESEARCH = 21
    """Unknown"""
    RETREAT = 9
    """Unknown"""
    RUNAWAY = 8
    """Unknown"""
    STOP = 7
    """Unknown"""
    TRADE = 16
    """Fires when a trade cart is returning to any of its own player's markets"""
    TRAIN = 20
    """Unknown"""
    TRANSPORT = 15
    """Unknown"""
    UNLOAD = 22
    """Fires when a transport ship is tasked to unload objects. Note that the transport gets stuck in this state!"""


class ButtonLocation(IntEnum):
    """
    This enum class provides the integer values used to reference the button locations in the game. These button
    locations are what determines where a unit's train button or a research's research button appears in a building's
    UI

    **Examples**

    >>> ButtonLocation.r2c2
    >>> 7
    """
    r1c1 = 1
    r1c2 = 2
    r1c3 = 3
    r1c4 = 4
    r1c5 = 5
    r2c1 = 6
    r2c2 = 7
    r2c3 = 8
    r2c4 = 9
    r2c5 = 10
    r3c1 = 11
    r3c2 = 12
    r3c3 = 13
    r3c4 = 14

    # r3c5 = 15  # Doesn't actually work in-game. Probably to make space for the arrow key.

    @classmethod
    def row_col(cls, row: int, col: int) -> int:
        """
        Get the button location ID of the row, column specified

        Args:
            row: The number of the row starting from the top (1-5)
            col: The number of the column starting from the left (1-3)

        Returns:
            The button location ID of the (row, column) location specified
        """
        return cls((row - 1) * 5 + col)


class PanelLocation(IntEnum):
    """
    This enum class provides the integer values used to reference the panel positons in the game. Used in the 'Display
    Information' effect.

    **Examples**

    >>> PanelLocation.TOP
    >>> 0
    """
    TOP = 0
    """Panel at the top of the screen. ~13% from the top"""
    BETWEEN = 1
    """Panel between the top and the center of the screen. ~33% from the top"""
    CENTER = 2
    """Panel close to the center of the screen. ~45% from the top"""


class TimeUnit(IntEnum):
    """
    This enum class provides the integer values used to reference the unit of time used in an effect. Used in the
    'Display Timer' effect.

    **Examples**

    >>> TimeUnit.YEARS
    >>> 1
    """
    YEARS = 2
    """In-Game years. A year is 5 seconds in-game time."""
    MINUTES = 1
    """In-Game minutes."""
    SECONDS = 0
    """In-Game seconds."""


class VisibilityState(IntEnum):
    """
    This enum class provides the integer values used to reference visibility state of a player for another player in the
    game. Used in the 'Set Visibility State' effect.

    **Examples**

    >>> VisibilityState.EXPLORED
    >>> 1
    """
    VISIBLE = 0
    EXPLORED = 1
    INVISIBLE = 2


class DifficultyLevel(IntEnum):
    """
    This enum class provides the integer values used to reference difficulty level of the game. Used in the 'Difficulty
    Level' condition.

    **Examples**

    >>> DifficultyLevel.HARD
    >>> 0
    """
    EASIEST = 4
    STANDARD = 3
    MODERATE = 2
    HARD = 1
    HARDEST = 0
    # EXTREME = 5  # ???


class TechnologyState(IntEnum):
    """
    This enum class provides the integer values used to reference technology state of a technology in the game. Used in
    the 'Technology State' condition.

    **Examples**

    >>> TechnologyState.NOT_READY
    >>> 0
    """
    DISABLED = -1
    NOT_READY = 0
    """A tech that is not available to be researched (Bombard Tower is not ready before chemistry is researched)"""
    READY = 1
    """A tech that is available to be researched (Bombard Tower is ready after chemistry is researched)"""
    RESEARCHING = 2
    """A tech that is currently being researched"""
    DONE = 3
    """A Tech that has already been researched"""
    QUEUED = 4
    """A tech that is waiting in queue to be researched"""


class Comparison(IntEnum):
    """
    This enum class provides the integer values used to reference the comparisons in the game. Used in a lot of
    conditions like 'Accumulate Attribute' to perform logical operations on the attribute values

    **Examples**

    >>> Comparison.EQUAL
    >>> 4
    """
    EQUAL = 0
    LESS = 1
    LARGER = 2
    LESS_OR_EQUAL = 3
    LARGER_OR_EQUAL = 4


class ObjectAttribute(IntEnum):
    """
    This enum class provides the integer values used to reference all the different object attributes in the game. Used
    in the 'Modify Attribute' effect to control which attribute of an object is modified.

    **Examples**

    >>> ObjectAttribute.LINE_OF_SIGHT
    >>> 1
    """
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
    GRAPHICS_ANGLE = 17
    TERRAIN_DEFENSE_BONUS = 18
    ENABLE_SMART_PROJECTILES = 19
    MINIMUM_RANGE = 20
    AMOUNT_OF_1ST_RESOURCES = 21
    BLAST_WIDTH = 22
    SEARCH_RADIUS = 23
    BONUS_DAMAGE_RESIST = 24
    ICON_ID = 25
    HERO_STATUS = 40
    FRAME_DELAY = 41
    TRAIN_LOCATION = 42
    TRAIN_BUTTON = 43
    BLAST_ATTACK_LEVEL = 44
    BLAST_DEFENSE_LEVEL = 45
    SHOWN_ATTACK = 46
    SHOWN_RANGE = 47
    SHOWN_MELEE_ARMOR = 48
    SHOWN_PIERCE_ARMOR = 49
    OBJECT_NAME_ID = 50
    SHORT_DESCRIPTION_ID = 51
    TERRAIN_RESTRICTION_ID = 53
    DEAD_UNIT_ID = 57
    HOTKEY_ID = 58
    RESOURCE_COSTS = 100
    TRAIN_TIME = 101
    TOTAL_MISSILES = 102
    FOOD_COSTS = 103
    WOOD_COSTS = 104
    GOLD_COSTS = 105
    STONE_COSTS = 106
    MAX_TOTAL_MISSILES = 107
    GARRISON_HEAL_RATE = 108
    """Hidden in the editor, but does work! Do not open effect in editor, will cause it to reset"""
    REGENERATION_RATE = 109


class Attribute(IntEnum):
    """
    This enum class provides the integer values used to reference all the player resources in the game. Used in effects
    and conditions like 'Accumulate Attribute' and 'Modify Resource'

    **Examples**

    >>> Attribute.FOOD
    >>> 0
    """
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
    RELIC_FOOD_PRODUCTION_RATE = 225
    """Relic Food Production Rate of the Source Player"""
    VILLAGERS_KILLED_BY_GAIA = 226
    """Villagers Lost to Gaia by the Source Player"""
    VILLAGERS_KILLED_BY_ANIMALS = 227
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
    SPAWN_LIMIT = 234
    """Number of buildings from which a tech with command type 7 (spawn) will spawn units"""
    FLEMISH_MILITIA_POPULATION = 235
    """Number of Flemish Militia of the Source Player"""
    FARMING_GOLD_TRICKLE = 236
    """
    Farming Gold Generation Rate*0.01 of the Source Player:

    - Burgundian Vineyards set this to 1.5 => 0.015g/s for One Farmer Continuously Farming.
    - in Practise, Its Closer to 0.01g/s Factoring in Walking Times
    """


class ObjectType(IntEnum):
    """
    This enum class provides the integer values used to reference the object types in the game. Used in a lot of effects
    and conditions, like 'Kill Object', 'Objects in Area'.

    **Examples**

    >>> ObjectType.OTHER
    >>> 1
    """
    OTHER = 1
    BUILDING = 2
    CIVILIAN = 3
    MILITARY = 4


class ObjectClass(IntEnum):
    """
    This enum class provides the integer values used to reference the object class in the game. Used in a lot of effects
    and conditions, like 'Kill Object', 'Objects in Area' under the name 'Object Group'.

    **Examples**

    >>> ObjectType.OTHER
    >>> 1
    """
    ARCHER = 0
    ARTIFACT = 1
    TRADE_BOAT = 2
    BUILDING = 3
    CIVILIAN = 4
    OCEAN_FISH = 5
    INFANTRY = 6
    BERRY_BUSH = 7
    STONE_MINE = 8
    PREY_ANIMAL = 9
    PREDATOR_ANIMAL = 10
    MISCELLANEOUS = 11
    CAVALRY = 12
    SIEGE_WEAPON = 13
    TERRAIN = 14
    TREE = 15
    TREE_STUMP = 16
    HEALER = 17
    MONK = 18
    TRADE_CART = 19
    TRANSPORT_BOAT = 20
    FISHING_BOAT = 21
    WARSHIP = 22
    CONQUISTADOR = 23
    WAR_ELEPHANT = 24
    HERO = 25
    ELEPHANT_ARCHER = 26
    WALL = 27
    PHALANX = 28
    DOMESTIC_ANIMAL = 29
    FLAG = 30
    DEEP_SEA_FISH = 31
    GOLD_MINE = 32
    SHORE_FISH = 33
    CLIFF = 34
    PETARD = 35
    CAVALRY_ARCHER = 36
    DOPPELGANGER = 37
    BIRD = 38
    GATE = 39
    SALVAGE_PILE = 40
    RESOURCE_PILE = 41
    RELIC = 42
    MONKWITH_RELIC = 43
    HAND_CANNONEER = 44
    TWO_HANDED_SWORDSMAN = 45
    PIKEMAN = 46
    SCOUT = 47
    ORE_MINE = 48
    FARM = 49
    SPEARMAN = 50
    PACKED_UNIT = 51
    TOWER = 52
    BOARDING_BOAT = 53
    UNPACKED_SIEGE_UNIT = 54
    BALLISTA = 55
    RAIDER = 56
    CAVALRY_RAIDER = 57
    LIVESTOCK = 58
    KING = 59
    MISC_BUILDING = 60
    CONTROLLED_ANIMAL = 61


class TerrainRestrictions(IntEnum):
    """
    This enum class provides the integer values used to reference the terrain restriction IDs in the game. Used in the
    'Modify Attribute' effects

    **Examples**

    >>> TerrainRestrictions.LAND_AND_SHALLOWS
    >>> 1
    """
    ALL = 0
    """Used by terrain eyecandy and sundries"""
    LAND_AND_SHALLOWS = 1
    """Used by part of animals"""
    BEACH = 2
    WATER_SMALL_TRAIL = 3
    """Used by most ships and sea gate"""
    LAND = 4
    """Used by most land buildings"""
    NOTHING = 5
    WATER_NO_TRAIL = 6
    """Used by docks"""
    ALL_EXCEPT_WATER = 7
    """Used by land troops"""
    LAND_EXCEPT_FARM = 8
    """Used by land resources"""
    NOTHING_2 = 9
    LAND_AND_BEACH = 10
    """Used by land walls and gates"""
    LAND_EXCEPT_FARM_2 = 11
    """Used by trees and mountains"""
    ALL_EXCEPT_WATER_BRIDGE_CANNON = 12
    WATER_MEDIUM_TRAIL = 13
    """Used by big fish and fishing ship"""
    ALL_EXCEPT_WATER_BRIDGE_ARROW = 14
    WATER_LARGE_TRAIL = 15
    """Only used by transport ship"""
    GRASS_AND_BEACH = 16
    WATER_AND_BRIDGE_EXCEPT_BEACH = 17
    ALL_EXCEPT_WATER_BRIDGE_SPEAR = 18
    ONLY_WATER_AND_ICE = 19
    """Used by fish"""
    ALL_EXCEPT_WATER_WHEEL = 20
    """Used by units with wheels, such as Rams and Scorpions"""
    SHALLOW_WATER = 21
    ALL_DART = 22
    ALL_ARROW_FIRE = 23
    """Only used by Arrows with fire (After chemistry)"""
    ALL_CANNON_FIRE = 24
    """Only used by Cannon balls (After chemistry)"""
    ALL_SPEAR_FIRE = 25
    """Only used by Spears with fire (After chemistry)"""
    ALL_DART_FIRE = 26
    """Only used by Darts with fire (After chemistry)"""
    ALL_LASER = 27
    """Only used by Projectile Laser with id 1595"""
    ALL_EXCEPT_WATER_CAVALRY = 28
    """Such as Cavalry Archer, Cavalry, Conquistador, Missionary and Flaming Camel"""
    ALL_EXCEPT_WATER_PACKET_TREBUCHET = 29
    """All types of Trebuchet(Packed)"""
    WATER_SMALLEST_TRAIL = 30
    """Used by medium ships, such as Trade Cog, Fire Galley and Longboat"""

class HeroStatusFlag(IntEnum):
    """
    This enum class provides the integer values for the different hero status flags that can be used in the 'Modify
    Attribute' effect with the 'Hero Status' attribute.

    **Methods**

    >>> HeroStatusFlag.combine()
    >>> HeroStatusFlag.split_flags()

    **Examples**

    >>> ObjectType.OTHER
    >>> 1
    """
    @staticmethod
    def combine(
            full_hero_status: bool = False,
            cannot_be_converted: bool = False,
            hero_regeneration: bool = False,
            defensive_stance_by_default: bool = False,
            protected_formation: bool = False,
            delete_confirmation: bool = False,
            hero_glow: bool = False,
            invert_all_flags: bool = False
    ) -> int:
        """
        This method combines the given hero status flags into an integer value

        Args:
            full_hero_status: Enabling this for a unit grants all the flags mentioned below except invert_all_flags
            cannot_be_converted: Enabling this for a unit makes it un-convertable
            hero_regeneration: Enabling this for a unit grants 0.5 HP/s heal rate to the unit
            defensive_stance_by_default: Enabling this for a unit makes it be on defensive stance by default
            protected_formation: Enabling this for a unit makes it be in protected formation by default
            delete_confirmation: Enabling this for a unit will bring up a delete confirmation for the unit when trying
            to delete it IF the player has them enabled
            hero_glow: Enabling this for a unit grants it the golden hero glow effect
            invert_all_flags: Enabling this for a unit will invert all the above flags except full_hero_status

        Returns:
            An integer combining all the different hero status flags into one value
        """
        total = 1 if full_hero_status else 0
        total += 2 if cannot_be_converted else 0
        total += 4 if hero_regeneration else 0
        total += 8 if defensive_stance_by_default else 0
        total += 16 if protected_formation else 0
        total += 32 if delete_confirmation else 0
        total += 64 if hero_glow else 0
        total += 128 if invert_all_flags else 0
        return total

    @staticmethod
    def split_flags(value: int) -> dict[HeroStatusFlag, bool]:
        """

        Split the Hero Status flags into boolean variables related to their effects

        Args:
            value: An integer value representing all the hero status flags set

        Returns:
            A dict with all the flags values as keys and a bool as their value
        """
        flags = {}
        for flag in HeroStatusFlag:
            flags[flag] = bool(flag & value)

        return flags


    FULL_HERO_STATUS = 1
    CANNOT_BE_CONVERTED = 2
    HERO_REGENERATION = 4
    DEFENSIVE_STANCE_BY_DEFAULT = 8
    PROTECTED_FORMATION = 16
    DELETE_CONFIRMATION = 32
    HERO_GLOW = 64
    INVERT_FLAGS = 128


class BlastLevel(IntEnum):
    """
    This enum class provides the integer values used to reference the blast level values used in the game. Used in the
    'Modify Attribute' effect with the 'Blast Attack/Defense Level' attributes

    **Examples**

    >>> BlastLevel.TREES
    >>> 1
    """
    RESOURCES = 0
    TREES = 1
    NEARBY_UNITS = 2
    TARGET_ONLY = 3
    FIXED_INFANTRY_TRAMPLE = 6
    """
    If an infantry unit is given this along with non 0 blast radius, it does a fixed 5 HP damage ignoring armour to all
    adjacent units
    """


class DamageClass(IntEnum):
    """
    This enum class provides the integer values that represent the damage classes in the game. Used in the 'Chnage
    Object Attack/Armour' and 'Modify Attribute' with the 'Attack/Armour' attibutes

    **Examples**

    >>> DamageClass.INFANTRY
    >>> 1
    """
    WONDER = 0
    """Since HD. Only wonders has this armour class. However there is no unit that has this attack class."""
    INFANTRY = 1
    TURTLE_SHIPS = 2
    BASE_PIERCE = 3
    BASE_MELEE = 4
    WAR_ELEPHANTS = 5
    UNUSED_ID6 = 6
    UNUSED_ID7 = 7
    CAVALRY = 8
    UNUSED_ID9 = 9
    UNUSED_ID10 = 10
    ALL_BUILDINGS_EXCEPT_PORT = 11
    """Port is the building with id 446"""
    UNUSED_ID12 = 12
    STONE_DEFENSE = 13
    PREDATOR_ANIMALS_FE = 14
    """Wolf, Bear, Jaguar, Tiger, etc. have this armour class"""
    ARCHERS = 15
    BATTLE_SHIPS_AND_SABOTEUR = 16
    """Camels also had this armour class before AK"""
    RAMS = 17
    TREES = 18
    UNIQUE_UNITS = 19
    SIEGE_WEAPONS = 20
    STANDARD_BUILDINGS = 21
    WALLS_AND_GATES = 22
    GUNPOWDER_UNITS = 23
    BOARS = 24
    MONKS = 25
    CASTLE = 26
    SPEARMEN = 27
    CAVALRY_ARCHERS = 28
    EAGLE_WARRIORS = 29
    CAMELS = 30
    """Camels use this armour class since and after AK"""
    LEITIS = 31
    CONDOTTIERO = 32
    ORGAN_GUN_BULLET = 33
    """Only Projectile Gunpowder (Secondary) with id 1119 has this damage class. No unit has this armour class."""
    FISHING_SHIP = 34
    MAMELUKES = 35
    HEROES_AND_KING = 36
    UNUSED_ID37 = 37
    UNUSED_ID38 = 38
    UNUSED_ID39 = 39
    UNUSED_ID40 = 40
    UNUSED_ID41 = 41
    UNUSED_ID42 = 42
    UNUSED_ID43 = 43
    UNUSED_ID44 = 44
    UNUSED_ID45 = 45
    UNUSED_ID46 = 46
    UNUSED_ID47 = 47
    UNUSED_ID48 = 48
    UNUSED_ID49 = 49


class Hotkey(IntEnum):
    """
    This enum class provides the integer values used to reference the blast level values used in the game. Used in the
    'Modify Attribute' effect with the 'HotKey ID' attribute

    Many hotkeys are missing from this file (Like arrow up). The reason for this is explained in the UGC guide:
    https://divy1211.github.io/AoE2DE_UGC_Guide/general/hotkeys/hotkeys/

    **Examples**

    >>> Hotkey.SPACE
    >>> 10101
    """
    SPACE = 10101
    PAGE_UP = 15000
    LEFT_ARROW = 2312
    RIGHT_ARROW = 19707
    DOWN_ARROW = 19731
    INSERT = 9025
    DELETE = 19602
    ZERO = 99
    ONE = 98
    TWO = 10360
    THREE = 9786
    FOUR = 10362
    FIVE = 9785
    SIX = 213
    SEVEN = 8828
    EIGHT = 9448
    NINE = 9783
    A = 1001
    B = 1005
    C = 1201
    D = 1151
    E = 1007
    F = 4137
    G = 2012
    H = 2407
    I = 1212
    J = 1222
    K = 4141
    L = 1101
    M = 1006
    N = 3001
    O = 214
    P = 1210
    Q = 4169
    R = 1200
    S = 1102
    T = 2016
    U = 1205
    V = 1150
    W = 1008
    X = 1002
    Y = 2008
    Z = 4174
    APPLICATION = 19704
    NUM_ZERO = 19721
    NUM_ONE = 4563
    NUM_FOUR = 19499
    NUM_FIVE = 5558
    NUM_SEVEN = 10069
    NUM_EIGHT = 1011
    NUM_DELETE = 20123
    F3 = 9798
    F4 = 22019
    F7 = 9840
    F8 = 1152
    F15 = 10661


class ColorMood(IntEnum):
    """
    This enum class provides the integer values used to reference the colour mood values used in the game. Used in the
    'Change Colour Mood' effect

    **Examples**

    >>> ColorMood.AUTUMN
    >>> 1
    """
    DEFAULT = 0
    AUTUMN = 1
    WINTER = 2
    JUNGLE = 3
    DESERT = 4


class ObjectState(IntEnum):
    """
    This enum class provides the integer values used to reference the object state values used in the game. Used in the
    'Object in Area' condition

    **Examples**

    >>> BlastLevel.TREES
    >>> 1
    """
    FOUNDATION = 0
    ALMOST_ALIVE = 1
    ALIVE = 2
    RESOURCE = 3
    DYING = 4
    DEAD = 5
    UNDEAD = 6
    REMOVE = 7
