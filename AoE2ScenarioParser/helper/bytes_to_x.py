import struct
from enum import Enum, IntEnum


def bytes_to_str(byte_elements, codec="utf-8"):
    return byte_elements.decode(codec)


def str_to_bytes(string, codec="utf-8"):
    return string.encode(codec)


def bytes_to_int(byte_elements, endian="little", signed=False):
    return int.from_bytes(byte_elements, endian, signed=signed)


def int_to_bytes(integer: IntEnum, length, endian="little", signed=True):
    if isinstance(integer, IntEnum):
        integer = integer.value
    return integer.to_bytes(length, byteorder=endian, signed=signed)


def bytes_to_float(byte_elements):
    return struct.unpack('f', byte_elements)[0]


def float_to_bytes(f):
    return struct.pack('f', f)


def bytes_to_double(byte_elements):
    return struct.unpack('d', byte_elements)[0]


def double_to_bytes(d):
    return struct.pack('d', d)
