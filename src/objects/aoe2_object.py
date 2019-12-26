import abc


class AoE2Object:
    def __init__(self):
        self.data_dict = {}

    @abc.abstractmethod
    def set_from_pieces(self, *args):
        """Method documentation"""
        return

    def _to_string(self):
        return str(self.data_dict)

    def __repr__(self):
        return self._to_string()

    def __str__(self):
        return self._to_string()
