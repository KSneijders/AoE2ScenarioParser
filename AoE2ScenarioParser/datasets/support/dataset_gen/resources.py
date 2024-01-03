class Attribute(_DataSetIntEnums):
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
    ENABLE_PTWC__KIDNAP__LOOT = 95
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