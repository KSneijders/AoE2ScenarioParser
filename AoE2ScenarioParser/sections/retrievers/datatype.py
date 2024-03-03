from __future__ import annotations


class DataType:
    """
    This class is used to represent the data type of the value being retrieved. Every retriever has this as an attribute
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

    def __init__(self, var: str = "0", repeat: int = 1, log_value: bool = False, type_length: tuple = None):
        """
        Args:
            var: string representation of the datatype
            repeat: the amount of times a value is repeated
            log_value: to log the value of the datatype when repeat is set
            type_length: a tuple containing the type and length of the datatype

        Descriptions:
            var:
                Almost always a string representation of the data you want to retrieve.
                This project uses the types from: https://dderevjanik.github.io/agescx/formatscx/#format

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

            log_value (Default: False):
                A boolean value indicating if the datatype should be logged

            type_length (Default: None):
                A tuple specifying the type and length of a retriever
        """
        self.log_value = log_value
        self.var = var
        self.repeat = repeat

        if type_length is not None:
            self.type, self.length = type_length
        else:
            self.type, self.length = datatype_to_type_length(self.var)

    def get_struct_name(self) -> str:
        """
        Returns the name of the datatype structure

        Returns:
            The name of the DataType structure

        Raises:
            ValueError: if the datatype is not a struct
        """
        if self.var.startswith("struct:"):
            return self.var[7:]
        raise ValueError("Datatype var is not a struct")

    @property
    def type_and_length(self) -> tuple:
        """A tuple of the type and length of the datatype"""
        return self.type, self.length

    @property
    def repeat(self) -> int:
        """The amount of times the datatype repeats"""
        return self._repeat

    @repeat.setter
    def repeat(self, value: int):
        """
        The setter for the repeat value of the datatype

        Args:
            value: The value to set repeat to. The value of an assignment is automatically passed as this argument
        """
        if type(value) is not int:
            raise TypeError(f"Repeat value must be an integer, now: {value}")

        if self.log_value and hasattr(self, '_debug_retriever_name'):
            print(f"[DataType] {self._debug_retriever_name} 'repeat' set to {value} (was: {self._repeat})")
        self._repeat = value

    def to_simple_string(self) -> str:
        """
        Get a string representation of the datatype containing its repeat value and the var type

        Returns:
            A string representation of the datatype
        """
        return f"{self._repeat} * {self.var}"

    def duplicate(self) -> DataType:
        """
        Create another datatype instance with the same values as this one

        Returns:
            A datatype instance with the same values as this one
        """
        return DataType(
            var=self.var,
            repeat=self.repeat,
            log_value=self.log_value,
            type_length=self.type_and_length
        )

    def __repr__(self):
        return f"[DataType]  " + self.to_simple_string()


def datatype_to_type_length(var: str) -> tuple:
    """
    Get the type and length of a datatype

    Args:
        var: The datatype string

    Returns:
        The type and length of a datatype. So: 'int32' returns 'int', 32.

    Raises:
        ValueError: if the variable type is not in [s, u, f, c, str, data]
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
