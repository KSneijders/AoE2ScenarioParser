from src.helper.datatype import DataType


class Retriever:
    """ A Class for defining how to retrieve data.
    The Constructor has quite some parameters which can all be used for getting the proper data
        name: The name of the item. Recommended to make this unique within the Piece or Struct
        datatype: A datatype object
        on_success: A lambda which can be used to execute some code once the data is retrieved. You can use one
                    parameter; the data that got retrieved.
        save_as: Save the value retrieved to a dict. Can be used later with the 'set_repeat' parameter
        set_repeat: Use a saved value (from 'save_as') to set repeat value. You can use values from the dict by
                    surrounding them with curly brackets. The string will be executed using eval.
        log_value: A boolean for, mostly, debugging. This will log this Retriever with it's data on retrieval.
    """

    def __init__(self, name, datatype=DataType(), on_success=None, save_as=None, set_repeat=None, log_value=False):
        self.name = name
        self.datatype = datatype
        self.on_success = on_success
        self.save_as = save_as
        self.set_repeat = set_repeat
        self.log_value = log_value
        self.data = None

    def set_data(self, data):
        self.data = data
        if self.on_success is not None:
            self.on_success(data)

    def _to_string(self):
        if self.data is not None:
            data = " >>> " + str(self.data)
        else:
            data = ""
        return "[Retriever] " + self.name + ": " + str(self.datatype) + data

    def __str__(self):
        return self._to_string()

    def __repr__(self):
        return self._to_string()


def find_retriever(retriever_list, name):
    for x in retriever_list:
        if x.name == name:
            return x
