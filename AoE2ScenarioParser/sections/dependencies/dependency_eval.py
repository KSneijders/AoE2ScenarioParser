from __future__ import annotations

from typing import Dict


class DependencyEval:
    def __init__(self, eval_code: str, eval_locals: Dict | None = None):
        """
        Object for storing dependency eval code and it's locals.

        Args:
            eval_code: The code executed using eval
            eval_locals: The locals dict handed to the eval function
        """
        if eval_locals is None:
            eval_locals = {}

        self.eval_code: str = eval_code
        self.eval_locals: Dict = eval_locals

    @classmethod
    def instance_or_none(cls, eval_code: str) -> DependencyEval:
        if eval_code is None:
            raise ValueError("The parameter `eval_code` cannot be None")
        return cls(eval_code)
