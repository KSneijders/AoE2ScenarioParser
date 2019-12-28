class AoE2Object:
    def __init__(self, data_dict):
        del data_dict['self']
        del data_dict['__class__']

        print(data_dict)

        self.data_dict = data_dict

    def _to_string(self):
        return str(self.data_dict)

    def __str__(self):
        return self._to_string()
