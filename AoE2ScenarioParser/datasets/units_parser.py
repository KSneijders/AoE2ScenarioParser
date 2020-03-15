import json

units = [
    0, 1, 4, 5, 6, 7, 8, 11, 13, 15, 17, 21, 24, 25, 36, 38, 39, 40, 41, 42, 46, 52, 56, 73, 74, 75, 77, 83, 93, 118,
    120, 122, 123, 124, 125, 128, 156, 185, 188, 204, 207, 232, 239, 250, 259, 275, 279, 280, 281, 282, 283, 286, 291,
    293, 299, 305, 329, 330, 331, 358, 359, 361, 420, 422, 434, 440, 441, 442, 448, 473, 474, 492, 493, 527, 528, 529,
    530, 531, 532, 533, 534, 539, 542, 545, 546, 548, 550, 553, 554, 555, 556, 557, 558, 559, 560, 561, 567, 569, 579,
    588, 592, 594, 639, 691, 692, 694, 705, 725, 726, 748, 751, 752, 753, 755, 757, 763, 765, 771, 773, 775, 778, 814,
    825, 827, 829, 831, 832, 833, 846, 850, 854, 860, 866, 868, 869, 871, 873, 875, 876, 878, 879, 881, 882, 892, 894,
    897, 1001, 1003, 1004, 1006, 1007, 1009, 1010, 1012, 1013, 1015, 1016, 1018, 1023, 1060, 1103, 1104, 1105, 1120,
    1122, 1123, 1125, 1126, 1128, 1129, 1131, 1132, 1134, 1142, 1145, 1155, 1222, 1225, 1227, 1228, 1230, 1231, 1233,
    1234, 1236, 1237, 1243, 1245, 1252, 1253, 1258, 1263, 1271, 1273, 1275, 1291, 1292, 1300, 1302, 1304, 1338, 1356,
    1370, 1372, 1374, 1377, 1400, 1570, 1572, 1577, 1596, 1598, 1600, 1602, 1604, 1606,
]
buildings = [
    1622, 251, 231, 899, 87, 1196, 1197, 1198, 1199, 1200, 12, 103, 236, 607, 740, 739, 738, 606, 605, 610,
    743, 742, 741, 609, 608, 1206, 1212, 1211, 1210, 1205, 1204, 1209, 1215, 1214, 1213, 1208, 1207, 1552,
    1558, 1557, 1556, 1551, 1550, 1555, 1561, 1560, 1559, 1554, 1553, 82, 599, 1396, 1579, 1583, 1587, 1591, 370,
    263, 45, 1369, 50, 1021, 1062, 190, 199, 119, 1102, 155, 33, 88, 659, 64, 667, 1217, 234, 1189, 70, 1082,
    1083, 1084, 1085, 1086, 1087, 1088, 235, 1251, 562, 84, 68, 584, 104, 826, 598, 793, 797, 789, 801, 72,
    689, 872, 1187, 1378, 1216, 1367, 1391, 1383, 1391, 1383, 1379, 1387, 1379, 1387, 1391, 1379, 1387, 785,
    788, 1264, 49, 101, 117, 1081, 637, 1097, 1098, 1099, 1100, 1101, 1368, 109, 444, 110, 209, 79, 276, 1311,
    1310, 1309, 1314, 1313, 1312, 712, 713, 714, 715, 716, 717, 718, 719
]

units_name_correction = {
    0: "Moveable Map Revealer",  # Test String
    185: "Slinger",  # Crossbowman
    207: "Imperial Camel Rider",  # Heavy Camel Rider
    639: "Penguin",  # Champion
    1300: "Alfred the Alpaca",  # Champion
    869: "Magyar Huszar",  # Cataphract
    871: "Elite Magyar Huszar",  # Cataphract
    52: "Royal Janissary",  # Elite Janissary
    293: "Villager (Female)",  # Villager (Male)
    204: "Trade Cart (Full)",  # Trade Cart (empty)
    1338: "Cart",  # Trade Cart (empty)
    1400: "Priest with Relic",  # Monk with Relic
    879: "Kamayuk",  # Samurai
    882: "Condottiero",  # Samurai
    305: "Llama",  # Sheep
    705: "Cow A",  # Sheep
    1596: "Cow B",  # Sheep
    1598: "Cow C",  # Sheep
    1600: "Cow D",  # Sheep
    881: "Elite Kamayuk",  # Elite Samurai
    814: "Horse A",  # Horse
    897: "Camel",  # Horse
    1237: "Bactrian Camel",  # Horse
    1356: "Horse B",  # Cow D
    1602: "Horse C",  # Horse
    1604: "Horse D",  # Horse
    1606: "Horse E",  # Horse
    873: "Elephant Archer",  # War Wagon
    875: "Elite Elephant Archer",  # War Wagon
    866: "Genoese Crossbowman",  # Elite War Wagon
    868: "Elite Genoese Crossbowman",  # Elite War Wagon
    1377: "Torch B (Convertable)",  # Torch A (Convertable)
    876: "Boyar",  # Paladin
    878: "Elite Boyar",  # Paladin
    1252: "Konnik (Dismounted)",  # Konnik
    1253: "Elite Konnik (Dismounted)",  # Elite Konnik
    1291: "Invisible Object",  # Test String
    753: "Eagle Warrior"  # <Empty String>
}
buildings_name_correction = {
    1622: "Aachen Cathedral",
    899: "Arch of Constantine",
    1369: "Dormition Cathedral",
    1378: "Rock Church",
    1367: "Sankore Madrasah",
    1368: "Tower of London",
    251: "Amphitheatre",
    872: "Quimper Cathedral",
    231: "Aqueduct",
    370: "City Wall",
    1196: "Army Tent A",
    1197: "Army Tent B",
    1198: "Army Tent C",
    1199: "Army Tent D",
    1200: "Army Tent E",
    1311: "Wooden Bridge A--Bottom",
    1310: "Wooden Bridge A--Middle",
    1309: "Wooden Bridge A--Top",
    1314: "Wooden Bridge B--Bottom",
    1313: "Wooden Bridge B--Middle",
    1312: "Wooden Bridge B--Top",
    1552: "Bridge E--Bottom",
    1558: "Bridge E--Broken Bottom",
    1557: "Bridge E--Broken Top",
    1556: "Bridge E--Cracked",
    1551: "Bridge E--Middle",
    1550: "Bridge E--Top",
    1555: "Bridge F--Bottom",
    1561: "Bridge F--Broken Bottom",
    1560: "Bridge F--Broken Top",
    1559: "Bridge F--Cracked",
    1554: "Bridge F--Middle",
    1553: "Bridge F--Top",
    33: "Fortress",
    263: "Colosseum",
    637: "Temple of Heaven",
    1396: "Chain",
    793: "Palisade Gate (down)",
    797: "Palisade Gate (horizontal)",
    789: "Palisade Gate (up)",
    801: "Palisade Gate (vertical)",
    1391: "Sea Gate",
    1383: "Sea Gate",
    1379: "Sea Gate",
    1387: "Sea Gate",
    1579: "City Gate1",
    1583: "City Gate2",
    1587: "City Gate3",
    1591: "City Gate4",
    1187: "Rice Farm",
    88: "Gate Down",
    659: "Gate Horizontal",
    64: "Gate Up",
    667: "Gate Vertical",
    1082: "Hut A",
    1097: "Tent A",
    1098: "Tent B",
    1099: "Tent C",
    1100: "Tent D",
    1101: "Tent E",
    1083: "Hut B",
    1084: "Hut C",
    1085: "Hut D",
    1086: "Hut E",
    1087: "Hut F",
    1088: "Hut G",
}

with open('units_buildings_techs.json', 'r') as f:
    d = json.load(f)
    result = {}
    # for obj_id in units:
    for obj_id in buildings:
        obj = d['units_buildings'][str(obj_id)]

        obj_class = obj['class']
        obj_hp = obj['hit_points']
        obj_los = obj['line_of_sight']
        if obj_id in buildings_name_correction.keys():
            localized_name = buildings_name_correction[obj_id]
        else:
            localized_name = obj['localised_name']

        localized_name = localized_name.lower() \
            .replace(' ', '_') \
            .replace('.', '_') \
            .replace('-', '_') \
            .replace(',', '_') \
            .replace('(', '') \
            .replace(')', '')
        localized_name = localized_name.replace('__', '_')

        try:
            result[localized_name].append(obj_id)
        except KeyError:
            result[localized_name] = [obj_id]

for key, value in result.items():
    if len(value) > 1:
        print(key, "=", value)
    else:
        # pass
        print(key, "=", value[0])
