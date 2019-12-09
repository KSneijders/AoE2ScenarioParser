class Retriever:
    def __init__(self, name, datatype, save_as=None, set_repeat=None):
        self.name = name
        self.datatype = datatype
        self.save_as = save_as
        self.set_repeat = set_repeat

    def _to_string(self):
        return "[Retriever] " + str(self.datatype)

    def __str__(self):
        return self._to_string()

    def __repr__(self):
        return self._to_string()
