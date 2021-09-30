class DataType:
    """
A class to identify what data you want to retrieve. This class has two parameters (var, repeat) which are very useful.


        var:
            Almost always a string representation of the data you want to retrieve. This project uses the types from:
            https://dderevjanik.github.io/agescx/formatscx/#format

            - **s**: Signed integer (parsed as little endian)
            - **u**: Unsigned integer (parsed as little endian)
            - **f**: float
            - **c**: Character string of fixed length
            - **str**: Character string of variable length. This type will read the number in bits given and parse it as
              an int. The number retrieved from it will be the amount of bytes read as a character string.
            - **Struct:<StructName>**: This is like a class, and is a collection of related information. Structs may
              contain sub-structs and other simpler data types. This will parse all DataType values in the Struct
              subclass. This can be handy for when blocks of data are repeated.
            - **(Empty)**: Is interpreted as regular byte data. In this project the '' is converted to 'data'

            ​
            Each datatype is followed by a number that tells how many bits/bytes are used to store it.

            - The types **s, u, f & str** use an amount of bits to specify their size.
            - The types **c & data** use bytes to specify their size.

            For example:
                * **s16**: A 16 bit signed integer.
                * **f32**: A 32 bit floating point number.
                * **c4**: A 32 bit (4 bytes) character string.
                * **str16**: A 16 bit integer will be parsed (n). Now n bytes will be read as character string.
                * **TerrainStruct**: The TerrainStruct will be instantiated and DataTypes from that struct will be
                  loaded in it's place.

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
    """
    Get the type and length of a datatype

    Args:
        var (str): The datatyoe string

    Returns:
        The type and length of a datatype. So: 'int32' returns 'int', 32.

    """
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
