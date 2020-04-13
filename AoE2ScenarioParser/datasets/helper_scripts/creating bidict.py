# from bidict import bidict
#
# from AoE2ScenarioParser.datasets import buildings
#
#
# def get_unit_id_by_string(tech):
#     try:
#         return eval(tech)
#     except NameError:
#         return None
#
#
# units_dict = bidict()
# for x in buildings.__dict__.keys():
#     if '__' not in x and x != 'get_building_id_by_string':
#         units_dict.put(x, buildings.get_building_id_by_string(x))
#
# print("building_names = bidict({")
# for key, value in units_dict.inverse.items():
#     print(" " * 4 + str(key) + ": \"" + str(value) + "\",")
# print("})")
