from enum import Enum

from bidict import bidict


class Techs(Enum):
    ANARCHY = 16
    ANDEAN_SLING = 516
    ARBALESTER = 237
    ARCHITECTURE = 51
    ARQUEBUS = 573
    ARROWSLITS = 608
    ARSON = 602
    ARTILLERY = 10
    ATHEISM = 21
    ATLATL = 460
    ATONEMENT = 319
    AZTECS = 543
    BAGAINS = 686
    BALLISTICS = 93
    BANKING = 17
    BEARDED_AXE = 83
    BERBERS = 583
    BERSERKERGANG = 49
    BLAST_FURNACE = 75
    BLOCK_PRINTING = 230
    BLOODLINES = 435
    BODKIN_ARROW = 200
    BOMBARD_CANNON = 188
    BOMBARD_TOWER = 64
    BOW_SAW = 203
    BRACER = 201
    BRITONS = 529
    BULGARIANS = 673
    BURMESE = 652
    BYZANTINES = 535
    CANNON_GALLEON = 37
    CAPPED_RAM = 96
    CARAVAN = 48
    CAREENING = 374
    CARRACK = 572
    CARTOGRAPHY = 19
    CASTLE_AGE = 102
    CAVALIER = 209
    CELTS = 541
    CHAIN_BARDING_ARMOR = 82
    CHAIN_MAIL_ARMOR = 76
    CHAMPION = 264
    CHATRAS = 628
    CHEMISTRY = 47
    CHINESE = 534
    CHIVALRY = 493
    COINAGE = 23
    CONSCRIPTION = 315
    CORVINIAN_ARMY = 514
    COURIERS = 517
    CRENELLATIONS = 11
    CROP_ROTATION = 12
    CROSSBOWMAN = 100
    CHINESE_50_PERCENT_HP_DEMOS = 396
    CUMAN_MERCENARIES = 690
    CUMANS = 675
    DARK_AGE = 104
    DOUBLE_CROSSBOW = 623
    FRANKS_FREE_FARMING_1 = 287
    DOUBLE_BIT_AXE = 202
    DRILL = 6
    DRUZHINA = 513
    DRY_DOCK = 375
    EAGLE_WARRIOR = 384
    EL_DORADO = 4
    ELITE_ARAMBAI = 619
    ELITE_BALLISTA_ELEPHANT = 615
    ELITE_BATTLE_ELEPHANT = 631
    ELITE_BERSERK = 398
    ELITE_BOYAR = 504
    ELITE_CAMEL_ARCHER = 565
    ELITE_CANNON_GALLEON = 376
    ELITE_CARAVEL = 597
    ELITE_CATAPHRACT = 361
    ELITE_CHU_KO_NU = 362
    ELITE_CONQUISTADOR = 60
    ELITE_EAGLE_WARRIOR = 434
    ELITE_ELEPHANT_ARCHER = 481
    ELITE_GBETO = 567
    ELITE_GENITOUR = 599
    ELITE_GENOESE_CROSSBOWMAN = 468
    ELITE_HUSKARL = 365
    ELITE_JAGUAR_WARRIOR = 432
    ELITE_JANISSARY = 369
    ELITE_KAMAYUK = 509
    ELITE_KARAMBIT_WARRIOR = 617
    ELITE_KESHIK = 680
    ELITE_KIPCHAK = 682
    CHIEFTAINS = 463
    ELITE_KONNIK = 678
    ELITE_LEITIS = 684
    ELITE_LONGBOAT = 372
    ELITE_LONGBOWMAN = 360
    ELITE_MAGYAR_HUSZAR = 472
    ELITE_MAMELUKE = 368
    ELITE_MANGUDAI = 371
    ELITE_ORGAN_GUN = 563
    ELITE_PLUMED_ARCHER = 27
    ELITE_RATTAN_ARCHER = 621
    ELITE_SAMURAI = 366
    ELITE_SHOTEL_WARRIOR = 569
    ELITE_SKIRMISHER = 98
    ELITE_STEPPE_LANCER = 715
    ELITE_TARKAN = 2
    ELITE_TEUTONIC_KNIGHT = 364
    ELITE_THROWING_AXEMAN = 363
    ELITE_TURTLE_SHIP = 448
    ELITE_WAR_ELEPHANT = 367
    ELITE_WAR_WAGON = 450
    ELITE_WOAD_RAIDER = 370
    ENABLE_COWS = 557
    ENABLE_LLAMAS = 556
    ENABLE_SHEEP = 555
    ENABLE_TURKEYS = 558
    ETHIOPIANS = 581
    FAITH = 45
    FARIMBA = 577
    FAST_FIRE_SHIP = 246
    FERVOR = 252
    FEUDAL_AGE = 101
    FIRE_TOWER = 527
    FLETCHING = 199
    FORCED_LEVY = 625
    FORGING = 67
    FORTIFIED_WALL = 194
    FRANKS = 530
    FREE_CARTOGRAPHY = 600
    FUROR_CELTICA = 5
    GALLEON = 35
    GARLAND_WARS = 24
    BONFIRE = 65
    GOLD_MINING = 55
    GOLD_SHAFT_MINING = 182
    GOTHS = 531
    GREAT_WALL = 462
    GREEK_FIRE = 464
    GUARD_TOWER = 140
    GUILDS = 15
    HALBERDIER = 429
    HAND_CANNON = 85
    HAND_CART = 249
    HEATED_SHOT = 380
    HEAVY_CAMEL_RIDER = 236
    HEAVY_CAV_ARCHER = 218
    HEAVY_DEMOLITION_SHIP = 244
    HEAVY_PLOW = 13
    HEAVY_SCORPION = 239
    HERBAL_MEDICINE = 441
    HERESY = 439
    HILL_FORTS_2 = 394
    HILL_FORTS = 691
    HOARDINGS = 379
    HORSE_COLLAR = 14
    HOWDAH = 626
    HUNS = 545
    HUNTING_DOGS = 526
    HUSBANDRY = 39
    HUSSAR = 428
    ILLUMINATION = 233
    IMPERIAL_AGE = 103
    IMPERIAL_CAMEL_RIDER = 521
    IMPERIAL_SKIRMISHER = 655
    INCAS = 549
    INDIANS = 548
    INQUISITION = 492
    IRON_CASTING = 68
    IRONCLAD = 489
    ITALIANS = 547
    JAPANESE = 533
    KAMANDARAN = 488
    KASBAH = 578
    KATAPARUTO = 59
    KEEP = 63
    KHMER = 650
    KOREANS = 546
    LEATHER_ARCHER_ARMOR = 212
    LIGHT_CAVALRY = 254
    LITHUANIANS = 676
    LOGISTICA = 61
    LONG_SWORDSMAN = 207
    LOOM = 22
    MADRASAH = 490
    MAGHRABI_CAMELS = 579
    MAGYARS = 550
    MAHOUTS = 7
    MALAY = 651
    MALIANS = 582
    MAN_AT_ARMS = 222
    MANIPUR_CAVALRY = 627
    MARAUDERS = 483
    MASONRY = 50
    MAYANS = 544
    MONGOLS = 540
    MURDER_HOLES = 322
    NOMADS = 487
    OBSIDIAN_ARROWS = 485
    ONAGER = 257
    ORTHODOXY = 512
    PADDED_ARCHER_ARMOR = 211
    PALADIN = 265
    PANOKSEON = 486
    PAPER_MONEY = 629
    PARTHIAN_TACTICS = 436
    PAVISE = 494
    PERFUSION = 457
    PERSIANS = 536
    PIKEMAN = 197
    PLATE_BARDING_ARMOR = 80
    PLATE_MAIL_ARMOR = 77
    PORTUGUESE = 580
    RECURVE_BOW = 515
    REDEMPTION = 316
    REVETMENTS = 525
    RING_ARCHER_ARMOR = 219
    ROCKETRY = 52
    ROYAL_HEIRS = 574
    SANCTITY = 231
    SAPPERS = 321
    SARACENS = 537
    SCALE_BARDING_ARMOR = 81
    SCALE_MAIL_ARMOR = 74
    SCORPION = 94
    SET_MAXIMUM_POPULATION_NO_HOUSES = 658
    SHATAGNI = 507
    SHINKICHON = 445
    SHIPWRIGHT = 373
    SIEGE_ENGINEERS = 377
    SIEGE_ONAGER = 320
    SIEGE_RAM = 255
    SILK_ARMOR = 687
    SILK_ROAD = 499
    SIPAHI = 491
    SLAVS = 551
    SPANISH = 542
    SPIES_AND_TREASON = 408
    SQUIRES = 215
    STEPPE_HUSBANDRY = 689
    STIRRUPS = 685
    STONE_MINING = 278
    STONE_SHAFT_MINING = 279
    STRONGHOLD = 482
    SULTANS = 506
    SUPPLIES = 716
    SUPREMACY = 440
    TATARS = 674
    TEUTONS = 532
    THALASSOCRACY = 624
    THEOCRACY = 438
    THUMB_RING = 437
    TIGUI = 576
    TIMURID_SIEGECRAFT = 688
    TORSION_ENGINES = 575
    TOWER_SHIELDS = 692
    TOWN_CENTER_SPAWN = 639
    TOWN_PATROL = 280
    TOWN_WATCH = 8
    TRACKING = 90
    TREADMILL_CRANE = 54
    TURKS = 538
    TUSK_SWORDS = 622
    TWO_HANDED_SWORDSMAN = 217
    TWO_MAN_SAW = 221
    VIETNAMESE = 653
    VIETNAMESE_VISION = 665
    VIKINGS = 539
    WAR_GALLEY = 34
    WARWOLF = 461
    WHEELBARROW = 213
    YASAMA = 484
    YEOMEN = 3
    ZEALOTRY = 9


tech_names = bidict({
    2: "elite_tarkan",
    3: "yeomen",
    4: "el_dorado",
    5: "furor_celtica",
    6: "drill",
    7: "mahouts",
    8: "town_watch",
    9: "zealotry",
    10: "artillery",
    11: "crenellations",
    12: "crop_rotation",
    13: "heavy_plow",
    14: "horse_collar",
    15: "guilds",
    16: "anarchy",
    17: "banking",
    19: "cartography",
    21: "atheism",
    22: "loom",
    23: "coinage",
    24: "garland_wars",
    27: "elite_plumed_archer",
    34: "war_galley",
    35: "galleon",
    37: "cannon_galleon",
    39: "husbandry",
    45: "faith",
    47: "chemistry",
    48: "caravan",
    49: "berserkergang",
    50: "masonry",
    51: "architecture",
    52: "rocketry",
    54: "treadmill_crane",
    55: "gold_mining",
    59: "kataparuto",
    60: "elite_conquistador",
    61: "logistica",
    63: "keep",
    64: "bombard_tower",
    65: "bonfire",
    67: "forging",
    68: "iron_casting",
    74: "scale_mail_armor",
    75: "blast_furnace",
    76: "chain_mail_armor",
    77: "plate_mail_armor",
    80: "plate_barding_armor",
    81: "scale_barding_armor",
    82: "chain_barding_armor",
    83: "bearded_axe",
    85: "hand_cannon",
    90: "tracking",
    93: "ballistics",
    94: "scorpion",
    96: "capped_ram",
    98: "elite_skirmisher",
    100: "crossbowman",
    101: "feudal_age",
    102: "castle_age",
    103: "imperial_age",
    104: "dark_age",
    140: "guard_tower",
    182: "gold_shaft_mining",
    188: "bombard_cannon",
    194: "fortified_wall",
    197: "pikeman",
    199: "fletching",
    200: "bodkin_arrow",
    201: "bracer",
    202: "double_bit_axe",
    203: "bow_saw",
    207: "long_swordsman",
    209: "cavalier",
    211: "padded_archer_armor",
    212: "leather_archer_armor",
    213: "wheelbarrow",
    215: "squires",
    217: "two_handed_swordsman",
    218: "heavy_cav_archer",
    219: "ring_archer_armor",
    221: "two_man_saw",
    222: "man_at_arms",
    230: "block_printing",
    231: "sanctity",
    233: "illumination",
    236: "heavy_camel_rider",
    237: "arbalester",
    239: "heavy_scorpion",
    244: "heavy_demolition_ship",
    246: "fast_fire_ship",
    249: "hand_cart",
    252: "fervor",
    254: "light_cavalry",
    255: "siege_ram",
    257: "onager",
    264: "champion",
    265: "paladin",
    278: "stone_mining",
    279: "stone_shaft_mining",
    280: "town_patrol",
    287: "franks_free_farming_1",
    315: "conscription",
    316: "redemption",
    319: "atonement",
    320: "siege_onager",
    321: "sappers",
    322: "murder_holes",
    360: "elite_longbowman",
    361: "elite_cataphract",
    362: "elite_chu_ko_nu",
    363: "elite_throwing_axeman",
    364: "elite_teutonic_knight",
    365: "elite_huskarl",
    366: "elite_samurai",
    367: "elite_war_elephant",
    368: "elite_mameluke",
    369: "elite_janissary",
    370: "elite_woad_raider",
    371: "elite_mangudai",
    372: "elite_longboat",
    373: "shipwright",
    374: "careening",
    375: "dry_dock",
    376: "elite_cannon_galleon",
    377: "siege_engineers",
    379: "hoardings",
    380: "heated_shot",
    384: "eagle_warrior",
    394: "hill_forts_2",
    396: "chinese_50_percent_hp_demos",
    398: "elite_berserk",
    408: "spies_and_treason",
    428: "hussar",
    429: "halberdier",
    432: "elite_jaguar_warrior",
    434: "elite_eagle_warrior",
    435: "bloodlines",
    436: "parthian_tactics",
    437: "thumb_ring",
    438: "theocracy",
    439: "heresy",
    440: "supremacy",
    441: "herbal_medicine",
    445: "shinkichon",
    448: "elite_turtle_ship",
    450: "elite_war_wagon",
    457: "perfusion",
    460: "atlatl",
    461: "warwolf",
    462: "great_wall",
    463: "chieftains",
    464: "greek_fire",
    468: "elite_genoese_crossbowman",
    472: "elite_magyar_huszar",
    481: "elite_elephant_archer",
    482: "stronghold",
    483: "marauders",
    484: "yasama",
    485: "obsidian_arrows",
    486: "panokseon",
    487: "nomads",
    488: "kamandaran",
    489: "ironclad",
    490: "madrasah",
    491: "sipahi",
    492: "inquisition",
    493: "chivalry",
    494: "pavise",
    499: "silk_road",
    504: "elite_boyar",
    506: "sultans",
    507: "shatagni",
    509: "elite_kamayuk",
    512: "orthodoxy",
    513: "druzhina",
    514: "corvinian_army",
    515: "recurve_bow",
    516: "andean_sling",
    517: "couriers",
    521: "imperial_camel_rider",
    525: "revetments",
    526: "hunting_dogs",
    527: "fire_tower",
    529: "britons",
    530: "franks",
    531: "goths",
    532: "teutons",
    533: "japanese",
    534: "chinese",
    535: "byzantines",
    536: "persians",
    537: "saracens",
    538: "turks",
    539: "vikings",
    540: "mongols",
    541: "celts",
    542: "spanish",
    543: "aztecs",
    544: "mayans",
    545: "huns",
    546: "koreans",
    547: "italians",
    548: "indians",
    549: "incas",
    550: "magyars",
    551: "slavs",
    555: "enable_sheep",
    556: "enable_llamas",
    557: "enable_cows",
    558: "enable_turkeys",
    563: "elite_organ_gun",
    565: "elite_camel_archer",
    567: "elite_gbeto",
    569: "elite_shotel_warrior",
    572: "carrack",
    573: "arquebus",
    574: "royal_heirs",
    575: "torsion_engines",
    576: "tigui",
    577: "farimba",
    578: "kasbah",
    579: "maghrabi_camels",
    580: "portuguese",
    581: "ethiopians",
    582: "malians",
    583: "berbers",
    597: "elite_caravel",
    599: "elite_genitour",
    600: "free_cartography",
    602: "arson",
    608: "arrowslits",
    615: "elite_ballista_elephant",
    617: "elite_karambit_warrior",
    619: "elite_arambai",
    621: "elite_rattan_archer",
    622: "tusk_swords",
    623: "double_crossbow",
    624: "thalassocracy",
    625: "forced_levy",
    626: "howdah",
    627: "manipur_cavalry",
    628: "chatras",
    629: "paper_money",
    631: "elite_battle_elephant",
    639: "town_center_spawn",
    650: "khmer",
    651: "malay",
    652: "burmese",
    653: "vietnamese",
    655: "imperial_skirmisher",
    658: "set_maximum_population_no_houses",
    665: "vietnamese_vision",
    673: "bulgarians",
    674: "tatars",
    675: "cumans",
    676: "lithuanians",
    678: "elite_konnik",
    680: "elite_keshik",
    682: "elite_kipchak",
    684: "elite_leitis",
    685: "stirrups",
    686: "bagains",
    687: "silk_armor",
    688: "timurid_siegecraft",
    689: "steppe_husbandry",
    690: "cuman_mercenaries",
    691: "hill_forts",
    692: "tower_shields",
    715: "elite_steppe_lancer",
    716: "supplies",
})
