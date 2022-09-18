from __future__ import annotations

from typing import Dict


class DependencyEval:
    """
    Provides the objects for storing dependency eval code and it's locals.
    """
    def __init__(self, eval_code: str, eval_locals: Dict | None = None):
        """
        Args:
            eval_code: The code executed using eval
            eval_locals: The locals dict handed to the eval function
        """
        if eval_locals is None:
            eval_locals = {}

        self.eval_code: str = eval_code
        self.eval_locals: Dict = eval_locals

    @classmethod
    def instance_or_none(cls, eval_code: str) -> DependencyEval | None:
        """
        Returns a DependencyEval instance created from the given code

        Args:
            eval_code (str): The code to create the DependencyEval object with

        Returns:
            An instance of the DependencyEval class
        """
        if eval_code is None:
            return None
        return cls(eval_code)
