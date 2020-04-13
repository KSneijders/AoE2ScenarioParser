import abc


class AoE2Object:
    def __init__(self):
        pass

    @staticmethod
    @abc.abstractmethod
    def _parse_object(parsed_data, **kwargs):
        pass

    @staticmethod
    @abc.abstractmethod
    def _reconstruct_object(parsed_data, objects, **kwargs):
        pass

    def __str__(self):
        return str(self.__class__.__name__) + ": " + str(self.__dict__)
