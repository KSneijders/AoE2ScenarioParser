from unittest import TestCase

from AoE2ScenarioParser.objects.support.area import Area


class TestArea(TestCase):
    area: Area

    def setUp(self) -> None:
        self.area = Area(144)

    def test_area_select_entire_map(self):
        self.area.select_entire_map()
        self.assertEqual(0, self.area.x1)
        self.assertEqual(0, self.area.y1)
        self.assertEqual(self.area._map_size, self.area.x2)
        self.assertEqual(self.area._map_size, self.area.y2)

    def test_area_select(self):
        self.area.select(10, 11, 20, 22)
        self.assertEqual(10, self.area.x1)
        self.assertEqual(11, self.area.y1)
        self.assertEqual(20, self.area.x2)
        self.assertEqual(22, self.area.y2)

    def test_area_shrink(self):
        self.area.select(10, 11, 20, 22).shrink_x1(5)  # ====== X1 ======
        self.assertEqual(15, self.area.x1)
        self.area.shrink_x1(10)
        self.assertEqual(20, self.area.x1)
        self.area.shrink_y1(6)  # ====== y1 ======
        self.assertEqual(17, self.area.y1)
        self.area.shrink_x2(3)  # ====== X2 ======
        self.assertEqual(20, self.area.x2)
        self.area.shrink_y2(3)  # ====== Y2 ======
        self.assertEqual(19, self.area.y2)
        self.area.shrink_y2(8)
        self.assertEqual(17, self.area.y2)

    def test_area_expand(self):
        self.area.select(10, 10, 20, 20).expand_x1(5)  # ====== X1 ======
        self.assertEqual(5, self.area.x1)
        self.area.expand_x1(10)
        self.assertEqual(0, self.area.x1)
        self.area.expand_y1(6)  # ====== y1 ======
        self.assertEqual(4, self.area.y1)
        self.area.expand_x2(50)  # ====== X2 ======
        self.assertEqual(70, self.area.x2)
        self.area.expand_y2(100)  # ====== Y2 ======
        self.assertEqual(120, self.area.y2)
        self.area.expand_y2(50)
        self.assertEqual(self.area._map_size, self.area.y2)

    def test_area_to_coords(self):
        self.area.select(3, 3, 5, 5)
        self.assertListEqual(
            [
                (3, 3), (4, 3), (5, 3),
                (3, 4), (4, 4), (5, 4),
                (3, 5), (4, 5), (5, 5),
            ],
            self.area.selection_to_coords()
        )
        self.area.shrink_x1(1)
        self.assertListEqual(
            [
                (4, 3), (5, 3),
                (4, 4), (5, 4),
                (4, 5), (5, 5),
            ],
            self.area.selection_to_coords()
        )

    def test_area_selection(self):
        self.assertEqual(((3, 3), (5, 5)), self.area.select(3, 3, 5, 5).selection)

    def test_area_center(self):
        self.assertEqual(((8, 8), (8, 8)), self.area.set_center(8, 8).selection)

        self.area.select(3, 3, 5, 5)
        self.assertEqual((4, 4), self.area.center)
        self.area.select(3, 3, 6, 6)
        self.assertEqual((4.5, 4.5), self.area.center)
        self.assertEqual((4, 4), self.area.center_int)

    def test_area_set_center(self):
        self.area.select(3, 3, 5, 5).set_center(8, 8)
        self.assertEqual((8.0, 8.0), self.area.center)
        self.assertEqual(((7, 7), (9, 9)), self.area.selection)

        self.area.select(5, 10, 20, 20).set_center(5, 0)
        self.assertEqual((6.0, 2.5), self.area.center)
        self.assertEqual(((0, 0), (12, 5)), self.area.selection)

    def test_area_set_center_bound(self):
        self.area.select(3, 3, 5, 5).set_center_bound(8, 8)
        self.assertEqual((8.0, 8.0), self.area.center)
        self.assertEqual(((7, 7), (9, 9)), self.area.selection)

        self.area.select(5, 10, 20, 20).set_center_bound(5, 0)
        self.assertEqual((7.5, 5.0), self.area.center)
        self.assertEqual(((0, 0), (15, 10)), self.area.selection)

        self.area.select(100, 80, 130, 128).set_center_bound(140, 140)
        self.assertEqual((128.0, 119.0), self.area.center)
        self.assertEqual(((113, 95), (self.area._map_size, self.area._map_size)), self.area.selection)

    def test_area_set_size(self):
        self.area.set_center(8, 8).set_size(9)
        self.assertEqual(((4, 4), (12, 12)), self.area.selection)

        self.area.set_size(10)
        self.assertEqual(((4, 4), (13, 13)), self.area.selection)

        self.area.set_center(5, 5).set_size(300)
        self.assertEqual(((0, 0), (self.area._map_size, self.area._map_size)), self.area.selection)
