class Retriever:
    def __init__(self, name, datatype, on_success=None, save_as=None, set_repeat=None):
        self.name = name
        self.datatype = datatype
        self.on_success = on_success
        self.save_as = save_as
        self.set_repeat = set_repeat

    def _to_string(self):
        return "[Retriever] " + self.name + ": " + str(self.datatype)

    def __str__(self):
        return self._to_string()

    def __repr__(self):
        return self._to_string()


def find_retriever(retriever_list, name):
    for x in retriever_list:
        if x.name == name:
            return x
