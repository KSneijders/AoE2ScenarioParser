from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from binary_file_parser import Retriever


def r(value) -> 'Retriever':
    """Helper to help Pycharm understand things thxPyC"""
    return value
