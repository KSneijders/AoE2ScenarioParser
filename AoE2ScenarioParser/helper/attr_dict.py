import typing

_KT = typing.TypeVar("_KT")  # Key type
_VT = typing.TypeVar("_VT")  # Value type


class AttrDict(dict, typing.Mapping[_KT, _VT]):
    def __init__(self, *args):
        dict.__init__(self, args)

    def __getattribute__(self, item):
        try:
            return self[item]
        except (AttributeError, KeyError):
            try:
                return dict.__getattribute__(self, item)
            except AttributeError:
                return None

    def __setattr__(self, key, value):
        self[key] = value
