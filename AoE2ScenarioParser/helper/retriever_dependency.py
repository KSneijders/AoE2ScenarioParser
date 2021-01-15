from enum import Enum

from AoE2ScenarioParser.helper.exceptions import InvalidScenarioStructure


class RetrieverDependency:
    def __init__(self, dependency_type, dependency_target=None, dependency_eval=None):
        """
        Object for handling dependencies between retrievers

        Args:
            dependency_type (DependencyAction): TODO: Add docstring
            dependency_target (DependencyTarget): TODO: Add docstring
            dependency_eval (DependencyEval): TODO: Add docstring
        """
        if dependency_type != DependencyAction.REFRESH_SELF and dependency_target is None:
            raise ValueError(f"Parameter dependency_target cannot be None when target is {dependency_type.name}")

        self.dependency_type = dependency_type
        self.dependency_target = dependency_target

        if dependency_type in [DependencyAction.SET_REPEAT, DependencyAction.SET_VALUE] and dependency_eval is None:
            dependency_eval = DependencyEval(dependency_target.piece_attr_name)

        self.dependency_eval = dependency_eval

    @classmethod
    def from_structure(cls, structure):
        dependency_action = DependencyAction[structure.get('action')]
        dependency_target = DependencyTarget.instance_or_none(structure.get('target'))
        dependency_eval = DependencyEval.instance_or_none(structure.get('eval'))

        return cls(
            dependency_type=dependency_action,
            dependency_target=dependency_target,
            dependency_eval=dependency_eval,
        )

    def __repr__(self):
        return f"[RetrieverDependency] {self.dependency_type} " \
               f"\n\tTarget: {self.dependency_target}" \
               f"\n\tEval: {self.dependency_eval.eval_code}"


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

    @staticmethod
    def instance_or_none(target_string):
        if target_string is None:
            return None
        DependencyTarget.validate_target_attr(target_string)

        if type(target_string) is str:
            return DependencyTarget(*target_string.split(":"))
        elif type(target_string) is list:
            target_list = [entry.split(':') for entry in target_string]
            target_list = list(map(list, zip(*target_list)))
            return DependencyTarget(*target_list)

    @staticmethod
    def validate_target_attr(target_attr):
        if type(target_attr) is str:
            DependencyTarget.validate_target_string(target_attr)
        elif type(target_attr) is list:
            for string in target_attr:
                DependencyTarget.validate_target_string(string)
        else:
            raise TypeError(f"Invalid target string type. (type: {type(target_attr)})")

    @staticmethod
    def validate_target_string(target_string):
        if ':' not in target_string:
            raise InvalidScenarioStructure("Invalid target string. Syntax: 'self'/{piece_name}:{name_of_retriever}")

    def __repr__(self) -> str:
        return f"[DependencyTarget] {self.target_piece} -> {self.piece_attr_name}"


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

    @staticmethod
    def instance_or_none(eval_code):
        if eval_code is None:
            return None
        return DependencyEval(eval_code)


class DependencyAction(Enum):
    REFRESH = 0
    REFRESH_SELF = 1
    SET_REPEAT = 2
    SET_VALUE = 3
