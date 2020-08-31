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
    def _reconstruct_object(parsed_header, parsed_data, objects, **kwargs):
        pass

    def __repr__(self):
        return str(self.__class__.__name__) + ": " + str(self.__dict__)


class CommittingUnbasedObjectError(Exception):
    """Raised when committing an object using `.commit()` that is not based on a piece or struct."""


class RemovedFlagRaisedError(Exception):
    """Raised when committing an object using `.commit()` but the object's removed flag has been set to True."""
