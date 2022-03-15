from __future__ import annotations

import math
import json
from pathlib import Path

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums, _DataSetIntFlags


class DiplomacyState(_DataSetIntEnums):
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


class Operation(_DataSetIntEnums):
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


class AttackStance(_DataSetIntEnums):
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


class UnitAIAction(_DataSetIntEnums):
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


class ButtonLocation(_DataSetIntEnums):
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


class PanelLocation(_DataSetIntEnums):
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


class TimeUnit(_DataSetIntEnums):
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
    MINUTES_AND_SECONDS = 3
    """In-Game Minutes abd seconds."""


class VisibilityState(_DataSetIntEnums):
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


class DifficultyLevel(_DataSetIntEnums):
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


class TechnologyState(_DataSetIntEnums):
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


class Comparison(_DataSetIntEnums):
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


class ObjectAttribute(_DataSetIntEnums):
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


_attribute_dataset_editor_names = None


class Attribute(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference all the player resources in the game. Used in effects
    and conditions like 'Accumulate Attribute' and 'Modify Resource'

    **Examples**

    >>> Attribute.FOOD_STORAGE
    <Attribute.FOOD_STORAGE: 0>

    You can also request the editor names of these player attributes (resources) to be used in <...> notation in
    trigger displays using:

    >>> Attribute.FOOD_STORAGE.editor_name
    '!Food Storage'
    """

    @property
    def editor_name(self):
        """
        The exact name of this resource in the editor. To be used in <...> notation in trigger displays
        """
        global _attribute_dataset_editor_names

        if _attribute_dataset_editor_names is None:
            with (Path(__file__).parent / 'sources' / 'resource_editor_names.json').open() as file:
                _attribute_dataset_editor_names = json.load(file)

        return _attribute_dataset_editor_names[self]

    FOOD_STORAGE = 0
    """
    - Purpose: Current food amount
    """
    WOOD_STORAGE = 1
    """
    - Purpose: Current wood amount
    """
    STONE_STORAGE = 2
    """
    - Purpose: Current stone amount
    """
    GOLD_STORAGE = 3
    """
    - Purpose: Current gold amount
    """
    POPULATION_HEADROOM = 4
    """
    - Purpose: Amount of free population space. Note that this is NOT the population cap
    """
    CONVERSION_RANGE = 5
    """
    - Purpose: Unknown... What does this resource do?
    """
    CURRENT_AGE = 6
    """
    - Purpose: Controls the age name and icon at the top of the screen

    - Default Values:

        - 0:  Dark Age

        - 1:  Feudal Age

        - 2:  Castle Age

        - 3:  Imperial Age

    - Note: Setting this to an amount higher than 3 cycles the icon but keeps the age at imperial
    """
    RELICS_CAPTURED = 7
    """
    - Purpose: Number of relics held
    """
    UNUSED_RESOURCE_008 = 8
    """
    - Purpose: Unused
    """
    TRADE_GOODS = 9
    """
    - Purpose: Unused
    """
    UNUSED_RESOURCE_010 = 10
    """
    - Purpose: Unused
    """
    CURRENT_POPULATION = 11
    """
    - Purpose: The current population
    """
    CORPSE_DECAY_TIME = 12
    """
    - Purpose: Unknown... What does this resource do?
    """
    REMARKABLE_DISCOVERY = 13
    """
    - Purpose: Unknown... What does this resource do?
    """
    MONUMENTS_CAPTURED = 14
    """
    - Purpose: Number of monuments owned
    """
    MEAT_STORAGE = 15
    """
    - Purpose: Unknown... What does this resource do?
    """
    BERRY_STORAGE = 16
    """
    - Purpose: Unknown... What does this resource do?
    """
    FISH_STORAGE = 17
    """
    - Purpose: Unknown... What does this resource do?
    """
    UNUSED_RESOURCE_018 = 18
    """
    - Purpose: Unused
    """
    TOTAL_UNITS_OWNED = 19
    """
    - Purpose: Total units owned, excluding buildings
    """
    UNITS_KILLED = 20
    """
    - Purpose: Total units killed, excluding buildings
    """
    TECHNOLOGY_COUNT = 21
    """
    - Purpose: Number of technologies researched till now
    """
    PERCENT_MAP_EXPLORED = 22
    """
    - Purpose: Percentage of the map explored
    """
    CASTLE_AGE_TECH_ID = 23
    """
    - Purpose: Always 102

    - Note: Nothing happens when you change this, probably for mods only
    """
    IMPERIAL_AGE_TECH_ID = 24
    """
    - Purpose: Always 103

    - Note: Nothing happens when you change this, probably for mods only
    """
    FEUDAL_AGE_TECH_ID = 25
    """
    - Purpose: Always 101

    - Note: Nothing happens when you change this, probably for mods only
    """
    ATTACK_WARNING_SOUND_ID = 26
    """
    - Purpose: Always 0

    - Note: Nothing happens when you change this, probably for mods only
    """
    ENABLE_MONK_CONVERSION = 27
    """
    - Purpose: Boolean: allow enemy monk conversions

    - Default Values:

        - 0:  No (default)

        - >= 1:  Yes, after Atonement
    """
    ENABLE_BUILDING_CONVERSION = 28
    """
    - Purpose: Boolean: allow enemy building conversions.

    - Default Values:

        - 0:  No (default)

        - 1:  Yes, after Redemption

        - >=2:  Monks can convert buildings from range
    """
    UNUSED_RESOURCE_029 = 29
    """
    - Purpose: Unused
    """
    UNUSED_RESOURCE_030 = 30
    """
    - Purpose: Unused
    """
    UNUSED_RESOURCE_031 = 31
    """
    - Purpose: Unused
    """
    BONUS_POPULATION_CAP = 32
    """
    - Purpose: Additional pop space to grant on top of maximum pop cap

    - Note: 10 for goths
    """
    FOOD_MAINTENANCE = 33
    """
    - Purpose: Unknown... What does this resource do?
    """
    FAITH = 34
    """
    - Purpose: Unknown... What does this resource do?
    """
    FAITH_RECHARGING_RATE = 35
    """
    - Purpose: Monk faith recovery rate

    - Default Values:

        - 1:  The unit of measurement for this rate is unknown
    """
    FARM_FOOD_AMOUNT = 36
    """
    - Purpose: Maximum farm food amount

    - Default Values:

        - 175:  Generic

        - 220:  Chinese

    - Note: This is what horse collar etc. technologies modify
    """
    CIVILIAN_POPULATION = 37
    """
    - Purpose: Current civilian population
    """
    UNUSED_RESOURCE_038 = 38
    """
    - Purpose: Unused
    """
    ALL_TECHS_ACHIEVED = 39
    """
    - Purpose: Boolean: If all available technologies have been researched

    - Default Values:

        - 0:  No

        - 1:  Yes
    """
    MILITARY_POPULATION = 40
    """
    - Purpose: Current military popupation
    """
    CONVERSIONS = 41
    """
    - Purpose: Number of units converted
    """
    STANDING_WONDERS = 42
    """
    - Purpose: Number of standing wonders
    """
    RAZINGS = 43
    """
    - Purpose: Number of buildings razed
    """
    KILL_RATIO = 44
    """
    - Purpose: This is the number of units lost subtracted from the number of units killed in total
    """
    SURVIVAL_TO_FINISH = 45
    """
    - Purpose: Boolean: This is set to `0` under the same conditions which are required to defeat a player

    - Default Values:

        - 0:  No

        - 1:  Yes
    """
    TRIBUTE_INEFFICIENCY = 46
    """
    - Purpose: This is the fraction of tributes sent that are collected as tax

    - Default Values:

        - 0.3:  Generic

        - 0.2:  After Coinage

        - 0:  After Banking
    """
    GOLD_MINING_PRODUCTIVITY = 47
    """
    - Purpose: Multiplier for gold mined by gold miners

    - Default Values:

        - 1:  Generic

        - 1.15:  Mayans

    - Note: Since this works by multiplying the amount of resources gathered by a villager, it has a side effect of increasing the gather rate. In the case of Mayans, This is compensated for by reducing villager work rate by 15%
    """
    TOWN_CENTER_UNAVAILABLE = 48
    """
    - Purpose: Boolean: allow building extra tcs

    - Default Values:

        - 0:  No (Sudden Death)

        - 1:  Yes (Normal)
    """
    GOLD_COUNTER = 49
    """
    - Purpose: Total gold collected
    """
    REVEAL_ALLY = 50
    """
    - Purpose: Boolean: show ally los for the source player

    - Default Values:

        - 0:  No (default)

        - 1:  Yes, after Cartography or with a Portuguese ally

    - Note: Once set to `1`, setting it back to `0` won't take away the LoS of allies
    """
    UNUSED_RESOURCE_051 = 51
    """
    - Purpose: Unused
    """
    MONASTERIES = 52
    """
    - Purpose: Number of monasteries
    """
    TRIBUTE_SENT = 53
    """
    - Purpose: Total of all resources tributed to others. This does not count taxes paid on tributing
    """
    ALL_MONUMENTS_CAPTURED = 54
    """
    - Purpose: Boolean: all monuments on the map captured

    - Default Values:

        - 0:  No

        - 1:  Yes
    """
    ALL_RELICS_CAPTURED = 55
    """
    - Purpose: Boolean: all relics on the map captured

    - Default Values:

        - 0:  No

        - 1:  Yes
    """
    ORE_STORAGE = 56
    """
    - Purpose: Unused
    """
    KIDNAP_STORAGE = 57
    """
    - Purpose: Number of units kidnapped

    - Note: This is probably only used by mods, this usage may be incorrect
    """
    DARK_AGE_TECH_ID = 58
    """
    - Purpose: Always 104 

    - Note: Nothing happens when you change this
    """
    UNUSED_RESOURCE_059 = 59
    """
    - Purpose: Unused
    """
    UNUSED_RESOURCE_060 = 60
    """
    - Purpose: Unused
    """
    UNUSED_RESOURCE_061 = 61
    """
    - Purpose: Unused
    """
    BUILDING_HOUSING_RATE = 62
    """
    - Purpose: Unknown... What does this resource do?
    """
    TAX_GATHER_RATE = 63
    """
    - Purpose: Unknown... What does this resource do?
    """
    GATHER_ACCUMULATOR = 64
    """
    - Purpose: Unknown... What does this resource do?
    """
    SALVAGE_DECAY_RATE = 65
    """
    - Purpose: Unknown... What does this resource do?
    """
    UNUSED_RESOURCE_066 = 66
    """
    - Purpose: Unused
    """
    CAN_CONVERT = 67
    """
    - Purpose: Boolean: monks can convert enemy units

    - Default Values:

        - 0:  No

        - 1:  Yes (default)
    """
    HIT_POINTS_KILLED = 68
    """
    - Purpose: Cumulative hp of all units killed
    """
    KILLED_P1 = 69
    """
    - Purpose: Number of player 1 units killed
    """
    KILLED_P2 = 70
    """
    - Purpose: Number of player 2 units killed
    """
    KILLED_P3 = 71
    """
    - Purpose: Number of player 3 units killed
    """
    KILLED_P4 = 72
    """
    - Purpose: Number of player 4 units killed
    """
    KILLED_P5 = 73
    """
    - Purpose: Number of player 5 units killed
    """
    KILLED_P6 = 74
    """
    - Purpose: Number of player 6 units killed
    """
    KILLED_P7 = 75
    """
    - Purpose: Number of player 7 units killed
    """
    KILLED_P8 = 76
    """
    - Purpose: Number of player 8 units killed
    """
    CONVERSION_RESISTANCE = 77
    """
    - Purpose: Coefficient of conversion resistance

    - Default Values:

        - 0:  Generic

        - +2:  with Teuton ally

        - +3:  after Faith

    - Note: Probability of conversion is divided by this value for ALL source player units, Teuton team bonus for conversion resistance works by increasing this.
    """
    TRADE_VIG_RATE = 78
    """
    - Purpose: Market exchange rate fraction for the source player

    - Default Values:

        - 0.3:  Generic Rate

        - 0.15:  after Guilds

        - 0.05:  Saracens
    """
    STONE_MINING_PRODUCTIVITY = 79
    """
    - Purpose: Multiplier for stone mined by stone miners

    - Default Values:

        - 1:  Generic

        - 1.15:  Mayans

    - Note: Since this works by multiplying the amount of resources gathered by a villager, it has a side effect of increasing the gather rate. In the case of Mayans, This is compensated for by reducing villager work rate by 15%
    """
    QUEUED_UNITS = 80
    """
    - Purpose: Amount of units in queue

    - Note: Note that only the units waiting to be trained are considered in the queue so if an archery range has 3 archers being made, there is 1 archer that is being trained and 2 archers that are in queue
    """
    TRAINING_COUNT = 81
    """
    - Purpose: Amount of units being trained

    - Note: Note that only the FIRST unit in each building is considered as being trained so if a town centre has 4 villagers being made, there is 1 archer that is being trained and 3 villagers that are in queue
    """
    START_WITH_UNIT_444_PTWC_ = 82
    """
    - Purpose: Boolean: started with PTWC

    - Note: Setting this to 1 in an RMS allows for starting with PTWC. Manually changing this in the editor does nothing
    """
    BOARDING_RECHARGE_RATE = 83
    """
    - Purpose: ABGAL faith recharge rate amount

    - Note: This is similar to monk's faith except for a special ship unit 536 called the ABGAL in the editor that can convert ships form 1 range away
    """
    STARTING_VILLAGERS = 84
    """
    - Purpose: Number of starting villagers

    - Default Values:

        - 3:  Generic

        - 4:  Mayans

        - 6:  Chinese

    - Note: Only works for RMS, changing this manually in the editor does nothing.
    """
    RESEARCH_COST_MODIFIER = 85
    """
    - Purpose: Multiply technology costs by this value

    - Default Values:

        - 1:  Generic

        - 0.9:  Chinese in feudal age

        - 0.85:  Chinese in castle age

        - 0.80:  Chinese in imperial age
    """
    RESEARCH_TIME_MODIFIER = 86
    """
    - Purpose: Multiply technology research times by this value
    """
    CONVERT_BOATS = 87
    """
    - Purpose: Boolean: allow monks to convert boats

    - Default Values:

        - 0:  No

        - 1:  Yes (default)
    """
    FISH_TRAP_FOOD_AMOUNT = 88
    """
    - Purpose: Maximum fishtrap food amount

    - Default Values:

        - 710:  Generic

        - 2130:  Malay
    """
    HEAL_RATE_MODIFIER = 89
    """
    - Purpose: Monk healing rate modifier

    - Default Values:

        - 0:  The unit of measuremeant for this is unknown
    """
    HEALING_RANGE = 90
    """
    - Purpose: Monk heal range

    - Default Values:

        - 4:  Tiles
    """
    STARTING_FOOD = 91
    """
    - Purpose: Starting food amount

    - Note: Only works for RMS, changing this manually in the editor does nothing but its a way to check starting food amount
    """
    STARTING_WOOD = 92
    """
    - Purpose: Starting wood amount

    - Note: Only works for RMS, changing this manually in the editor does nothing but its a way to check starting wood amount
    """
    STARTING_STONE = 93
    """
    - Purpose: Starting stone amount

    - Note: Only works for RMS, changing this manually in the editor does nothing but its a way to check starting stone amount
    """
    STARTING_GOLD = 94
    """
    - Purpose: Starting gold amount

    - Note: Only works for RMS, changing this manually in the editor does nothing but its a way to check starting gold amount
    """
    ENABLE_PTWC_KIDNAP_LOOT = 95
    """
    - Purpose: Enable town centre packing for the source player

    - Default Values:

        - 0:  default

        - 1:  allows the TC to be packed and moved

        - >=2:  no noticeable effect

    - Note: Enabling kidnap/loot requires modding the units to have the kidnap/pillage action
    """
    UNUSED_RESOURCE_096 = 96
    """
    - Purpose: Unused
    """
    DOMINANT_SHEEP_CONTROL = 97
    """
    - Purpose: Boolean: force sheep conversion

    - Default Values:

        - 0:  Generic

        - 1:  Celts

    - Note: If this is set to a non zero value, other players' sheep convert to you even if they have a unit in their LOS, unless this is also a non zero value for them. Celt sheep bonus
    """
    BUILDING_COST_SUM = 98
    """
    - Purpose: Total cost of all units and buildings owned
    """
    TECH_COST_SUM = 99
    """
    - Purpose: Total cost of all researches researched
    """
    RELIC_INCOME_SUM = 100
    """
    - Purpose: Total relic gold generated
    """
    TRADE_INCOME_SUM = 101
    """
    - Purpose: Total trade gold generated
    """
    P1_TRIBUTE = 102
    """
    - Purpose: Amount of resources tributed to player 1
    """
    P2_TRIBUTE = 103
    """
    - Purpose: Amount of resources tributed to player 2
    """
    P3_TRIBUTE = 104
    """
    - Purpose: Amount of resources tributed to player 3
    """
    P4_TRIBUTE = 105
    """
    - Purpose: Amount of resources tributed to player 4
    """
    P5_TRIBUTE = 106
    """
    - Purpose: Amount of resources tributed to player 5
    """
    P6_TRIBUTE = 107
    """
    - Purpose: Amount of resources tributed to player 6
    """
    P7_TRIBUTE = 108
    """
    - Purpose: Amount of resources tributed to player 7
    """
    P8_TRIBUTE = 109
    """
    - Purpose: Amount of resources tributed to player 8
    """
    P1_KILL_VALUE = 110
    """
    - Purpose: Total cost of all units killed of player 1
    """
    P2_KILL_VALUE = 111
    """
    - Purpose: Total cost of all units killed of player 2
    """
    P3_KILL_VALUE = 112
    """
    - Purpose: Total cost of all units killed of player 3
    """
    P4_KILL_VALUE = 113
    """
    - Purpose: Total cost of all units killed of player 4
    """
    P5_KILL_VALUE = 114
    """
    - Purpose: Total cost of all units killed of player 5
    """
    P6_KILL_VALUE = 115
    """
    - Purpose: Total cost of all units killed of player 6
    """
    P7_KILL_VALUE = 116
    """
    - Purpose: Total cost of all units killed of player 7
    """
    P8_KILL_VALUE = 117
    """
    - Purpose: Total cost of all units killed of player 8
    """
    P1_RAZINGS = 118
    """
    - Purpose: Number of buildings destroyed of player 1
    """
    P2_RAZINGS = 119
    """
    - Purpose: Number of buildings destroyed of player 2
    """
    P3_RAZINGS = 120
    """
    - Purpose: Number of buildings destroyed of player 3
    """
    P4_RAZINGS = 121
    """
    - Purpose: Number of buildings destroyed of player 4
    """
    P5_RAZINGS = 122
    """
    - Purpose: Number of buildings destroyed of player 5
    """
    P6_RAZINGS = 123
    """
    - Purpose: Number of buildings destroyed of player 6
    """
    P7_RAZINGS = 124
    """
    - Purpose: Number of buildings destroyed of player 7
    """
    P8_RAZINGS = 125
    """
    - Purpose: Number of buildings destroyed of player 8
    """
    P1_RAZING_VALUE = 126
    """
    - Purpose: Total cost of all buildings destroyed of player 1
    """
    P2_RAZING_VALUE = 127
    """
    - Purpose: Total cost of all buildings destroyed of player 2
    """
    P3_RAZING_VALUE = 128
    """
    - Purpose: Total cost of all buildings destroyed of player 3
    """
    P4_RAZING_VALUE = 129
    """
    - Purpose: Total cost of all buildings destroyed of player 4
    """
    P5_RAZING_VALUE = 130
    """
    - Purpose: Total cost of all buildings destroyed of player 5
    """
    P6_RAZING_VALUE = 131
    """
    - Purpose: Total cost of all buildings destroyed of player 6
    """
    P7_RAZING_VALUE = 132
    """
    - Purpose: Total cost of all buildings destroyed of player 7
    """
    P8_RAZING_VALUE = 133
    """
    - Purpose: Total cost of all buildings destroyed of player 8
    """
    STANDING_CASTLES = 134
    """
    - Purpose: Number of standing castles
    """
    HIT_POINTS_RAZED = 135
    """
    - Purpose: Total HP of all buildings destroyed
    """
    KILLS_BY_P1 = 136
    """
    - Purpose: Number of own units killed by player 1
    """
    KILLS_BY_P2 = 137
    """
    - Purpose: Number of own units killed by player 2
    """
    KILLS_BY_P3 = 138
    """
    - Purpose: Number of own units killed by player 3
    """
    KILLS_BY_P4 = 139
    """
    - Purpose: Number of own units killed by player 4
    """
    KILLS_BY_P5 = 140
    """
    - Purpose: Number of own units killed by player 5
    """
    KILLS_BY_P6 = 141
    """
    - Purpose: Number of own units killed by player 6
    """
    KILLS_BY_P7 = 142
    """
    - Purpose: Number of own units killed by player 7
    """
    KILLS_BY_P8 = 143
    """
    - Purpose: Number of own units killed by player 8
    """
    RAZINGS_BY_P1 = 144
    """
    - Purpose: Number of own buildings destroyed by player 1
    """
    RAZINGS_BY_P2 = 145
    """
    - Purpose: Number of own buildings destroyed by player 2
    """
    RAZINGS_BY_P3 = 146
    """
    - Purpose: Number of own buildings destroyed by player 3
    """
    RAZINGS_BY_P4 = 147
    """
    - Purpose: Number of own buildings destroyed by player 4
    """
    RAZINGS_BY_P5 = 148
    """
    - Purpose: Number of own buildings destroyed by player 5
    """
    RAZINGS_BY_P6 = 149
    """
    - Purpose: Number of own buildings destroyed by player 6
    """
    RAZINGS_BY_P7 = 150
    """
    - Purpose: Number of own buildings destroyed by player 7
    """
    RAZINGS_BY_P8 = 151
    """
    - Purpose: Number of own buildings destroyed by player 8
    """
    VALUE_KILLED_BY_OTHERS = 152
    """
    - Purpose: Total cost of all own units lost
    """
    VALUE_RAZED_BY_OTHERS = 153
    """
    - Purpose: Total cost of all own buildings lost
    """
    KILLED_BY_OTHERS = 154
    """
    - Purpose: Number of own units killed by other players
    """
    RAZED_BY_OTHERS = 155
    """
    - Purpose: Number of own buildings destroyed by other players
    """
    TRIBUTE_FROM_P1 = 156
    """
    - Purpose: Tribute received from player 1
    """
    TRIBUTE_FROM_P2 = 157
    """
    - Purpose: Tribute received from player 2
    """
    TRIBUTE_FROM_P3 = 158
    """
    - Purpose: Tribute received from player 3
    """
    TRIBUTE_FROM_P4 = 159
    """
    - Purpose: Tribute received from player 4
    """
    TRIBUTE_FROM_P5 = 160
    """
    - Purpose: Tribute received from player 5
    """
    TRIBUTE_FROM_P6 = 161
    """
    - Purpose: Tribute received from player 6
    """
    TRIBUTE_FROM_P7 = 162
    """
    - Purpose: Tribute received from player 7
    """
    TRIBUTE_FROM_P8 = 163
    """
    - Purpose: Tribute received from player 8
    """
    VALUE_CURRENT_UNITS = 164
    """
    - Purpose: Total cost of all own alive units
    """
    VALUE_CURRENT_BUILDINGS = 165
    """
    - Purpose: Total cost of all own standing buildings
    """
    FOOD_TOTAL = 166
    """
    - Purpose: Total food collected
    """
    WOOD_TOTAL = 167
    """
    - Purpose: Total wood collected
    """
    STONE_TOTAL = 168
    """
    - Purpose: Total stone collected
    """
    GOLD_TOTAL = 169
    """
    - Purpose: Total gold collected
    """
    TOTAL_VALUE_OF_KILLS = 170
    """
    - Purpose: Total cost of all units killed
    """
    TOTAL_TRIBUTE_RECEIVED = 171
    """
    - Purpose: Total of all resources received in tribute
    """
    TOTAL_VALUE_OF_RAZINGS = 172
    """
    - Purpose: Total cost of all buildings destroyed
    """
    TOTAL_CASTLES_BUILT = 173
    """
    - Purpose: Number of total castles built
    """
    TOTAL_WONDERS_BUILT = 174
    """
    - Purpose: Number of total wonders built
    """
    TRIBUTE_SCORE = 175
    """
    - Purpose: Total amount of resources sent in tribute including taxes. 10% of this is counted towards the economy score
    """
    CONVERT_MIN_ADJUSTMENT = 176
    """
    - Purpose: Additional monk seconds needed before a conversion is even possible

    - Note: A great explanation of how this works: https://youtu.be/-qRUaOHpbwI?t=870 by T-West
    """
    CONVERT_MAX_ADJUSTMENT = 177
    """
    - Purpose: Additional monk seconds needed before a conversion is forced

    - Note: A great explanation of how this works: https://youtu.be/-qRUaOHpbwI?t=870 by T-West
    """
    CONVERT_RESIST_MIO_ADJUSTMENT = 178
    """
    - Purpose: Additional monk seconds needed before conversion by enemy monks is even possible

    - Note: A great explanation of how this works: https://youtu.be/-qRUaOHpbwI?t=830 by T-West
    """
    CONVERT_RESIST_MAX_ADJUSTMENT = 179
    """
    - Purpose: Additional monk seconds needed before conversion by enemy monks is forced

    - Note: A great explanation of how this works: https://youtu.be/-qRUaOHpbwI?t=830 by T-West
    """
    CONVERT_BUILDING_MIN = 180
    """
    - Purpose: Minimum time required to convert a building

    - Note: A great explanation of how this works: https://youtu.be/-qRUaOHpbwI?t=902 by T-West
    """
    CONVERT_BUILDING_MAX = 181
    """
    - Purpose: Maximum time required to convert a building

    - Note: A great explanation for how this works: https://youtu.be/-qRUaOHpbwI?t=902 by T-West
    """
    CONVERT_BUILDING_CHANCE = 182
    """
    - Purpose: Percent chance for monks to convert buildings

    - Note: A great explanation for how this works: https://youtu.be/-qRUaOHpbwI?t=902 by T-West
    """
    REVEAL_ENEMY = 183
    """
    - Purpose: Boolean: show enemy los for the source player

    - Default Values:

        - 0:  No (default)

        - 1:  Yes, after Spies

    - Note: Once set to `1`, setting it back to `0` won't take away LoS of enemies!
    """
    VALUE_WONDERS_CASTLES = 184
    """
    - Purpose: Total cost of all wonders and castles constructed
    """
    FOOD_SCORE = 185
    """
    - Purpose: Unknown... what does this resource do?
    """
    WOOD_SCORE = 186
    """
    - Purpose: Unknown... what does this resource do?
    """
    STONE_SCORE = 187
    """
    - Purpose: Unknown... what does this resource do?
    """
    GOLD_SCORE = 188
    """
    - Purpose: Unknown... what does this resource do?
    """
    CHOPPING_PRODUCTIVITY = 189
    """
    - Purpose: Multiplier for wood chopped by lumberjacks

    - Default Values:

        - 1:  Generic

        - 1.15:  Mayans

    - Note: Since this works by multiplying the amount of resources gathered by a villager, it has a side effect of increasing the gather rate. In the case of Mayans, This is compensated for by reducing villager work rate by 15%
    """
    FOOD_GATHERING_PRODUCTIVITY = 190
    """
    - Purpose: Multiplier for food gathered from all sources

    - Default Values:

        - 1:  Generic

        - 1.15:  Mayans

    - Note: Since this works by multiplying the amount of resources gathered by a villager, it has a side effect of increasing the gather rate. In the case of Mayans, This is compensated for by reducing villager work rate by 15%. The work rate for farmers is reduced by about 23.4%
    """
    RELIC_GOLD_PRODUCTION_RATE = 191
    """
    - Purpose: Relic gold generation rate in gold per second

    - Default Values:

        - 0.5:  default

        - 0.25:  after getting hit with Atheism 
    """
    CONVERTED_UNITS_DIE = 192
    """
    - Purpose: Boolean: converted units die instead of switching over to the enemy

    - Default Values:

        - 0:  No (default)

        - 1:  Yes, after Heresey
    """
    THEOCRACY = 193
    """
    - Purpose: Boolean: only one monk needs to regen faith after group conversion for the source player

    - Default Values:

        - 0:  No (default)

        - 1:  Yes, after researching Theocracy
    """
    CRENELLATIONS = 194
    """
    - Purpose: Boolean: Garrisoned infantry fire arrows

    - Default Values:

        - 0:  No (default)

        - 1:  Yes, after crenellations
    """
    CONSTRUCTION_RATE_MODIFIER = 195
    """
    - Purpose: Builder work rate multiplier

    - Default Values:

        - 0:  Generic

        - 1.3:  Spanish

    - Note: The actual work rate for builders is given by `construction_rate_mod * builder.default_work_rate`
    """
    HUN_WONDER_DISCOUNT = 196
    """
    - Purpose: Additional time required for relic/wonder victories in one tenth of a year

    - Default Values:

        - 0:  default

        - 1000:  (100 years) for the Hun player, after researching atheism. The value of this resource of each player is added to determine the total extra time for relic/wonder victories, i.e. it adds up if multiple hun players get the tech

    - Note: Internally, relic and wonder victory countdowns are measured in one tenths of an year, the fractional part is just not shown ingame
    """
    SPIES_DISCOUNT = 197
    """
    - Purpose: Boolean: Halves the cost of spies per villager, and caps it at 15k gold max instead of the usual 30k.

    - Default Values:

        - 0:  Default
    """
    UNUSED_RESOURCE_198 = 198
    """
    - Purpose: Unused
    """
    UNUSED_RESOURCE_199 = 199
    """
    - Purpose: Unused
    """
    UNUSED_RESOURCE_200 = 200
    """
    - Purpose: Unused
    """
    UNUSED_RESOURCE_201 = 201
    """
    - Purpose: Unused
    """
    UNUSED_RESOURCE_202 = 202
    """
    - Purpose: Unused
    """
    UNUSED_RESOURCE_203 = 203
    """
    - Purpose: Unused
    """
    UNUSED_RESOURCE_204 = 204
    """
    - Purpose: Unused
    """
    FEITORIA_FOOD_PRODUCTIVITY = 205
    """
    - Purpose: Feitoria food production rate multiplier

    - Default Values:

        - 1:  Generic

    - Note: The amount of food obtained from owning `n` number of Feitorias is given by `n * feitoria_food_productivity * 1.6`
    """
    FEITORIA_WOOD_PRODUCTIVITY = 206
    """
    - Purpose: Feitoria wood production rate multiplier

    - Default Values:

        - 1:  Generic

    - Note: The amount of wood obtained from owning `n` number of Feitorias is given by `n * feitoria_wood_productivity * 1`
    """
    FEITORIA_STONE_PRODUCTIVITY = 207
    """
    - Purpose: Feitoria stone production rate multiplier

    - Default Values:

        - 1:  Generic

    - Note: The amount of stone obtained from owning `n` number of Feitorias is given by `n * feitoria_stone_productivity * 0.3`
    """
    FEITORIA_GOLD_PRODUCTIVITY = 208
    """
    - Purpose: Feitoria gold production rate multiplier

    - Default Values:

        - 1:  Generic

    - Note: The amount of gold obtained from owning `n` number of Feitorias is given by `n * feitoria_gold_productivity * 0.7`
    """
    REVEAL_ENEMY_TOWN_CENTERS = 209
    """
    - Purpose: Boolean: reveal enemy town centre location for the source player

    - Default Values:

        - 0:  Generic

        - 5:  Vietnamese

    - Note: The bonus works for all values >=1, the choice of setting it to 5 for vietnamese seems arbitrary
    """
    RELICS_VISIBLE_ON_MAP = 210
    """
    - Purpose: Boolean: reveal relics on map amount

    - Default Values:

        - -1:  Generic

        - 42:  Burmese

    - Note: Burmese reveal relics on map bonus. Only works in RMS, manually changing this in the editor does not seem to have any effects
    """
    ELEVATION_HIGHER_BONUS = 211
    """
    - Purpose: The fraction for additional bonus damage dealt from higher elevation

    - Default Values:

        - 0:  Generic

        - 0.25:  Tatars

    - Note: Damage that units on higher elevation deal to units on lower elevation is multiplied by `1.25 + elevation_bonus_higher`
    """
    ELEVATION_LOWER_BONUS = 212
    """
    - Purpose: The fraction for additional bonus damage dealt from lower elevation

    - Default Values:

        - 0:  Generic

    - Note: Damage that units on lower elevation deal to units on higher elevation is multiplied by `0.75 + elevation_bonus_lower`
    """
    RAIDING_PRODUCTIVITY = 213
    """
    - Purpose: Keshik gold generation rate per 100 seconds

    - Default Values:

        - 0:  Generic

        - 50:  (0.5 g/s) Tatars

    - Note: Note that in practice, due to attack reload time and frame delay, Keshiks don't actually produce 0.5 g/s, but a slightly lower value
    """
    MERCENARY_KIPCHAK_COUNT = 214
    """
    - Purpose: Total number of mercenary kipchak creatable

    - Default Values:

        - 0:  Generic

        - 10:  after a Cuman ally researches Cuman Mercenaries

    - Note: Researching Cuman Mercenaries sets this to 10. Making mercenary Kipchaks costs one unit of this resource
    """
    MERCENARY_KIPCHAK_LIMIT = 215
    """
    - Purpose: Number of mercenary kipchaks created/queued

    - Note: Making mercenary Kipchaks gives one unit of this resource
    """
    SHEPHERD_PRODUCTIVITY = 216
    """
    - Purpose: Amount of food collected from sheep multiplier

    - Default Values:

        - 1:  Generic

        - 1.57:  Tatars

    - Note: Since this works by multiplying the amount of resources gathered by a villager, it has a side effect of increasing the gather rate. In the case of Tatars, This is compensated for by reducing villager work rate by 57%
    """
    SHARED_LINE_OF_SIGHT = 217
    """
    - Purpose: Unknown... what does this resource do?
    """
    FEUDAL_TOWN_CENTER_LIMIT = 218
    """
    - Purpose: This is the number of extra TCs a player is allowed to build IF TCs are enabled in feudal age.

    - Default Values:

        - 10002.1:  Generic

        - 2.1:  Cumans

    - Note: Since generic civs don't get access to TCs in feudal, the 10k amount doesn't matter, but if you're trying to make a map where you want people to be able to make TCs in feudal, make sure to set this value to 10k for cumans!
    """
    FISHING_PRODUCTIVITY = 219
    """
    - Purpose: Multiplier for food gathered by fishing ships

    - Default Values:

        - 1:  Generic

    - Note: Since this works by multiplying the amount of resources gathered by a fishing ship, it has a side effect of increasing the gather rate
    """
    UNUSED_RESOURCE_220 = 220
    """
    - Purpose: Unused
    """
    MONUMENT_FOOD_PRODUCTIVITY = 221
    """
    - Purpose: Monument food trickle rate multiplier

    - Default Values:

        - 1:  In KoTH games

    - Note: The amount of resources obtained by owning a monument is `0.7925 * food_trickle_from_monument`
    """
    MONUMENT_WOOD_PRODUCTIVITY = 222
    """
    - Purpose: Monument wood trickle rate multiplier

    - Default Values:

        - 1:  In KoTH games

    - Note: The amount of resources obtained by owning a monument is `0.7925 * wood_trickle_from_monument`
    """
    MONUMENT_STONE_PRODUCTIVITY = 223
    """
    - Purpose: Monument stone trickle rate multiplier

    - Default Values:

        - 1:  In KoTH games

    - Note: The amount of resources obtained by owning a monument is `0.7925 * stone_trickle_from_monument`
    """
    MONUMENT_GOLD_PRODUCTIVITY = 224
    """
    - Purpose: Monument gold trickle rate multiplier

    - Default Values:

        - 1:  In KoTH games

    - Note: The amount of resources obtained by owning a monument is `0.7925 * gold_trickle_from_monument`
    """
    RELIC_FOOD_PRODUCTION_RATE = 225
    """
    - Purpose: Relic food production per minute

    - Default Values:

        - 0:  Generic

        - 30:  Burgundians

        - 15:  Burgundians after getting hit with Atheism
    """
    VILLAGERS_KILLED_BY_GAIA = 226
    """
    - Purpose: Total number of villagers lost to gaia
    """
    VILLAGERS_KILLED_BY_ANIMALS = 227
    """
    - Purpose: Total number of villagers lost to wild animals
    """
    VILLAGERS_KILLED_BY_AL_PLAYER = 228
    """
    - Purpose: Total number of villagers lost to AIs
    """
    VILLAGERS_KILLED_BY_HUMAN_PLAYER = 229
    """
    - Purpose: Total number of villagers lost to human players
    """
    FOOD_GENERATION_RATE = 230
    """
    - Purpose: Free food trickle rate (per minute)
    """
    WOOD_GENERATION_RATE = 231
    """
    - Purpose: Free wood trickle rate (per minute)
    """
    STONE_GENERATION_RATE = 232
    """
    - Purpose: Free stone trickle rate (per minute)
    """
    GOLD_GENERATION_RATE = 233
    """
    - Purpose: Free gold trickle rate (per minute)
    """
    SPAWN_LIMIT = 234
    """
    - Purpose: The limit to the number of spawning buildings that can spawn units from spawn command in a technology

    - Note: This is usually overridden by techs
    """
    FLEMISH_MILITIA_POPULATION = 235
    """
    - Purpose: Number of alive flemish militia
    """
    FARMING_GOLD_PRODUCTIVITY = 236
    """
    - Purpose: Farming gold generation rate per 100 seconds

    - Default Values:

        - 0:  Generic

        - 2:  (0.02 g/s per farmer) after Burgundian Vineyards
    """
    FOLWARK_COLLECTION_AMOUNT = 237
    """
    - Purpose: This is the amount of food collected from farms built around a folwark

    - Default Values:

        - 0:  Generic

        - 17.5:  Poles

        - 19.25:  Poles with Chinese Ally

        - 25:  Poles with Horse Collar

        - 27.5:  Poles with Horse Collar & Chinese Ally

        - 37.5:  Poles with Heavy Plow

        - 41.25:  Poles with Heavy Plow & Chinese Ally

        - 55:  Poles with Crop Rotation

        - 60.5:  Poles with Crop Rotation & Chinese Ally
    """
    FOLWARK_ATTRIBUTE_TYPE = 238
    """
    - Purpose: This is the ID of the resource that is given when a farm is constructed around a folwark

    - Default Values:

        - 0:  Poles

        - -1:  Generic
    """
    FOLWARK_BUILDING_TYPE = 239
    """
    - Purpose: This is the ID of the building that the Folwark needs to upgrade from for the farm collection ability to work

    - Default Values:

        - 68:  (Mill) Poles

        - -1:  Generic
    """
    UNITS_CONVERTED = 240
    """
    - Purpose: The amount of units lost to enemy conversions
    """
    STONE_MINING_GOLD_PRODUCTIVITY = 241
    """
    - Purpose: Stone mining gold generation rate per 100 seconds

    - Default Values:

        - 0:  Generic

        - 18:  Poles

        - 20.7:  Poles with Stone Mining

        - 23.805:  Poles with Stone Shaft Mining
    """
    TRADE_WORKSHOP_FOOD_PRODUCTIVITY = 242
    """
    - Purpose: Trade Workshop food production rate multiplier

    - Default Values:

        - 1:  Generic

    - Note: The amount of food obtained from owning `n` number of TWS (Unit 1647) is given by `n * tws_food_productivity * 2.25`.
    """
    TRADE_WORKSHOP_WOOD_PRODUCTIVITY = 243
    """
    - Purpose: Trade Workshop wood production rate multiplier

    - Default Values:

        - 1:  Generic

    - Note: The amount of wood obtained from owning `n` number of TWS (Unit 1647) is given by `n * tws_wood_productivity * 2.25`.
    """
    TRADE_WORKSHOP_STONE_PRODUCTIVITY = 244
    """
    - Purpose: Trade Workshop stone production rate multiplier

    - Default Values:

        - 0:  Generic

    - Note: The amount of stone obtained from owning `n` number of TWS (Unit 1647) is given by `n * tws_stone_productivity * 2.25`.
    """
    TRADE_WORKSHOP_GOLD_PRODUCTIVITY = 245
    """
    - Purpose: Trade Workshop gold production rate multiplier

    - Default Values:

        - 1:  Generic

    - Note: The amount of gold obtained from owning `n` number of TWS (Unit 1647) is given by `n * tws_gold_productivity * 2.25`.
    """


class ObjectType(_DataSetIntEnums):
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


class ObjectClass(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the object class in the game. Used in a lot of effects
    and conditions, like 'Kill Object', 'Objects in Area' under the name 'Object Group'.

    **Examples**

    >>> ObjectClass.CIVILIAN
    <ObjectClass.CIVILIAN: 4>
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


class TerrainRestrictions(_DataSetIntEnums):
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


class HeroStatusFlag(_DataSetIntFlags):
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


class BlastLevel(_DataSetIntEnums):
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


class SmartProjectile(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the smart projectile flag values used in the game. Used in the
    'Modify Attribute' effect with the 'Enable Smart Projectile' attribute

    **Examples**

    >>> SmartProjectile.ENABLED
    <SmartProjectile.ENABLED: 1>
    """
    ENABLED = 1
    FULL_DAMAGE_ON_MISSED_HIT = 2


class DamageClass(_DataSetIntEnums):
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


class Hotkey(_DataSetIntEnums):
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


class ColorMood(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the color mood values used in the game. Used in the
    'Change Color Mood' effect

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


class ObjectState(_DataSetIntEnums):
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


class Age(_DataSetIntEnums):
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


class ActionType(_DataSetIntEnums):
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


class SecondaryGameMode(_DataSetIntFlags):
    """
    This enum class provides the integer values for the different secondary game modes.

    **Examples**

    >>> SecondaryGameMode.EMPIRE_WARS
    <SecondaryGameMode.EMPIRE_WARS: 1>
    >>> SecondaryGameMode.SUDDEN_DEATH | SecondaryGameMode.REGICIDE
    <HeroStatusFlag.SUDDEN_DEATH|REGICIDE: 6>
    """

    @staticmethod
    def combine(
            empire_wars: bool = False,
            sudden_death: bool = False,
            regicide: bool = False,
            king_of_the_hill: bool = False,
    ) -> SecondaryGameMode:
        """
        This method combines the given hero status flags into an integer value

        Args:
            empire_wars (bool): If empire wars should be enabled
            sudden_death (bool): If sudden death should be enabled
            regicide (bool): If regicide should be enabled
            king_of_the_hill (bool): If king of the hill should be enabled

        Returns:
            An integer combining all the different hero status flags into one value
        """
        total = 1 if empire_wars else 0
        total += 2 if sudden_death else 0
        total += 4 if regicide else 0
        total += 8 if king_of_the_hill else 0
        return SecondaryGameMode(total)

    EMPIRE_WARS = 1
    SUDDEN_DEATH = 2
    REGICIDE = 4
    KING_OF_THE_HILL = 8
