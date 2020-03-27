import abc


class AoE2Object:
    def __init__(self, data_dict):
        del data_dict['self']
        del data_dict['__class__']

        self.data_dict = data_dict

        # Block terrain, units and effects from logging (respectively)
        # if 'terrain_id' not in self.__str__() and \
        #         'id_on_map' not in self.__str__() and \
        #         'Effect type' not in self.__str__():
        #     print(data_dict)

    @staticmethod
    @abc.abstractmethod
    def _parse_object(parsed_data, **kwargs):
        pass

    @staticmethod
    @abc.abstractmethod
    def _reconstruct_object(parsed_data, objects, **kwargs):
        pass

    def __str__(self):
        return str(self.data_dict)
