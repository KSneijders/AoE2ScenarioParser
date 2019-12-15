import struct


def bytes_to_str(byte_elements, codec="ascii"):
    return byte_elements.decode(codec)


def bytes_to_int(byte_elements, endian="little", signed=False):
    return int.from_bytes(byte_elements, endian, signed=signed)


def bytes_to_float(byte_elements):
    return struct.unpack_from('f', byte_elements)[0]
