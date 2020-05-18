import json

units_ids = [
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
gaia_units_ids = [
    486, 1608, 1610, 1609, 1031, 65, 89, 1301, 1056, 96, 76, 1239, 810, 812, 822, 1135, 1029,
    816, 1026, 202, 1139, 303, 1241, 1028, 862, 1137, 1305, 1247, 48, 884, 835, 126, 1019
]
buildings_ids = [
    1622, 251, 231, 899, 87, 1196, 1197, 1198, 1199, 1200, 12, 103, 236, 607, 740, 739, 738, 606, 605, 610,
    743, 742, 741, 609, 608, 1206, 1212, 1211, 1210, 1205, 1204, 1209, 1215, 1214, 1213, 1208, 1207, 1552,
    1558, 1557, 1556, 1551, 1550, 1555, 1561, 1560, 1559, 1554, 1553, 82, 599, 1396, 1579, 1583, 1587, 1591, 370,
    263, 45, 1369, 50, 1021, 1062, 190, 199, 119, 1102, 155, 33, 88, 659, 64, 667, 1217, 234, 1189, 70, 1082,
    1083, 1084, 1085, 1086, 1087, 1088, 235, 1251, 562, 84, 68, 584, 104, 826, 598, 793, 797, 789, 801, 72,
    689, 872, 1187, 1378, 1216, 1367, 1391, 1383, 1391, 1383, 1379, 1387, 1379, 1387, 1391, 1379, 1387, 785,
    788, 1264, 49, 101, 117, 1081, 637, 1097, 1098, 1099, 1100, 1101, 1368, 109, 444, 110, 209, 79, 276, 1311,
    1310, 1309, 1314, 1313, 1312, 712, 713, 714, 715, 716, 717, 718, 719
]
techs_ids = [
    16, 516, 237, 51, 573, 608, 602, 10, 21, 460, 319, 543, 686, 93, 17, 83, 583, 49, 75, 230, 435, 200, 188, 64, 203,
    201, 529, 673, 652, 535, 37, 96, 48, 374, 572, 19, 102, 209, 541, 82, 76, 264, 628, 47, 534, 493, 23, 315, 514, 517,
    11, 12, 100, 396, 690, 675, 104, 623, 287, 202, 6, 513, 375, 384, 4, 619, 615, 631, 398, 504, 565, 376, 597, 361,
    362, 60, 434, 481, 567, 599, 468, 365, 432, 369, 509, 617, 680, 682, 463, 678, 684, 372, 360, 472, 368, 371, 563,
    27, 621, 366, 569, 98, 715, 2, 364, 363, 448, 367, 450, 370, 557, 556, 555, 558, 581, 45, 577, 246, 252, 101, 527,
    199, 625, 67, 194, 530, 600, 5, 35, 24, 65, 55, 182, 531, 462, 464, 140, 15, 429, 85, 249, 380, 236, 218, 244, 13,
    239, 441, 439, 394, 691, 379, 14, 626, 545, 526, 39, 428, 233, 103, 521, 655, 549, 548, 492, 68, 489, 547, 533, 488,
    578, 59, 63, 650, 546, 212, 254, 676, 61, 207, 22, 490, 579, 550, 7, 651, 582, 222, 627, 483, 50, 544, 540, 322,
    487, 485, 257, 512, 211, 265, 486, 629, 436, 494, 457, 536, 197, 80, 77, 580, 515, 316, 525, 219, 52, 574, 231, 321,
    537, 81, 74, 94, 658, 507, 445, 373, 377, 320, 255, 687, 499, 491, 551, 542, 408, 215, 689, 685, 278, 279, 482, 506,
    716, 440, 674, 532, 624, 438, 437, 576, 688, 575, 692, 639, 280, 8, 90, 54, 538, 622, 217, 221, 653, 665, 539, 34,
    461, 213, 484, 3, 9
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
gaia_units_name_correction = {
    1056: "Falcon",
    1028: "Stork",
    1247: "Wild Bactrian Camel",
    884: "Wild Camel",
    835: "Wild Horse",
    1305: "Vulture",
    1301: "Elephant",
    1610: "BUTTERFL3",
    1609: "BUTTERFL2",
    1608: "BUTTERFL1",
    486: "BEAR",
}
buildings_name_correction = {
    1622: "Aachen Cathedral",  # Wonder
    899: "Arch of Constantine",  # Wonder
    1369: "Dormition Cathedral",  # Wonder
    1378: "Rock Church",  # Wonder
    1367: "Sankore Madrasah",  # Wonder
    1368: "Tower of London",  # Wonder
    251: "Amphitheatre",  # Dome of the Rock
    872: "Quimper Cathedral",  # Dome of the Rock
    231: "Aqueduct",  # Buddha Statue A
    370: "City Wall",  # Buddha Statue A
    1196: "Army Tent A",  # Army Tent
    1197: "Army Tent B",  # Army Tent
    1198: "Army Tent C",  # Army Tent
    1199: "Army Tent D",  # Army Tent
    1200: "Army Tent E",  # Army Tent
    1311: "Wooden Bridge A--Bottom",  # Bridge A--Bottom
    1310: "Wooden Bridge A--Middle",  # Bridge A--Middle
    1309: "Wooden Bridge A--Top",  # Bridge A--Top
    1314: "Wooden Bridge B--Bottom",  # Bridge B--Bottom
    1313: "Wooden Bridge B--Middle",  # Bridge B--Middle
    1312: "Wooden Bridge B--Top",  # Bridge B--Top
    1552: "Bridge E--Bottom",  # Bridge C--Bottom
    1558: "Bridge E--Broken Bottom",  # Bridge C--Broken Bottom
    1557: "Bridge E--Broken Top",  # Bridge C--Broken Top
    1556: "Bridge E--Cracked",  # Bridge C--Cracked
    1551: "Bridge E--Middle",  # Bridge C--Middle
    1550: "Bridge E--Top",  # Bridge C--Top
    1555: "Bridge F--Bottom",  # Bridge D--Bottom
    1561: "Bridge F--Broken Bottom",  # Bridge D--Broken Bottom
    1560: "Bridge F--Broken Top",  # Bridge D--Broken Top
    1559: "Bridge F--Cracked",  # Bridge D--Cracked
    1554: "Bridge F--Middle",  # Bridge D--Middle
    1553: "Bridge F--Top",  # Bridge D--Top
    33: "Fortress",  # Castle
    263: "Colosseum",  # Cathedral
    637: "Temple of Heaven",  # Cathedral
    1396: "Chain",  # Sea Gate
    793: "Palisade Gate (down)",  # Sea Gate
    797: "Palisade Gate (horizontal)",  # Sea Gate
    789: "Palisade Gate (up)",  # Sea Gate
    801: "Palisade Gate (vertical)",  # Sea Gate
    1391: "Sea Gate",  # Sea Gate
    1383: "Sea Gate",  # Sea Gate
    1379: "Sea Gate",  # Sea Gate
    1387: "Sea Gate",  # Sea Gate
    1579: "City Gate1",  # City Gate
    1583: "City Gate2",  # City Gate
    1587: "City Gate3",  # City Gate
    1591: "City Gate4",  # City Gate
    1187: "Rice Farm",  # Farm
    88: "Gate Down",  # Gate
    659: "Gate Horizontal",  # Gate
    64: "Gate Up",  # Gate
    667: "Gate Vertical",  # Gate
    1082: "Hut A",  #
    1097: "Tent A",  #
    1098: "Tent B",  #
    1099: "Tent C",  #
    1100: "Tent D",  #
    1101: "Tent E",  #
    1083: "Hut B",  # Hut
    1084: "Hut C",  # Hut
    1085: "Hut D",  # Hut
    1086: "Hut E",  # Hut
    1087: "Hut F",  # Hut
    1088: "Hut G",  # Hut
}
techs_name_correction = {
    557: "Enable Cows",
    556: "Enable llamas",
    555: "Enable sheep",
    558: "Enable turkeys",
    526: "Hunting Dogs",
    543: "Aztecs",
    583: "Berbers",
    529: "Britons",
    673: "Bulgarians",
    652: "Burmese",
    535: "Byzantines",
    541: "Celts",
    534: "Chinese",
    675: "Cumans",
    581: "Ethiopians",
    527: "Fire Tower",
    530: "Franks",
    600: "Free Cartography",
    531: "Goths",
    545: "Huns",
    549: "Incas",
    548: "Indians",
    547: "Italians",
    533: "Japanese",
    650: "Khmer",
    546: "Koreans",
    676: "Lithuanians",
    550: "Magyars",
    651: "Malay",
    582: "Malians",
    544: "Mayans",
    540: "Mongols",
    536: "Persians",
    580: "Portuguese",
    525: "Revetments",
    537: "Saracens",
    551: "Slavs",
    542: "Spanish",
    674: "Tatars",
    532: "Teutons",
    639: "Town Center Spawn",
    538: "Turks",
    653: "Vietnamese",
    665: "Vietnamese Vision",
    539: "Vikings",
    394: "Hill Forts 2",
    512: "Orthodoxy",
    513: "Druzhina",
    287: "Franks Free Farming 1",
    396: "Chinese 50 percent HP Demos"
}

units_buildings = True
with open('units_buildings_techs.json', 'r') as f:
    d = json.load(f)
    result = {}

    # for key, value in buildings_name_correction.items():
    #     a = d['units_buildings'][str(key)]
    #     print("\t" + str(key) + ": \"" + value + "\",  # " + str(a['localised_name']))
    # exit()

    # for obj_id in units_ids:
    # for obj_id in buildings_ids:
    # for obj_id in techs_ids:
    for obj_id in gaia_units_ids:
        obj = d['units_buildings' if units_buildings else 'techs'][str(obj_id)]

        if obj_id in gaia_units_name_correction.keys():
            localized_name = gaia_units_name_correction[obj_id]
        else:
            localized_name = obj['localised_name']

        localized_name = localized_name.lower() \
            .replace(' ', '_') \
            .replace('.', '_') \
            .replace('-', '_') \
            .replace(',', '_') \
            .replace('/', '_and_') \
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
