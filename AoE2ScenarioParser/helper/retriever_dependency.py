from enum import Enum


class RetrieverDependency:
    def __init__(self, dependency_type, dependency_target=None, dependency_eval=None):
        """
        Object for handling dependencies between retrievers

        Args:
            dependency_type (DependencyAction): TODO: Add docstring
            dependency_target (DependencyTarget): TODO: Add docstring
            dependency_eval (DependencyEval): TODO: Add docstring
        """
        self.dependency_type = dependency_type
        self.dependency_target = dependency_target

        if dependency_type in [DependencyAction.SET_REPEAT, DependencyAction.SET_VALUE] and dependency_eval is None:
            dependency_eval = DependencyEval('x')

        self.dependency_eval = dependency_eval


class DependencyTarget:
    def __init__(self, target_piece, piece_attr_name):
        """
        Object for targeting a specific retriever based on it's piece name (or 'self') and the retriever name.

        Args:
            target_piece (Union[str, List[str]]): The name of the targeted piece or 'self' for own list
            piece_attr_name (Union[str, List[str]]): The name of the attribute in targeted piece or own list
        """
        if not ((type(target_piece) is list and type(piece_attr_name) is list) or
                (type(target_piece) is str and type(piece_attr_name) is str)):
            raise TypeError("Both parameters should be of the same type. This can be list or str.")
        if type(target_piece) is list:
            if not (len(target_piece) == len(piece_attr_name)):
                raise ValueError("Both parameters should be of the same length when using lists.")
        self.target_piece = target_piece
        self.piece_attr_name = piece_attr_name


class DependencyEval:
    def __init__(self, eval_code, eval_locals=None, values_as_variable=None):
        """
        Object for storing dependency eval code and it's locals.

        Args:
            eval_code (str): The code executed using eval
            eval_locals (dict): The locals dict handed to the eval function
        """
        if eval_locals is None:
            eval_locals = {}
        if values_as_variable is None:
            values_as_variable = []
        self.eval_code = eval_code
        self.eval_locals = eval_locals
        self.values_as_variable = values_as_variable


class DependencyAction(Enum):
    UNDEFINED = -1
    REFRESH = 0
    REFRESH_SELF = 1
    SET_REPEAT = 2
    SET_VALUE = 3
