import uuid
from unittest import TestCase

from AoE2ScenarioParser.objects.support.uuid_list import UuidList


# Todo: REMOVE BEFORE V1 RELEASE


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
        self._uuid = uuid.uuid4()
        self.values = UuidList(self._uuid, (U(), U(), U()))

    def __repr__(self):
        return f"u'{self._uuid}'"

class TestUuidList(TestCase):
    lst: UuidList

    def setUp(self) -> None:
        self._uuid = uuid.uuid4()
        self.lst = UuidList(self._uuid)

    def test_uuid_transfer_init(self):
        self.lst = UuidList(self._uuid, (U(),))

        self.assertEqual(self._uuid, self.lst[0]._uuid)

    def test_uuid_transfer_init_nested(self):
        self.lst = UuidList(self._uuid, ((U(), U(),), (U(), U(),)))

        for lst in self.lst:
            self.assertEqual(self._uuid, lst.uuid)
            for e in lst:
                self.assertEqual(self._uuid, e._uuid)

    # ################## Append ##################

    def test_uuid_transfer_append(self):
        u = U()
        self.lst.append(u)
        self.assertEqual(self._uuid, u._uuid)

    def test_uuid_transfer_append_nested(self):
        self.lst.append(UuidList(uuid.uuid4(), (U(),)))
        self.lst.append([U()])
        for lst in self.lst:
            self.assertEqual(self._uuid, lst.uuid)
            for e in lst:
                self.assertEqual(self._uuid, e._uuid)

    # ################## Extend ##################

    def test_uuid_transfer_extend(self):
        lst = [U(), U(), U()]
        self.lst.extend(lst)
        for u in self.lst:
            self.assertEqual(self._uuid, u._uuid)

    def test_uuid_transfer_extend_nested(self):
        self.lst.extend(
            UuidList(uuid.uuid4(), (
                UuidList(uuid.uuid4(), (U(),)),
                UuidList(uuid.uuid4(), (U(),))
            ))
        )
        self.lst.extend([(U(),), (U(),)])
        self.lst.extend([(U(),), UuidList(uuid.uuid4(), (U(),))])

        for lst in self.lst:
            self.assertEqual(self._uuid, lst.uuid)
            for e in lst:
                self.assertEqual(self._uuid, e._uuid)

    # ################## Insert ##################

    def test_uuid_transfer_insert(self):
        u = U()
        self.lst.insert(0, u)
        self.assertEqual(self._uuid, u._uuid)

    def test_uuid_transfer_insert_nested(self):
        self.lst.insert(0, UuidList(uuid.uuid4(), (U(),)))
        self.lst.insert(0, (U(),))
        for lst in self.lst:
            self.assertEqual(self._uuid, lst.uuid)
            for e in lst:
                self.assertEqual(self._uuid, e._uuid)

    # ################## __setitem__ ##################

    def test_uuid_transfer_setitem_single(self):
        u = U()
        self.lst.extend((U(), U(), U()))
        self.lst[1] = u
        self.assertEqual(self._uuid, u._uuid)

    def test_uuid_transfer_setitem_single_nested(self):
        self.lst.extend(((U(), U(), U()), (U(), U(), U())))

        self.lst[0] = (U(), U(), U())
        self.lst[1][2] = U()

        for lst in self.lst:
            self.assertEqual(self._uuid, lst.uuid)
            for e in lst:
                self.assertEqual(self._uuid, e._uuid)

    def test_uuid_transfer_setitem_slice(self):
        self.lst.extend((U(), U(), U()))

        self.lst[1:3] = (U(), U())
        for u in self.lst:
            self.assertEqual(self._uuid, u._uuid)

    def test_uuid_transfer_setitem_slice_nested(self):
        self.lst.extend((
            (U(), U(), U()),
            (U(), U(), U()),
            (U(), U(), U()),
            (U(), U(), U())
        ))

        self.lst[1:3] = ((U(), U()), (U(), U()))
        for lst in self.lst:
            self.assertEqual(self._uuid, lst.uuid)
            for e in lst:
                self.assertEqual(self._uuid, e._uuid)

    # ################## __setitem__ Callback Entry ##################

    def test_uuid_transfer_init_callback_entry(self):
        def set_other(e):
            e.other = 11

        self.lst = UuidList(self._uuid, on_update_execute_entry=set_other)
        self.lst.append(U())

        self.assertEqual(self._uuid, self.lst[0]._uuid)
        self.assertEqual(11, self.lst[0].other)

    def test_uuid_transfer_init_callback_list(self):
        def set_other(lst):
            for i, e in enumerate(lst):
                e.other = i

        self.lst = UuidList(self._uuid, on_update_execute_list=set_other)
        self.lst.extend((U(), U(), U(), U(), U(), U()))

        for index, entry in enumerate(self.lst):
            self.assertEqual(self._uuid, entry._uuid)
            self.assertEqual(index, entry.other)

    def test_uuid_transfer_init_callback_entry_nested(self):
        def set_nested(e):
            e.values.uuid = e._uuid

        self.lst = UuidList(self._uuid, on_update_execute_entry=set_nested)
        self.lst.append(NU())

        self.assertEqual(self._uuid, self.lst[0]._uuid)
        self.assertEqual(self._uuid, self.lst[0].values[0]._uuid)
        self.assertEqual(self._uuid, self.lst[0].values[1]._uuid)
        self.assertEqual(self._uuid, self.lst[0].values[2]._uuid)
