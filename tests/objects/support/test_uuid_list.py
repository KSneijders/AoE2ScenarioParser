from unittest import TestCase

from AoE2ScenarioParser.objects.support.uuid_list import UuidList


class U:
    """Mock object like AoE2Object"""

    def __init__(self):
        self._uuid = ''
        self.other = 0

    def __repr__(self):
        return f"u'{self._uuid}'"


class NU:
    """Nested Mock object like AoE2Object"""

    def __init__(self):
        self._uuid = ''
        self.values = UuidList(self._uuid, (U(), U(), U()))

    def __repr__(self):
        return f"u'{self._uuid}'"


class TestUuidList(TestCase):
    lst: UuidList

    def setUp(self) -> None:
        self.lst = UuidList("uuid")

    def test_uuid_transfer_init(self):
        self.lst = UuidList("uuid", (U(),))

        self.assertEqual("uuid", self.lst[0]._uuid)

    def test_uuid_transfer_init_nested(self):
        self.lst = UuidList("uuid", ((U(), U(),), (U(), U(),)))

        for lst in self.lst:
            self.assertEqual("uuid", lst.uuid)
            for e in lst:
                self.assertEqual("uuid", e._uuid)

    # ################## Append ##################

    def test_uuid_transfer_append(self):
        u = U()
        self.lst.append(u)
        self.assertEqual("uuid", u._uuid)

    def test_uuid_transfer_append_nested(self):
        self.lst.append(UuidList('not-uuid', (U(),)))
        self.lst.append([U()])
        for lst in self.lst:
            self.assertEqual("uuid", lst.uuid)
            for e in lst:
                self.assertEqual("uuid", e._uuid)

    # ################## Extend ##################

    def test_uuid_transfer_extend(self):
        lst = [U(), U(), U()]
        self.lst.extend(lst)
        for u in self.lst:
            self.assertEqual("uuid", u._uuid)

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
            self.assertEqual("uuid", lst.uuid)
            for e in lst:
                self.assertEqual("uuid", e._uuid)

    # ################## Insert ##################

    def test_uuid_transfer_insert(self):
        u = U()
        self.lst.insert(0, u)
        self.assertEqual("uuid", u._uuid)

    def test_uuid_transfer_insert_nested(self):
        self.lst.insert(0, UuidList('not-uuid3', (U(),)))
        self.lst.insert(0, (U(),))
        for lst in self.lst:
            self.assertEqual("uuid", lst.uuid)
            for e in lst:
                self.assertEqual("uuid", e._uuid)

    # ################## __setitem__ ##################

    def test_uuid_transfer_setitem_single(self):
        u = U()
        self.lst.extend((U(), U(), U()))
        self.lst[1] = u
        self.assertEqual("uuid", u._uuid)

    def test_uuid_transfer_setitem_single_nested(self):
        self.lst.extend(((U(), U(), U()), (U(), U(), U())))

        self.lst[0] = (U(), U(), U())
        self.lst[1][2] = U()

        for lst in self.lst:
            self.assertEqual("uuid", lst.uuid)
            for e in lst:
                self.assertEqual("uuid", e._uuid)

    def test_uuid_transfer_setitem_slice(self):
        self.lst.extend((U(), U(), U()))

        self.lst[1:3] = (U(), U())
        for u in self.lst:
            self.assertEqual("uuid", u._uuid)

    def test_uuid_transfer_setitem_slice_nested(self):
        self.lst.extend((
            (U(), U(), U()),
            (U(), U(), U()),
            (U(), U(), U()),
            (U(), U(), U())
        ))

        self.lst[1:3] = ((U(), U()), (U(), U()))
        for lst in self.lst:
            self.assertEqual("uuid", lst.uuid)
            for e in lst:
                self.assertEqual("uuid", e._uuid)

    # ################## __setitem__ Callback Entry ##################

    def test_uuid_transfer_init_callback_entry(self):
        def set_other(e):
            e.other = 11

        self.lst = UuidList("uuid", on_update_execute_entry=set_other)
        self.lst.append(U())

        self.assertEqual("uuid", self.lst[0]._uuid)
        self.assertEqual(11, self.lst[0].other)

    def test_uuid_transfer_init_callback_list(self):
        def set_other(lst):
            for i, e in enumerate(lst):
                e.other = i

        self.lst = UuidList("uuid", on_update_execute_list=set_other)
        self.lst.extend((U(), U(), U(), U(), U(), U()))

        for index, entry in enumerate(self.lst):
            self.assertEqual("uuid", entry._uuid)
            self.assertEqual(index, entry.other)

    def test_uuid_transfer_init_callback_entry_nested(self):
        def set_nested(e):
            e.values.uuid = e._uuid

        self.lst = UuidList("uuid", on_update_execute_entry=set_nested)
        self.lst.append(NU())

        self.assertEqual("uuid", self.lst[0]._uuid)
        self.assertEqual("uuid", self.lst[0].values[0]._uuid)
        self.assertEqual("uuid", self.lst[0].values[1]._uuid)
        self.assertEqual("uuid", self.lst[0].values[2]._uuid)
