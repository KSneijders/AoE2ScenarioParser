from __future__ import annotations

import math
from enum import IntEnum, IntFlag


class _TriggerList:
    def attribute_presentation(self) -> str:
        raise NotImplemented("_TriggerList.attribute_presentation has to be implemented")


class _TriggerListIntEnums(_TriggerList, IntEnum):
    def attribute_presentation(self) -> str:
        """
        Get the string representation of an enum entry. Uses `.name` when not overridden.
        Returns:
            The string representation of an enum entry.
        """
        return super().name


class _TriggerListIntFlags(_TriggerList, IntFlag):
    def attribute_presentation(self) -> str:
        """
        Get the string representation of an enum entry. Uses `.name` when not overridden.
        Returns:
            The string representation of an enum entry.
        """
        return super().name


class DiplomacyState(_TriggerListIntEnums):
    """
    This enum class provides the integer values used to reference the diplomacy states in the game. Used in the 'Change
    Diplomacy' effect and the 'Diplomacy State' condition

    **Examples**

    >>> DiplomacyState.ALLY
    <DiplomacyState.ALLY: 0>
    """
    ALLY = 0
    NEUTRAL = 1
    ENEMY = 3


class Operation(_TriggerListIntEnums):
    """
    This enum class provides the integer values used to reference the operations in the game. Used in a lot of effects
    like 'Modify Attribute' to control whether an attribute is set, added to, multiplied or divided by a value.

    **Examples**

    >>> Operation.MULTIPLY
    <Operation.MULTIPLY: 4>
    """
    SET = 1
    ADD = 2
    SUBTRACT = 3
    MULTIPLY = 4
    DIVIDE = 5


class AttackStance(_TriggerListIntEnums):
    """
    This enum class provides the integer values used to reference the different unit stances in the game. Used in the
    'Change Object Stance' effect

    **Examples**

    >>> AttackStance.AGGRESSIVE_STANCE
    <AttackStance.AGGRESSIVE_STANCE: 0>
    """
    AGGRESSIVE_STANCE = 0
    DEFENSIVE_STANCE = 1
    STAND_GROUND = 2
    NO_ATTACK_STANCE = 3


class UnitAIAction(_TriggerListIntEnums):
    """
    This enum class provides the integer values used to reference the unit AI actions in the game. Used in the 'Object
    Has Action' condition.

    **Examples**

    >>> UnitAIAction.ATTACK
    <UnitAIAction.ATTACK: 1>
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


class ButtonLocation(_TriggerListIntEnums):
    """
    This enum class provides the integer values used to reference the button locations in the game. These button
    locations are what determines where a unit's train button or a research's research button appears in a building's
    UI

    **Examples**

    >>> ButtonLocation.r2c2
    <ButtonLocation.r2c2: 7>
    >>> ButtonLocation.r3c1.attribute_presentation()
    'row_3_col_1'
    """
    _r1c1 = 0
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

    def attribute_presentation(self):
        val = self.value or 1  # Change VAL 0 to 1
        row = math.ceil(val / 5)
        col = val - (row - 1) * 5
        return f"row_{row}_col_{col}"

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


class PanelLocation(_TriggerListIntEnums):
    """
    This enum class provides the integer values used to reference the panel positons in the game. Used in the 'Display
    Information' effect.

    **Examples**

    >>> PanelLocation.TOP
    <PanelLocation.TOP: 0>
    """
    TOP = 0
    """Panel at the top of the screen. ~13% from the top"""
    BETWEEN = 1
    """Panel between the top and the center of the screen. ~33% from the top"""
    CENTER = 2
    """Panel close to the center of the screen. ~45% from the top"""


class TimeUnit(_TriggerListIntEnums):
    """
    This enum class provides the integer values used to reference the unit of time used in an effect. Used in the
    'Display Timer' effect.

    **Examples**

    >>> TimeUnit.YEARS
    <TimeUnit.YEARS: 0>
    """
    YEARS = 0
    """In-Game years. A year is 5 seconds in-game time."""
    MINUTES = 1
    """In-Game minutes."""
    SECONDS = 2
    """In-Game seconds."""


class VisibilityState(_TriggerListIntEnums):
    """
    This enum class provides the integer values used to reference visibility state of a player for another player in the
    game. Used in the 'Set Visibility State' effect.

    **Examples**

    >>> VisibilityState.EXPLORED
    <VisibilityState.EXPLORED: 1>
    """
    VISIBLE = 0
    EXPLORED = 1
    INVISIBLE = 2


class DifficultyLevel(_TriggerListIntEnums):
    """
    This enum class provides the integer values used to reference difficulty level of the game. Used in the 'Difficulty
    Level' condition.

    **Examples**

    >>> DifficultyLevel.HARD
    <DifficultyLevel.HARD: 1>
    """
    EASIEST = 4
    STANDARD = 3
    MODERATE = 2
    HARD = 1
    HARDEST = 0
    # EXTREME = 5  # ???


class TechnologyState(_TriggerListIntEnums):
    """
    This enum class provides the integer values used to reference technology state of a technology in the game. Used in
    the 'Technology State' condition.

    **Examples**

    >>> TechnologyState.NOT_READY
    <TechnologyState.NOT_READY: 0>
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


class Comparison(_TriggerListIntEnums):
    """
    This enum class provides the integer values used to reference the comparisons in the game. Used in a lot of
    conditions like 'Accumulate Attribute' to perform logical operations on the attribute values

    **Examples**

    >>> Comparison.EQUAL
    <Comparison.EQUAL: 0>
    """
    EQUAL = 0
    LESS = 1
    LARGER = 2
    LESS_OR_EQUAL = 3
    LARGER_OR_EQUAL = 4


class ObjectAttribute(_TriggerListIntEnums):
    """
    This enum class provides the integer values used to reference all the different object attributes in the game. Used
    in the 'Modify Attribute' effect to control which attribute of an object is modified.

    **Examples**

    >>> ObjectAttribute.LINE_OF_SIGHT
    <ObjectAttribute.LINE_OF_SIGHT: 1>
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
    BUILDING_ICON_OVERRIDE = 17
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


class Attribute(_TriggerListIntEnums):
    """
    This enum class provides the integer values used to reference all the player resources in the game. Used in effects
    and conditions like 'Accumulate Attribute' and 'Modify Resource'

    **Examples**

    >>> Attribute.FOOD
    <Attribute.FOOD: 0>
    """

    FOOD = 0
    """
    Food amount of the source player
    """
    WOOD = 1
    """
    Wood amount of the source player
    """
    STONE = 2
    """
    Stone amount of the source player
    """
    GOLD = 3
    """
    Gold amount of the source player
    """
    POPULATION_CAP = 4
    """
    Current max pop of the source player
    """
    CONVERSION_RANGE = 5
    """
    Unknown amount of the source player
    """
    CURRENT_AGE = 6
    """
    Age name and icon at the top of the screen of the source player

    - Default Values:

        - 0:  Dark Age

        - 1:  Feudal Age

        - 2:  Castle Age

        - 3:  Imperial Age

    - Additional Information: Setting this to an amount higher than 3 cycles the icon but keeps the age at imperial
    """
    RELICS = 7
    """
    Number of relics held by the source player
    """
    TRADE_BONUS = 8
    """
    Unused amount of the source player
    """
    TRADE_GOODS = 9
    """
    Unused amount of the source player
    """
    TRADE_PRODUCTION = 10
    """
    Unused amount of the source player
    """
    CURRENT_POPULATION = 11
    """
    Current pop of the source player
    """
    CORPSE_DECAY_TIME = 12
    """
    Time taken by corpses to decay for the source player

    - Additional Information: Doesn't seem to do anything when changed
    """
    REMARKABLE_DISCOVERY = 13
    """
    Unknown amount of the source player
    """
    MONUMENTS_CAPTURED = 14
    """
    Number of monuments owned by the source player
    """
    MEAT_STORAGE = 15
    """
    Unknown amount of the source player
    """
    BERRY_STORAGE = 16
    """
    Unknown amount of the source player
    """
    FISH_STORAGE = 17
    """
    Unknown amount of the source player
    """
    UNUSED_RESOURCE_018 = 18
    """
    Unused amount of the source player
    """
    TOTAL_UNITS_OWNED = 19
    """
    Total units owned by the source player
    """
    KILLS = 20
    """
    Total units killed of the source player
    """
    RESEARCH_COUNT = 21
    """
    Research count of the source player
    """
    EXPLORATION = 22
    """
    Percent map explored by the source player
    """
    CASTLE_AGE_TECH_ID = 23
    """
    Always 102 

    - Additional Information: Nothing happens when you change this
    """
    IMPERIAL_AGE_TECH_ID = 24
    """
    Always 103 

    - Additional Information: Nothing happens when you change this
    """
    FEUDAL_AGE_TECH_ID = 25
    """
    Always 101 

    - Additional Information: Nothing happens when you change this
    """
    ATTACK_SOUND_EFFECT_ID = 26
    """
    Always 0 

    - Additional Information: Nothing happens when you change this
    """
    ENABLE_MONK_CONVERSION = 27
    """
    Boolean: allow enemy monk conversions by the source player

    - Default Values:

        - 0:  Don't Allow

        - $\geq$ 1:  Allow

    - Additional Information: Set to 1 when atonement is researched
    """
    ENABLE_BUILDING_CONVERSIONS = 28
    """
    Boolean: allow enemy building conversions by the source player.

    - Default Values:

        - 0:  Don't Allow

        - 1:  Allow

        - $\geq$2:  Monks can convert buildings from range

    - Additional Information: Set to 1 when redemption is researched
    """
    UNUSED_RESOURCE_029 = 29
    """
    Unused amount of the source player
    """
    BUILDING_LIMIT = 30
    """
    Unused amount of the source player
    """
    FOOD_LIMIT = 31
    """
    Unused amount of the source player
    """
    BONUS_POPULATION_CAP = 32
    """
    Additional max pop space of the source player

    - Additional Information: 10 for goths
    """
    FOOD_MAINTENANCE = 33
    """
    Unknown amount of the source player
    """
    FAITH = 34
    """
    Boolean: faith researched by the source player

    - Additional Information: Set to 1 when faith is researched, ONLY  a boolean value, does not force faith's effects if manually set to 1
    """
    FAITH_RECHARGE_RATE = 35
    """
    Monk faith recovery rate of the source player
    """
    FARM_FOOD = 36
    """
    Max farm food of the source player
    """
    CIVILIAN_POPULATION = 37
    """
    Civilian pop of the source player
    """
    UNUSED_RESOURCE_038 = 38
    """
    Unused amount of the source player
    """
    ALL_TECHS_ACHIEVED = 39
    """
    Boolean: researched all enabled techs by the source player

    - Default Values:

        - 0:  when all techs not researched

        - 1:  when all techs are researched
    """
    MILITARY_POPULATION = 40
    """
    Military pop of the source player
    """
    CONVERSIONS = 41
    """
    Number of units converted by the source player
    """
    WONDER = 42
    """
    Number of standing wonders of the source player
    """
    RAZINGS = 43
    """
    Number of buildings destroyed by the source player
    """
    KILL_RATIO = 44
    """
    Ceil of kills/deaths of the source player
    """
    PLAYER_KILLED = 45
    """
    Boolean: survival to finish of the source player

    - Default Values:

        - 0:  No

        - 1:  Yes
    """
    TRIBUTE_INEFFICIENCY = 46
    """
    Tribute tax fraction imposed on the source player
    """
    GOLD_MINING_PRODUCTIVITY = 47
    """
    Amount of gold mined multiplier of the source player

    - Default Values:

        - 1:  Generic

        - 1.15:  Mayans

    - Additional Information: Since this works by multiplying the amount of resources gathered by a villager, it has a side effect of increasing the gather rate as well. In the case of Mayans, This is compensated for by reducing villager work rate by 15%
    """
    TOWN_CENTER_UNAVAILABLE = 48
    """
    Boolean: allow building tcs for the source player

    - Default Values:

        - 0:  No (Sudden Death)

        - 1:  Yes
    """
    GOLD_COUNTER = 49
    """
    Total gold collected by the source player
    """
    REVEAL_ALLY = 50
    """
    Boolean: show ally los for the source player

    - Default Values:

        - 0:  No Allied Vision

        - 1:  Allied Vision

    - Additional Information: Note - Once enabled, Allied vison cannot be undone
    """
    HOUSES = 51
    """
    Unused amount of the source player
    """
    MONASTERIES = 52
    """
    Number of monasteries of the source player
    """
    TRIBUTE_SENT = 53
    """
    Amount tributed by the source player
    """
    ALL_MONUMENTS_CAPTURED = 54
    """
    Boolean: all monuments captured by the source player
    """
    ALL_RELICS_CAPTURED = 55
    """
    Boolean: all relics captured by the source player
    """
    ORE = 56
    """
    SWGB ore amount of the source player
    """
    CAPTURED_UNIT = 57
    """
    Number of units kidnapped by the source player
    """
    DARK_AGE_TECH_ID = 58
    """
    Always 104 

    - Additional Information: Nothing happens when you change this
    """
    TRADE_GOOD_QUALITY = 59
    """
    Unused amount of the source player
    """
    TRADE_MARKET_LEVEL = 60
    """
    Unused amount of the source player
    """
    FORMATIONS = 61
    """
    Unused amount of the source player
    """
    BUILDING_HOUSE_RATE = 62
    """
    Unknown amount of the source player
    """
    GATHER_TAX_RATE = 63
    """
    Unknown amount of the source player
    """
    GATHER_ACCUMULATION = 64
    """
    Unknown amount of the source player
    """
    SALVAGE_DECAY_RATE = 65
    """
    Boat corpse decay rate of the source player

    - Additional Information: Changing this doesn't seem to do anything
    """
    ALLOW_FORMATIONS = 66
    """
    Unused amount of the source player
    """
    CAN_CONVERT = 67
    """
    Boolean: allow enemy object conversions amount of the source player

    - Default Values:

        - 0:  Don't allow even regular unit conversion

        - 1:  Allows regular unit conversion
    """
    HITPOINTS_KILLED = 68
    """
    Cumulative hp of all units killed by the source player
    """
    PLAYER1_KILLS = 69
    """
    Number of player 1 units killed by the source player
    """
    PLAYER2_KILLS = 70
    """
    Number of player 2 units killed by the source player
    """
    PLAYER3_KILLS = 71
    """
    Number of player 3 units killed by the source player
    """
    PLAYER4_KILLS = 72
    """
    Number of player 4 units killed by the source player
    """
    PLAYER5_KILLS = 73
    """
    Number of player 5 units killed by the source player
    """
    PLAYER6_KILLS = 74
    """
    Number of player 6 units killed by the source player
    """
    PLAYER7_KILLS = 75
    """
    Number of player 7 units killed by the source player
    """
    PLAYER8_KILLS = 76
    """
    Number of player 8 units killed by the source player
    """
    CONVERSION_RESISTANCE = 77
    """
    Coefficient of conversion resistance of the source player

    - Additional Information: Probability of conversion is divided by this value for ALL source player units, Teuton team bonus for conversion resistance works by increasing this.
    """
    TRADE_VIG_RATE = 78
    """
    Market exchange rate fraction for the source player

    - Default Values:

        - 0.3:  Generic rate

        - 0.15:  after guilds

        - 0.05:  for saracens
    """
    STONE_MINING_PRODUCTIVITY = 79
    """
    Amount of stone mined multiplier of the source player

    - Default Values:

        - 1:  Generic

        - 1.15:  Mayans

    - Additional Information: Since this works by multiplying the amount of resources gathered by a villager, it has a side effect of increasing the gather rate as well. In the case of Mayans, This is compensated for by reducing villager work rate by 15%
    """
    QUEUED_COUNT = 80
    """
    Amount of units in queue of the source player

    - Additional Information: Note that only the units waiting to be trained are considered in the queue so if an archery range has 3 archers being made, there is 1 archer that is being trained and 2 archers that are in queue
    """
    TRAINING_COUNT = 81
    """
    Amount of units being trained of the source player

    - Additional Information: Note that only the FIRST unit in each building is considered as being trained so if a town centre has 4 villagers being made, there is 1 archer that is being trained and 3 villagers that are in queue
    """
    START_WITH_PACKED_TOWN_CENTRE = 82
    """
    Boolean: started with PTWC of the source player

    - Additional Information: Setting this to 1 in an RMS allows for starting with PTWC. Manually changing this in the editor does nothing
    """
    BOARDING_RECHARGE_RATE = 83
    """
    ABGAL faith recharge rate amount of the source player

    - Additional Information: This is similar to monk's faith except for a special ship unit 536 called the ABGAL in the editor that can convert ships form 1 range away
    """
    STARTING_VILLAGERS = 84
    """
    Number of starting villagers of the source player

    - Default Values:

        - 3:  For generic civs

        - 4:  For Mayans

        - 6:  For Chinese

    - Additional Information: Only works for RMS, Changing this manually in the editor does nothing x2 on budapest, x3 on metropolis
    """
    RESEARCH_COST_MODIFIER = 85
    """
    Reduce tech cost to fraction for the source player
    """
    RESEARCH_TIME_MODIFIER = 86
    """
    Reduce tech research time to fraction for the source player
    """
    CONVERT_BOATS = 87
    """
    Boolean: allow monks to convert boats amount of the source player
    """
    FISH_TRAP_FOOD = 88
    """
    Max fishtrap food of the source player
    """
    HEAL_RATE_MODIFIER = 89
    """
    Monk healing rate of the source player
    """
    HEAL_RANGE = 90
    """
    Monk heal range of the source player
    """
    STARTING_FOOD = 91
    """
    Starting food amount of the source player

    - Additional Information: Only works for RMS. Changing this manually in the editor does nothing but its a way to check starting food amount
    """
    STARTING_WOOD = 92
    """
    Starting wood amount of the source player

    - Additional Information: Only works for RMS. Changing this manually in the editor does nothing but its a way to check starting wood amount
    """
    STARTING_STONE = 93
    """
    Starting stone amount of the source player

    - Additional Information: Only works for RMS. Changing this manually in the editor does nothing but its a way to check starting stone amount
    """
    STARTING_GOLD = 94
    """
    Starting gold amount of the source player

    - Additional Information: Only works for RMS. Changing this manually in the editor does nothing but its a way to check starting gold amount
    """
    ENABLE_PTWC_OR_KIDNAP_OR_LOOT = 95
    """
    Enable town centre packing for the source player

    - Default Values:

        - 0:  Normal

        - 1:  Enables Pack Button on TC but it is bugged, if you click it then TC goes berserk

        - $\geq$2:  No noticeable effect
    """
    BERSERKER_HEAL_TIMER = 96
    """
    Time difference between berserker heal rate for source player

    - Additional Information: This is divided by two every time berserkergang is researched
    """
    DOMINANT_SHEEP_CONTROL = 97
    """
    Boolean: force sheep conversion of the source player

    - Default Values:

        - 0:  Normal Sheep conversion behaviour

        - $\geq$1:  If another player does not also have this set to a non zero value, their sheep will force convert to source player

    - Additional Information: This is how the celt bonus of sheep not converting works
    """
    OBJECT_COST_SUMMATION = 98
    """
    Total cost of all units and buildings owned by the source player
    """
    RESEARCH_COST_SUMMATION = 99
    """
    Total cost of all researches researched by the source player
    """
    RELIC_INCOME_SUMMATION = 100
    """
    Total relic gold generated by the source player
    """
    TRADE_INCOME_SUMMATION = 101
    """
    Total trade gold generated by the source player
    """
    PLAYER1_TRIBUTE = 102
    """
    Amount of resources tributed to player 1 by the source player
    """
    PLAYER2_TRIBUTE = 103
    """
    Amount of resources tributed to player 2 by the source player
    """
    PLAYER3_TRIBUTE = 104
    """
    Amount of resources tributed to player 3 by the source player
    """
    PLAYER4_TRIBUTE = 105
    """
    Amount of resources tributed to player 4 by the source player
    """
    PLAYER5_TRIBUTE = 106
    """
    Amount of resources tributed to player 5 by the source player
    """
    PLAYER6_TRIBUTE = 107
    """
    Amount of resources tributed to player 6 by the source player
    """
    PLAYER7_TRIBUTE = 108
    """
    Amount of resources tributed to player 7 by the source player
    """
    PLAYER8_TRIBUTE = 109
    """
    Amount of resources tributed to player 8 by the source player
    """
    PLAYER1_KILL_VALUE = 110
    """
    Cost of units of player 1 killed by the source player
    """
    PLAYER2_KILL_VALUE = 111
    """
    Cost of units of player 2 killed by the source player
    """
    PLAYER3_KILL_VALUE = 112
    """
    Cost of units of player 3 killed by the source player
    """
    PLAYER4_KILL_VALUE = 113
    """
    Cost of units of player 4 killed by the source player
    """
    PLAYER5_KILL_VALUE = 114
    """
    Cost of units of player 5 killed by the source player
    """
    PLAYER6_KILL_VALUE = 115
    """
    Cost of units of player 6 killed by the source player
    """
    PLAYER7_KILL_VALUE = 116
    """
    Cost of units of player 7 killed by the source player
    """
    PLAYER8_KILL_VALUE = 117
    """
    Cost of units of player 8 killed by the source player
    """
    PLAYER1_RAZINGS = 118
    """
    Number of buildings destroyed of player 1 by the source player
    """
    PLAYER2_RAZINGS = 119
    """
    Number of buildings destroyed of player 2 by the source player
    """
    PLAYER3_RAZINGS = 120
    """
    Number of buildings destroyed of player 3 by the source player
    """
    PLAYER4_RAZINGS = 121
    """
    Number of buildings destroyed of player 4 by the source player
    """
    PLAYER5_RAZINGS = 122
    """
    Number of buildings destroyed of player 5 by the source player
    """
    PLAYER6_RAZINGS = 123
    """
    Number of buildings destroyed of player 6 by the source player
    """
    PLAYER7_RAZINGS = 124
    """
    Number of buildings destroyed of player 7 by the source player
    """
    PLAYER8_RAZINGS = 125
    """
    Number of buildings destroyed of player 8 by the source player
    """
    PLAYER1_RAZING_VALUE = 126
    """
    Cost of buildings destroyed of player 1 by the source player
    """
    PLAYER2_RAZING_VALUE = 127
    """
    Cost of buildings destroyed of player 2 by the source player
    """
    PLAYER3_RAZING_VALUE = 128
    """
    Cost of buildings destroyed of player 3 by the source player
    """
    PLAYER4_RAZING_VALUE = 129
    """
    Cost of buildings destroyed of player 4 by the source player
    """
    PLAYER5_RAZING_VALUE = 130
    """
    Cost of buildings destroyed of player 5 by the source player
    """
    PLAYER6_RAZING_VALUE = 131
    """
    Cost of buildings destroyed of player 6 by the source player
    """
    PLAYER7_RAZING_VALUE = 132
    """
    Cost of buildings destroyed of player 7 by the source player
    """
    PLAYER8_RAZING_VALUE = 133
    """
    Cost of buildings destroyed of player 8 by the source player
    """
    CASTLE = 134
    """
    Number of standing castles by the source player
    """
    HIT_POINT_RAZINGS = 135
    """
    Cumulative hp of all buildings destroyed by the source player
    """
    KILLS_BY_PLAYER1 = 136
    """
    Number of units killed by player 1 of the source player
    """
    KILLS_BY_PLAYER2 = 137
    """
    Number of units killed by player 2 of the source player
    """
    KILLS_BY_PLAYER3 = 138
    """
    Number of units killed by player 3 of the source player
    """
    KILLS_BY_PLAYER4 = 139
    """
    Number of units killed by player 4 of the source player
    """
    KILLS_BY_PLAYER5 = 140
    """
    Number of units killed by player 5 of the source player
    """
    KILLS_BY_PLAYER6 = 141
    """
    Number of units killed by player 6 of the source player
    """
    KILLS_BY_PLAYER7 = 142
    """
    Number of units killed by player 7 of the source player
    """
    KILLS_BY_PLAYER8 = 143
    """
    Number of units killed by player 8 of the source player
    """
    RAZINGS_BY_PLAYER1 = 144
    """
    Number of buildings destroyed by player 1 of the source player
    """
    RAZINGS_BY_PLAYER2 = 145
    """
    Number of buildings destroyed by player 2 of the source player
    """
    RAZINGS_BY_PLAYER3 = 146
    """
    Number of buildings destroyed by player 3 of the source player
    """
    RAZINGS_BY_PLAYER4 = 147
    """
    Number of buildings destroyed by player 4 of the source player
    """
    RAZINGS_BY_PLAYER5 = 148
    """
    Number of buildings destroyed by player 5 of the source player
    """
    RAZINGS_BY_PLAYER6 = 149
    """
    Number of buildings destroyed by player 6 of the source player
    """
    RAZINGS_BY_PLAYER7 = 150
    """
    Number of buildings destroyed by player 7 of the source player
    """
    RAZINGS_BY_PLAYER8 = 151
    """
    Number of buildings destroyed by player 8 of the source player
    """
    VALUE_KILLED_BY_OTHERS = 152
    """
    Cumulative cost of units lost by the source player
    """
    VALUE_RAZED_BY_OTHERS = 153
    """
    Cumulative cost of buildings lost by the source player
    """
    KILLED_BY_OTHERS = 154
    """
    Number of units killed by other players of the source player
    """
    RAZED_BY_OTHERS = 155
    """
    Number of buildings destroyed by other players amount of the source player
    """
    TRIBUTE_FROM_PLAYER1 = 156
    """
    Tribute received from player 1 of the source player
    """
    TRIBUTE_FROM_PLAYER2 = 157
    """
    Tribute received from player 2 of the source player
    """
    TRIBUTE_FROM_PLAYER3 = 158
    """
    Tribute received from player 3 of the source player
    """
    TRIBUTE_FROM_PLAYER4 = 159
    """
    Tribute received from player 4 of the source player
    """
    TRIBUTE_FROM_PLAYER5 = 160
    """
    Tribute received from player 5 of the source player
    """
    TRIBUTE_FROM_PLAYER6 = 161
    """
    Tribute received from player 6 of the source player
    """
    TRIBUTE_FROM_PLAYER7 = 162
    """
    Tribute received from player 7 of the source player
    """
    TRIBUTE_FROM_PLAYER8 = 163
    """
    Tribute received from player 8 of the source player
    """
    VALUE_CURRENT_UNITS = 164
    """
    Cumulative cost of alive units of the source player
    """
    VALUE_CURRENT_BUILDINGS = 165
    """
    Cumulative cost of standing buildings of the source player
    """
    FOOD_TOTAL = 166
    """
    Total food collected by the source player
    """
    WOOD_TOTAL = 167
    """
    Total wood collected by the source player
    """
    STONE_TOTAL = 168
    """
    Total stone collected by the source player
    """
    GOLD_TOTAL = 169
    """
    Total gold collected by the source player
    """
    TOTAL_VALUE_OF_KILLS = 170
    """
    Cumulative cost of all units killed by the source player
    """
    TOTAL_TRIBUTE_RECEIVED = 171
    """
    Total amount of resources received in tribute by the source player
    """
    TOTAL_VALUE_OF_RAZINGS = 172
    """
    Cumulative cost of all buildings destroyed by of the source player
    """
    TOTAL_CASTLES_BUILT = 173
    """
    Number of total castles built by the source player
    """
    TOTAL_WONDERS_BUILT = 174
    """
    Number of total wonders built by the source player
    """
    TRIBUTE_SCORE = 175
    """
    Tribute score of the source player
    """
    CONVERT_MIN_ADJ = 176
    """
    Additional monk seconds needed before conversion starts for the source player

    - Additional Information: A great explanation for how this works [here](https://youtu.be/-qRUaOHpbwI?t=870 "Explanatory video by T-West") by T-West
    """
    CONVERT_MAX_ADJ = 177
    """
    Additional monk seconds needed before forced conversion for the source player

    - Additional Information: A great explanation for how this works [here](https://youtu.be/-qRUaOHpbwI?t=870 "Explanatory video by T-West") by T-West
    """
    CONVERT_RESIST_MIN_ADJ = 178
    """
    Additional monk seconds needed before conversion starts against the source player

    - Additional Information: A great explanation for how this works [here](https://youtu.be/-qRUaOHpbwI?t=830 "Explanatory video by T-West") by T-West
    """
    CONVERT_RESIST_MAX_ADJ = 179
    """
    Additional monk seconds needed before forced conversion for the source player

    - Additional Information: A great explanation for how this works [here](https://youtu.be/-qRUaOHpbwI?t=870 "Explanatory video by T-West") by T-West
    """
    CONVERT_BUILDING_MIN = 180
    """
    Building conversion min time of the source player

    - Additional Information: A great explanation for how this works [here](https://youtu.be/-qRUaOHpbwI?t=902 "Explanatory video by T-West") by T-West
    """
    CONVERT_BUILDING_MAX = 181
    """
    Building conversion max time of the source player

    - Additional Information: A great explanation for how this works [here](https://youtu.be/-qRUaOHpbwI?t=902 "Explanatory video by T-West") by T-West
    """
    CONVERT_BUILDING_CHANCE = 182
    """
    Percent chance for monks to convert buildings by the source player

    - Additional Information: A great explanation for how this works [here](https://youtu.be/-qRUaOHpbwI?t=902 "Explanatory video by T-West") by T-West
    """
    SPIES = 183
    """
    Boolean: show enemy los for the source player
    """
    VALUE_WONDERS_CASTLES = 184
    """
    Total cost of all wonders and castles of the source player
    """
    FOOD_SCORE = 185
    """
    Unknown amount of the source player
    """
    WOOD_SCORE = 186
    """
    Unknown amount of the source player
    """
    STONE_SCORE = 187
    """
    Unknown amount of the source player
    """
    GOLD_SCORE = 188
    """
    Unknown amount of the source player
    """
    WOOD_BONUS = 189
    """
    Amount of wood chopped multiplier of the source player

    - Default Values:

        - 1:  Generic

        - 1.15:  Mayans

    - Additional Information: Since this works by multiplying the amount of resources gathered by a villager, it has a side effect of increasing the gather rate as well. In the case of Mayans, This is compensated for by reducing villager work rate by 15%
    """
    FOOD_BONUS = 190
    """
    Amount of food gathered from all sources (except from sheep) multiplier of the source player

    - Default Values:

        - 1:  Generic

        - 1.15:  Mayans

    - Additional Information: Since this works by multiplying the amount of resources gathered by a villager, it has a side effect of increasing the gather rate as well. In the case of Mayans, This is compensated for by reducing villager work rate by 15%. The work rate for farmers is reduced by about 23.4%
    """
    RELIC_RATE = 191
    """
    Relic gold generation rate for the source player

    - Default Values:

        - 0.5:  by default
    """
    HERESY = 192
    """
    Boolean: converted units die for the source player
    """
    THEOCRACY = 193
    """
    Boolean: only one monk needs to regen faith after group conversion for the source player
    """
    CRENELLATIONS = 194
    """
    Boolean: researched crenellations amount of the source player

    - Additional Information: Set to 1 if crenellations is researched, does not give the effect of crenellations, just a boolean
    """
    CONSTRUCTION_RATE_MOD = 195
    """
    Builder work rate multiplier of the source player

    - Default Values:

        - 0:  Generic

        - 1.3:  Spanish

    - Additional Information: The actual work rate for builders is given by `construction_rate_mod * builder.default_work_rate`
    """
    HUN_WONDER_BONUS = 196
    """
    Additional time for relic/wonder victories in one tenth of an year by any player

    - Additional Information: Internally, relic and wonder victory countdowns are measured in one tenths of an year, the fractional part is just not shown ingame This is additive per player Set to 1000 if atheism is researched
    """
    SPIES_DISCOUNT = 197
    """
    Boolean: give discount on spies for the source player

    - Additional Information: Set to 1 if atheism is researched
    """
    UNKNOWN_RESOURCE_198 = 198
    """
    Unknown amount of source player
    """
    UNKNOWN_RESOURCE_199 = 199
    """
    Unknown amount of source player
    """
    UNKNOWN_RESOURCE_200 = 200
    """
    Unknown amount of source player
    """
    UNKNOWN_RESOURCE_201 = 201
    """
    Unknown amount of source player
    """
    UNKNOWN_RESOURCE_202 = 202
    """
    Unknown amount of source player
    """
    UNKNOWN_RESOURCE_203 = 203
    """
    Unknown amount of source player
    """
    UNKNOWN_RESOURCE_204 = 204
    """
    Unknown amount of source player
    """
    FEITORIA_FOOD_PRODUCTIVITY = 205
    """
    Feitoria/BR Trade Workshop food production multiplier of the source player

    - Default Values:

        - 1:  Generic

    - Additional Information: The amount of food obtained from owning `n` number of Feitorias (BR Trade Workshops) is given by `n * feitoria_food_productivity * 1.6 (2.25)`.
    """
    FEITORIA_WOOD_PRODUCTIVITY = 206
    """
    Feitoria/BR Trade Workshop wood production multiplier of the source player

    - Default Values:

        - 1:  Generic

    - Additional Information: The amount of wood obtained from owning `n` number of Feitorias (BR Trade Workshops) is given by `n * feitoria_wood_productivity * 1 (2.25)`.
    """
    FEITORIA_STONE_PRODUCTIVITY = 207
    """
    Feitoria/BR Trade Workshop stone production multiplier of the source player

    - Default Values:

        - 1:  Generic

    - Additional Information: The amount of stone obtained from owning `n` number of Feitorias (BR Trade Workshops) is given by `n * feitoria_stone_productivity * 0.3 (0)`.
    """
    FEITORIA_GOLD_PRODUCTIVITY = 208
    """
    Feitoria/BR Trade Workshop gold production multiplier of the source player

    - Default Values:

        - 1:  Generic

    - Additional Information: The amount of gold obtained from owning `n` number of Feitorias (BR Trade Workshops) is given by `n * feitoria_gold_productivity * 0.7 (2.25)`.
    """
    REVEAL_ENEMY_TOWN_CENTRE = 209
    """
    Boolean: reveal enemy town centre location for the source player

    - Default Values:

        - 0:  Generic

        - 5:  Vietnamese

    - Additional Information: The bonus works for all values $\geq$1, the choice of setting it to 5 for vietnamese seems arbitrary Vietnamese reveal enemy tc location bonus
    """
    REVEAL_RELICS = 210
    """
    Boolean: reveal relics on map amount of the source player

    - Default Values:

        - -1:  Generic

        - 42:  Burmese

    - Additional Information: Burmese reveal relics on map bonus (probably) Only works in RMS, Manually changing this in the editor does not seem to have any effects
    """
    ELEVATION_BONUS_HIGHER = 211
    """
    The fraction for additional bonus damage dealt from higher elevation for the source player

    - Default Values:

        - 0:  Generic

        - 0.25:  Tatars

    - Additional Information: Damage that units on higher elevation deal to units on lower elevation is multiplied by `1.25 + elevation_bonus_higher`
    """
    ELEVATION_BONUS_LOWER = 212
    """
    The fraction for additional bonus damage dealt from lower elevation for the source player

    - Default Values:

        - 0:  Generic

    - Additional Information: Damage that units on lower elevation deal to units on higher elevation is multiplied by `0.75 + elevation_bonus_lower`
    """
    RAIDING_PRODUCTIVITY = 213
    """
    Keshik gold generation rate per second*100 of the source player

    - Default Values:

        - 50:  Tatars

    - Additional Information: Note that in practice, due to attack reload time and frame delay, Keshiks don't actually produce 0.5 gold per second, but a lower value
    """
    MERCENARY_KIPCHAK_COUNT = 214
    """
    Total number of mercenary kipchak creatable by the source player

    - Additional Information: Researching Cuman Mercenaries sets this to 10. Making mercenary Kipchaks costs one unit of this resource
    """
    MERCENARY_KIPCHAK_LIMIT = 215
    """
    Number of mercenary kipchaks created/queued by the source player

    - Additional Information: Making mercenary Kipchaks gives one unit of this resource
    """
    SHEPHERD_PRODUCTIVITY = 216
    """
    Amount of food collected from sheep multiplier of the source player

    - Default Values:

        - 1:  Generic

        - 1.15:  Mayans

        - 1.57:  Tatars

    - Additional Information: Since this works by multiplying the amount of resources gathered by a villager, it has a side effect of increasing the gather rate as well. In the case of Mayans/Tatars, This is compensated for by reducing villager work rate by 15%/57%
    """
    TRIGGER_SHARED_LOS = 217
    """
    Boolean: reveal ally for the source player

    - Default Values:

        - 0:  No Allied Vision

        - 1:  Allied Vision

    - Additional Information: Note - Once enabled, Allied vison cannot be undone
    """
    UNKNOWN_RESOURCE_218 = 218
    """
    Unknown amount of the source player
    """
    UNKNOWN_RESOURCE_219 = 219
    """
    Unknown amount of the source player
    """
    UNKNOWN_RESOURCE_220 = 220
    """
    Unknown amount of the source player
    """
    FOOD_TRICKLE_FROM_MONUMENT = 221
    """
    Monument food trickle rate multiplier of source player

    - Default Values:

        - 1:  In KoTH games

    - Additional Information: The amount of resources obtained by owning a monument is `0.7925 * food_trickle_from_monument`
    """
    WOOD_TRICKLE_FROM_MONUMENT = 222
    """
    Monument wood trickle rate multiplier of source player

    - Default Values:

        - 1:  In KoTH games

    - Additional Information: The amount of resources obtained by owning a monument is `0.7925 * wood_trickle_from_monument`
    """
    STONE_TRICKLE_FROM_MONUMENT = 223
    """
    Monument stone trickle rate multiplier of source player

    - Default Values:

        - 1:  In KoTH games

    - Additional Information: The amount of resources obtained by owning a monument is `0.7925 * stone_trickle_from_monument`
    """
    GOLD_TRICKLE_FROM_MONUMENT = 224
    """
    Monument gold trickle rate multiplier of source player

    - Default Values:

        - 1:  In KoTH games

    - Additional Information: The amount of resources obtained by owning a monument is `0.7925 * gold_trickle_from_monument`
    """
    RELIC_FOOD_PRODUCTION_RATE = 225
    """
    Relic food production per minute of the source player

    - Default Values:

        - 30:  Burgundians

        - 0: Generic
    """
    VILLAGERS_KILLED_BY_GAIA = 226
    """
    Villagers lost to gaia by the source player
    """
    VILLAGERS_KILLED_BY_ANIMALS = 227
    """
    Villagers lost to wild animals by the source player
    """
    VILLAGERS_KILLED_BY_AI_PLAYER = 228
    """
    Villagers lost to ais by the source player
    """
    VILLAGERS_KILLED_BY_HUMAN_PLAYER = 229
    """
    Villagers lost to humans by the source player
    """
    FOOD_TRICKLE = 230
    """
    Food given per minute to the source player
    """
    WOOD_TRICKLE = 231
    """
    Wood given per minute to the source player
    """
    STONE_TRICKLE = 232
    """
    Stone given per minute to the source player
    """
    GOLD_TRICKLE = 233
    """
    Gold given per minute to the source player
    """
    SPAWN_LIMIT = 234
    """
    Limit of the number of spawning buildings that spawn units from spawn command in a technology of the source player
    """
    FLEMISH_MILITIA_POPULATION = 235
    """
    Number of flemish militia of the source player
    """
    FARMING_GOLD_TRICKLE = 236
    """
    Farming gold generation rate per second*100 of the source player

    - Additional Information: used by the Burgundian Vineyards technology. Set to 2 when researched
    """
    FOLWARK_COLLECTION_AMOUNT = 237
    """
    This is the amount of food collected from farms built around a Folwark by the source player

    - Default Values:

        - 0:  Generic

        - 17.5:  Poles

        - 25:  Poles with Horse Collar

        - 37.5:  Poles with Heavy Plow

        - 55:  Poles with Crop Rotation

    - Additional Information: Poles set this to 17.5. Horse Collar adds 7.5 to it, Heavy Plow adds 12.5 to it and Crop Rotation adds 17.5 to it
    """
    FOLWARK_ATTRIBUTE_TYPE = 238
    """
    This is the ID of the resource that is given to the player from a farm constructed around a Folwark to the source player

    - Default Values:

        - 0:  Poles

        - -1:  Generic
    """
    FOLWARK_BUILDING_TYPE = 239
    """
    This is the ID of the building that the Folwark needs to upgrade from for the farm collection ability to work for the source player

    - Default Values:

        - 68 (Mill):  Poles

        - -1:  Generic
    """
    UNITS_CONVERTED = 240
    """
    The amount of units lost to enemy conversions by the source player
    """
    STONE_MINING_GOLD_PRODUCTIVITY = 241
    """
    Stone mining gold generation rate per second*100 of the source player

    - Default Values:

        - 0:  Generic

        - 18:  Poles

        - 20.7:  Poles with Stone Mining

        - 23.805:  Poles with Stone Shaft Mining
    """
    NUMBER_OF_FREE_TRANSPORTS = 242
    """
    This is the number of free transport ships trainable by having a Sicilian ally to the source player

    - Default Values:

    	- 1:  Generic

    - Additional Information: One unit of this resource is required to be able to train the free transport ship granted by having a Sicilian ally. This seemingly useless cost is necessary to prevent shift queuing multiple of the free transport ship unit. Note that as soon as at least one free transport ship is created, the unit disables itself, no matter how much of this resource is left. It is possible to change this by disabling technology 229, but then keep in mind that regular transport ships won't be trainable once this resource runs out
    """


class ObjectType(_TriggerListIntEnums):
    """
    This enum class provides the integer values used to reference the object types in the game. Used in a lot of effects
    and conditions, like 'Kill Object', 'Objects in Area'.

    **Examples**

    >>> ObjectType.OTHER
    <ObjectType.OTHER: 1>
    """
    OTHER = 1
    BUILDING = 2
    CIVILIAN = 3
    MILITARY = 4


class ObjectClass(_TriggerListIntEnums):
    """
    This enum class provides the integer values used to reference the object class in the game. Used in a lot of effects
    and conditions, like 'Kill Object', 'Objects in Area' under the name 'Object Group'.

    **Examples**

    >>> ObjectType.OTHER
    <ObjectType.OTHER: 1>
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


class TerrainRestrictions(_TriggerListIntEnums):
    """
    This enum class provides the integer values used to reference the terrain restriction IDs in the game. Used in the
    'Modify Attribute' effects

    **Examples**

    >>> TerrainRestrictions.LAND_AND_SHALLOWS
    <TerrainRestrictions.LAND_AND_SHALLOWS: 1>
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


class HeroStatusFlag(_TriggerListIntFlags):
    """
    This enum class provides the integer values for the different hero status flags that can be used in the 'Modify
    Attribute' effect with the 'Hero Status' attribute.

    **Methods**

    - ``HeroStatusFlag.combine()``
    - ``HeroStatusFlag.split_flags()``


    **Examples**

    >>> HeroStatusFlag.HERO_REGENERATION
    <HeroStatusFlag.HERO_REGENERATION: 4>
    >>> HeroStatusFlag.HERO_REGENERATION | HeroStatusFlag.HERO_GLOW
    <HeroStatusFlag.HERO_GLOW|HERO_REGENERATION: 68>
    >>> HeroStatusFlag.combine(hero_regeneration=True, hero_glow=True)
    <HeroStatusFlag.HERO_GLOW|HERO_REGENERATION: 68>
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
    ) -> HeroStatusFlag:
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
        return HeroStatusFlag(total)

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


class BlastLevel(_TriggerListIntEnums):
    """
    This enum class provides the integer values used to reference the blast level values used in the game. Used in the
    'Modify Attribute' effect with the 'Blast Attack/Defense Level' attributes

    **Examples**

    >>> BlastLevel.TREES
    <BlastLevel.TREES: 1>
    """
    RESOURCES = 0
    """
    Damage Resources
    """
    TREES = 1
    """
    Damage Trees
    """
    NEARBY_UNITS = 2
    """
    Damage surrounding units
    """
    TARGET_ONLY = 3
    """
    Damage targetted unit only
    """
    FIXED_FIVE = 4
    """
    Deal a fixed, 5 HP of damage to surrounding units
    """
    FIFTY_PERCENT = 8
    """
    Deal 50% damage to surrounding units
    """
    TWNETY_FIVE_PERCENT = 16
    """
    Deal 25% damage to surrounding units
    """
    THIRTY_THREE_PERCENT = 32
    """
    Deal 33% damage to surrounding units
    """
    DISTANCE_ATTENUATION = 64
    """
    Only works for infantry units, reduces blast damage done based on distance
    """


class SmartProjectile(_TriggerListIntEnums):
    """
    This enum class provides the integer values used to reference the smart projectile flag values used in the game. Used in the
    'Modify Attribute' effect with the 'Enable Smart Projectile' attribute

    **Examples**

    >>> SmartProjectile.ENABLED
    <SmartProjectile.ENABLED: 1>
    """
    ENABLED = 1
    FULL_DAMAGE_ON_MISSED_HIT = 2


class DamageClass(_TriggerListIntEnums):
    """
    This enum class provides the integer values that represent the damage classes in the game. Used in the 'Chnage
    Object Attack/Armour' and 'Modify Attribute' with the 'Attack/Armour' attibutes

    **Examples**

    >>> DamageClass.INFANTRY
    <DamageClass.INFANTRY: 1>
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


class Hotkey(_TriggerListIntEnums):
    """
    This enum class provides the integer values used to reference the blast level values used in the game. Used in the
    'Modify Attribute' effect with the 'HotKey ID' attribute

    Many hotkeys are missing from this file (Like arrow up). The reason for this is explained in the UGC guide:
    https://divy1211.github.io/AoE2DE_UGC_Guide/general/hotkeys/hotkeys/

    **Examples**

    >>> Hotkey.SPACE
    <Hotkey.SPACE: 10101>
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


class ColorMood(_TriggerListIntEnums):
    """
    This enum class provides the integer values used to reference the colour mood values used in the game. Used in the
    'Change Colour Mood' effect

    **Examples**

    >>> ColorMood.AUTUMN
    <ColorMood.AUTUMN: 1>
    """
    DEFAULT = 0
    AUTUMN = 1
    WINTER = 2
    JUNGLE = 3
    DESERT = 4
    NIGHT = 5


class ObjectState(_TriggerListIntEnums):
    """
    This enum class provides the integer values used to reference the object state values used in the game. Used in the
    'Object in Area' condition

    **Examples**

    >>> BlastLevel.TREES
    <BlastLevel.TREES: 1>
    """
    FOUNDATION = 0
    ALMOST_ALIVE = 1
    ALIVE = 2
    RESOURCE = 3
    DYING = 4
    DEAD = 5
    UNDEAD = 6
    REMOVE = 7


class Age(_TriggerListIntEnums):
    """
    This enum class provides the integer values used to reference the different ages in the game. These values are
    used by the 'Current Age' player resource

    **Examples**

    >>> Age.IMPERIAL_AGE
    <Age.IMPERIAL_AGE: 3>
    """

    DARK_AGE = 0
    FEUDAL_AGE = 1
    CASTLE_AGE = 2
    IMPERIAL_AGE = 3


class ActionType(_TriggerListIntEnums):
    """
    This enum class provides the integer values used to reference the different action types in the game.
    These values are used in the Task Object effect

    **Examples**

    >>> ActionType.DROP_RELIC
    <ActionType.DROP_RELIC: 14>
    """
    DEFAULT = 0
    MOVE = 1
    PATROL = 2
    GUARD = 3
    FOLLOW = 4
    STOP = 5
    ATTACK_GROUND = 6
    GARRISON = 7
    KILL = 8
    UNLOAD = 9
    GATHER_POINT = 10
    LOCK_UNLOCK = 11
    WORK = 12
    UNGARRISON = 13
    DROP_RELIC = 14
    PACK = 15
    UNPACK = 16
    ATTACK_MOVE = 17
