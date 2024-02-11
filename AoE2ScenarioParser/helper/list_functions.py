from typing import List, Any, Generator, Iterator

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


# Written by: Ned Batchelder @ https://stackoverflow.com/a/312464/7230293
def list_chunks(list_: List[T], n: int) -> Iterator[List[T]]:
    """Yield successive n-sized chunks from given list"""
    for i in range(0, len(list_), n):
        yield list_[i:i + n]
