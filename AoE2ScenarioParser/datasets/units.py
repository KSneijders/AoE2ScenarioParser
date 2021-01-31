from enum import IntEnum

from bidict import bidict


class Unit(IntEnum):
    MOVEABLE_MAP_REVEALER = 0
    ALFRED_THE_ALPACA = 1300
    AMAZON_ARCHER = 850
    AMAZON_WARRIOR = 825
    ARAMBAI = 1126
    ARBALESTER = 492
    ARCHER = 4
    BACTRIAN_CAMEL = 1237
    BALLISTA_ELEPHANT = 1120
    BANDIT = 299
    BATTERING_RAM = 1258
    BATTLE_ELEPHANT = 1132
    BERSERK = 692
    BOMBARD_CANNON = 36
    BOYAR = 876
    BUILDER = 118
    CAMEL = 897
    CAMEL_ARCHER = 1007
    CAMEL_RIDER = 329
    CANNON_GALLEON = 420
    CANOE = 778
    CAPPED_RAM = 422
    CARAVEL = 1004
    CART = 1338
    CATAPHRACT = 40
    CAVALIER = 283
    CAVALRY_ARCHER = 39
    CENTURION = 275
    CHAMPION = 567
    CHU_KO_NU = 73
    COBRA_CAR = 748
    CONDOTTIERO = 882
    CONQUISTADOR = 771
    COW_A = 705
    COW_B = 1596
    COW_C = 1598
    COW_D = 1600
    CROSSBOWMAN = 24
    DEMOLITION_RAFT = 1104
    DEMOLITION_SHIP = 527
    DONKEY = 846
    DRAGON_SHIP = 1302
    EAGLE_SCOUT = 751
    EAGLE_WARRIOR = 753
    EASTERN_SWORDSMAN = 894
    ELEPHANT_ARCHER = 873
    ELITE_ARAMBAI = 1128
    ELITE_BALLISTA_ELEPHANT = 1122
    ELITE_BATTLE_ELEPHANT = 1134
    ELITE_BERSERK = 694
    ELITE_BOYAR = 878
    ELITE_CAMEL_ARCHER = 1009
    ELITE_CANNON_GALLEON = 691
    ELITE_CARAVEL = 1006
    ELITE_CATAPHRACT = 553
    ELITE_CHU_KO_NU = 559
    ELITE_CONQUISTADOR = 773
    ELITE_EAGLE_WARRIOR = 752
    ELITE_ELEPHANT_ARCHER = 875
    ELITE_GBETO = 1015
    ELITE_GENITOUR = 1012
    ELITE_GENOESE_CROSSBOWMAN = 868
    ELITE_HUSKARL = 555
    ELITE_JAGUAR_WARRIOR = 726
    ELITE_JANISSARY = 557
    ELITE_KAMAYUK = 881
    ELITE_KARAMBIT_WARRIOR = 1125
    ELITE_KESHIK = 1230
    ELITE_KIPCHAK = 1233
    ELITE_KONNIK = 1227
    ELITE_KONNIK_DISMOUNTED = 1253
    ELITE_LEITIS = 1236
    ELITE_LONGBOAT = 533
    ELITE_LONGBOWMAN = 530
    ELITE_MAGYAR_HUSZAR = 871
    ELITE_MAMELUKE = 556
    ELITE_MANGUDAI = 561
    ELITE_ORGAN_GUN = 1003
    ELITE_PLUMED_ARCHER = 765
    ELITE_RATTAN_ARCHER = 1131
    ELITE_SAMURAI = 560
    ELITE_SHOTEL_WARRIOR = 1018
    ELITE_SKIRMISHER = 6
    ELITE_STEPPE_LANCER = 1372
    ELITE_TARKAN = 757
    ELITE_TEUTONIC_KNIGHT = 554
    ELITE_THROWING_AXEMAN = 531
    ELITE_TURTLE_SHIP = 832
    ELITE_WAR_ELEPHANT = 558
    ELITE_WAR_WAGON = 829
    ELITE_WOAD_RAIDER = 534
    FARMER = 259
    FAST_FIRE_SHIP = 532
    FIRE_GALLEY = 1103
    FIRE_SHIP = 529
    FISHERMAN = 56
    FISHING_SHIP = 13
    FLAMETHROWER = 188
    FLAMING_CAMEL = 1263
    FORAGER = 120
    FURIOUS_THE_MONKEY_BOY = 860
    GALLEON = 442
    GALLEY = 539
    GBETO = 1013
    GENITOUR = 1010
    GENOESE_CROSSBOWMAN = 866
    GOAT = 1060
    GOLD_MINER = 579
    GOOSE = 1243
    HALBERDIER = 359
    HAND_CANNONEER = 5
    HEAVY_CAMEL_RIDER = 330
    HEAVY_CAVALRY_ARCHER = 474
    HEAVY_CROSSBOWMAN = 493
    HEAVY_DEMOLITION_SHIP = 528
    HEAVY_PIKEMAN = 892
    HEAVY_SCORPION = 542
    HEAVY_SWORDSMAN = 76
    HORSE_A = 814
    HORSE_B = 1356
    HORSE_C = 1602
    HORSE_D = 1604
    HORSE_E = 1606
    HUNTER = 122
    HUSKARL = 41
    HUSSAR = 441
    IMPERIAL_CAMEL_RIDER = 207
    IMPERIAL_SKIRMISHER = 1155
    INVISIBLE_OBJECT = 1291
    IROQUOIS_WARRIOR = 1374
    JAGUAR_WARRIOR = 725
    JANISSARY = 46
    JUNK = 15
    KAMAYUK = 879
    KARAMBIT_WARRIOR = 1123
    KESHIK = 1228
    KHAN = 1275
    KING = 434
    KIPCHAK = 1231
    KNIGHT = 38
    KONNIK = 1225
    KONNIK_DISMOUNTED = 1252
    LEGIONARY = 1
    LEITIS = 1234
    LIGHT_CAVALRY = 546
    LLAMA = 305
    LONG_SWORDSMAN = 77
    LONGBOAT = 250
    LONGBOWMAN = 8
    LUMBERJACK = 123
    MAGYAR_HUSZAR = 869
    MAMELUKE = 282
    MAN_AT_ARMS = 75
    MANGONEL = 280
    MANGUDAI = 11
    MERCHANT = 1572
    MILITIA = 74
    MISSIONARY = 775
    MONK = 125
    MONK_WITH_RELIC = 286
    NINJA = 1145
    NORSE_WARRIOR = 361
    ONAGER = 550
    ORGAN_GUN = 1001
    OX_CART = 1271
    OX_WAGON = 1273
    PALADIN = 569
    PENGUIN = 639
    PETARD = 440
    PHOTONMAN = 1577
    PIG = 1245
    PIKEMAN = 358
    PLUMED_ARCHER = 763
    PRIEST = 1023
    PRIEST_WITH_RELIC = 1400
    QUEEN = 1292
    RATTAN_ARCHER = 1129
    RELIC_CART = 1304
    REPAIRER = 156
    ROYAL_JANISSARY = 52
    SAMURAI = 291
    SCORPION = 279
    SCOUT_CAVALRY = 448
    SHARKATZOR = 1222
    SHEEP = 594
    SHEPHERD = 592
    SHOTEL_WARRIOR = 1016
    SIEGE_ONAGER = 588
    SIEGE_RAM = 548
    SIEGE_TOWER = 1105
    SKIRMISHER = 7
    SLINGER = 185
    SPEARMAN = 93
    STEPPE_LANCER = 1370
    STONE_MINER = 124
    TARKAN = 755
    TEUTONIC_KNIGHT = 25
    THROWING_AXEMAN = 281
    TORCH_A_CONVERTABLE = 854
    TORCH_B_CONVERTABLE = 1377
    TRADE_CART_EMPTY = 128
    TRADE_CART_FULL = 204
    TRADE_COG = 17
    TRANSPORT_SHIP = 545
    TREBUCHET = 42
    TREBUCHET_PACKED = 331
    TURKEY = 833
    TURTLE_SHIP = 831
    TWO_HANDED_SWORDSMAN = 473
    VILLAGER_FEMALE = 293
    VILLAGER_MALE = 83
    WAR_ELEPHANT = 239
    WAR_GALLEY = 21
    WAR_WAGON = 827
    WATER_BUFFALO = 1142
    WOAD_RAIDER = 232
    XOLOTL_WARRIOR = 1570
    SMALL_TEMP_MAP_REVEAL = 112
    LARGE_TEMP_MAP_REVEAL = 332
    BOARDER_GALLEY = 536
    """Monk for ships - can convert enemy boats with 1 range"""
    HUSKARL_BARRACKS = 759
    ELITE_HUSKARL_BARRACKS = 761
    TARKAN_STABLE = 886
    ELITE_TARKAN_STABLE = 887
    GENITOUR_ORIGINAL = 583
    """Refers to the original unit named genitour, which was a militia with a ranged attack, like a skirmisher"""
    ELITE_GENITOUR_ORIGINAL = 596
    """Refers to the original unit named genitour, which was a militia with a ranged attack, like a skirmisher"""

    # Lords of the West - DLC Units
    COUSTILLIER = 1655
    ELITE_COUSTILLIER = 1657
    FLEMISH_MILITIA = 1699
    FLEMISH_MILITIA_M = 1667
    """Refers to the Flemish militia after being converted from a male villager"""
    FLEMISH_MILITIA_F = 1697
    """Refers to the Flemish militia after being converted from a female villager"""
    SERJEANT = 1658
    ELITE_SERJEANT = 1659
    SERJEANT_DONJON = 1660
    ELITE_SERJEANT_DONJON = 1661


class GaiaUnit(IntEnum):
    # GAIA Units
    BEAR = 486
    BUTTERFLY1 = 1608
    BUTTERFLY2 = 1609
    BUTTERFLY3 = 1610
    CROCODILE = 1031
    DEER = 65
    DIRE_WOLF = 89
    ELEPHANT = 1301
    FALCON = 1056
    HAWK = 96
    IBEX = 1239
    IRON_BOAR = 810
    JAGUAR = 812
    JAVELINA = 822
    KOMODO_DRAGON = 1135
    LION = 1029
    MACAW = 816
    OSTRICH = 1026
    RABID_WOLF = 202
    RHINOCEROS = 1139
    SEAGULLS = 303
    SNOW_LEOPARD = 1241
    STORK = 1028
    STORMY_DOG = 862
    TIGER = 1137
    VULTURE = 1305
    WILD_BACTRIAN_CAMEL = 1247
    WILD_BOAR = 48
    WILD_CAMEL = 884
    WILD_HORSE = 835
    WOLF = 126
    ZEBRA = 1019

    # Player Units
    MOVEABLE_MAP_REVEALER = 0
    ALFRED_THE_ALPACA = 1300
    AMAZON_ARCHER = 850
    AMAZON_WARRIOR = 825
    ARAMBAI = 1126
    ARBALESTER = 492
    ARCHER = 4
    BACTRIAN_CAMEL = 1237
    BALLISTA_ELEPHANT = 1120
    BANDIT = 299
    BATTERING_RAM = 1258
    BATTLE_ELEPHANT = 1132
    BERSERK = 692
    BOMBARD_CANNON = 36
    BOYAR = 876
    BUILDER = 118
    CAMEL = 897
    CAMEL_ARCHER = 1007
    CAMEL_RIDER = 329
    CANNON_GALLEON = 420
    CANOE = 778
    CAPPED_RAM = 422
    CARAVEL = 1004
    CART = 1338
    CATAPHRACT = 40
    CAVALIER = 283
    CAVALRY_ARCHER = 39
    CENTURION = 275
    CHAMPION = 567
    CHU_KO_NU = 73
    COBRA_CAR = 748
    CONDOTTIERO = 882
    CONQUISTADOR = 771
    COW_A = 705
    COW_B = 1596
    COW_C = 1598
    COW_D = 1600
    CROSSBOWMAN = 24
    DEMOLITION_RAFT = 1104
    DEMOLITION_SHIP = 527
    DONKEY = 846
    DRAGON_SHIP = 1302
    EAGLE_SCOUT = 751
    EAGLE_WARRIOR = 753
    EASTERN_SWORDSMAN = 894
    ELEPHANT_ARCHER = 873
    ELITE_ARAMBAI = 1128
    ELITE_BALLISTA_ELEPHANT = 1122
    ELITE_BATTLE_ELEPHANT = 1134
    ELITE_BERSERK = 694
    ELITE_BOYAR = 878
    ELITE_CAMEL_ARCHER = 1009
    ELITE_CANNON_GALLEON = 691
    ELITE_CARAVEL = 1006
    ELITE_CATAPHRACT = 553
    ELITE_CHU_KO_NU = 559
    ELITE_CONQUISTADOR = 773
    ELITE_EAGLE_WARRIOR = 752
    ELITE_ELEPHANT_ARCHER = 875
    ELITE_GBETO = 1015
    ELITE_GENITOUR = 1012
    ELITE_GENOESE_CROSSBOWMAN = 868
    ELITE_HUSKARL = 555
    ELITE_JAGUAR_WARRIOR = 726
    ELITE_JANISSARY = 557
    ELITE_KAMAYUK = 881
    ELITE_KARAMBIT_WARRIOR = 1125
    ELITE_KESHIK = 1230
    ELITE_KIPCHAK = 1233
    ELITE_KONNIK = 1227
    ELITE_KONNIK_DISMOUNTED = 1253
    ELITE_LEITIS = 1236
    ELITE_LONGBOAT = 533
    ELITE_LONGBOWMAN = 530
    ELITE_MAGYAR_HUSZAR = 871
    ELITE_MAMELUKE = 556
    ELITE_MANGUDAI = 561
    ELITE_ORGAN_GUN = 1003
    ELITE_PLUMED_ARCHER = 765
    ELITE_RATTAN_ARCHER = 1131
    ELITE_SAMURAI = 560
    ELITE_SHOTEL_WARRIOR = 1018
    ELITE_SKIRMISHER = 6
    ELITE_STEPPE_LANCER = 1372
    ELITE_TARKAN = 757
    ELITE_TEUTONIC_KNIGHT = 554
    ELITE_THROWING_AXEMAN = 531
    ELITE_TURTLE_SHIP = 832
    ELITE_WAR_ELEPHANT = 558
    ELITE_WAR_WAGON = 829
    ELITE_WOAD_RAIDER = 534
    FARMER = 259
    FAST_FIRE_SHIP = 532
    FIRE_GALLEY = 1103
    FIRE_SHIP = 529
    FISHERMAN = 56
    FISHING_SHIP = 13
    FLAMETHROWER = 188
    FLAMING_CAMEL = 1263
    FORAGER = 120
    FURIOUS_THE_MONKEY_BOY = 860
    GALLEON = 442
    GALLEY = 539
    GBETO = 1013
    GENITOUR = 1010
    GENOESE_CROSSBOWMAN = 866
    GOAT = 1060
    GOLD_MINER = 579
    GOOSE = 1243
    HALBERDIER = 359
    HAND_CANNONEER = 5
    HEAVY_CAMEL_RIDER = 330
    HEAVY_CAVALRY_ARCHER = 474
    HEAVY_CROSSBOWMAN = 493
    HEAVY_DEMOLITION_SHIP = 528
    HEAVY_PIKEMAN = 892
    HEAVY_SCORPION = 542
    HEAVY_SWORDSMAN = 76
    HORSE_A = 814
    HORSE_B = 1356
    HORSE_C = 1602
    HORSE_D = 1604
    HORSE_E = 1606
    HUNTER = 122
    HUSKARL = 41
    HUSSAR = 441
    IMPERIAL_CAMEL_RIDER = 207
    IMPERIAL_SKIRMISHER = 1155
    INVISIBLE_OBJECT = 1291
    IROQUOIS_WARRIOR = 1374
    JAGUAR_WARRIOR = 725
    JANISSARY = 46
    JUNK = 15
    KAMAYUK = 879
    KARAMBIT_WARRIOR = 1123
    KESHIK = 1228
    KHAN = 1275
    KING = 434
    KIPCHAK = 1231
    KNIGHT = 38
    KONNIK = 1225
    KONNIK_DISMOUNTED = 1252
    LEGIONARY = 1
    LEITIS = 1234
    LIGHT_CAVALRY = 546
    LLAMA = 305
    LONG_SWORDSMAN = 77
    LONGBOAT = 250
    LONGBOWMAN = 8
    LUMBERJACK = 123
    MAGYAR_HUSZAR = 869
    MAMELUKE = 282
    MAN_AT_ARMS = 75
    MANGONEL = 280
    MANGUDAI = 11
    MERCHANT = 1572
    MILITIA = 74
    MISSIONARY = 775
    MONK = 125
    MONK_WITH_RELIC = 286
    NINJA = 1145
    NORSE_WARRIOR = 361
    ONAGER = 550
    ORGAN_GUN = 1001
    OX_CART = 1271
    OX_WAGON = 1273
    PALADIN = 569
    PENGUIN = 639
    PETARD = 440
    PHOTONMAN = 1577
    PIG = 1245
    PIKEMAN = 358
    PLUMED_ARCHER = 763
    PRIEST = 1023
    PRIEST_WITH_RELIC = 1400
    QUEEN = 1292
    RATTAN_ARCHER = 1129
    RELIC_CART = 1304
    REPAIRER = 156
    ROYAL_JANISSARY = 52
    SAMURAI = 291
    SCORPION = 279
    SCOUT_CAVALRY = 448
    SHARKATZOR = 1222
    SHEEP = 594
    SHEPHERD = 592
    SHOTEL_WARRIOR = 1016
    SIEGE_ONAGER = 588
    SIEGE_RAM = 548
    SIEGE_TOWER = 1105
    SKIRMISHER = 7
    SLINGER = 185
    SPEARMAN = 93
    STEPPE_LANCER = 1370
    STONE_MINER = 124
    TARKAN = 755
    TEUTONIC_KNIGHT = 25
    THROWING_AXEMAN = 281
    TORCH_A_CONVERTABLE = 854
    TORCH_B_CONVERTABLE = 1377
    TRADE_CART_EMPTY = 128
    TRADE_CART_FULL = 204
    TRADE_COG = 17
    TRANSPORT_SHIP = 545
    TREBUCHET = 42
    TREBUCHET_PACKED = 331
    TURKEY = 833
    TURTLE_SHIP = 831
    TWO_HANDED_SWORDSMAN = 473
    VILLAGER_FEMALE = 293
    VILLAGER_MALE = 83
    WAR_ELEPHANT = 239
    WAR_GALLEY = 21
    WAR_WAGON = 827
    WATER_BUFFALO = 1142
    WOAD_RAIDER = 232
    XOLOTL_WARRIOR = 1570
    SMALL_TEMP_MAP_REVEAL = 112
    LARGE_TEMP_MAP_REVEAL = 332
    BOARDER_GALLEY = 536
    """Monk for ships - can convert enemy boats with 1 range"""
    HUSKARL_BARRACKS = 759
    ELITE_HUSKARL_BARRACKS = 761
    TARKAN_STABLE = 886
    ELITE_TARKAN_STABLE = 887
    GENITOUR_ORIGINAL = 583
    """Refers to the original unit named genitour, which was a militia with a ranged attack, like a skirmisher"""
    ELITE_GENITOUR_ORIGINAL = 596
    """Refers to the original unit named genitour, which was a militia with a ranged attack, like a skirmisher"""

    # Lords of the West - DLC Units
    COUSTILLIER = 1655
    ELITE_COUSTILLIER = 1657
    FLEMISH_MILITIA = 1699
    FLEMISH_MILITIA_M = 1667
    """Refers to the Flemish militia after being converted from a male villager"""
    FLEMISH_MILITIA_F = 1697
    """Refers to the Flemish militia after being converted from a female villager"""
    SERJEANT = 1658
    ELITE_SERJEANT = 1659
    SERJEANT_DONJON = 1660
    ELITE_SERJEANT_DONJON = 1661


class UnitIcon(IntEnum):
    MOVEABLE_MAP_REVEALER = -1
    ALFRED_THE_ALPACA = 177
    AMAZON_ARCHER = 165
    AMAZON_WARRIOR = 166
    ARAMBAI = 230
    ARBALESTER = 90
    ARCHER = 17
    BACTRIAN_CAMEL = 266
    BALLISTA_ELEPHANT = 231
    BANDIT = 8
    BATTERING_RAM = 74
    BATTLE_ELEPHANT = 228
    BERSERK = 38
    BOMBARD_CANNON = 30
    BOYAR = 114
    BUILDER = 330
    CAMEL = 135
    CAMEL_ARCHER = 191
    CAMEL_RIDER = 78
    CANNON_GALLEON = 55
    CANOE = 164
    CAPPED_RAM = 63
    CARAVEL = 198
    CART = 34
    CATAPHRACT = 35
    CAVALIER = 49
    CAVALRY_ARCHER = 19
    CENTURION = 138
    CHAMPION = 72
    CHU_KO_NU = 36
    COBRA_CAR = 142
    CONDOTTIERO = 134
    CONQUISTADOR = 106
    COW_A = 150
    COW_B = 150
    COW_C = 150
    COW_D = 150
    CROSSBOWMAN = 18
    DEMOLITION_RAFT = 202
    DEMOLITION_SHIP = 84
    DONKEY = 158
    DRAGON_SHIP = 178
    EAGLE_SCOUT = 109
    EAGLE_WARRIOR = 148
    EASTERN_SWORDSMAN = 186
    ELEPHANT_ARCHER = 93
    ELITE_ARAMBAI = 230
    ELITE_BALLISTA_ELEPHANT = 231
    ELITE_BATTLE_ELEPHANT = 246
    ELITE_BERSERK = 38
    ELITE_BOYAR = 114
    ELITE_CAMEL_ARCHER = 191
    ELITE_CANNON_GALLEON = 298
    ELITE_CARAVEL = 198
    ELITE_CATAPHRACT = 35
    ELITE_CHU_KO_NU = 36
    ELITE_CONQUISTADOR = 106
    ELITE_EAGLE_WARRIOR = 149
    ELITE_ELEPHANT_ARCHER = 93
    ELITE_GBETO = 197
    ELITE_GENITOUR = 201
    ELITE_GENOESE_CROSSBOWMAN = 133
    ELITE_HUSKARL = 50
    ELITE_JAGUAR_WARRIOR = 110
    ELITE_JANISSARY = 39
    ELITE_KAMAYUK = 97
    ELITE_KARAMBIT_WARRIOR = 233
    ELITE_KESHIK = 251
    ELITE_KIPCHAK = 252
    ELITE_KONNIK = 249
    ELITE_KONNIK_DISMOUNTED = 250
    ELITE_LEITIS = 253
    ELITE_LONGBOAT = 40
    ELITE_LONGBOWMAN = 41
    ELITE_MAGYAR_HUSZAR = 99
    ELITE_MAMELUKE = 37
    ELITE_MANGUDAI = 42
    ELITE_ORGAN_GUN = 190
    ELITE_PLUMED_ARCHER = 108
    ELITE_RATTAN_ARCHER = 232
    ELITE_SAMURAI = 44
    ELITE_SHOTEL_WARRIOR = 195
    ELITE_SKIRMISHER = 21
    ELITE_STEPPE_LANCER = 274
    ELITE_TARKAN = 105
    ELITE_TEUTONIC_KNIGHT = 45
    ELITE_THROWING_AXEMAN = 46
    ELITE_TURTLE_SHIP = 116
    ELITE_WAR_ELEPHANT = 43
    ELITE_WAR_WAGON = 117
    ELITE_WOAD_RAIDER = 47
    FARMER = 332
    FAST_FIRE_SHIP = 85
    FIRE_GALLEY = 203
    FIRE_SHIP = 86
    FISHERMAN = 332
    FISHING_SHIP = 24
    FLAMETHROWER = 144
    FLAMING_CAMEL = 270
    FORAGER = 332
    FURIOUS_THE_MONKEY_BOY = 132
    GALLEON = 60
    GALLEY = 87
    GBETO = 197
    GENITOUR = 201
    GENOESE_CROSSBOWMAN = 133
    GOAT = 200
    GOLD_MINER = 334
    GOOSE = 265
    HALBERDIER = 104
    HAND_CANNONEER = 22
    HEAVY_CAMEL_RIDER = 79
    HEAVY_CAVALRY_ARCHER = 71
    HEAVY_CROSSBOWMAN = 133
    HEAVY_DEMOLITION_SHIP = 83
    HEAVY_PIKEMAN = 136
    HEAVY_SCORPION = 89
    HEAVY_SWORDSMAN = 184
    HORSE_A = 112
    HORSE_B = 112
    HORSE_C = 112
    HORSE_D = 112
    HORSE_E = 112
    HUNTER = 332
    HUSKARL = 50
    HUSSAR = 103
    IMPERIAL_CAMEL_RIDER = 185
    IMPERIAL_SKIRMISHER = 229
    INVISIBLE_OBJECT = -1
    IROQUOIS_WARRIOR = 297
    JAGUAR_WARRIOR = 110
    JANISSARY = 39
    JUNK = 211
    KAMAYUK = 97
    KARAMBIT_WARRIOR = 233
    KESHIK = 251
    KHAN = 258
    KING = 48
    KIPCHAK = 252
    KNIGHT = 1
    KONNIK = 249
    KONNIK_DISMOUNTED = 250
    LEGIONARY = 139
    LEITIS = 253
    LIGHT_CAVALRY = 91
    LLAMA = 156
    LONG_SWORDSMAN = 13
    LONGBOAT = 40
    LONGBOWMAN = 41
    LUMBERJACK = 339
    MAGYAR_HUSZAR = 99
    MAMELUKE = 37
    MAN_AT_ARMS = 10
    MANGONEL = 27
    MANGUDAI = 42
    MERCHANT = 346
    MILITIA = 8
    MISSIONARY = 107
    MONK = 33
    MONK_WITH_RELIC = 33
    NINJA = 299
    NORSE_WARRIOR = 140
    ONAGER = 101
    ORGAN_GUN = 190
    OX_CART = 263
    OX_WAGON = 264
    PALADIN = 2
    PENGUIN = 157
    PETARD = 113
    PHOTONMAN = 300
    PIG = 269
    PIKEMAN = 11
    PLUMED_ARCHER = 108
    PRIEST = 294
    PRIEST_WITH_RELIC = 33
    QUEEN = 168
    RATTAN_ARCHER = 232
    RELIC_CART = 295
    REPAIRER = 330
    ROYAL_JANISSARY = 296
    SAMURAI = 44
    SCORPION = 80
    SCOUT_CAVALRY = 64
    SHARKATZOR = 352
    SHEEP = 96
    SHEPHERD = 332
    SHOTEL_WARRIOR = 195
    SIEGE_ONAGER = 102
    SIEGE_RAM = 73
    SIEGE_TOWER = 212
    SKIRMISHER = 20
    SLINGER = 143
    SPEARMAN = 31
    STEPPE_LANCER = 273
    STONE_MINER = 336
    TARKAN = 105
    TEUTONIC_KNIGHT = 45
    THROWING_AXEMAN = 46
    TORCH_A_CONVERTABLE = -1
    TORCH_B_CONVERTABLE = -1
    TRADE_CART_EMPTY = 34
    TRADE_CART_FULL = 34
    TRADE_CART_MESO = 287
    TRADE_COG = 23
    TRANSPORT_SHIP = 95
    TREBUCHET = 28
    TREBUCHET_PACKED = 29
    TURKEY = 115
    TURTLE_SHIP = 116
    TWO_HANDED_SWORDSMAN = 12
    VILLAGER_FEMALE = 16
    VILLAGER_MALE = 15
    WAR_ELEPHANT = 43
    WAR_GALLEY = 25
    WAR_WAGON = 117
    WATER_BUFFALO = 224
    WOAD_RAIDER = 47
    XOLOTL_WARRIOR = 351
    SMALL_TEMP_MAP_REVEAL = -1
    LARGE_TEMP_MAP_REVEAL = -1
    BOARDER_GALLEY = 82
    HUSKARL_BARRACKS = 50
    ELITE_HUSKARL_BARRACKS = 50
    TARKAN_STABLE = 105
    ELITE_TARKAN_STABLE = 105
    GENITOUR_ORIGINAL = 19
    ELITE_GENITOUR_ORIGINAL = 19
    COUSTILLIER = 355
    ELITE_COUSTILLIER = 355
    FLEMISH_MILITIA = 354
    FLEMISH_MILITIA_M = -1
    FLEMISH_MILITIA_F = 354
    SERJEANT = 356
    ELITE_SERJEANT = 356
    SERJEANT_DONJON = 356
    ELITE_SERJEANT_DONJON = 356


class GaiaUnitIcon(IntEnum):
    BEAR = 151
    BUTTERFLY1 = -1
    BUTTERFLY2 = -1
    BUTTERFLY3 = -1
    CROCODILE = 193
    DEER = 3
    DIRE_WOLF = 7
    ELEPHANT = 179
    FALCON = 5
    HAWK = 283
    IBEX = 267
    IRON_BOAR = 98
    JAGUAR = 111
    JAVELINA = 98
    KOMODO_DRAGON = 226
    LION = 194
    MACAW = 284
    OSTRICH = 196
    RABID_WOLF = 7
    RHINOCEROS = 225
    SEAGULLS = -1
    SNOW_LEOPARD = 268
    STORK = 285
    STORMY_DOG = 159
    TIGER = 227
    VULTURE = 286
    WILD_BACTRIAN_CAMEL = 266
    WILD_BOAR = 98
    WILD_CAMEL = 135
    WILD_HORSE = 112
    WOLF = 7
    ZEBRA = 192
    MOVEABLE_MAP_REVEALER = -1
    ALFRED_THE_ALPACA = 177
    AMAZON_ARCHER = 165
    AMAZON_WARRIOR = 166
    ARAMBAI = 230
    ARBALESTER = 90
    ARCHER = 17
    BACTRIAN_CAMEL = 266
    BALLISTA_ELEPHANT = 231
    BANDIT = 8
    BATTERING_RAM = 74
    BATTLE_ELEPHANT = 228
    BERSERK = 38
    BOMBARD_CANNON = 30
    BOYAR = 114
    BUILDER = 330
    CAMEL = 135
    CAMEL_ARCHER = 191
    CAMEL_RIDER = 78
    CANNON_GALLEON = 55
    CANOE = 164
    CAPPED_RAM = 63
    CARAVEL = 198
    CART = 34
    CATAPHRACT = 35
    CAVALIER = 49
    CAVALRY_ARCHER = 19
    CENTURION = 138
    CHAMPION = 72
    CHU_KO_NU = 36
    COBRA_CAR = 142
    CONDOTTIERO = 134
    CONQUISTADOR = 106
    COW_A = 150
    COW_B = 150
    COW_C = 150
    COW_D = 150
    CROSSBOWMAN = 18
    DEMOLITION_RAFT = 202
    DEMOLITION_SHIP = 84
    DONKEY = 158
    DRAGON_SHIP = 178
    EAGLE_SCOUT = 109
    EAGLE_WARRIOR = 148
    EASTERN_SWORDSMAN = 186
    ELEPHANT_ARCHER = 93
    ELITE_ARAMBAI = 230
    ELITE_BALLISTA_ELEPHANT = 231
    ELITE_BATTLE_ELEPHANT = 246
    ELITE_BERSERK = 38
    ELITE_BOYAR = 114
    ELITE_CAMEL_ARCHER = 191
    ELITE_CANNON_GALLEON = 298
    ELITE_CARAVEL = 198
    ELITE_CATAPHRACT = 35
    ELITE_CHU_KO_NU = 36
    ELITE_CONQUISTADOR = 106
    ELITE_EAGLE_WARRIOR = 149
    ELITE_ELEPHANT_ARCHER = 93
    ELITE_GBETO = 197
    ELITE_GENITOUR = 201
    ELITE_GENOESE_CROSSBOWMAN = 133
    ELITE_HUSKARL = 50
    ELITE_JAGUAR_WARRIOR = 110
    ELITE_JANISSARY = 39
    ELITE_KAMAYUK = 97
    ELITE_KARAMBIT_WARRIOR = 233
    ELITE_KESHIK = 251
    ELITE_KIPCHAK = 252
    ELITE_KONNIK = 249
    ELITE_KONNIK_DISMOUNTED = 250
    ELITE_LEITIS = 253
    ELITE_LONGBOAT = 40
    ELITE_LONGBOWMAN = 41
    ELITE_MAGYAR_HUSZAR = 99
    ELITE_MAMELUKE = 37
    ELITE_MANGUDAI = 42
    ELITE_ORGAN_GUN = 190
    ELITE_PLUMED_ARCHER = 108
    ELITE_RATTAN_ARCHER = 232
    ELITE_SAMURAI = 44
    ELITE_SHOTEL_WARRIOR = 195
    ELITE_SKIRMISHER = 21
    ELITE_STEPPE_LANCER = 274
    ELITE_TARKAN = 105
    ELITE_TEUTONIC_KNIGHT = 45
    ELITE_THROWING_AXEMAN = 46
    ELITE_TURTLE_SHIP = 116
    ELITE_WAR_ELEPHANT = 43
    ELITE_WAR_WAGON = 117
    ELITE_WOAD_RAIDER = 47
    FARMER = 332
    FAST_FIRE_SHIP = 85
    FIRE_GALLEY = 203
    FIRE_SHIP = 86
    FISHERMAN = 332
    FISHING_SHIP = 24
    FLAMETHROWER = 144
    FLAMING_CAMEL = 270
    FORAGER = 332
    FURIOUS_THE_MONKEY_BOY = 132
    GALLEON = 60
    GALLEY = 87
    GBETO = 197
    GENITOUR = 201
    GENOESE_CROSSBOWMAN = 133
    GOAT = 200
    GOLD_MINER = 334
    GOOSE = 265
    HALBERDIER = 104
    HAND_CANNONEER = 22
    HEAVY_CAMEL_RIDER = 79
    HEAVY_CAVALRY_ARCHER = 71
    HEAVY_CROSSBOWMAN = 133
    HEAVY_DEMOLITION_SHIP = 83
    HEAVY_PIKEMAN = 136
    HEAVY_SCORPION = 89
    HEAVY_SWORDSMAN = 184
    HORSE_A = 112
    HORSE_B = 112
    HORSE_C = 112
    HORSE_D = 112
    HORSE_E = 112
    HUNTER = 332
    HUSKARL = 50
    HUSSAR = 103
    IMPERIAL_CAMEL_RIDER = 185
    IMPERIAL_SKIRMISHER = 229
    INVISIBLE_OBJECT = -1
    IROQUOIS_WARRIOR = 297
    JAGUAR_WARRIOR = 110
    JANISSARY = 39
    JUNK = 211
    KAMAYUK = 97
    KARAMBIT_WARRIOR = 233
    KESHIK = 251
    KHAN = 258
    KING = 48
    KIPCHAK = 252
    KNIGHT = 1
    KONNIK = 249
    KONNIK_DISMOUNTED = 250
    LEGIONARY = 139
    LEITIS = 253
    LIGHT_CAVALRY = 91
    LLAMA = 156
    LONG_SWORDSMAN = 13
    LONGBOAT = 40
    LONGBOWMAN = 41
    LUMBERJACK = 339
    MAGYAR_HUSZAR = 99
    MAMELUKE = 37
    MAN_AT_ARMS = 10
    MANGONEL = 27
    MANGUDAI = 42
    MERCHANT = 346
    MILITIA = 8
    MISSIONARY = 107
    MONK = 33
    MONK_WITH_RELIC = 33
    NINJA = 299
    NORSE_WARRIOR = 140
    ONAGER = 101
    ORGAN_GUN = 190
    OX_CART = 263
    OX_WAGON = 264
    PALADIN = 2
    PENGUIN = 157
    PETARD = 113
    PHOTONMAN = 300
    PIG = 269
    PIKEMAN = 11
    PLUMED_ARCHER = 108
    PRIEST = 294
    PRIEST_WITH_RELIC = 33
    QUEEN = 168
    RATTAN_ARCHER = 232
    RELIC_CART = 295
    REPAIRER = 330
    ROYAL_JANISSARY = 296
    SAMURAI = 44
    SCORPION = 80
    SCOUT_CAVALRY = 64
    SHARKATZOR = 352
    SHEEP = 96
    SHEPHERD = 332
    SHOTEL_WARRIOR = 195
    SIEGE_ONAGER = 102
    SIEGE_RAM = 73
    SIEGE_TOWER = 212
    SKIRMISHER = 20
    SLINGER = 143
    SPEARMAN = 31
    STEPPE_LANCER = 273
    STONE_MINER = 336
    TARKAN = 105
    TEUTONIC_KNIGHT = 45
    THROWING_AXEMAN = 46
    TORCH_A_CONVERTABLE = -1
    TORCH_B_CONVERTABLE = -1
    TRADE_CART_EMPTY = 34
    TRADE_CART_FULL = 34
    TRADE_CART_MESO = 287
    TRADE_COG = 23
    TRANSPORT_SHIP = 95
    TREBUCHET = 28
    TREBUCHET_PACKED = 29
    TURKEY = 115
    TURTLE_SHIP = 116
    TWO_HANDED_SWORDSMAN = 12
    VILLAGER_FEMALE = 16
    VILLAGER_MALE = 15
    WAR_ELEPHANT = 43
    WAR_GALLEY = 25
    WAR_WAGON = 117
    WATER_BUFFALO = 224
    WOAD_RAIDER = 47
    XOLOTL_WARRIOR = 351
    SMALL_TEMP_MAP_REVEAL = -1
    LARGE_TEMP_MAP_REVEAL = -1
    BOARDER_GALLEY = 82
    HUSKARL_BARRACKS = 50
    ELITE_HUSKARL_BARRACKS = 50
    TARKAN_STABLE = 105
    ELITE_TARKAN_STABLE = 105
    GENITOUR_ORIGINAL = 19
    ELITE_GENITOUR_ORIGINAL = 19
    COUSTILLIER = 355
    ELITE_COUSTILLIER = 355
    FLEMISH_MILITIA = 354
    FLEMISH_MILITIA_M = -1
    FLEMISH_MILITIA_F = 354
    SERJEANT = 356
    ELITE_SERJEANT = 356
    SERJEANT_DONJON = 356
    ELITE_SERJEANT_DONJON = 356


unit_names = bidict({
    0: "moveable_map_revealer",
    1: "legionary",
    4: "archer",
    5: "hand_cannoneer",
    6: "elite_skirmisher",
    7: "skirmisher",
    8: "longbowman",
    11: "mangudai",
    13: "fishing_ship",
    15: "junk",
    17: "trade_cog",
    21: "war_galley",
    24: "crossbowman",
    25: "teutonic_knight",
    36: "bombard_cannon",
    38: "knight",
    39: "cavalry_archer",
    40: "cataphract",
    41: "huskarl",
    42: "trebuchet",
    46: "janissary",
    52: "royal_janissary",
    56: "fisherman",
    73: "chu_ko_nu",
    74: "militia",
    75: "man_at_arms",
    76: "heavy_swordsman",
    77: "long_swordsman",
    83: "villager_male",
    93: "spearman",
    118: "builder",
    120: "forager",
    122: "hunter",
    123: "lumberjack",
    124: "stone_miner",
    125: "monk",
    128: "trade_cart_empty",
    156: "repairer",
    185: "slinger",
    188: "flamethrower",
    204: "trade_cart_full",
    207: "imperial_camel_rider",
    232: "woad_raider",
    239: "war_elephant",
    250: "longboat",
    259: "farmer",
    275: "centurion",
    279: "scorpion",
    280: "mangonel",
    281: "throwing_axeman",
    282: "mameluke",
    283: "cavalier",
    286: "monk_with_relic",
    291: "samurai",
    293: "villager_female",
    299: "bandit",
    305: "llama",
    329: "camel_rider",
    330: "heavy_camel_rider",
    331: "trebuchet_packed",
    358: "pikeman",
    359: "halberdier",
    361: "norse_warrior",
    420: "cannon_galleon",
    422: "capped_ram",
    434: "king",
    440: "petard",
    441: "hussar",
    442: "galleon",
    448: "scout_cavalry",
    473: "two_handed_swordsman",
    474: "heavy_cavalry_archer",
    492: "arbalester",
    493: "heavy_crossbowman",
    527: "demolition_ship",
    528: "heavy_demolition_ship",
    529: "fire_ship",
    530: "elite_longbowman",
    531: "elite_throwing_axeman",
    532: "fast_fire_ship",
    533: "elite_longboat",
    534: "elite_woad_raider",
    539: "galley",
    542: "heavy_scorpion",
    545: "transport_ship",
    546: "light_cavalry",
    548: "siege_ram",
    550: "onager",
    553: "elite_cataphract",
    554: "elite_teutonic_knight",
    555: "elite_huskarl",
    556: "elite_mameluke",
    557: "elite_janissary",
    558: "elite_war_elephant",
    559: "elite_chu_ko_nu",
    560: "elite_samurai",
    561: "elite_mangudai",
    567: "champion",
    569: "paladin",
    579: "gold_miner",
    588: "siege_onager",
    592: "shepherd",
    594: "sheep",
    639: "penguin",
    691: "elite_cannon_galleon",
    692: "berserk",
    694: "elite_berserk",
    705: "cow_a",
    725: "jaguar_warrior",
    726: "elite_jaguar_warrior",
    748: "cobra_car",
    751: "eagle_scout",
    752: "elite_eagle_warrior",
    753: "eagle_warrior",
    755: "tarkan",
    757: "elite_tarkan",
    763: "plumed_archer",
    765: "elite_plumed_archer",
    771: "conquistador",
    773: "elite_conquistador",
    775: "missionary",
    778: "canoe",
    814: "horse_a",
    825: "amazon_warrior",
    827: "war_wagon",
    829: "elite_war_wagon",
    831: "turtle_ship",
    832: "elite_turtle_ship",
    833: "turkey",
    846: "donkey",
    850: "amazon_archer",
    854: "torch_a_convertable",
    860: "furious_the_monkey_boy",
    866: "genoese_crossbowman",
    868: "elite_genoese_crossbowman",
    869: "magyar_huszar",
    871: "elite_magyar_huszar",
    873: "elephant_archer",
    875: "elite_elephant_archer",
    876: "boyar",
    878: "elite_boyar",
    879: "kamayuk",
    881: "elite_kamayuk",
    882: "condottiero",
    892: "heavy_pikeman",
    894: "eastern_swordsman",
    897: "camel",
    1001: "organ_gun",
    1003: "elite_organ_gun",
    1004: "caravel",
    1006: "elite_caravel",
    1007: "camel_archer",
    1009: "elite_camel_archer",
    1010: "genitour",
    1012: "elite_genitour",
    1013: "gbeto",
    1015: "elite_gbeto",
    1016: "shotel_warrior",
    1018: "elite_shotel_warrior",
    1023: "priest",
    1060: "goat",
    1103: "fire_galley",
    1104: "demolition_raft",
    1105: "siege_tower",
    1120: "ballista_elephant",
    1122: "elite_ballista_elephant",
    1123: "karambit_warrior",
    1125: "elite_karambit_warrior",
    1126: "arambai",
    1128: "elite_arambai",
    1129: "rattan_archer",
    1131: "elite_rattan_archer",
    1132: "battle_elephant",
    1134: "elite_battle_elephant",
    1142: "water_buffalo",
    1145: "ninja",
    1155: "imperial_skirmisher",
    1222: "sharkatzor",
    1225: "konnik",
    1227: "elite_konnik",
    1228: "keshik",
    1230: "elite_keshik",
    1231: "kipchak",
    1233: "elite_kipchak",
    1234: "leitis",
    1236: "elite_leitis",
    1237: "bactrian_camel",
    1243: "goose",
    1245: "pig",
    1252: "konnik_dismounted",
    1253: "elite_konnik_dismounted",
    1258: "battering_ram",
    1263: "flaming_camel",
    1271: "ox_cart",
    1273: "ox_wagon",
    1275: "khan",
    1291: "invisible_object",
    1292: "queen",
    1300: "alfred_the_alpaca",
    1302: "dragon_ship",
    1304: "relic_cart",
    1338: "cart",
    1356: "horse_b",
    1370: "steppe_lancer",
    1372: "elite_steppe_lancer",
    1374: "iroquois_warrior",
    1377: "torch_b_convertable",
    1400: "priest_with_relic",
    1570: "xolotl_warrior",
    1572: "merchant",
    1577: "photonman",
    1596: "cow_b",
    1598: "cow_c",
    1600: "cow_d",
    1602: "horse_c",
    1604: "horse_d",
    1606: "horse_e",

    # Gaia Units
    48: "wild_boar",
    65: "deer",
    89: "dire_wolf",
    96: "hawk",
    126: "wolf",
    202: "rabid_wolf",
    303: "seagulls",
    486: "bear",
    810: "iron_boar",
    812: "jaguar",
    816: "macaw",
    822: "javelina",
    835: "wild_horse",
    862: "stormy_dog",
    884: "wild_camel",
    1019: "zebra",
    1026: "ostrich",
    1028: "stork",
    1029: "lion",
    1031: "crocodile",
    1137: "tiger",
    1056: "falcon",
    1135: "komodo_dragon",
    1139: "rhinoceros",
    1241: "snow_leopard",
    1247: "wild_bactrian_camel",
    1301: "elephant",
    1305: "vulture",
    1239: "ibex",
    1608: "butterfly1",
    1609: "butterfly2",
    1610: "butterfly3",

    # Lords of the West - DLC Units
    1655: "coustillier",
    1657: "elite_coustillier",
    1699: "flemish_militia",
    1667: "flemish_militia_m",
    1697: "flemish_militia_f",
    1658: "serjeant",
    1659: "elite_serjeant",
    1660: "serjeant_donjon",
    1661: "elite_serjeant_donjon",
})
