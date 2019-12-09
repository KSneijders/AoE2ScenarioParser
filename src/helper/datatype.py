class DataType:
    var = ""
    repeat = -1

    def __init__(self, var, repeat=1):
        self.var = var
        self.repeat = repeat

    def to_simple_string(self):
        return str(self.repeat) + " * " + self.var

    def _to_string(self):
        return "[DataType] " + self.to_simple_string()

    def __str__(self):
        return self._to_string()

    def __repr__(self):
        return self._to_string()
