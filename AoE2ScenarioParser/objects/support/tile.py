class Tile:
    def __init__(self, x: int, y: int):
        self.x: float = x
        self.y: float = y

    def __repr__(self):
        return f"Tile[x: {self.x}, y: {self.y}]"

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, val: int):
        self._x = int(val) + .5

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, val: int):
        self._y = int(val) + .5

    @property
    def x1(self) -> int:
        return int(self.x - .5)

    @property
    def y1(self) -> int:
        return int(self.y - .5)

    @property
    def x2(self) -> int:
        return int(self.x + .5)

    @property
    def y2(self) -> int:
        return int(self.y + .5)