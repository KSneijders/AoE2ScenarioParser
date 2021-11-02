from unittest import TestCase

from AoE2ScenarioParser.objects.support.uuid_list import UuidList


class U:
    """Mock object like AoE2Object"""

    def __init__(self):
        self._host_uuid = ''

    def __repr__(self):
        return f"u'{self._host_uuid}'"


class TestUuidList(TestCase):
    lst: UuidList

    def setUp(self) -> None:
        self.lst = UuidList("uuid")

    def test_uuid_transfer_init(self):
        self.lst = UuidList("uuid", (U(),))

        self.assertEqual(self.lst[0]._host_uuid, "uuid")

    def test_uuid_transfer_init_nested(self):
        self.lst = UuidList("uuid", ((U(), U(),), (U(), U(),)))

        for lst in self.lst:
            self.assertEqual(lst.uuid, "uuid")
            for e in lst:
                self.assertEqual(e._host_uuid, "uuid")

    # ################## Append ##################

    def test_uuid_transfer_append(self):
        u = U()
        self.lst.append(u)
        self.assertEqual(u._host_uuid, "uuid")

    def test_uuid_transfer_append_nested(self):
        self.lst.append(UuidList('not-uuid', (U(),)))
        self.lst.append([U()])
        for lst in self.lst:
            self.assertEqual(lst.uuid, "uuid")
            for e in lst:
                self.assertEqual(e._host_uuid, "uuid")

    # ################## Extend ##################

    def test_uuid_transfer_extend(self):
        lst = [U(), U(), U()]
        self.lst.extend(lst)
        for u in self.lst:
            self.assertEqual(u._host_uuid, "uuid")

    def test_uuid_transfer_extend_nested(self):
        self.lst.extend(
            UuidList('not-uuid', (
                UuidList('not-uuid2', (U(),)),
                UuidList('not-uuid2', (U(),))
            ))
        )
        self.lst.extend([(U(),), (U(),)])
        self.lst.extend([(U(),), UuidList('not-uuid3', (U(),))])

        for lst in self.lst:
            self.assertEqual(lst.uuid, "uuid")
            for e in lst:
                self.assertEqual(e._host_uuid, "uuid")

    # ################## Insert ##################

    def test_uuid_transfer_insert(self):
        u = U()
        self.lst.insert(0, u)
        self.assertEqual(u._host_uuid, "uuid")

    def test_uuid_transfer_insert_nested(self):
        self.lst.insert(0, UuidList('not-uuid3', (U(),)))
        self.lst.insert(0, (U(),))
        for lst in self.lst:
            self.assertEqual(lst.uuid, "uuid")
            for e in lst:
                self.assertEqual(e._host_uuid, "uuid")

    # ################## __setitem__ ##################

    def test_uuid_transfer_setitem_single(self):
        u = U()
        self.lst.extend((U(), U(), U()))
        self.lst[1] = u
        self.assertEqual(u._host_uuid, "uuid")

    def test_uuid_transfer_setitem_single_nested(self):
        self.lst.extend(((U(), U(), U()), (U(), U(), U())))

        self.lst[0] = (U(), U(), U())
        self.lst[1][2] = U()

        for lst in self.lst:
            self.assertEqual(lst.uuid, "uuid")
            for e in lst:
                self.assertEqual(e._host_uuid, "uuid")

    def test_uuid_transfer_setitem_slice(self):
        self.lst.extend((U(), U(), U()))

        self.lst[1:3] = (U(), U())
        for u in self.lst:
            self.assertEqual(u._host_uuid, "uuid")

    def test_uuid_transfer_setitem_slice_nested(self):
        self.lst.extend((
            (U(), U(), U()),
            (U(), U(), U()),
            (U(), U(), U()),
            (U(), U(), U())
        ))

        self.lst[1:3] = ((U(), U()), (U(), U()))
        for lst in self.lst:
            self.assertEqual(lst.uuid, "uuid")
            for e in lst:
                self.assertEqual(e._host_uuid, "uuid")
