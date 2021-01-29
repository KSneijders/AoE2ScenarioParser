from enum import IntEnum

from bidict import bidict


class Building(IntEnum):
    AACHEN_CATHEDRAL = 1622
    AMPHITHEATRE = 251
    AQUEDUCT = 231
    ARCH_OF_CONSTANTINE = 899
    ARCHERY_RANGE = 87
    ARMY_TENT_A = 1196
    ARMY_TENT_B = 1197
    ARMY_TENT_C = 1198
    ARMY_TENT_D = 1199
    ARMY_TENT_E = 1200
    BARRACKS = 12
    BLACKSMITH = 103
    BOMBARD_TOWER = 236
    BRIDGE_A_BOTTOM = 607
    BRIDGE_A_BROKEN_BOTTOM = 740
    BRIDGE_A_BROKEN_TOP = 739
    BRIDGE_A_CRACKED = 738
    BRIDGE_A_MIDDLE = 606
    BRIDGE_A_TOP = 605
    BRIDGE_B_BOTTOM = 610
    BRIDGE_B_BROKEN_BOTTOM = 743
    BRIDGE_B_BROKEN_TOP = 742
    BRIDGE_B_CRACKED = 741
    BRIDGE_B_MIDDLE = 609
    BRIDGE_B_TOP = 608
    BRIDGE_C_BOTTOM = 1206
    BRIDGE_C_BROKEN_BOTTOM = 1212
    BRIDGE_C_BROKEN_TOP = 1211
    BRIDGE_C_CRACKED = 1210
    BRIDGE_C_MIDDLE = 1205
    BRIDGE_C_TOP = 1204
    BRIDGE_D_BOTTOM = 1209
    BRIDGE_D_BROKEN_BOTTOM = 1215
    BRIDGE_D_BROKEN_TOP = 1214
    BRIDGE_D_CRACKED = 1213
    BRIDGE_D_MIDDLE = 1208
    BRIDGE_D_TOP = 1207
    BRIDGE_E_BOTTOM = 1552
    BRIDGE_E_BROKEN_BOTTOM = 1558
    BRIDGE_E_BROKEN_TOP = 1557
    BRIDGE_E_CRACKED = 1556
    BRIDGE_E_MIDDLE = 1551
    BRIDGE_E_TOP = 1550
    BRIDGE_F_BOTTOM = 1555
    BRIDGE_F_BROKEN_BOTTOM = 1561
    BRIDGE_F_BROKEN_TOP = 1560
    BRIDGE_F_CRACKED = 1559
    BRIDGE_F_MIDDLE = 1554
    BRIDGE_F_TOP = 1553
    CASTLE = 82
    CATHEDRAL = 599
    CHAIN_WEST_TO_EAST = 1398
    CHAIN_SOUTHWEST_TO_NORTHEAST = 1396
    CHAIN_NORTH_TO_SOUTH = 1399
    CHAIN_NORTHWEST_TO_SOUTHEAST = 1397
    CITY_GATE_WEST_TO_EAST = 1587
    CITY_GATE_SOUTHWEST_TO_NORTHEAST = 1579
    CITY_GATE_NORTH_TO_SOUTH = 1591
    CITY_GATE_NORTHWEST_TO_SOUTHEAST = 1583
    CITY_WALL = 370
    COLOSSEUM = 263
    DOCK = 45
    DORMITION_CATHEDRAL = 1369
    FARM = 50
    FEITORIA = 1021
    FENCE = 1062
    FIRE_TOWER = 190
    FISH_TRAP = 199
    FORTIFIED_PALISADE_WALL = 119
    FORTIFIED_TOWER = 1102
    FORTIFIED_WALL = 155
    FORTRESS = 33
    GATE_NORTHWEST_TO_SOUTHEAST = 88
    GATE_WEST_TO_EAST = 659
    GATE_SOUTHWEST_TO_NORTHEAST = 64
    GATE_NORTH_TO_SOUTH = 667
    GOL_GUMBAZ = 1217
    GUARD_TOWER = 234
    HARBOR = 1189
    HOUSE = 70
    HUT_A = 1082
    HUT_B = 1083
    HUT_C = 1084
    HUT_D = 1085
    HUT_E = 1086
    HUT_F = 1087
    HUT_G = 1088
    KEEP = 235
    KREPOST = 1251
    LUMBER_CAMP = 562
    MARKET = 84
    MILL = 68
    MINING_CAMP = 584
    MONASTERY = 104
    MONUMENT = 826
    OUTPOST = 598
    PALISADE_GATE_SOUTHWEST_TO_NORTHEAST = 793
    PALISADE_GATE_WEST_TO_EAST = 797
    PALISADE_GATE_NORTHWEST_TO_SOUTHEAST = 789
    PALISADE_GATE_NORTH_TO_SOUTH = 801
    PALISADE_WALL = 72
    PYRAMID = 689
    QUIMPER_CATHEDRAL = 872
    RICE_FARM = 1187
    ROCK_CHURCH = 1378
    SANCHI_STUPA = 1216
    SANKORE_MADRASAH = 1367
    SEA_GATE_SOUTHWEST_TO_NORTHEAST = 1379
    SEA_GATE_NORTH_TO_SOUTH = 1391
    SEA_GATE_WEST_TO_EAST = 1387
    SEA_GATE_NORTHWEST_TO_SOUTHEAST = 1383
    SEA_TOWER = 785
    SEA_WALL = 788
    SHRINE = 1264
    SIEGE_WORKSHOP = 49
    STABLE = 101
    STONE_WALL = 117
    STORAGE = 1081
    TEMPLE_OF_HEAVEN = 637
    TENT_A = 1097
    TENT_B = 1098
    TENT_C = 1099
    TENT_D = 1100
    TENT_E = 1101
    TOWER_OF_LONDON = 1368
    TOWN_CENTER = 109
    KHOSRAU = 444
    TRADE_WORKSHOP = 110
    UNIVERSITY = 209
    WATCH_TOWER = 79
    WONDER = 276
    WOODEN_BRIDGE_A_BOTTOM = 1311
    WOODEN_BRIDGE_A_MIDDLE = 1310
    WOODEN_BRIDGE_A_TOP = 1309
    WOODEN_BRIDGE_B_BOTTOM = 1314
    WOODEN_BRIDGE_B_MIDDLE = 1313
    WOODEN_BRIDGE_B_TOP = 1312
    YURT_A = 712
    YURT_B = 713
    YURT_C = 714
    YURT_D = 715
    YURT_E = 716
    YURT_F = 717
    YURT_G = 718
    YURT_H = 719

    # Lords of the West - DLC Buildings
    DONJON = 1665


class GaiaBuilding(IntEnum):
    # Gaia Buildings
    RUINS = 345

    # Normal Buildings
    AACHEN_CATHEDRAL = 1622
    AMPHITHEATRE = 251
    AQUEDUCT = 231
    ARCH_OF_CONSTANTINE = 899
    ARCHERY_RANGE = 87
    ARMY_TENT_A = 1196
    ARMY_TENT_B = 1197
    ARMY_TENT_C = 1198
    ARMY_TENT_D = 1199
    ARMY_TENT_E = 1200
    BARRACKS = 12
    BLACKSMITH = 103
    BOMBARD_TOWER = 236
    BRIDGE_A_BOTTOM = 607
    BRIDGE_A_BROKEN_BOTTOM = 740
    BRIDGE_A_BROKEN_TOP = 739
    BRIDGE_A_CRACKED = 738
    BRIDGE_A_MIDDLE = 606
    BRIDGE_A_TOP = 605
    BRIDGE_B_BOTTOM = 610
    BRIDGE_B_BROKEN_BOTTOM = 743
    BRIDGE_B_BROKEN_TOP = 742
    BRIDGE_B_CRACKED = 741
    BRIDGE_B_MIDDLE = 609
    BRIDGE_B_TOP = 608
    BRIDGE_C_BOTTOM = 1206
    BRIDGE_C_BROKEN_BOTTOM = 1212
    BRIDGE_C_BROKEN_TOP = 1211
    BRIDGE_C_CRACKED = 1210
    BRIDGE_C_MIDDLE = 1205
    BRIDGE_C_TOP = 1204
    BRIDGE_D_BOTTOM = 1209
    BRIDGE_D_BROKEN_BOTTOM = 1215
    BRIDGE_D_BROKEN_TOP = 1214
    BRIDGE_D_CRACKED = 1213
    BRIDGE_D_MIDDLE = 1208
    BRIDGE_D_TOP = 1207
    BRIDGE_E_BOTTOM = 1552
    BRIDGE_E_BROKEN_BOTTOM = 1558
    BRIDGE_E_BROKEN_TOP = 1557
    BRIDGE_E_CRACKED = 1556
    BRIDGE_E_MIDDLE = 1551
    BRIDGE_E_TOP = 1550
    BRIDGE_F_BOTTOM = 1555
    BRIDGE_F_BROKEN_BOTTOM = 1561
    BRIDGE_F_BROKEN_TOP = 1560
    BRIDGE_F_CRACKED = 1559
    BRIDGE_F_MIDDLE = 1554
    BRIDGE_F_TOP = 1553
    CASTLE = 82
    CATHEDRAL = 599
    CHAIN_WEST_TO_EAST = 1398
    CHAIN_SOUTHWEST_TO_NORTHEAST = 1396
    CHAIN_NORTH_TO_SOUTH = 1399
    CHAIN_NORTHWEST_TO_SOUTHEAST = 1397
    CITY_GATE_WEST_TO_EAST = 1587
    CITY_GATE_SOUTHWEST_TO_NORTHEAST = 1579
    CITY_GATE_NORTH_TO_SOUTH = 1591
    CITY_GATE_NORTHWEST_TO_SOUTHEAST = 1583
    CITY_WALL = 370
    COLOSSEUM = 263
    DOCK = 45
    DORMITION_CATHEDRAL = 1369
    FARM = 50
    FEITORIA = 1021
    FENCE = 1062
    FIRE_TOWER = 190
    FISH_TRAP = 199
    FORTIFIED_PALISADE_WALL = 119
    FORTIFIED_TOWER = 1102
    FORTIFIED_WALL = 155
    FORTRESS = 33
    GATE_NORTHWEST_TO_SOUTHEAST = 88
    GATE_WEST_TO_EAST = 659
    GATE_SOUTHWEST_TO_NORTHEAST = 64
    GATE_NORTH_TO_SOUTH = 667
    GOL_GUMBAZ = 1217
    GUARD_TOWER = 234
    HARBOR = 1189
    HOUSE = 70
    HUT_A = 1082
    HUT_B = 1083
    HUT_C = 1084
    HUT_D = 1085
    HUT_E = 1086
    HUT_F = 1087
    HUT_G = 1088
    KEEP = 235
    KREPOST = 1251
    LUMBER_CAMP = 562
    MARKET = 84
    MILL = 68
    MINING_CAMP = 584
    MONASTERY = 104
    MONUMENT = 826
    OUTPOST = 598
    PALISADE_GATE_SOUTHWEST_TO_NORTHEAST = 793
    PALISADE_GATE_WEST_TO_EAST = 797
    PALISADE_GATE_NORTHWEST_TO_SOUTHEAST = 789
    PALISADE_GATE_NORTH_TO_SOUTH = 801
    PALISADE_WALL = 72
    PYRAMID = 689
    QUIMPER_CATHEDRAL = 872
    RICE_FARM = 1187
    ROCK_CHURCH = 1378
    SANCHI_STUPA = 1216
    SANKORE_MADRASAH = 1367
    SEA_GATE_SOUTHWEST_TO_NORTHEAST = 1379
    SEA_GATE_NORTH_TO_SOUTH = 1391
    SEA_GATE_WEST_TO_EAST = 1387
    SEA_GATE_NORTHWEST_TO_SOUTHEAST = 1383
    SEA_TOWER = 785
    SEA_WALL = 788
    SHRINE = 1264
    SIEGE_WORKSHOP = 49
    STABLE = 101
    STONE_WALL = 117
    STORAGE = 1081
    TEMPLE_OF_HEAVEN = 637
    TENT_A = 1097
    TENT_B = 1098
    TENT_C = 1099
    TENT_D = 1100
    TENT_E = 1101
    TOWER_OF_LONDON = 1368
    TOWN_CENTER = 109
    KHOSRAU = 444
    TRADE_WORKSHOP = 110
    UNIVERSITY = 209
    WATCH_TOWER = 79
    WONDER = 276
    WOODEN_BRIDGE_A_BOTTOM = 1311
    WOODEN_BRIDGE_A_MIDDLE = 1310
    WOODEN_BRIDGE_A_TOP = 1309
    WOODEN_BRIDGE_B_BOTTOM = 1314
    WOODEN_BRIDGE_B_MIDDLE = 1313
    WOODEN_BRIDGE_B_TOP = 1312
    YURT_A = 712
    YURT_B = 713
    YURT_C = 714
    YURT_D = 715
    YURT_E = 716
    YURT_F = 717
    YURT_G = 718
    YURT_H = 719

    # Lords of the West - DLC Buildings
    DONJON = 1665


building_names = bidict({
    12: "barracks",
    33: "fortress",
    45: "dock",
    49: "siege_workshop",
    50: "farm",
    64: "gate_southwest_to_northeast",
    68: "mill",
    70: "house",
    72: "palisade_wall",
    79: "watch_tower",
    82: "castle",
    84: "market",
    87: "archery_range",
    88: "gate_northwest_to_southeast",
    101: "stable",
    103: "blacksmith",
    104: "monastery",
    109: "town_center",
    110: "trade_workshop",
    117: "stone_wall",
    119: "fortified_palisade_wall",
    155: "fortified_wall",
    190: "fire_tower",
    199: "fish_trap",
    209: "university",
    231: "aqueduct",
    234: "guard_tower",
    235: "keep",
    236: "bombard_tower",
    251: "amphitheatre",
    263: "colosseum",
    276: "wonder",
    370: "city_wall",
    444: "khosrau",
    562: "lumber_camp",
    584: "mining_camp",
    598: "outpost",
    599: "cathedral",
    605: "bridge_a_top",
    606: "bridge_a_middle",
    607: "bridge_a_bottom",
    608: "bridge_b_top",
    609: "bridge_b_middle",
    610: "bridge_b_bottom",
    637: "temple_of_heaven",
    659: "gate_west_to_east",
    667: "gate_north_to_south",
    689: "pyramid",
    712: "yurt_a",
    713: "yurt_b",
    714: "yurt_c",
    715: "yurt_d",
    716: "yurt_e",
    717: "yurt_f",
    718: "yurt_g",
    719: "yurt_h",
    738: "bridge_a_cracked",
    739: "bridge_a_broken_top",
    740: "bridge_a_broken_bottom",
    741: "bridge_b_cracked",
    742: "bridge_b_broken_top",
    743: "bridge_b_broken_bottom",
    785: "sea_tower",
    788: "sea_wall",
    793: "palisade_gate_southwest_to_northeast",
    797: "palisade_gate_west_to_east",
    789: "palisade_gate_northwest_to_southeast",
    801: "palisade_gate_north_to_south",
    826: "monument",
    872: "quimper_cathedral",
    899: "arch_of_constantine",
    1021: "feitoria",
    1062: "fence",
    1081: "storage",
    1082: "hut_a",
    1083: "hut_b",
    1084: "hut_c",
    1085: "hut_d",
    1086: "hut_e",
    1087: "hut_f",
    1088: "hut_g",
    1097: "tent_a",
    1098: "tent_b",
    1099: "tent_c",
    1100: "tent_d",
    1101: "tent_e",
    1102: "fortified_tower",
    1187: "rice_farm",
    1189: "harbor",
    1196: "army_tent_a",
    1197: "army_tent_b",
    1198: "army_tent_c",
    1199: "army_tent_d",
    1200: "army_tent_e",
    1204: "bridge_c_top",
    1205: "bridge_c_middle",
    1206: "bridge_c_bottom",
    1207: "bridge_d_top",
    1208: "bridge_d_middle",
    1209: "bridge_d_bottom",
    1210: "bridge_c_cracked",
    1211: "bridge_c_broken_top",
    1212: "bridge_c_broken_bottom",
    1213: "bridge_d_cracked",
    1214: "bridge_d_broken_top",
    1215: "bridge_d_broken_bottom",
    1216: "sanchi_stupa",
    1217: "gol_gumbaz",
    1251: "krepost",
    1264: "shrine",
    1309: "wooden_bridge_a_top",
    1310: "wooden_bridge_a_middle",
    1311: "wooden_bridge_a_bottom",
    1312: "wooden_bridge_b_top",
    1313: "wooden_bridge_b_middle",
    1314: "wooden_bridge_b_bottom",
    1367: "sankore_madrasah",
    1368: "tower_of_london",
    1369: "dormition_cathedral",
    1378: "rock_church",
    1379: "sea_gate_southwest_to_northeast",
    1391: "sea_gate_north_to_south",
    1387: "sea_gate_west_to_east",
    1383: "sea_gate_northwest_to_southeast",
    1396: "chain_southwest_to_northeast",
    1397: "chain_northwest_to_southeast",
    1398: "chain_west_to_east",
    1399: "chain_north_to_south",
    1550: "bridge_e_top",
    1551: "bridge_e_middle",
    1552: "bridge_e_bottom",
    1553: "bridge_f_top",
    1554: "bridge_f_middle",
    1555: "bridge_f_bottom",
    1556: "bridge_e_cracked",
    1557: "bridge_e_broken_top",
    1558: "bridge_e_broken_bottom",
    1559: "bridge_f_cracked",
    1560: "bridge_f_broken_top",
    1561: "bridge_f_broken_bottom",
    1579: "city_gate_southwest_to_northeast",
    1583: "city_gate_northwest_to_southeast",
    1587: "city_gate_west_to_east",
    1591: "city_gate_north_to_south",
    1622: "aachen_cathedral",

    # Gaia Buildings
    345: "ruins",

    # Lords of the West - DLC Buildings
    1665: "donjon"
})
