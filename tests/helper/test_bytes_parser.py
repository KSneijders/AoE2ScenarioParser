from unittest import TestCase

from AoE2ScenarioParser.helper.bytes_parser import *
from AoE2ScenarioParser.sections.retrievers.datatype import DataType
from AoE2ScenarioParser.sections.retrievers.retriever import Retriever


class Test(TestCase):
    def test_vorl(self):
        # Test repeat == 1 && len(value) == 1
        retriever = Retriever('name', 0, DataType('1', repeat=1))
        self.assertEqual(vorl(retriever, [10]), 10)

        # Test repeat > 1 && len(value) == 1
        retriever = Retriever('name', 0, DataType('1', repeat=2))
        self.assertEqual(vorl(retriever, [10]), [10])

        # Test repeat == 1 && len(value) > 1
        retriever = Retriever('name', 0, DataType('1', repeat=1))
        self.assertEqual(vorl(retriever, [10, 20]), [10, 20])

        # Test repeat > 1 && len(value) > 1
        retriever = Retriever('name', 0, DataType('1', repeat=2))
        self.assertEqual(vorl(retriever, [10, 20]), [10, 20])

        # Test repeat == 1 && is_list && len(value) == 1
        retriever = Retriever('name', 0, DataType('1', repeat=1), is_list=True)
        self.assertEqual(vorl(retriever, [10]), [10])

        # Test repeat == 1 && not is_list && len(value) == 1
        retriever = Retriever('name', 0, DataType('1', repeat=1), is_list=False)
        self.assertEqual(vorl(retriever, [10]), 10)

    #

    # def test_retrieve_bytes(self):
    #     self.fail()
    #
    # def test_is_end_of_file_mark(self):
    #     self.fail()
    #
    # def test_handle_end_of_file_mark(self):
    #     self.fail()
