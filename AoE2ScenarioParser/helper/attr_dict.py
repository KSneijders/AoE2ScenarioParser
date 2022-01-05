class AttrDict(dict):
    def __init__(self, *args):
        dict.__init__(self, args)

    def __getattribute__(self, item):
        try:
            return self[item]
        except (AttributeError, KeyError):
            return dict.__getattribute__(self, item)

    def __setattr__(self, key, value):
        self[key] = value
