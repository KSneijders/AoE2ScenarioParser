import itertools
from typing import Any, Iterable, List

from typing_extensions import Generator

from AoE2ScenarioParser.objects.support.typedefs import T


def hash_list(list_: List) -> int:
    return hash(tuple(list_))


def list_changed(list_: List[Any], lst_hash) -> bool:
    return lst_hash != hash(tuple(list_))


def listify(value: T) -> List[T]:
    """Always return item as list"""
    return value if isinstance(value, list) else [value]


def update_order_array(order_array: List[int], supposed_length: int) -> None:
    """
    Update an order array.

    Remove all IDs which are out of the range or add all missing IDs

    Args:
        order_array: The order array like trigger.condition_order
        supposed_length: The length the array should be
    """
    actual_length = len(order_array)

    if actual_length > supposed_length:
        for i in range(supposed_length, actual_length):
            order_array.remove(i)
    elif supposed_length > actual_length:
        for i in range(supposed_length):
            if i not in order_array:
                order_array.append(i)


def list_chunks(iterable: Iterable[T], n: int):
    return list(list(item) for item in chunk(iterable, n))


def tuple_chunks(iterable: Iterable[T], n: int):
    return tuple(tuple(item) for item in chunk(iterable, n))


# Todo: Replace entire function by itertools.batched() when on PY 3.12
def chunk(it: Iterable[T], n: int) -> Generator[Iterable[T], Any, None]:
    it = iter(it)

    while (nxt := next(it, None)) is not None:
        yield itertools.islice(itertools.chain([nxt], it), n)
