class Alias():
    """
    class that allows to build aliases in handler objects
    so that they can access and modify directly data contained in the pieces
    Aliases should only be used for immutable objects, and thus do not support complex ones
    """
    def __init__(self, expression):
        self.expression = expression

    def __get__(self, instance, owner):
        # Evaluate the expression where self refers to the instance
        return eval(self.expression, globals(), {'self': instance})

    def __set__(self, instance, value):
        # Execute the expression to assign it the new value
        exec(self.expression + " = " + str(value), globals(), {'self': instance})
            

