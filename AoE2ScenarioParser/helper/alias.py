class Alias():
    """
    class that allows to build aliases in handler objects
    so that they can access and modify directly data contained in the pieces
    """
    def __init__(self, expression):
        self.expression = expression

    def __get__(self, instance, owner):
        # Evaluate the expression where self refers to the instance
        return eval(self.expression, {}, {'self': instance})

    def __set__(self, instance, value):
        # Execute the expression to assign it the new value
        exec(self.expression + " = value", {}, {'self': instance, 'value': value})
            

