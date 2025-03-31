from __future__ import annotations

from AoE2ScenarioParser.datasets.dataset_enum import _DataSetIntEnums


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
    This is the quantity of armour a unit has on any of its `Armour Classes`. If you do not know what an `Armour Class` is, refer to the [Damage Calculation](../damage_calculation "Jump to: Game Mechanics > Damage Calculation") section of this guide. Note that changing the armour through this option will show it as being added to the base armour amount. (for example: 4+4)
    """
    ATTACK = 9
    """
    This is the quantity of attack a unit has on any of its `Attack Classes`. If you do not know what an `Attack Class` is, refer to the [Damage Calculation](../damage_calculation "Jump to: Game Mechanics > Damage Calculation") section of this guide. Note that changing the attack through this option will show it as being added to the base attack amount. (for example: 6+2)
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
        ![Visually Smaller](./imgs/visually_smaller.png "Targets that are farther away are visually smaller")
        In this image, you can see that shots that were fired in the red area in the 2nd scenario would've hit if the target had been closer like in the first scenario, but since the target is far away, they actually miss
        More technically, the visual angle of an object of the same size that is farther away is smaller, thus giving a smaller room for error for the shot in terms of the range of angles that will make the shot hit
        The chance of a unit getting converted by a monk is also determined by its accuracy
        If you modify an onager to have a big blast radius and give it a small accuracy, then attack a lot of units bunched together, the accuracy determines what percentage of units take damage from the blast of the onager! This is the reason why warwolf trebuchets get 100% accuracy because otherwise the blast wouldn't damage all of the units. Another interesting consequence of this is the delete trick with onagers and mangonels. This is where a mangonel is deleted immediately after it fires its shot and because a dead unit doesn't have an accuracy, it defaults to 100% and thus deals more damage to all the units in the blast radius
        Note: There are two other factors that play a role in determining the damage from the shot fired by the deleted mangonel
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
    This is the quantity of base armour a unit has on any of its `Armour Classes`. If you do not know what an `Armour Class` is, refer to the [Damage Calculation](../damage_calculation "Jump to: Game Mechanics > Damage Calculation") section of this guide. Note that changing the armour through this option will show it as the base armour itself, and it will not be added to the regular amount
    """
    PROJECTILE_UNIT = 16
    """
    This is the ID of the projectile that a unit fires
    """
    BUILDING_ICON_OVERRIDE = 17
    """
    The functionality of this attribute is unknown as it doesn't always behave certainly. If you know what this attribute does, please let the authors of this guide know!
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
    OBSTRUCTION_TYPE = 78
    """
    Controls unit outline and collision. Use the ``ObstructionType`` dataset for auto completion
    
    - Flags:
    
        - 0: Square outline, and passable
        - 1: Same as 0
        - 2: Solid square outline, and has collision box
        - 3: Square outline, and has collision box
        - 4: No outline, and passable
        - 5: Round outline, and has collision box
        - 10: Same as 2, but designed for mountains
    """
    BLOCKAGE_CLASS = 79
    """
    Controls unit blockage class. Use the ``BlockageClass`` dataset for auto completion
    
    - Flags:
    
        - 0: Forces default obstruction type
        - 1: Resource
        - 2: Unit
        - 3: Building
        - 4: Wall
        - 5: Gate, allows trespassing
        - 6: Cliff, blocks walling
    """
    SELECTION_EFFECT = 80
    """
    Controls unit hit point bar and outline. Use the ``SelectionEffect`` dataset for auto completion
    
    - Flags:
    
        - 0: Has hit point bar
        - 1: Has hit point bar, and outline
        - 2: No hit point bar, or outline
        - 3: No hit point bar, but has outline
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