from __future__ import annotations

from binary_file_parser import BaseStruct, Retriever
from binary_file_parser.types import float32


class PlayerDataBlock4(BaseStruct):
    food: float = Retriever(float32, default=0.0)
    """duplicate"""
    wood: float = Retriever(float32, default=0.0)
    """duplicate"""
    gold: float = Retriever(float32, default=0.0)
    """duplicate"""
    stone: float = Retriever(float32, default=0.0)
    """duplicate"""
    ore_x: float = Retriever(float32, default=0.0)
    """duplicate"""
    trade_goods: float = Retriever(float32, default=0.0)
    population_limit: float = Retriever(float32, default=200.0)

    def __init__(self, struct_version: tuple[int, ...] = (1, 47), parent: BaseStruct = None, initialise_defaults=True):
        super().__init__(struct_version, parent, initialise_defaults)
