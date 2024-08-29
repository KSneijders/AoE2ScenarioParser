import warnings
from unittest import TestCase

from AoE2ScenarioParser.helper.bytes_conversions import *
from AoE2ScenarioParser.sections.retrievers.datatype import DataType
from AoE2ScenarioParser.sections.retrievers.retriever import Retriever


class Test(TestCase):
    def test_bytes_to_fixed_chars(self):
        self.assertEqual(bytes_to_fixed_chars(b'Test Byte String'), 'Test Byte String')

    def test_fixed_chars_to_bytes(self):
        self.assertEqual(fixed_chars_to_bytes('Test String', 11), b'Test String')
        self.assertEqual(fixed_chars_to_bytes('Test String', 20), b'Test String\x00\x00\x00\x00\x00\x00\x00\x00\x00')

    def test_bytes_to_str(self):
        normal = b'Test Byte String'
        zero_char = b'Test Byte String With 0 char at end\x00'
        latin1 = b'latin-1 encoded string > \xe9\xe1\xfb'
        utf8 = b'utf-8 encoded string > \xc3\xa9\xc3\xa1\xc3\xbb'
        latin1_zero_char = b'latin-1 encoded string > \xe9\xe1\xfb\x00'
        utf8_zero_char = b'utf-8 encoded string > \xc3\xa9\xc3\xa1\xc3\xbb\x00'

        self.assertEqual(bytes_to_str(normal), 'Test Byte String')
        self.assertEqual(bytes_to_str(zero_char), 'Test Byte String With 0 char at end')
        self.assertEqual(bytes_to_str(latin1), 'latin-1 encoded string > éáû')
        self.assertEqual(bytes_to_str(utf8), 'utf-8 encoded string > éáû')
        self.assertEqual(bytes_to_str(latin1_zero_char), 'latin-1 encoded string > éáû')
        self.assertEqual(bytes_to_str(utf8_zero_char), 'utf-8 encoded string > éáû')

        # When not able to decode using a given charset, it *should* give the input back as-is.
        warnings.filterwarnings(action='ignore', category=ByteDecodeWarning)
        self.assertEqual(bytes_to_str(latin1, charset='ascii', fallback_charset='ascii'), latin1)
        self.assertEqual(bytes_to_str(utf8_zero_char, charset='ascii', fallback_charset='ascii'), utf8_zero_char)

    def test_str_to_bytes(self):
        self.assertEqual(str_to_bytes('Test String'), b'Test String')

        self.assertEqual(str_to_bytes(b'Test String'), b'Test String')

    def test_bytes_to_int(self):
        self.assertEqual(bytes_to_int(b'\x20\x81', signed=True), -32480)
        self.assertEqual(bytes_to_int(b'\x20\x81', signed=False), 33056)
        self.assertEqual(bytes_to_int(b'\x20\x71', signed=True), 28960)
        self.assertEqual(bytes_to_int(b'\x20\x71', signed=False), 28960)

    def test_int_to_bytes(self):
        self.assertEqual(int_to_bytes(100, 1, signed=False), b'\x64')
        self.assertEqual(int_to_bytes(100, 1, signed=True), b'\x64')
        self.assertRaises(OverflowError, int_to_bytes, -100, 1, signed=False)
        self.assertEqual(int_to_bytes(-100, 1, signed=True), b'\x9c')

        self.assertEqual(int_to_bytes(100, 2, signed=False), b'\x64\x00')
        self.assertEqual(int_to_bytes(100, 3, signed=False), b'\x64\x00\x00')
        self.assertEqual(int_to_bytes(100, 4, signed=False), b'\x64\x00\x00\x00')

    def test_bytes_to_float(self):
        self.assertEqual(bytes_to_float(b'\x01\x00\x00\x00'), 1.401298464324817e-45)
        self.assertEqual(bytes_to_float(b'\xff\x93\xde\x09'), 5.358373081446331e-33)

    def test_float_to_bytes(self):
        self.assertEqual(float_to_bytes(1.401298464324817e-45), b'\x01\x00\x00\x00')
        self.assertEqual(float_to_bytes(5.358373081446331e-33), b'\xff\x93\xde\x09')

    def test_bytes_to_double(self):
        self.assertEqual(bytes_to_double(b'\x01\x00\x00\x00\x01\x00\x00\x00'), 2.1219957915e-314)
        self.assertEqual(bytes_to_double(b'\xff\x93\xde\x09\xff\x93\xde\x09'), 3.884314764846234e-261)

    def test_double_to_bytes(self):
        self.assertEqual(double_to_bytes(2.1219957915e-314), b'\x01\x00\x00\x00\x01\x00\x00\x00')
        self.assertEqual(double_to_bytes(3.884314764846234e-261), b'\xff\x93\xde\x09\xff\x93\xde\x09')

    def test_parse_val_to_bytes(self):
        retriever = Retriever(name='_', default_value=0, datatype=DataType("u16"))
        self.assertEqual(parse_val_to_bytes(retriever, 1), b'\x01\x00')
        retriever.datatype = DataType("s16")
        self.assertEqual(parse_val_to_bytes(retriever, -1), b'\xff\xff')
        retriever.datatype = DataType("str16")
        self.assertEqual(parse_val_to_bytes(retriever, "Hello World"), b'\x0c\x00Hello World\x00')
        self.assertEqual(parse_val_to_bytes(retriever, b"Hello World"), b'\x0c\x00Hello World\x00')
        retriever.datatype = DataType("c15")
        self.assertEqual(parse_val_to_bytes(retriever, "Hello World"), b'Hello World\x00\x00\x00\x00')
        retriever.datatype = DataType("20")
        self.assertEqual(parse_val_to_bytes(retriever, b'Direct bytes\x11\xff'), b'Direct bytes\x11\xff')
        retriever.datatype = DataType("f32")
        self.assertEqual(parse_val_to_bytes(retriever, 3.14), b'\xc3\xf5\x48\x40')

    def test_parse_bytes_to_val(self):
        retriever = Retriever(name='_', default_value=0, datatype=DataType("u16"))
        self.assertEqual(parse_bytes_to_val(retriever, b'\x01\x00'), 1)
        retriever.datatype = DataType("s16")
        self.assertEqual(parse_bytes_to_val(retriever, b'\xff\xff'), -1)
        retriever.datatype = DataType("str16")
        self.assertEqual(parse_bytes_to_val(retriever, b'\x0b\x00Hello World\x00'), "Hello World")
        retriever.datatype = DataType("c20")
        self.assertEqual(parse_bytes_to_val(retriever, b'Hello World'), "Hello World")
        retriever.datatype = DataType("20")
        self.assertEqual(parse_bytes_to_val(retriever, b'Direct bytes\x11\xff'), b'Direct bytes\x11\xff')
        retriever.datatype = DataType("f32")
        self.assertEqual(parse_bytes_to_val(retriever, b'\xc3\xf5\x48\x40'), 3.140000104904175)
