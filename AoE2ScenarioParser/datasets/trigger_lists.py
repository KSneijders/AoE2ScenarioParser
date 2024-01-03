from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Dict

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
    EXTREME = -1
    """
    The only exception in the entire scenario where the value -1 is NOT an unselected/invalid value. 
    This might cause issues in the parser, please report them if you find any.
    """


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
    """
    This attribute refers to the health of the units
    """
    LINE_OF_SIGHT = 1
    """
    This is the distance a unit can see around itself
    """
    GARRISON_CAPACITY = 2
    """
    This is the amount of units that can garrison inside another unit
    """
    UNIT_SIZE_X = 3
    """
    This determines the x-size of the unit's collision hitbox (width of the unit)
    """
    UNIT_SIZE_Y = 4
    """
    This determines the y-size of the unit's collision hitbox (length of the unit)
    """
    MOVEMENT_SPEED = 5
    """
    This is the movement speed of a unit, measured in tiles per second
    """
    ROTATION_SPEED = 6
    """
    This is the rate at which units can rotate, measured in seconds per frame (this many seconds must pass before the object can switch to the next rotation frame). For example, for a trebuchet to start attacking a building facing the opposite direction, it has to rotate to face that way first
    """
    ARMOR = 8
    """
    This is the quantity of armour a unit has on any of its `Armour Classes`. Note that changing the armour through this option will show it as being added to the base armour amount. (for example: 4+4)
    """
    ATTACK = 9
    """
    This is the quantity of attack a unit has on any of its `Attack Classes`. Note that changing the attack through this option will show it as being added to the base attack amount. (for example: 6+2)
    """
    ATTACK_RELOAD_TIME = 10
    """
    This is the minimum time that must pass before a unit is able to fire another shot. For melee units it is the minimum time between two successive hits that they can do
    """
    ACCURACY_PERCENT = 11
    """
    This determines how accurately a unit can aim at another unit

    - Notes:

        This accuracy is the accuracy of a unit to fire at the exact centre of its target. If the shot fired is not aimed at the exact centre of the target, it may still hit the target if its not off by too much since it can still land within the hitbox of the target, just not at the exact centre
        Thus, bigger targets are actually easier to hit, which explains why buildings are an easier target to hit for trebuchets than small units
        In this image, you can see that shots that were fired in the red area in the 2nd scenario would've hit if the target had been closer like in the first scenario, but since the target is far away, they actually miss
        More technically, the visual angle of an object of the same size that is farther away is smaller, thus giving a smaller room for error for the shot in terms of the range of angles that will make the shot hit
        The chance of a unit getting converted by a monk is also determined by its accuracy
        If you modify an onager to have a big blast radius and give it a small accuracy, then attack a lot of units bunched together, the accuracy determines what percentage of units take damage from the blast of the onager! This is the reason why warwolf trebuchets get 100% accuracy because otherwise the blast wouldn't damage all of the units. Another interesting consequence of this is the delete trick with onagers and mangonels. This is where a mangonel is deleted immediately after it fires its shot and because a dead unit doesn't have an accuracy, it defaults to 100% and thus deals more damage to all the units in the blast radius
        
        There are two other factors that play a role in determining the damage from the shot fired by the deleted mangonel
        
        1. The damage from a mangonel's shot is decreased over distance when moving outward from the centre of the blast (the targeted point). However, when the mangonel is deleted, this decrease over distance doesn't happen, and the projectile deals the full 100% damage to all the units in the blast radius!
        2. A shot that is fired from lower elevation would normally deal only 75% of its normal damage due to the elevation damage reduction. deleting a mangonel in this case also makes the damage the full 100% as if there was no elevation difference
    """
    MAX_RANGE = 12
    """
    This is the maximum range of a unit. Note that to be able to shoot at a target, it must be visible to the unit via its own line of sight or from another unit's line of sight
    """
    WORK_RATE = 13
    """
    This is the work rate for any unit that can do work. Villagers, Fishing Ships, Serjeants
    """
    CARRY_CAPACITY = 14
    """
    This is the carry capacity of Villagers
    """
    BASE_ARMOR = 15
    """
    This is the quantity of base armour a unit has on any of its `Armour Classes`. Note that changing the armour through this option will show it as the base armour itself, and it will not be added to the regular amount
    """
    PROJECTILE_UNIT = 16
    """
    This is the ID of the projectile that a unit fires
    """
    BUILDING_ICON_OVERRIDE = 17
    """
    The functionality of this attribute is unknown as it doesn't always behave certainly.
    """
    TERRAIN_DEFENSE_BONUS = 18
    """
    Unknown... What does this attribute do?
    """
    PROJECTILE_SMART_MODE = 19
    """
    This is a combinable bit field. Controls the following two behaviours for projectiles:

    - Flags:

        - 0: No Ballistics
        - 1: Has Ballistics
        - 2: Deals full damage on missed hit

    - Notes:

        For example, if we set this property of the projectile used by an archer to `1`, it will have ballistics. (This is exactly what researching ballistics does in the first place). If we set this property to `2`, a missed projectile that hits another unit will deal its full damage instead of the 50% that it would normally do
        What if we want to enable both properties at once? This is achieved by adding the flag values for both of them together. Setting this property to `3` enables both effects
    """
    MINIMUM_RANGE = 20
    """
    The minimum distance a unit must be from an attacking unit for the attacking unit to be able to fire its projectile
    """
    AMOUNT_OF_1ST_RESOURCE_STORAGE = 21
    """
    This is the amount of 1st resource contained in any unit. Refer to A.G.E. to see which resource this is for each unit
    """
    BLAST_WIDTH = 22
    """
    All enemy units inside this radius take damage from an attacking unit. This is used by elephants, Druzhina Halberdiers, and Logistica Cataphracts
    """
    SEARCH_RADIUS = 23
    """
    The maximum distance at which a unit can detect and auto attack enemy units
    """
    BONUS_DAMAGE_RESISTANCE = 24
    """
    Used by Sicilians for the 33% bonus damage resistance. Set to 0.33 for all Sicilian land military units except siege

    - Notes:

        Do not make it greater than 1
    """
    ICON_ID = 25
    """
    The ID of the icon that you want a unit to show
    """
    AMOUNT_OF_2ND_RESOURCE_STORAGE = 26
    """
    This is the amount of 2nd resource contained in any unit. Refer to A.G.E. to see which resource this is for each unit
    """
    AMOUNT_OF_3RD_RESOURCE_STORAGE = 27
    """
    This is the amount of 3rd resource contained in any unit. Refer to A.G.E. to see which resource this is for each unit
    """
    FOG_VISIBILITY = 28
    """
    Controls visibility of a unit through the fog of war

    - Flags:

        - 0: Not Visible
        - 1: Always Visible
        - 2: Visible If Alive
        - 3: Inverted Visibility
        - 4: Check Doppelganger
    """
    OCCLUSION_MODE = 29
    """
    This is a combinable bit field. Controls the outlines of units as seen through other units

    - Flags:

        - 0: No outline
        - 1: Display outline when behind other units that have flag 2
        - 2: Other units' outlines are rendered when they are behind this unit
        - 4: Display outline on this unit's foundation when behind other units that have flag 2
    """
    GARRISON_TYPE = 30
    """
    This is a combinable bit field. Controls which units are able to garrison in a building. A unit needs to have the garrison in building task to be able to garrison in a building to begin with

    - Flags:

        - 1: Villagers
        - 2: Infantry
        - 4: Cavalry
        - 8: Monks
        - 16: Herdables
        - 32: Siege
        - 64: Ships
    """
    UNIT_SIZE_Z = 32
    """
    This determines the z-size of the unit's collision hitbox (height of the unit)

    - Notes:

        Setting this to 0 allows other units to walk over this unit
        Does this still control the HP bar location as specified in A.G.E.?
    """
    CAN_BE_BUILT_ON = 33
    """
    Determines if a building foundation can be placed on top of a unit

    - Flags:

        - 0: Disallow unit to be built on. This is the value for almost all units
        - 1: Allow unit to be built on. This is the value for corpses, rubble, eye candy
    """
    FOUNDATION_TERRAIN = 34
    """
    This is the ID of the terrain created under a building when its construction is finished

    - Flags:

        - -1: No terrain change

    - Notes:

        Only affects units of Type 80 (Building)

    """
    HERO_STATUS = 40
    """
    This is a combinable bit field. Controls the following properties:

    - Flags:

        - 1: Full Hero Status
        - 2: Cannot be Converted
        - 4: Self Regeneration (30 HP/min)
        - 8: Defensive Stance by Default
        - 16: Protected Formation by Default
        - 32: Safe Delete Confirmation
        - 64: Hero Glow
        - 128: Invert All Flags (except flag 1)

    - Notes:

        For example, if we set the hero status of a knight to 2, a monk will not be able to convert it. If we set the hero status of a militia to 4, it will regenerate HP automatically
        What if we want to enable multiple properties at once? This is achieved by adding the flag values for those properties together and setting the hero status to that value. For example, if we want to make a paladin both unconvertable and regenerate HP automatically, we can set its hero status to 2+4 = 6. This means that the hero status of a unit can take on any values in the range 1-63. If you set it to any other value, it does not have any effect on the unit
        This works because notice that there is one and only one way to add different flag values together to obtain a particular value for the hero status! For example, if we have a value of 20 for the hero status of a unit, the only way to make 20 from the above flag values is to add 4 and 16. Thus, we know that the properties corresponding to the flag values 4 (self regeneration) and 16 (protected formation by default) must be enabled for that unit
        This is a consequence of the fact that every number can be represented as a unique sum of powers of two (binary numbers)
    """
    FRAME_DELAY = 41
    """
    The amount of delay between the point when the attacking animation starts and the actual hit happening for military units. This is what makes Cavalry Archers annoying to micro
    """
    TRAIN_LOCATION = 42
    """
    The ID of the unit that trains any given unit. Barracks train Militia, so the train location of a Militia is the ID of the Barracks
    """
    TRAIN_BUTTON = 43
    """
    The button used for training any given unit. For example, Militia are trained by using the first button, hence the Button Location of Militia is 1. This number ranges from 0-15
    """
    BLAST_ATTACK_LEVEL = 44
    """
    A unit deals blast damage to ***other*** units with ***equal or higher*** [Blast Defense Level](./#45-blast-defense-level "Jump to: Blast Defense Level") that are in its blast radius. For example, while mangonels (blast attack: 2) can damage your own units (blast defense of all player owned units is always 2), scorpions (blast attack: 3) cannot do the same

    - Flags:

        - 0: damage resources, nearby allied units and tress
        - 1: damage trees, nearby allied units
        - 2: damage nearby and allied units
        - 3: damage targeted unit only
        - 4: damage enemy units only
        - 64: Attenuate damage as distance from the centre of attack increases (infantry only)
        - 128: Blast damage is dealt along the direction the unit is facing only. This area is a very narrow cone

    - Notes:

        One of the flags 0-3 can be combined with the combinable flags 4 to 128 by adding the two values
    """
    BLAST_DEFENSE_LEVEL = 45
    """
    A unit feels the blast damage from ***other*** units with ***equal or lower*** [Blast Attack Level](./#44-blast-attack-level "Jump to: Blast Attack Level") and if it is inside the attacker's blast radius. For example, while onagers (blast attack: 1) can cut trees (blast defense 1), mangonels (blast attack: 2) cannot do the same

    - Flags:

        - 0: damage resources, nearby allied units and tress
        - 1: damage trees, nearby allied units
        - 2: damage nearby allied units
        - 3: damage targeted unit only
    """
    SHOWN_ATTACK = 46
    """
    The amount of attack that is displayed as a unit's attack (may not actually be the true attack)
    """
    SHOWN_RANGE = 47
    """
    The quantity that is displayed as a unit's attack ingame (may not actually be the true attack)
    """
    SHOWN_MELEE_ARMOR = 48
    """
    The quantity that is displayed as a unit's melee armour ingame (may not actually be the true armour)
    """
    SHOWN_PIERCE_ARMOR = 49
    """
    The quantity that is displayed as a unit's pierce armour ingame (may not actually be the true armour)
    """
    OBJECT_NAME_ID = 50
    """
    The string ID to use for the name of an object. A string ID is used for refering to strings that the game recognises by default. It can be used to automatically set names by using a value that the game recognises. Trying out the value 1 on a unit and seeing what happens is left as an excersise for the reader
    """
    SHORT_DESCRIPTION_ID = 51
    """
    The string ID for the Short Description of an object. A string ID is used for refering to strings that the game recognises by default. It can be used to automatically set a Short Description by using a value that the game recognises. Trying out the value 1 on a unit and seeing what happens is left as an excersise for the reader
    """
    TERRAIN_RESTRICTION_ID = 53
    """
    This number determines how a unit interacts with terrains and which terrains it can walk on

    - Flags:

        - 0: All
        - 1: Land And Shallows
        - 2: Beach
        - 3: Water Small Trail
        - 4: Land
        - 5: Nothing
        - 6: Water No Trail
        - 7: All Except Water
        - 8: Land Except Farm
        - 9: Nothing 2
        - 10: Land And Beach
        - 11: Land Except Farm 2
        - 12: All Except Water Bridge Cannon
        - 13: Water Medium Trail
        - 14: All Except Water Bridge Arrow
        - 15: Water Large Trail
        - 16: Grass And Beach
        - 17: Water And Bridge Except Beach
        - 18: All Except Water Bridge Spear
        - 19: Only Water And Ice
        - 20: All Except Water Wheel
        - 21: Shallow Water
        - 22: All Dart
        - 23: All Arrow Fire
        - 24: All Cannon Fire
        - 25: All Spear Fire
        - 26: All Dart Fire
        - 27: All Laser
        - 28: All Except Water Cavalry
        - 29: All Except Water Packet Trebuchet
        - 30: Water Smallest Trail
    """
    UNIT_TRAIT = 54
    """
    This is a combinable bit field. Controls the following properties:

    - Flags:

        - 1: Garrison Unit
        - 2: Ship Unit
        - 4: Build Another Building (Serjeants)
        - 8: Transform Into Another Unit (Ratha)
        - 16: Auto Scout Unit

    - Notes:

        See Also:

    [Trait Piece](./#56-trait-piece)
    """
    TRAIT_PIECE = 56
    """
    This can be set to the ID of a unit that is used along with some of the Unit Traits

    - Flags:

        - 1: Unused
        - 2: Unused
        - 4: Build Unit
        - 8: Transform Unit
        - 16: Unused

    - Notes:

        See Also:

    [Unit Trait](./#54-unit-trait)
    """
    DEAD_UNIT_ID = 57
    """
    This is the ID of the unit to spawn after the current unit dies. This is whats used to make the dismounted konniks possible
    """
    HOTKEY_ID = 58
    """
    This number determines which hotkey is assigned to a unit
    """
    MAXIMUM_CHARGE = 59
    """
    The maximum amount of charge that a unit can hold
    """
    RECHARGE_RATE = 60
    """
    The rate of charge regeneration per second
    """
    CHARGE_EVENT = 61
    """
    This action depletes the unit's charge

    - Flags:

        - 1: If charge type is set to `1`, `2` or `3`, depletes charge on attacking
    """
    CHARGE_TYPE = 62
    """
    The type of charge that a unit holds

    - Flags:

        - 1: Attack charge
        - 2: ??? charge
        - 3: Area attack charge
        - 4: Agility charge
    """
    COMBAT_ABILITY = 63
    """
    Combinable bit field. Controls several attacking behaviours for units

    - Flags:

        - 1: Ignore melee and pierce armours of the targeted unit
        - 2: Resist armour-ignoring attacks
        - 4: Damage the targeted unit's armor (Obuch)
        - 8: Attack ground ability
        - 16: Bulk volley release (kipchak/siege weapons)
        - 32: Enable task 155 ability (Stronghold castle/Caravanserai/Centurion)
    """
    ATTACK_DISPERSION = 64
    """
    Half of the radius from the target unit in which missed projectiles fired by this unit can land in
    """
    SECONDARY_PROJECTILE_UNIT = 65
    """
    This is the ID of the secondary projectile that a unit fires (Chu Ko Nu)
    """
    BLOOD_UNIT = 66
    """
    This is the ID of a secondary unit to spawn after the current unit dies. This could potentially be used along with dead unit ID to spawn two units after a single unit dies
    """
    PROJECTILE_HIT_MODE = 67
    """
    Controls how a projectile collides with units in the path of its target. Currently changing this through XS has no effect

    - Flags:

        - 0: Collide only with the targeted unit
        - 1: Collide with any damage-able units in the path to the targetted unit
        - 2: Collide with any unit in the path to the targetted unit
    """
    PROJECTILE_VANISH_MODE = 68
    """
    Controls if a projectile passes through or disappears on impact. Currently changing this through XS has no effect

    - Flags:

        - 0: Disappear on first impact
        - 1: Pass through
    """
    PROJECTILE_ARC = 69
    """
    Controls the maximum height of the fired projectile
    """
    ATTACK_GRAPHIC = 70
    """
    Controls the Attack Graphic
    """
    STANDING_GRAPHIC = 71
    """
    The sprite animation shown when a unit is idle

    - Notes:

        Units randomly choose between this or Standing Graphic 2
    """
    STANDING_GRAPHIC_2 = 72
    """
    The sprite animation shown when a unit is idle

    - Notes:

        Units randomly choose between this or Standing Graphic
    """
    DYING_GRAPHIC = 73
    """
    The sprite animation shown when a unit dies
    """
    UNDEAD_GRAPHIC = 74
    """
    This graphic is shown after a unit's dying animation instead of replacing it with its dead unit if its "Undead Mode" is set to `1`

    - Notes:

        Requires "Undead Mode" to be set to `1`
    """
    WALKING_GRAPHIC = 75
    """
    The sprite animation shown when a unit is walking
    """
    RUNNING_GRAPHIC = 76
    """
    The sprite animation shown when a unit is running

    - Notes:

        A unit runs when it is issued an attack command, or when a unit is fleeing (deer-like units)
        Most units do not have a running graphic
        A graphic can multiply the speed of the unit it is applied to
        This is used for deer, wolves, boars, etc. when they are issued an attack command
    """
    SPECIAL_GRAPHIC = 77
    """
    This sprite animation is shown  when a unit uses one of "Block", "Charge", or "Counter Charge" special abilities

    - Notes:

        Special abilities are an unused feature in AoE2, they were planned but never made it into AoK
    """
    RESOURCE_COSTS = 100
    """
    Refers to the first resource cost of a unit. Refer to A.G.E. to see which resource cost that is
    """
    TRAIN_TIME = 101
    """
    This is the amount of time it takes to create a unit
    """
    TOTAL_MISSILES = 102
    """
    This is the number of projectiles a unit fires. The Chu Ko Nu fires 3 and the Elite Chu Ko Nu fires 5
    """
    FOOD_COSTS = 103
    """
    The food cost of a unit
    """
    WOOD_COSTS = 104
    """
    The wood cost of a unit
    """
    GOLD_COSTS = 105
    """
    The gold cost of a unit
    """
    STONE_COSTS = 106
    """
    The stone cost of a unit
    """
    MAX_TOTAL_MISSILES = 107
    """
    The maximum number of projectiles a unit can fire when other units are garrisoned inside of it. A castle fires 5 projectiles by default but can fire more if units are garrisoned inside it. This attribute controls the maximum number of those
    """
    GARRISON_HEAL_RATE = 108
    """
    The rate measured in HP/s at which garissoned units are healed inside a given building
    """
    REGENERATION_RATE = 109
    """
    The rate measured in HP/minute at which units heal themselves. This value is overridden to 30 HP/minute if the flag for Self Regeneration is set in the [Hero Status](./#40-hero-status "Jump to: 26. Hero Status") of a unit
    """
    POPULATION = 110
    """
    Modifies the population headroom storage of a unit. Negative values = require population (units), positive values = give population (houses). This is not a real attribute that exists in A.G.E., just seems like a way to edit the population heardroom provided by a unit
    """
    MINIMUM_CONVERSION_TIME_MODIFIER = 111
    """
    Adds to the minimum time required to convert the unit

    - Notes:

        By default, units have a 4 monk second minimum conversion time
        The overall minimum conversion time for all units is also affected by [Convert Resist Min Adjustment](../../resources/resources/#178-convert-resist-min-adjustment)
    """
    MAXIMUM_CONVERSION_TIME_MODIFIER = 112
    """
    Adds to the maximum time after which a unit conversion is forced

    - Notes:

        By default, units have a 10 monk second maximum conversion time
        The overall maximum conversion time for all units is also affected by [Convert Resist Max Adjustment](../../resources/resources/#179-convert-resist-max-adjustment)
    """
    CONVERSION_CHANCE_MODIFIER = 113
    """
    The probability of conversion every monk second is divided by this value for the unit

    - Notes:

        The overall conversion probability for all units is also affected by [Conversion Resistance](../../resources/resources/#77-conversion-resistance)
    """
    FORMATION_CATEGORY = 114
    """
    Control where the units in formation

    - Flags:

        - 0: Not using formation
        - 1: Mobile
        - 2: Body
        - 3: Ranged
        - 4: Long Ranged
        - 5: Protected
    """
    AREA_DAMAGE = 115
    """
    Blast damage multiplier to non directly targeted units. Blast damage to non directly targeted units is a fixed value if this is negative
    """


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

    - Defaults:

        - 0: Dark Age
        - 1: Feudal Age
        - 2: Castle Age
        - 3: Imperial Age

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

    - Defaults:

        - 0: No (default)
        - >= 1: Yes, after Atonement
    """
    ENABLE_BUILDING_CONVERSION = 28
    """
    - Purpose: Boolean: allow enemy building conversions

    - Defaults:

        - 0: No (default)
        - 1: Yes, after Redemption
        - >=2: Monks can convert buildings from range
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

    - Defaults:

        - 1: The unit of measurement for this rate is unknown
    """
    FARM_FOOD_AMOUNT = 36
    """
    - Purpose: Maximum farm food amount

    - Defaults:

        - 175: Default
        - 220: Chinese

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

    - Defaults:

        - 0: No
        - 1: Yes
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

    - Defaults:

        - 0: No
        - 1: Yes
    """
    TRIBUTE_INEFFICIENCY = 46
    """
    - Purpose: This is the fraction of tributes sent that are collected as tax

    - Defaults:

        - 0.3: Default
        - 0.2: After Coinage
        - 0: After Banking
    """
    GOLD_MINING_PRODUCTIVITY = 47
    """
    - Purpose: Multiplier for gold mined by gold miners

    - Defaults:

        - 1: Default
        - 1.15: Mayans

    - Note: Since this works by multiplying the amount of resources gathered by a villager, it has a side effect of increasing the gather rate. In the case of Mayans, This is compensated for by reducing villager work rate by 15%
    """
    TOWN_CENTER_UNAVAILABLE = 48
    """
    - Purpose: Boolean: allow building extra tcs

    - Defaults:

        - 0: No (Sudden Death)
        - 1: Yes (Normal)
    """
    GOLD_COUNTER = 49
    """
    - Purpose: Total gold collected
    """
    REVEAL_ALLY = 50
    """
    - Purpose: Boolean: show ally los for the source player

    - Defaults:

        - 0: No (default)
        - 1: Yes, after Cartography or with a Portuguese ally

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

    - Defaults:

        - 0: No
        - 1: Yes
    """
    ALL_RELICS_CAPTURED = 55
    """
    - Purpose: Boolean: all relics on the map captured

    - Defaults:

        - 0: No
        - 1: Yes
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

    - Defaults:

        - 0: No
        - 1: Yes (default)
    """
    HIT_POINTS_KILLED = 68
    """
    - Purpose: Cumulative hp of all units killed
    """
    KILLED_P1 = 69
    """
    - Purpose: Number of player1 units killed
    """
    KILLED_P2 = 70
    """
    - Purpose: Number of player2 units killed
    """
    KILLED_P3 = 71
    """
    - Purpose: Number of player3 units killed
    """
    KILLED_P4 = 72
    """
    - Purpose: Number of player4 units killed
    """
    KILLED_P5 = 73
    """
    - Purpose: Number of player5 units killed
    """
    KILLED_P6 = 74
    """
    - Purpose: Number of player6 units killed
    """
    KILLED_P7 = 75
    """
    - Purpose: Number of player7 units killed
    """
    KILLED_P8 = 76
    """
    - Purpose: Number of player8 units killed
    """
    CONVERSION_RESISTANCE = 77
    """
    - Purpose: Coefficient of conversion resistance

    - Defaults:

        - 0: Default

    - Note: Probability of conversion every monk second is divided by this value for ALL source player units.
    """
    TRADE_VIG_RATE = 78
    """
    - Purpose: Market exchange rate fraction for the source player

    - Defaults:

        - 0.3: Default
        - 0.15: after Guilds
        - 0.05: Saracens
    """
    STONE_MINING_PRODUCTIVITY = 79
    """
    - Purpose: Multiplier for stone mined by stone miners

    - Defaults:

        - 1: Default
        - 1.15: Mayans

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
    START_WITH_UNIT_444_PTWC = 82
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

    - Defaults:

        - 3: Default
        - 4: Mayans
        - 6: Chinese

    - Note: Only works for RMS, changing this manually in the editor does nothing
    """
    RESEARCH_COST_MODIFIER = 85
    """
    - Purpose: Multiply technology costs by this value

    - Defaults:

        - 1: Default
        - 0.9: Chinese in feudal age
        - 0.85: Chinese in castle age
        - 0.80: Chinese in imperial age
    """
    RESEARCH_TIME_MODIFIER = 86
    """
    - Purpose: Multiply technology research times by this value
    """
    CONVERT_BOATS = 87
    """
    - Purpose: Boolean: allow monks to convert boats

    - Defaults:

        - 0: No
        - 1: Yes (default)
    """
    FISH_TRAP_FOOD_AMOUNT = 88
    """
    - Purpose: Maximum fishtrap food amount

    - Defaults:

        - 710: Default
        - 2130: Malay
    """
    HEAL_RATE_MODIFIER = 89
    """
    - Purpose: Monk healing rate modifier

    - Defaults:

        - 0: The unit of measuremeant for this is unknown
    """
    HEALING_RANGE = 90
    """
    - Purpose: Monk heal range

    - Defaults:

        - 4: Tiles
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

    - Defaults:

        - 0: Default
        - 1: Allows the TC to be packed and moved
        - >=2: No noticeable effect

    - Note: Enabling kidnap/loot requires modding the units to have the kidnap/pillage action
    """
    NO_DROPSITE_FARMERS = 96
    """
    - Purpose: Enable Khmer farmer bonus

    - Defaults:

        - 0: Default
        - 1: Khmer. Farmers no longer need dropoff and steadily gain resources while farming
    """
    DOMINANT_SHEEP_CONTROL = 97
    """
    - Purpose: Boolean: force sheep conversion

    - Defaults:

        - 0: Default
        - >=1: Celts

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
    - Purpose: Amount of resources tributed to player1
    """
    P2_TRIBUTE = 103
    """
    - Purpose: Amount of resources tributed to player2
    """
    P3_TRIBUTE = 104
    """
    - Purpose: Amount of resources tributed to player3
    """
    P4_TRIBUTE = 105
    """
    - Purpose: Amount of resources tributed to player4
    """
    P5_TRIBUTE = 106
    """
    - Purpose: Amount of resources tributed to player5
    """
    P6_TRIBUTE = 107
    """
    - Purpose: Amount of resources tributed to player6
    """
    P7_TRIBUTE = 108
    """
    - Purpose: Amount of resources tributed to player7
    """
    P8_TRIBUTE = 109
    """
    - Purpose: Amount of resources tributed to player8
    """
    P1_KILL_VALUE = 110
    """
    - Purpose: Total cost of all units killed of player1
    """
    P2_KILL_VALUE = 111
    """
    - Purpose: Total cost of all units killed of player2
    """
    P3_KILL_VALUE = 112
    """
    - Purpose: Total cost of all units killed of player3
    """
    P4_KILL_VALUE = 113
    """
    - Purpose: Total cost of all units killed of player4
    """
    P5_KILL_VALUE = 114
    """
    - Purpose: Total cost of all units killed of player5
    """
    P6_KILL_VALUE = 115
    """
    - Purpose: Total cost of all units killed of player6
    """
    P7_KILL_VALUE = 116
    """
    - Purpose: Total cost of all units killed of player7
    """
    P8_KILL_VALUE = 117
    """
    - Purpose: Total cost of all units killed of player8
    """
    P1_RAZINGS = 118
    """
    - Purpose: Number of buildings destroyed of player1
    """
    P2_RAZINGS = 119
    """
    - Purpose: Number of buildings destroyed of player2
    """
    P3_RAZINGS = 120
    """
    - Purpose: Number of buildings destroyed of player3
    """
    P4_RAZINGS = 121
    """
    - Purpose: Number of buildings destroyed of player4
    """
    P5_RAZINGS = 122
    """
    - Purpose: Number of buildings destroyed of player5
    """
    P6_RAZINGS = 123
    """
    - Purpose: Number of buildings destroyed of player6
    """
    P7_RAZINGS = 124
    """
    - Purpose: Number of buildings destroyed of player7
    """
    P8_RAZINGS = 125
    """
    - Purpose: Number of buildings destroyed of player8
    """
    P1_RAZING_VALUE = 126
    """
    - Purpose: Total cost of all buildings destroyed of player1
    """
    P2_RAZING_VALUE = 127
    """
    - Purpose: Total cost of all buildings destroyed of player2
    """
    P3_RAZING_VALUE = 128
    """
    - Purpose: Total cost of all buildings destroyed of player3
    """
    P4_RAZING_VALUE = 129
    """
    - Purpose: Total cost of all buildings destroyed of player4
    """
    P5_RAZING_VALUE = 130
    """
    - Purpose: Total cost of all buildings destroyed of player5
    """
    P6_RAZING_VALUE = 131
    """
    - Purpose: Total cost of all buildings destroyed of player6
    """
    P7_RAZING_VALUE = 132
    """
    - Purpose: Total cost of all buildings destroyed of player7
    """
    P8_RAZING_VALUE = 133
    """
    - Purpose: Total cost of all buildings destroyed of player8
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
    - Purpose: Number of own units killed by player1
    """
    KILLS_BY_P2 = 137
    """
    - Purpose: Number of own units killed by player2
    """
    KILLS_BY_P3 = 138
    """
    - Purpose: Number of own units killed by player3
    """
    KILLS_BY_P4 = 139
    """
    - Purpose: Number of own units killed by player4
    """
    KILLS_BY_P5 = 140
    """
    - Purpose: Number of own units killed by player5
    """
    KILLS_BY_P6 = 141
    """
    - Purpose: Number of own units killed by player6
    """
    KILLS_BY_P7 = 142
    """
    - Purpose: Number of own units killed by player7
    """
    KILLS_BY_P8 = 143
    """
    - Purpose: Number of own units killed by player8
    """
    RAZINGS_BY_P1 = 144
    """
    - Purpose: Number of own buildings destroyed by player1
    """
    RAZINGS_BY_P2 = 145
    """
    - Purpose: Number of own buildings destroyed by player2
    """
    RAZINGS_BY_P3 = 146
    """
    - Purpose: Number of own buildings destroyed by player3
    """
    RAZINGS_BY_P4 = 147
    """
    - Purpose: Number of own buildings destroyed by player4
    """
    RAZINGS_BY_P5 = 148
    """
    - Purpose: Number of own buildings destroyed by player5
    """
    RAZINGS_BY_P6 = 149
    """
    - Purpose: Number of own buildings destroyed by player6
    """
    RAZINGS_BY_P7 = 150
    """
    - Purpose: Number of own buildings destroyed by player7
    """
    RAZINGS_BY_P8 = 151
    """
    - Purpose: Number of own buildings destroyed by player8
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
    - Purpose: Tribute received from player1
    """
    TRIBUTE_FROM_P2 = 157
    """
    - Purpose: Tribute received from player2
    """
    TRIBUTE_FROM_P3 = 158
    """
    - Purpose: Tribute received from player3
    """
    TRIBUTE_FROM_P4 = 159
    """
    - Purpose: Tribute received from player4
    """
    TRIBUTE_FROM_P5 = 160
    """
    - Purpose: Tribute received from player5
    """
    TRIBUTE_FROM_P6 = 161
    """
    - Purpose: Tribute received from player6
    """
    TRIBUTE_FROM_P7 = 162
    """
    - Purpose: Tribute received from player7
    """
    TRIBUTE_FROM_P8 = 163
    """
    - Purpose: Tribute received from player8
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
    CONVERT_RESIST_MIN_ADJUSTMENT = 178
    """
    - Purpose: Additional monk seconds needed before conversion by enemy monks is even possible

    - Note: A great explanation of how this works: https://youtu.be/-qRUaOHpbwI?t=830 by T-West
    """
    CONVERT_RESIST_MAX_ADJUSTMENT = 179
    """
    - Purpose: Additional monk seconds needed before conversion by enemy monks is forced

    - Note: A great explanation of how this works: https://youtu.be/-qRUaOHpbwI?t=830 by T-West.
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

    - Defaults:

        - 0: No (default)
        - 1: Yes, after Spies

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

    - Defaults:

        - 1: Default
        - 1.15: Mayans

    - Note: Since this works by multiplying the amount of resources gathered by a villager, it has a side effect of increasing the gather rate. In the case of Mayans, This is compensated for by reducing villager work rate by 15%
    """
    FOOD_GATHERING_PRODUCTIVITY = 190
    """
    - Purpose: Multiplier for food gathered from all sources

    - Defaults:

        - 1: Default
        - 1.15: Mayans

    - Note: Since this works by multiplying the amount of resources gathered by a villager, it has a side effect of increasing the gather rate. In the case of Mayans, This is compensated for by reducing villager work rate by 15%. The work rate for farmers is reduced by about 23.4%
    """
    RELIC_GOLD_PRODUCTION_RATE = 191
    """
    - Purpose: Relic gold generation rate in gold per minute

    - Defaults:

        - 30: Default. 30 gold per minute (0.5 gold per second)
        - 15: After getting hit with Atheism
    """
    CONVERTED_UNITS_DIE = 192
    """
    - Purpose: Boolean: converted units die instead of switching over to the enemy

    - Defaults:

        - 0: No (default)
        - 1: Yes, after Heresey
    """
    THEOCRACY = 193
    """
    - Purpose: Boolean: only one monk needs to regen faith after group conversion for the source player

    - Defaults:

        - 0: No (default)
        - 1: Yes, after researching Theocracy
    """
    CRENELLATIONS = 194
    """
    - Purpose: Boolean: Garrisoned infantry fire arrows

    - Defaults:

        - 0: No (default)
        - 1: Yes, after crenellations
    """
    CONSTRUCTION_RATE_MODIFIER = 195
    """
    - Purpose: Builder work rate multiplier

    - Defaults:

        - 0: Default
        - 1.3: Spanish

    - Note: The actual work rate for builders is given by `construction_rate_mod * builder.default_work_rate`
    """
    HUN_WONDER_DISCOUNT = 196
    """
    - Purpose: Additional time required for relic/wonder victories in one tenth of a year

    - Defaults:

        - 0: default
        - 1000: (100 years) for the Hun player, after researching atheism. The value of this resource of each player is added to determine the total extra time for relic/wonder victories, i.e. it adds up if multiple hun players get the tech

    - Note: Internally, relic and wonder victory countdowns are measured in one tenths of an year, the fractional part is just not shown ingame
    """
    SPIES_DISCOUNT = 197
    """
    - Purpose: Boolean: Halves the cost of spies per villager, and caps it at 15k gold max instead of the usual 30k

    - Defaults:

        - 0: Default
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

    - Defaults:

        - 1: Default

    - Note: The amount of food obtained from owning `n` number of Feitorias is given by `n * feitoria_food_productivity * 1.6`
    """
    FEITORIA_WOOD_PRODUCTIVITY = 206
    """
    - Purpose: Feitoria wood production rate multiplier

    - Defaults:

        - 1: Default

    - Note: The amount of wood obtained from owning `n` number of Feitorias is given by `n * feitoria_wood_productivity * 0.7`
    """
    FEITORIA_STONE_PRODUCTIVITY = 207
    """
    - Purpose: Feitoria stone production rate multiplier

    - Defaults:

        - 1: Default

    - Note: The amount of stone obtained from owning `n` number of Feitorias is given by `n * feitoria_stone_productivity * 0.3`
    """
    FEITORIA_GOLD_PRODUCTIVITY = 208
    """
    - Purpose: Feitoria gold production rate multiplier

    - Defaults:

        - 1: Default

    - Note: The amount of gold obtained from owning `n` number of Feitorias is given by `n * feitoria_gold_productivity * 1`
    """
    REVEAL_ENEMY_TOWN_CENTERS = 209
    """
    - Purpose: Boolean: reveal enemy town centre location for the source player

    - Defaults:

        - 0: Default
        - 5: Vietnamese

    - Note: The bonus works for all values >=1, the choice of setting it to 5 for vietnamese seems arbitrary
    """
    RELICS_VISIBLE_ON_MAP = 210
    """
    - Purpose: Boolean: reveal relics on map amount

    - Defaults:

        - -1: Default
        - 42: Burmese

    - Note: Burmese reveal relics on map bonus. Only works in RMS, manually changing this in the editor does not seem to have any effects
    """
    ELEVATION_HIGHER_BONUS = 211
    """
    - Purpose: The fraction for additional bonus damage dealt from higher elevation

    - Defaults:

        - 0: Default
        - 0.25: Tatars

    - Note: Damage that units on higher elevation deal to units on lower elevation is multiplied by `1.25 + elevation_bonus_higher`
    """
    ELEVATION_LOWER_BONUS = 212
    """
    - Purpose: The fraction for additional bonus damage dealt from lower elevation

    - Defaults:

        - 0: Default

    - Note: Damage that units on lower elevation deal to units on higher elevation is multiplied by `0.75 + elevation_bonus_lower`
    """
    RAIDING_PRODUCTIVITY = 213
    """
    - Purpose: Keshik gold generation rate per 100 seconds

    - Defaults:

        - 0: Default
        - 50: (0.5 g/s) Tatars

    - Note: Note that in practice, due to attack reload time and frame delay, Keshiks don't actually produce 0.5 g/s, but a slightly lower value
    """
    MERCENARY_KIPCHAK_COUNT = 214
    """
    - Purpose: Total number of mercenary kipchak creatable

    - Defaults:

        - 0: Default
        - 10: after a Cuman ally researches Cuman Mercenaries

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

    - Defaults:

        - 1: Default
        - 1.57: Tatars

    - Note: Since this works by multiplying the amount of resources gathered by a villager, it has a side effect of increasing the gather rate. In the case of Tatars, This is compensated for by reducing villager work rate by 57%
    """
    SHARED_LINE_OF_SIGHT = 217
    """
    - Purpose: Unknown... what does this resource do?
    """
    EARLY_TOWN_CENTER_LIMIT = 218
    """
    - Purpose: This is the number of extra TCs a player is allowed to build IF TCs are enabled in feudal age

    - Defaults:

        - 1: Default
        - 2: Cumans

    - Note: Since generic civs don't get access to TCs in feudal, the 10k amount doesn't matter, but if you're trying to make a map where you want people to be able to make TCs in feudal, make sure to set this value to 10k for cumans!
    """
    FISHING_PRODUCTIVITY = 219
    """
    - Purpose: Multiplier for food gathered by fishing ships

    - Defaults:

        - 1: Default

    - Note: Since this works by multiplying the amount of resources gathered by a fishing ship, it has a side effect of increasing the gather rate
    """
    UNUSED_RESOURCE_220 = 220
    """
    - Purpose: Unused
    """
    MONUMENT_FOOD_PRODUCTIVITY = 221
    """
    - Purpose: Monument food trickle rate multiplier

    - Defaults:

        - 1: In KoTH games

    - Note: The amount of resources obtained by owning a monument is `0.7925 * food_trickle_from_monument`
    """
    MONUMENT_WOOD_PRODUCTIVITY = 222
    """
    - Purpose: Monument wood trickle rate multiplier

    - Defaults:

        - 1: In KoTH games

    - Note: The amount of resources obtained by owning a monument is `0.7925 * wood_trickle_from_monument`
    """
    MONUMENT_STONE_PRODUCTIVITY = 223
    """
    - Purpose: Monument stone trickle rate multiplier

    - Defaults:

        - 1: In KoTH games

    - Note: The amount of resources obtained by owning a monument is `0.7925 * stone_trickle_from_monument`
    """
    MONUMENT_GOLD_PRODUCTIVITY = 224
    """
    - Purpose: Monument gold trickle rate multiplier

    - Defaults:

        - 1: In KoTH games

    - Note: The amount of resources obtained by owning a monument is `0.7925 * gold_trickle_from_monument`
    """
    RELIC_FOOD_PRODUCTION_RATE = 225
    """
    - Purpose: Relic food production per minute

    - Defaults:

        - 0: Default
        - 30: Burgundians
        - 15: Burgundians after getting hit with Atheism
    """
    VILLAGERS_KILLED_BY_GAIA = 226
    """
    - Purpose: Total number of villagers lost to gaia
    """
    VILLAGERS_KILLED_BY_ANIMALS = 227
    """
    - Purpose: Total number of villagers lost to wild animals
    """
    VILLAGERS_KILLED_BY_AI_PLAYER = 228
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

    - Defaults:

        - 0: Default
        - 2: (0.02 g/s per farmer) after Burgundian Vineyards

    - Note: Only generates gold while collecting food from farms, and not when walking on them down
    """
    FOLWARK_COLLECTION_AMOUNT = 237
    """
    - Purpose: This is the amount of food collected from farms built around a folwark

    - Defaults:

        - 0: Default
        - 17.5: Poles
        - 19.25: Poles with Chinese Ally
        - 25: Poles with Horse Collar
        - 27.5: Poles with Horse Collar & Chinese Ally
        - 37.5: Poles with Heavy Plow
        - 41.25: Poles with Heavy Plow & Chinese Ally
        - 55: Poles with Crop Rotation
        - 60.5: Poles with Crop Rotation & Chinese Ally
    """
    FOLWARK_ATTRIBUTE_TYPE = 238
    """
    - Purpose: This is the ID of the resource that is given when a farm is constructed around a folwark

    - Defaults:

        - 0: Poles
        - -1: Default
    """
    FOLWARK_BUILDING_TYPE = 239
    """
    - Purpose: This is the ID of the building that the Folwark needs to upgrade from for the farm collection ability to work

    - Defaults:

        - 68: (Mill) Poles
        - -1: Default
    """
    UNITS_CONVERTED = 240
    """
    - Purpose: The amount of units lost to enemy conversions
    """
    STONE_MINING_GOLD_PRODUCTIVITY = 241
    """
    - Purpose: Stone mining gold generation rate per 100 seconds

    - Defaults:

        - 0: Default
        - 18: Poles
        - 20.7: Poles with Stone Mining
        - 23.805: Poles with Stone Shaft Mining
    """
    TRADE_WORKSHOP_FOOD_PRODUCTIVITY = 242
    """
    - Purpose: Trade Workshop food production rate multiplier

    - Defaults:

        - 1: Default

    - Note: The amount of food obtained from owning `n` number of TWS (Unit 1647) is given by `n * tws_food_productivity * 2.25`
    """
    TRADE_WORKSHOP_WOOD_PRODUCTIVITY = 243
    """
    - Purpose: Trade Workshop wood production rate multiplier

    - Defaults:

        - 1: Default

    - Note: The amount of wood obtained from owning `n` number of TWS (Unit 1647) is given by `n * tws_wood_productivity * 2.25`
    """
    TRADE_WORKSHOP_STONE_PRODUCTIVITY = 244
    """
    - Purpose: Trade Workshop stone production rate multiplier

    - Defaults:

        - 0: Default

    - Note: The amount of stone obtained from owning `n` number of TWS (Unit 1647) is given by `n * tws_stone_productivity * 2.25`
    """
    TRADE_WORKSHOP_GOLD_PRODUCTIVITY = 245
    """
    - Purpose: Trade Workshop gold production rate multiplier

    - Defaults:

        - 1: Default

    - Note: The amount of gold obtained from owning `n` number of TWS (Unit 1647) is given by `n * tws_gold_productivity * 2.25`
    """
    UNITS_VALUE_TOTAL = 246
    """
    - Purpose: Total cost of all units created so far

    - Note: This does **not** decrease when the units die
    """
    BUILDINGS_VALUE_TOTAL = 247
    """
    - Purpose: Total cost of all buildings created so far

    - Note: Increases when foundations are placed. This does **not** decrease if the foundation is deleted
    """
    VILLAGERS_CREATED_TOTAL = 248
    """
    - Purpose: Total number of villagers created so far
    """
    VILLAGERS_IDLE_PERIODS_TOTAL = 249
    """
    - Purpose: Amount of villagers that *entered* an idle state since game start

    - Note: 
    1. This only updates every 5 physical minutes.
    2. The number of villagers that *entered* an idle state since the last updated is added to this resource.
    3. Starting villager count is the initial value
    """
    VILLAGERS_IDLE_SECONDS_TOTAL = 250
    """
    - Purpose: Amount of total seconds all villagers have been idle since game start

    - Note: 
    1. This only updates every 5 physical minutes.
    2. The idle time in seconds for all villagers since the last time this resource was updated is added  to this resource.
    3. A villager immediately adds its own idle time to this resource if it dies
    """
    TRADE_FOOD_PERCENT = 251
    """
    - Purpose: Percentage of gold generated from trade that is also given as food

    - Defaults:

        - 0: Default
        - 10: Bengalis
    """
    TRADE_WOOD_PERCENT = 252
    """
    - Purpose: Percentage of gold generated from trade that is also given as wood

    - Defaults:

        - 0: Default
    """
    TRADE_STONE_PERCENT = 253
    """
    - Purpose: Percentage of gold generated from trade that is also given as stone

    - Defaults:

        - 0: Default
    """
    LIVESTOCK_FOOD_PRODUCTIVITY = 254
    """
    - Purpose: Garrisoned herdable food generation rate per 60 seconds

    - Defaults:

        - 0: Default
        - 3.5: (0.0583 f/s per herdable) Gurjaras
    """
    SPEED_UP_BUILDING_TYPE = 255
    """
    - Purpose: This is the ID of the building to use for the speed up effect.

    - Defaults:

        - 1754: (Caravanserai) Default

    - Note: See also:

        - https://ugc.aoe2.rocks/general/resources/resources/#255-speed-up-building-type
        - https://ugc.aoe2.rocks/general/resources/resources/#256-speed-up-building-range
        - https://ugc.aoe2.rocks/general/resources/resources/#257-speed-up-percentage
        - https://ugc.aoe2.rocks/general/resources/resources/#258-speed-up-object-type
        - https://ugc.aoe2.rocks/general/resources/resources/#259-speed-up-effect-type
        - https://ugc.aoe2.rocks/general/resources/resources/#260-speed-up-secondary-effect-type
        - https://ugc.aoe2.rocks/general/resources/resources/#261-speed-up-secondary-percentage
    """
    SPEED_UP_BUILDING_RANGE = 256
    """
    - Purpose: This specifies the range (in tiles) of the area created around the building ([Speed Up Building Type](./#255-speed-up-building-type)) (square, from the edges of the building) for the speed up effect

    - Defaults:

        - 8: Default

    - Note: See also:

        - https://ugc.aoe2.rocks/general/resources/resources/#255-speed-up-building-type
        - https://ugc.aoe2.rocks/general/resources/resources/#256-speed-up-building-range
        - https://ugc.aoe2.rocks/general/resources/resources/#257-speed-up-percentage
        - https://ugc.aoe2.rocks/general/resources/resources/#258-speed-up-object-type
        - https://ugc.aoe2.rocks/general/resources/resources/#259-speed-up-effect-type
        - https://ugc.aoe2.rocks/general/resources/resources/#260-speed-up-secondary-effect-type
        - https://ugc.aoe2.rocks/general/resources/resources/#261-speed-up-secondary-percentage
    """
    SPEED_UP_PERCENTAGE = 257
    """
    - Purpose: The formulae given below are used with this resource as the `value` to adjust the attribute ([Speed Up Effect Type](./#259-speed-up-effect-type)) of all units of class ([Speed Up Object Type](./#258-speed-up-object-type)) when they are in the range of the speed up effect

    - Defaults:

        - 0.2: Default

    - Note: For each of the attributes that work with this resource, the new value to set is determined using the following formulae:

    (013) `new_workrate = original + value`

    (005) `new_movement_speed = original * (1 + value)`

    (109) `new_regeneration_rate = original + (3600/value)`

    See also:

        - https://ugc.aoe2.rocks/general/resources/resources/#255-speed-up-building-type
        - https://ugc.aoe2.rocks/general/resources/resources/#256-speed-up-building-range
        - https://ugc.aoe2.rocks/general/resources/resources/#257-speed-up-percentage
        - https://ugc.aoe2.rocks/general/resources/resources/#258-speed-up-object-type
        - https://ugc.aoe2.rocks/general/resources/resources/#259-speed-up-effect-type
        - https://ugc.aoe2.rocks/general/resources/resources/#260-speed-up-secondary-effect-type
        - https://ugc.aoe2.rocks/general/resources/resources/#261-speed-up-secondary-percentage
    """
    SPEED_UP_OBJECT_TYPE = 258
    """
    - Purpose: This is `900 + class_id` for the class of units that should be affected by the speed up effect

    - Defaults:

        - 919: (Trade Cart class) Default

    - Note: See also:

        - https://ugc.aoe2.rocks/general/resources/resources/#255-speed-up-building-type
        - https://ugc.aoe2.rocks/general/resources/resources/#256-speed-up-building-range
        - https://ugc.aoe2.rocks/general/resources/resources/#257-speed-up-percentage
        - https://ugc.aoe2.rocks/general/resources/resources/#258-speed-up-object-type
        - https://ugc.aoe2.rocks/general/resources/resources/#259-speed-up-effect-type
        - https://ugc.aoe2.rocks/general/resources/resources/#260-speed-up-secondary-effect-type
        - https://ugc.aoe2.rocks/general/resources/resources/#261-speed-up-secondary-percentage
    """
    SPEED_UP_EFFECT_TYPE = 259
    """
    - Purpose: The ID of the attribute that is modified by the speed up effect. Only 5 (Movement Speed), 13 (Work Rate) and 109 (Regeneration) have been found to work so far

    - Defaults:

        - 5: (Movement Speed) Default

    - Note: See also:

        - https://ugc.aoe2.rocks/general/resources/resources/#255-speed-up-building-type
        - https://ugc.aoe2.rocks/general/resources/resources/#256-speed-up-building-range
        - https://ugc.aoe2.rocks/general/resources/resources/#257-speed-up-percentage
        - https://ugc.aoe2.rocks/general/resources/resources/#258-speed-up-object-type
        - https://ugc.aoe2.rocks/general/resources/resources/#259-speed-up-effect-type
        - https://ugc.aoe2.rocks/general/resources/resources/#260-speed-up-secondary-effect-type
        - https://ugc.aoe2.rocks/general/resources/resources/#261-speed-up-secondary-percentage
    """
    SPEED_UP_SECONDARY_EFFECT_TYPE = 260
    """
    - Purpose: This is the ID of the secondary attribute that is modified by the speed up effect. Only 5 (Movement Speed), 13 (Work Rate) and 109 (Regeneration) have been found to work so far

    - Defaults:

        - 109: (Regeneration Rate) Default

    - Note: See also:

        - https://ugc.aoe2.rocks/general/resources/resources/#255-speed-up-building-type
        - https://ugc.aoe2.rocks/general/resources/resources/#256-speed-up-building-range
        - https://ugc.aoe2.rocks/general/resources/resources/#257-speed-up-percentage
        - https://ugc.aoe2.rocks/general/resources/resources/#258-speed-up-object-type
        - https://ugc.aoe2.rocks/general/resources/resources/#259-speed-up-effect-type
        - https://ugc.aoe2.rocks/general/resources/resources/#260-speed-up-secondary-effect-type
        - https://ugc.aoe2.rocks/general/resources/resources/#261-speed-up-secondary-percentage
    """
    SPEED_UP_SECONDARY_PERCENTAGE = 261
    """
    - Purpose: This amount is added to the secondary attribute ([Speed Up Secondary Effect Type](./#260-speed-up-secondary-effect-type)) of all units of class ([Speed Up Object Type](./#258-speed-up-object-type)) when they are in the range of the speed up effect

    - Defaults:

        - 60: Default

    - Note: See also:

        - https://ugc.aoe2.rocks/general/resources/resources/#255-speed-up-building-type
        - https://ugc.aoe2.rocks/general/resources/resources/#256-speed-up-building-range
        - https://ugc.aoe2.rocks/general/resources/resources/#257-speed-up-percentage
        - https://ugc.aoe2.rocks/general/resources/resources/#258-speed-up-object-type
        - https://ugc.aoe2.rocks/general/resources/resources/#259-speed-up-effect-type
        - https://ugc.aoe2.rocks/general/resources/resources/#260-speed-up-secondary-effect-type
        - https://ugc.aoe2.rocks/general/resources/resources/#261-speed-up-secondary-percentage
    """
    CIVILIZATION_NAME_OVERRIDE = 262
    """
    - Purpose: 
    """
    STARTING_SCOUT_ID = 263
    """
    - Purpose: Unit ID for the starting scout. Can be set to any unit (even buildings)

    - Defaults:

        - 448: (Scout Cavalry) Default
        - 751: (Eagle Scout) Aztecs, Incas and Mayans
        - 1755: (Camel Scout) Gurjaras
    """
    RELIC_WOOD_PRODUCTION_RATE = 264
    """
    - Purpose: Relic wood production per minute

    - Defaults:

        - 0: Default

    - Note: This is not affected by Atheism
    """
    RELIC_STONE_PRODUCTION_RATE = 265
    """
    - Purpose: Relic stone production per minute

    - Note: This is not affected by Atheism
    """
    CHOPPING_GOLD_PRODUCTIVITY = 266
    """
    - Purpose: Lumberjack chopping gold generation rate per 100 seconds

    - Defaults:

        - 0: Default
        - 1.5: (0.015 g/s per lumberjack) Vietnamese with paper money
        - 1.8: (0.018 g/s per lumberjack) Vietnamese with paper money & Double Bit Axe
        - 2.16: (0.0216 g/s per lumberjack) Vietnamese with paper money & Double Bit Axe & Bow Saw
        - 2.376: (0.02376 g/s per lumberjack) Vietnamese with paper money & Double Bit Axe & Bow Saw & Two-Man Saw

    - Note: Only generates gold while collecting wood from trees, and not when cutting them down
    """
    FORAGING_WOOD_PRODUCTIVITY = 267
    """
    - Purpose: Forager foraging wood generation rate per 100 seconds

    - Defaults:

        - 0: Default
        - 10.4753: (0.104753 w/s per forager) Portuguese
    """
    HUNTER_PRODUCTIVITY = 268
    """
    - Purpose: Hunter hunting gold production rate per 100 seconds
    """
    TECHNOLOGY_REWARD_EFFECT = 269
    """
    - Purpose: This is the ID of an additional effect which will fire when any technology is researched
    """
    UNIT_REPAIR_COST = 270
    """
    - Purpose: Percentage of cost required to repair siege units and ships
    """
    BUILDING_REPAIR_COST = 271
    """
    - Purpose: Percentage of cost required to repair buildings
    """
    ELEVATION_HIGHER_DAMAGE = 272
    """
    - Purpose: Damage modifier for own units when attacked from higher elevation

    - Note: This is applied after the calculations from [Elevation Higher Bonus](./#211-elevation-higher-bonus) and [Elevation Lower Bonus](./#212-elevation-lower-bonus)
    """
    ELEVATION_LOWER_DAMAGE = 273
    """
    - Purpose: Damage modifier for own units when attacked from lower elevation

    - Note: This is applied after the calculations from [Elevation Higher Bonus](./#211-elevation-higher-bonus) and [Elevation Lower Bonus](./#212-elevation-lower-bonus)
    """
    INFANTRY_KILL_REWARD = 274
    """
    - Purpose: This resource currently effectively enables/disables gold generation per second by infantry killing villagers, trade units and monks

    - Defaults:

        - 0: All Civs
        - 1: Vikings after Chieftains

    - Note: Technically, this resource is used as a multiplier for the resource generated by task 154 currently on infantry units. Task 154 can change which resource does this, and it is what really controls which resource is generated (Resource Out) and the rate of generation (Work Value 1) which is set to the different rates for different types of targets for infantry
    """
    UNUSED_RESOURCE_275 = 275
    """
    - Purpose: Unused
    """
    UNUSED_RESOURCE_276 = 276
    """
    - Purpose: Unused
    """
    UNUSED_RESOURCE_277 = 277
    """
    - Purpose: Unused
    """
    UNUSED_RESOURCE_278 = 278
    """
    - Purpose: Unused
    """
    MILITARY_CAN_CONVERT = 279
    """
    - Purpose: Military units with the conversion task can convert units if this is set to > 0 for a player
    """
    MILITARY_CONVERT_RANGE = 280
    """
    - Purpose: Adds to the conversion range of military units
    """
    MILITARY_CONVERT_CHANCE = 281
    """
    - Purpose: Determines the conversion probability per monk second
    """
    MILITARY_CONVERT_RECHARGE = 282
    """
    - Purpose: Determines the faith recharge rate after successful conversions
    """
    SPAWN_INSIDE = 283
    """
    - Purpose: Unknown
    """
    CAVALRY_KILL_REWARD = 284
    """
    - Purpose: This resource effectively sets the gold generation rate per second by cavalry fighting other military units

    - Defaults:

        - 0: All Civs

    - Note: Technically, this resource is used as a multiplier for the resource generated by task 154 currently on cavalry units. Task 154 can change which resource does this, and it is also what really controls which resource is generated (Resource Out) and the rate of generation (Work Value 1) which is just set to 1 for cavalry.
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
    Attribute' effect with the 'Hero Status' attribute. This is a combinable bit field

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
    def split_flags(value: int) -> Dict[HeroStatusFlag, bool]:
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

    NO_HERO_STATUS = 0
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
    damage resources, nearby allied units and tress
    """
    TREES = 1
    """
    damage trees, nearby allied units
    """
    NEARBY_UNITS = 2
    """
    damage nearby allied units
    """
    TARGET_ONLY = 3
    """
    damage targeted unit only
    """
    FIXED_FIVE = 4
    """
    Deal a fixed 5 HP of damage to nearby units
    """
    FIFTY_PERCENT = 8
    """
    Deal 50% of unit's own damage to nearby units
    """
    TWENTY_FIVE_PERCENT = 16
    """
    Deal 25% of unit's own damage to nearby units
    """
    THIRTY_THREE_PERCENT = 32
    """
    Deal 33% of unit's own damage to nearby units
    """
    DISTANCE_ATTENUATION = 64
    """
    Attenuate damage as distance from the centre of attack increases (infantry only)
    """
    DIRECTIONAL = 128
    """
    Blast damage is dealt along the direction the unit is facing only. This area is a very narrow cone    
    """


class ProjectileSmartMode(_DataSetIntFlags):
    """
    This enum class provides the integer values used to reference the smart projectile flag values used in the game.
    Used in the 'Modify Attribute' effect with the 'Projectile Smart Mode' attribute. This is a combainable bit field

    **Examples**

    >>> ProjectileSmartMode.HAS_BALLISTICS
    <ProjectileSmartMode.HAS_BALLISTICS: 1>
    """
    TARGET_CURRENT_LOCATION = 0
    TARGET_FUTURE_LOCATION = 1
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
    RAMS_TREBUCHETS_SIEGE_TOWERS = 17
    TREES = 18
    UNIQUE_UNITS = 19
    SIEGE_WEAPONS = 20
    STANDARD_BUILDINGS = 21
    WALLS_AND_GATES = 22
    GUNPOWDER_UNITS = 23
    BOARS = 24
    MONKS = 25
    CASTLES = 26
    """Castles, Kreposts, Fortresses, Poenari Castles"""
    SPEARMEN = 27
    CAVALRY_ARCHERS = 28
    EAGLE_WARRIORS = 29
    CAMELS = 30
    """Camels use this armour class since and after AK"""
    UNUSED_ID31 = 31
    CONDOTTIERI = 32
    PROJECTILE_GUNPOWDER_SECONDARY = 33
    FISHING_SHIPS = 34
    MAMELUKES = 35
    HEROES_AND_KINGS = 36
    HUSSITE_WAGONS = 37
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

    >>> ObjectState.FOUNDATION
    <ObjectState.FOUNDATION: 0>
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

    # todo: we can probably add this to the base dataset int flags class, I have an idea on how to generic-ify this
    #  method although idk if its actually good - Alian
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
            empire_wars: If empire wars should be enabled
            sudden_death: If sudden death should be enabled
            regicide: If regicide should be enabled
            king_of_the_hill: If king of the hill should be enabled

        Returns:
            An integer combining all the different hero status flags into one value
        """
        total = 1 if empire_wars else 0
        total += 2 if sudden_death else 0
        total += 4 if regicide else 0
        total += 8 if king_of_the_hill else 0
        return SecondaryGameMode(total)

    NONE = 0
    EMPIRE_WARS = 1
    SUDDEN_DEATH = 2
    REGICIDE = 4
    KING_OF_THE_HILL = 8


class VictoryTimerType(_DataSetIntEnums):
    """
    This enum class provides the integer values used to reference the different types of victory timer types.

    **Examples**

    >>> VictoryTimerType.WONDER_TIMER
    <VictoryTimerType.WONDER_TIMER: 0>
    """
    WONDER_TIMER = 0
    RELIC_TIMER = 1
    KING_OF_THE_HILL_TIMER = 2


class ChargeType(_DataSetIntEnums):
    """
    This enum provides the integer values used to reference the type of charge that a unit holds

    **Examples**

    >>> ChargeType.AREA_ATTACK_CHARGE
    <ChargeType.AREA_ATTACK_CHARGE: 3>
    """
    ATTACK_CHARGE = 1
    UNKNOWN_CHARGE = 2
    AREA_ATTACK_CHARGE = 3
    AGILITY_CHARGE = 4


class ChargeEvent(_DataSetIntEnums):
    """
    This enum provides the integer values used to reference the action which depletes a unit's charge

    **Examples**

    >>> ChargeEvent.DEPLETES_CHARGE_ON_ATTACKING
    <ChargeEvent.DEPLETES_CHARGE_ON_ATTACKING: 1>
    """
    NO_CHARGE_DEPLETED = 0
    CHARGE_DEPLETED_ON_ATTACK = 1


class CombatAbility(_DataSetIntFlags):
    """
    This enum class provides the integer values for the break off combat flags that can be used
    in the 'Modify Attribute' effect with the 'Combat Ability' attribute. This is a combinable bit field.

    **Examples**

    >>> CombatAbility.RESIST_ARMOR_IGNORING_ATTACKS
    <CombatAbility.RESIST_ARMOR_IGNORING_ATTACKS: 2>
    """
    NORMAL = 0
    IGNORE_MELEE_PIERCE_ARMOR = 1
    RESIST_ARMOR_IGNORING_ATTACKS = 2
    DAMAGE_TARGET_ARMOR = 4
    ATTACK_GROUND = 8
    BULK_VOLLEY_RELEASE = 16


class FogVisibility(_DataSetIntEnums):
    """
    This enum class provides the integer values used to references the different fog visibility settings that can be
    used in the 'Modify Attribute' effect with the 'Fog Visibility' attribute.

    **Examples**

    >>> FogVisibility.VISIBLE_IF_ALIVE
    <FogVisibility.VISIBLE_IF_ALIVE: 2>
    """
    NOT_VISIBLE = 0
    ALWAYS_VISIBLE = 1
    VISIBLE_IF_ALIVE = 2
    INVERTED_VISIBILITY = 3
    CHECK_DOPPELGANGER = 4


class GarrisonType(_DataSetIntFlags):
    """
    This enum class provides the integer values for the different garrison type flags that can be used in the 'Modify
    Attribute' effect with the 'Garrison Type' attribute. This is a combinable bit field

    **Examples**

    >>> GarrisonType.VILLAGERS
    <GarrisonType.VILLAGERS: 1>
    """
    NONE = 0
    VILLAGERS = 1
    INFANTRY = 2
    CAVALRY = 4
    MONKS = 8
    HERDABLES = 16
    SIEGE = 32
    SHIPS = 64


class OcclusionMode(_DataSetIntFlags):
    """
    This enum class provides the integer values for the different occlusion mode flags that can be used in the 'Modify
    Attribute' effect with the 'OcclusionMode' attribute. This is a combinable bit field.

    **Examples**

    >>> OcclusionMode.NO_OUTLINE
    <OcclusionMode.NO_OUTLINE: 0>
    """
    NO_OCCLUSION = 0
    """
    No outline
    """
    DISPLAY_OUTLINE = 1
    """
    Display outline when behind other units that have flag 2
    """
    OCCLUDES_OTHERS = 2
    """
    Other units' outlines are rendered when they are behind this unit
    """
    DISPLAY_OUTLINE_FOR_FOUNDATION = 4
    """
    Display outline on this unit's foundation when behind other units that have flag 
    """


class ProjectileHitMode(_DataSetIntEnums):
    """
    This enum class provides the integer values used to references the different projectile hit mode settings that can
    be used in the 'Modify Attribute' effect with the 'Projectile Hit Mode' attribute.

    **Examples**

    >>> ProjectileHitMode.ANY_OBSTACLE
    <ProjectileHitMode.ANY_OBSTACLE: 2>
    """
    TARGET_ONLY = 0
    """
    Collide only with the targeted unit"
    """
    ANY_PLAYER_UNIT = 1
    """
    Collide with any damage-able units in the path to the targeted unit"
    """
    ANY_OBSTACLE = 2
    """
    Collide with any unit in the path to the targeted unit
    """


class ProjectileVanishMode(_DataSetIntEnums):
    """
    This enum class provides the integer values used to references the different projectile vanish mode settings that
    can be used in the 'Modify Attribute' effect with the 'Projectile Vanish Mode' attribute.

    **Examples**

    >>> ProjectileVanishMode.DISAPPEAR_ON_IMPACT
    <ProjectileVanishMode.DISAPPEAR_ON_IMPACT: 0>
    """
    DISAPPEAR_ON_IMPACT = 0
    PASS_THROUGH = 1


class UnitTrait(_DataSetIntFlags):
    """
    This enum class provides the integer values used to references the different unit trait flags that can be used in
    the 'Modify Attribute' effect with the 'Unit Trait' attribute.

    **Examples**

    >>> UnitTrait.NO_OUTLINE
    <UnitTrait.NO_OUTLINE: 0>
    """
    GARRISONABLE = 1
    SHIP = 2
    BUILD_BUILDING = 4
    TRANSFORMABLE = 8
    AUTO_SCOUT = 16


class VictoryCondition(_DataSetIntEnums):
    """
    This enum class provides the integer values used to references the different victory conditions that can be set
    using the Global Victory tab in the in-game editor.

    **Examples**

    >>> VictoryCondition.TIME_LIMIT
    <VictoryCondition.TIME_LIMIT: 3>
    """
    STANDARD = 0
    CONQUEST = 1
    SCORE = 2
    TIME_LIMIT = 3
    CUSTOM = 4
    SECONDARY_GAME_MODE = 6
