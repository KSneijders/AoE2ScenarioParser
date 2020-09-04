from typing import List, Type
from AoE2ScenarioParser.helper.retriever import RetrieverObjectLink


class AoE2Object:
    _link_list: List = []

    def __init__(self, ):
        self.instance_number = -1
        self._pieces = {}

    @property
    def _instance_number(self):
        return self._hidden_instance_number

    @_instance_number.setter
    def _instance_number(self, value):
        if self._pieces == {}:
            raise ValueError("Cannot set instance_number reference without pieces.")
        self._hidden_instance_number = value

    @classmethod
    def _construct(cls, pieces, instance_number: int):
        obj = cls()
        obj._pieces = pieces
        obj._instance_number = instance_number

        for link in obj._link_list:
            value = eval(link.link, {}, {'pieces': obj._pieces, '__index__': obj._instance_number})

            if link.process_as_object is not None:
                value_list = []
                for index, struct in enumerate(value):
                    value_list.append(link.process_as_object(obj._pieces, instance_number=index))
                value = value_list

            obj.__setattr__(link.name, value)
        return obj

    # TODO: RECREATE CREATION !!!EVERYWHERE!!! to use _construct() instead of constructor!
    # TODO: ADD EXCEPTION FOR OBJECT WITHOUT PIECE. REDO WITH PIECE AFTER/ALWAYS COMMIT WITH PIECE REFERENCE?

    def commit(self, local_link_list: Type[List[RetrieverObjectLink]] = None):
        """
        Commits all changes to the piece & struct structure of the object it's called upon.

        Args:
            local_link_list: a separate list of RetrieverObjectLinks. This way it's possible to commit only specific
            properties instead of all from an object.
        """
        if self._pieces == {}:
            raise ValueError("Unable to commit object. No reference to pieces set.")

        if local_link_list is None:
            local_link_list = self._link_list

        for link in local_link_list:
            if link.process_as_object is not None:
                object_list: List[AoE2Object] = self.__getattribute__(link.name)
                link_piece = link.get_piece_datatype(self._pieces)

                exec(f"{link.link} = [link_piece() for x in range(r)]", locals(), {
                    'pieces': self._pieces,
                    'link_piece': link_piece,
                    'r': len(object_list)
                })

                for index, obj in enumerate(object_list):
                    obj._pieces = self._pieces
                    obj._instance_number = index
                    obj.commit()

            else:
                exec(link.link + " = value", {}, {
                    'pieces': self._pieces,
                    'value': self.__getattribute__(link.name),
                    '__index__': self._instance_number
                })

    @staticmethod
    def get_instance_number(obj: AoE2Object = None, instance_number_history=None) -> int:
        if obj is None and instance_number_history is None:
            raise ValueError("The use of the parameter 'obj' or 'instance_number_history' is required.")
        if obj is not None and instance_number_history is not None:
            raise ValueError("Cannot use both the parameter 'obj' and 'instance_number_history'.")

        if instance_number_history is None:
            instance_number_history = []

        if obj is None:
            return instance_number_history[-1] if len(instance_number_history) > 0 else -1
        else:
            return obj._instance_number_history[-1] if len(obj._instance_number_history) > 0 else -1

    def __repr__(self):
        return str(self.__class__.__name__) + ": " + str(self.__dict__)
