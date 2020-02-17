import json

units = [
    0, 1, 4, 5, 7, 8, 11, 13, 15, 17, 25, 36, 38, 39, 40, 41, 42, 46, 52, 73, 74, 83, 93, 125, 128, 185, 188, 204, 207,
    232, 239, 250, 275, 279, 280, 281, 282, 286, 291, 293, 299, 305, 329, 331, 361, 420, 434, 440, 448, 493, 531, 533,
    534, 539, 545, 553, 554, 555, 556, 557, 558, 559, 560, 561, 594, 639, 692, 694, 705, 725, 726, 748, 751, 755, 757,
    763, 765, 771, 773, 775, 778, 814, 825, 827, 829, 831, 832, 833, 846, 850, 854, 860, 866, 868, 869, 871, 873, 875,
    876, 878, 879, 881, 882, 892, 894, 897, 1001, 1003, 1004, 1006, 1007, 1009, 1010, 1012, 1013, 1015, 1016, 1018,
    1023, 1060, 1103, 1104, 1105, 1120, 1122, 1123, 1125, 1126, 1128, 1129, 1131, 1132, 1142, 1145, 1155, 1222, 1225,
    1227, 1228, 1230, 1231, 1233, 1234, 1236, 1237, 1243, 1245, 1252, 1253, 1258, 1263, 1271, 1273, 1275, 1291, 1292,
    1302, 1304, 1338, 1356, 1370, 1374, 1377, 1400, 1570, 1572, 1577, 1596, 1598, 1600, 1602, 1604, 1606
]

with open('units_buildings_techs.json', 'r') as f:
    d = json.load(f)
    result = {}
    # for building_id in d['units_buildings']:
    for building_id in units:
        building = d['units_buildings'][str(building_id)]

        object_hp = building['hit_points']
        object_class = building['class']
        object_los = building['line_of_sight']
        localized_name = building['name']

        localized_name = localized_name.lower()
        localized_name = localized_name.replace(' ', '_')
        localized_name = localized_name.replace('.', '_')
        localized_name = localized_name.replace('-', '_')
        localized_name = localized_name.replace(',', '_')

        # name_cannot_contain = ['rubble', 'bridge']
        #
        # if localized_name is not '' and \
        #         len([a for a in name_cannot_contain if a in localized_name]) == 0 and \
        #         object_hp > 0 and \
        #         object_los > 0 and \
        #         object_class not in [-1, 11]:
        try:
            result[localized_name].append(building_id)
        except KeyError:
            result[localized_name] = [building_id]

for key, value in result.items():
    if len(value) > 1:
        print(key, "=", value)
    else:
        print(key, "=", value[0])
