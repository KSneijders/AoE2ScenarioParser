from bidict import bidict

aachen_cathedral = 1622
amphitheatre = 251
aqueduct = 231
arch_of_constantine = 899
archery_range = 87
army_tent_a = 1196
army_tent_b = 1197
army_tent_c = 1198
army_tent_d = 1199
army_tent_e = 1200
barracks = 12
blacksmith = 103
bombard_tower = 236
bridge_a_bottom = 607
bridge_a_broken_bottom = 740
bridge_a_broken_top = 739
bridge_a_cracked = 738
bridge_a_middle = 606
bridge_a_top = 605
bridge_b_bottom = 610
bridge_b_broken_bottom = 743
bridge_b_broken_top = 742
bridge_b_cracked = 741
bridge_b_middle = 609
bridge_b_top = 608
bridge_c_bottom = 1206
bridge_c_broken_bottom = 1212
bridge_c_broken_top = 1211
bridge_c_cracked = 1210
bridge_c_middle = 1205
bridge_c_top = 1204
bridge_d_bottom = 1209
bridge_d_broken_bottom = 1215
bridge_d_broken_top = 1214
bridge_d_cracked = 1213
bridge_d_middle = 1208
bridge_d_top = 1207
bridge_e_bottom = 1552
bridge_e_broken_bottom = 1558
bridge_e_broken_top = 1557
bridge_e_cracked = 1556
bridge_e_middle = 1551
bridge_e_top = 1550
bridge_f_bottom = 1555
bridge_f_broken_bottom = 1561
bridge_f_broken_top = 1560
bridge_f_cracked = 1559
bridge_f_middle = 1554
bridge_f_top = 1553
castle = 82
cathedral = 599
chain = 1396
city_gate1 = 1579
"""Please note: The game does not handle this building properly at this point"""
city_gate2 = 1583
"""Please note: The game does not handle this building properly at this point"""
city_gate3 = 1587
"""Please note: The game does not handle this building properly at this point"""
city_gate4 = 1591
"""Please note: The game does not handle this building properly at this point"""
city_wall = 370
colosseum = 263
dock = 45
dormition_cathedral = 1369
farm = 50
feitoria = 1021
fence = 1062
fire_tower = 190
fish_trap = 199
fortified_palisade_wall = 119
fortified_tower = 1102
fortified_wall = 155
fortress = 33
gate_down = 88
gate_horizontal = 659
gate_up = 64
gate_vertical = 667
gol_gumbaz = 1217
guard_tower = 234
harbor = 1189
house = 70
hut_a = 1082
hut_b = 1083
hut_c = 1084
hut_d = 1085
hut_e = 1086
hut_f = 1087
hut_g = 1088
keep = 235
krepost = 1251
lumber_camp = 562
market = 84
mill = 68
mining_camp = 584
monastery = 104
monument = 826
outpost = 598
palisade_gate_down = 793
palisade_gate_horizontal = 797
palisade_gate_up = 789
palisade_gate_vertical = 801
palisade_wall = 72
pyramid = 689
quimper_cathedral = 872
rice_farm = 1187
rock_church = 1378
sanchi_stupa = 1216
sankore_madrasah = 1367
sea_gate1 = 1391
"""Please note: The game does not handle this building properly at this point"""
sea_gate2 = 1383
"""Please note: The game does not handle this building properly at this point"""
sea_gate3 = 1379
"""Please note: The game does not handle this building properly at this point"""
sea_gate4 = 1387
"""Please note: The game does not handle this building properly at this point"""
sea_tower = 785
sea_wall = 788
shrine = 1264
siege_workshop = 49
stable = 101
stone_wall = 117
storage = 1081
temple_of_heaven = 637
tent_a = 1097
tent_b = 1098
tent_c = 1099
tent_d = 1100
tent_e = 1101
tower_of_london = 1368
town_center = 109
khosrau = 444
trade_workshop = 110
university = 209
watch_tower = 79
wonder = 276
wooden_bridge_a_bottom = 1311
wooden_bridge_a_middle = 1310
wooden_bridge_a_top = 1309
wooden_bridge_b_bottom = 1314
wooden_bridge_b_middle = 1313
wooden_bridge_b_top = 1312
yurt_a = 712
yurt_b = 713
yurt_c = 714
yurt_d = 715
yurt_e = 716
yurt_f = 717
yurt_g = 718
yurt_h = 719

building_names = bidict({
    12: "barracks",
    33: "fortress",
    45: "dock",
    49: "siege_workshop",
    50: "farm",
    64: "gate_up",
    68: "mill",
    70: "house",
    72: "palisade_wall",
    79: "watch_tower",
    82: "castle",
    84: "market",
    87: "archery_range",
    88: "gate_down",
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
    659: "gate_horizontal",
    667: "gate_vertical",
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
    789: "palisade_gate_up",
    793: "palisade_gate_down",
    797: "palisade_gate_horizontal",
    801: "palisade_gate_vertical",
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
    1379: "sea_gate3",
    1383: "sea_gate2",
    1387: "sea_gate4",
    1391: "sea_gate1",
    1396: "chain",
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
    1579: "city_gate1",
    1583: "city_gate2",
    1587: "city_gate3",
    1591: "city_gate4",
    1622: "aachen_cathedral",
})
