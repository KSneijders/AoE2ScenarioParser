class DataType:
    """ A class to identify what data you want to retrieve. This class has two parameters which are very useful.
        var:
            - Almost always a string representation of the data you want to retrieve. This project uses the types from:
                http://dderevjanik.github.io/agescx/formatscx/#format
                s: Signed integer       All integers (signed and unsigned) are parsed as little endian
                u: Unsigned integer     All integers (signed and unsigned) are parsed as little endian
                f: float
                c: Character string of fixed length
                (Empty): Is interpreted as regular byte data. In this project the '' is converted to 'data'
                str: Character string of variable length.
                    This type will read the number in bits given and parse it as an int. The number retrieved from it
                    will be the amount of bytes read as a character string.
            - Another option for the var parameter is to give a Struct (not Python struct) subclass as var. This will
            parse all DataType values in the Struct subclass. This can be handy for when blocks of data are repeated.
            - Per data type you can save how large the value is bit/byte wise. While this may be confusing not all
            values are in bit format. Some are in byte format.
                Bit format: [s, u, f, str]
                Byte format: [c, data]
            - To define a length to your data type, write the datatype with the length behind it (no whitespaces)
                Example 1:  s16             > A signed integer of 16 bits.
                Example 2:  f32             > A 32 bit floating point number.
                Example 3:  c4              > A 32 bit (4 bytes) character string.
                Example 4:  str16           > A 16 bit integer will be parsed (n). Now n bytes will be read as character
                                            string.
                Example 5:  TerrainStruct   > The TerrainStruct will be instantiated and DataTypes from that struct will
                                            be loaded in it's place.
        repeat:
            The amount of times the above datatype needs to be repeated
    """

    __slots__ = [
        'var',
        '_repeat',
        'log_value',
        'type',
        'length',
        '_debug_retriever_name'
    ]

    _debug_retriever_name: str

    def __init__(self, var="0", repeat=1, log_value=False, type_length=None):
        self.var = var
        self._repeat = repeat
        self.log_value = log_value

        if type_length is not None:
            self.type, self.length = type_length
        else:
            self.type, self.length = datatype_to_type_length(self.var)

    def get_struct_name(self) -> str:
        if self.var.startswith("struct:"):
            return self.var[7:]
        raise ValueError("Datatype var is not a struct")

    @property
    def type_and_length(self):
        return self.type, self.length

    @property
    def repeat(self):
        return self._repeat

    @repeat.setter
    def repeat(self, value):
        if self.log_value:
            print(f"[DataType] {self._debug_retriever_name} 'repeat' set to {value} (was: {self._repeat})")
        self._repeat = value

    def to_simple_string(self):
        return f"{self._repeat} * {self.var}"

    def __repr__(self):
        return f"[DataType] " + self.to_simple_string()

    def duplicate(self):
        return DataType(
            var=self.var,
            repeat=self.repeat,
            log_value=self.log_value,
            type_length=(self.type, self.length)
        )


def datatype_to_type_length(var):
    """Returns the type and length of a datatype. So: 'int32' returns 'int', 32. """
    if var[:7] == "struct:":
        return "struct", 0

    # Filter numbers out for length, filter text for type
    var_len = int(''.join(filter(str.isnumeric, var)))
    var_type = ''.join(filter(str.isalpha, var))

    if var_type == '':
        var_type = "data"

    if var_type not in datatype_types:
        raise ValueError(f"Unknown variable type '{var_type}'")

    # Divide by 8, and parse from float to int
    if var_type not in ["c", "data"]:
        var_len = int(var_len / 8)

    return var_type, var_len


datatype_types = [
    "s",  # Signed int
    "u",  # Unsigned int
    "f",  # FloatingPoint
    "c",  # Character string
    "str",  # Variable length string
    "data",  # Data (Can be changed by used using bytes_to_x functions)
]
