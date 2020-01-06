class AoE2Object:
    def __init__(self, data_dict):
        del data_dict['self']
        del data_dict['__class__']

        self.data_dict = data_dict

        if 'terrain_id' not in self.__str__() and 'id_on_map' not in self.__str__():
            print(data_dict)

    def _to_string(self):
        return str(self.data_dict)

    def __str__(self):
        return self._to_string()
