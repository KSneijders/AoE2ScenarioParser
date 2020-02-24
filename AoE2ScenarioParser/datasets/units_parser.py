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

units_name_correction = {
    0: "Moveable Map Revealer",           # Test String
    185: "Slinger",                       # Crossbowman
    207: "Imperial Camel Rider",          # Heavy Camel Rider
    639: "Penguin",                       # Champion
    1300: "Alfred the Alpaca",            # Champion
    869: "Magyar Huszar",                 # Cataphract
    871: "Elite Magyar Huszar",           # Cataphract
    52: "Royal Janissary",                # Elite Janissary
    293: "Villager (Female)",             # Villager (Male)
    204: "Trade Cart (Full)",             # Trade Cart (empty)
    1338: "Cart",                         # Trade Cart (empty)
    1400: "Priest with Relic",            # Monk with Relic
    879: "Kamayuk",                       # Samurai
    882: "Condottiero",                   # Samurai
    305: "Llama",                         # Sheep
    705: "Cow A",                         # Sheep
    1596: "Cow B",                        # Sheep
    1598: "Cow C",                        # Sheep
    1600: "Cow D",                        # Sheep
    881: "Elite Kamayuk",                 # Elite Samurai
    814: "Horse A",                       # Horse
    897: "Camel",                         # Horse
    1237: "Bactrian Camel",               # Horse
    1356: "Horse B",                      # Cow D
    1602: "Horse C",                      # Horse
    1604: "Horse D",                      # Horse
    1606: "Horse E",                      # Horse
    873: "Elephant Archer",               # War Wagon
    875: "Elite Elephant Archer",         # War Wagon
    866: "Genoese Crossbowman",           # Elite War Wagon
    868: "Elite Genoese Crossbowman",     # Elite War Wagon
    1377: "Torch B (Convertable)",        # Torch A (Convertable)
    876: "Boyar",                         # Paladin
    878: "Elite Boyar",                   # Paladin
    1252: "Konnik (Dismounted)",          # Konnik
    1253: "Elite Konnik (Dismounted)",    # Elite Konnik
    1291: "Invisible Object",             # Test String
    753: "Eagle Warrior"                  # <Empty String>
}

with open('units_buildings_techs.json', 'r') as f:
    d = json.load(f)
    result = {}
    for obj_id in units:
        obj = d['units_buildings'][str(obj_id)]

        obj_class = obj['class']
        obj_hp = obj['hit_points']
        obj_los = obj['line_of_sight']
        if obj_id in units_name_correction.keys():
            localized_name = units_name_correction[obj_id]
        else:
            localized_name = obj['localised_name']

        localized_name = localized_name.lower().replace(' ', '_').replace('.', '_').replace('-', '_').replace(',', '_')\
            .replace('(', '').replace(')', '')

        # name_cannot_contain = ['rubble', 'bridge']
        #
        # if localized_name is not '' and \
        #         len([a for a in name_cannot_contain if a in localized_name]) == 0 and \
        #         obj_hp > 0 and \
        #         obj_los > 0 and \
        #         obj_class not in [-1, 11]:
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
