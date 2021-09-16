from unittest import TestCase

from AoE2ScenarioParser.helper.helper import xy_to_i, i_to_xy


"""
x = Cols (West -> North)
y = Rows (West -> South)
m = Map Size
i = Index

So:
    (x4, y0, m10)   == i 4
    (x9, y0, m10)   == i 9
    (x2, y1, m10)   == i 12
"""


class Test(TestCase):
    def test_xy_to_i(self):
        self.assertEqual(xy_to_i(0, 0, 10), 0)
        self.assertRaises(ValueError, lambda: xy_to_i(11, 0, 10))

        self.assertEqual(xy_to_i(0, 1, 10), 10)
        self.assertEqual(xy_to_i(2, 2, 10), 22)
        self.assertEqual(xy_to_i(5, 5, 25), 130)

    def test_i_to_xy(self):
        self.assertEqual(i_to_xy(0, 10), (0, 0))
        self.assertRaises(ValueError, lambda: i_to_xy(25, 5))

        self.assertEqual(i_to_xy(10, 10), (0, 1))
        self.assertEqual(i_to_xy(22, 10), (2, 2))
        self.assertEqual(i_to_xy(130, 25), (5, 5))

    def test_conv_combination(self):
        self.assertEqual(i_to_xy(xy_to_i(25, 3, 100), 100), (25, 3))
        self.assertEqual(xy_to_i(*i_to_xy(325, 100), 100), 325)
