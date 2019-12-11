class Retriever:
    def __init__(self,
                 name,  # Name of the item
                 datatype,  # Datatype Object
                 on_success=None,  # Lambda for what happens with the value once it's retrieved
                 save_as=None,  # Save the value for other usage
                 set_repeat=None,  # Use saved value to set repeat value. Use String and use saved name like {name}
                 # All Python functions and math is allowed, example: {length}*{width}+4
                 pre_read=None,
                 ):
        self.name = name
        self.datatype = datatype
        self.on_success = on_success
        self.save_as = save_as
        self.set_repeat = set_repeat
        self.pre_read = pre_read

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
