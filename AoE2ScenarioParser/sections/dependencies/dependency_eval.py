class DependencyEval:
    def __init__(self, eval_code, eval_locals=None):
        """
        Object for storing dependency eval code and it's locals.

        Args:
            eval_code (str): The code executed using eval
            eval_locals (dict): The locals dict handed to the eval function
        """
        if eval_locals is None:
            eval_locals = {}

        self.eval_code = eval_code
        self.eval_locals = eval_locals

    @classmethod
    def instance_or_none(cls, eval_code):
        if eval_code is None:
            return None
        return cls(eval_code)
