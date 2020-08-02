class Alias():
    """
    class that allows to build aliases in handler objects
    so that they can access and modify directly data contained in the pieces
    """
    def __init__(self, data_holder, name):
        self.data_holder = data_holder
        self.name = name
    def __get__(self, instance, owner):
        return getattr(getattr(instance, self.data_holder), self.name)
    def __set__(self, instance, value):
        setattr(getattr(instance, self.data_holder), self.name, value)