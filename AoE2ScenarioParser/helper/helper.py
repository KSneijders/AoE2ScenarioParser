def update_order_array(order_array, supposed_length):
    for i in range(0, supposed_length):
        if i not in order_array:
            order_array.append(i)


def create_textual_hex(string, space_distance=2, enter_distance=48):
    """Please note that the 'enter_distance' parameter is including the - to be added - spaces. If you calculated it
    without the spaces, please multiply the number by: `block size incl space / block size excl space`"""
    return insert_char(insert_char(string, " ", space_distance), "\n", enter_distance)


# Credits: gurney alex @ https://stackoverflow.com/a/2657733/7230293
def insert_char(string, char, every=64):
    return char.join(string[i:i + every] for i in range(0, len(string), every))


def add_str_trail(string):
    return (string + ("\x00" if string[-1] != "\x00" else "")) if len(string) > 0 else string


def del_str_trail(string):
    return string.replace('\x00', "")


def pretty_print_list(plist):
    return_string = "[\n"
    for x in plist:
        return_string += "\t" + str(x)
    return return_string + "]\n"


def add_prefix_chars(string, char, length):
    if len(string) > length:
        return string
    else:
        return char * (length - len(string)) + string


def add_suffix_chars(string, char, length):
    if len(string) > length:
        return string
    else:
        return string + char * (length - len(string))


def pretty_print_name(name: str) -> str:
    """
    Returns a pretty-printed version of the name string.
    Replaces all underscores with spaces and capitalizes the first letter
    of each word.
    For example, elite_chu_ko_nu -> Elite Chu Ko Nu.

    :Author:
        T-West (https://github.com/twestura/)
    """
    return ' '.join(s[0].upper() + s[1:] for s in name.split('_'))


class SimpleLogger:
    def __init__(self, should_log):
        self.should_log = should_log

    def print(self, string):
        if self.should_log:
            print(string)

    def __repr__(self):
        return f"SimpleLogger[should_log: {self.should_log}]"


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
