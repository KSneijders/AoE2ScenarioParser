from __future__ import annotations

from typing import overload, Self

from AoE2ScenarioParser.objects.support.location import Location


# Todo: Add immutability to class
class Point(Location):

    @overload
    def __init__(self, x: float, y: float) -> None:
        ...

    @overload
    def __init__(self, point: tuple[float, float]) -> None:
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value: float):
        self._x = value

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value: float):
        self._y = value

    @overload
    def move(self, x_offset: float = 0, y_offset: float = 0) -> Self:
        ...

    def move(self, *args, **kwargs):
        super().move(*args, **kwargs)

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
