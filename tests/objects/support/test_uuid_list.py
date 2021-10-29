from unittest import TestCase

from AoE2ScenarioParser.objects.support.uuid_list import UuidList


class U:
    def __init__(self):
        self._host_uuid = ''

    def __repr__(self):
        return f"X: {self._host_uuid}"


class TestUuidList(TestCase):
    lst: UuidList

    def setUp(self) -> None:
        self.lst = UuidList("uuid")

    def test_uuid_transfer_init(self):
        lst = UuidList("uuid", (U(),))

        self.assertEqual(lst[0]._host_uuid, "uuid")

    def test_uuid_transfer_append(self):
        u = U()
        self.lst.append(u)
        self.assertEqual(u._host_uuid, "uuid")

    def test_uuid_transfer_append_nested(self):
        self.lst.uuid_list_depth = 2
        self.lst.append(UuidList('not-uuid', (U(), )))
        self.lst.append([U()])
        for lst in self.lst:
            self.assertEqual(lst.uuid, "uuid")
            for e in lst:
                self.assertEqual(e._host_uuid, "uuid")

    def test_uuid_transfer_extend(self):
        lst = [U(), U(), U()]
        self.lst.extend(lst)
        for u in self.lst:
            self.assertEqual(u._host_uuid, "uuid")

    def test_uuid_transfer_extend_nested(self):
        self.lst.uuid_list_depth = 2
        self.lst.extend(UuidList('not-uuid', UuidList('not-uuid2', (U(), U()))))
        self.lst.extend([[U(), U()], [U(), U()]])
        for lst in self.lst:
            self.assertEqual(lst.uuid, "uuid")
            for e in lst:
                self.assertEqual(e._host_uuid, "uuid")

    def test_uuid_transfer_insert(self):
        u = U()
        self.lst.insert(0, u)
        self.assertEqual(u._host_uuid, "uuid")

    def test_uuid_transfer_setitem_single(self):
        u = U()
        self.lst.extend((U(), U(), U()))
        self.lst[1] = u
        self.assertEqual(u._host_uuid, "uuid")

    def test_uuid_transfer_setitem_slice(self):
        slc = (U(), U())
        self.lst.extend((U(), U(), U()))
        self.lst[1:3] = slc
        for u in self.lst:
            self.assertEqual(u._host_uuid, "uuid")
