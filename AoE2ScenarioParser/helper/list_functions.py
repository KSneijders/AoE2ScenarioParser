from typing import List, Any


def hash_list(lst: List):
    return hash(tuple(lst))


def list_changed(lst, lst_hash):
    return lst_hash != hash(tuple(lst))


def listify(var: Any) -> List[Any]:
    """Always return item as list"""
    return var if type(var) is list else [var]


def update_order_array(order_array: List[int], supposed_length: int) -> None:
    """
    Update an order array.

    Args:
        order_array: The order array like trigger.condition_order
        supposed_length: The length the array should be

    """
    actual_length = len(order_array)

    if actual_length > supposed_length:
        order_array[:] = [x for x in order_array if x < supposed_length]
    elif supposed_length > actual_length:
        order_array.extend(i for i in range(actual_length, supposed_length))


def remove_from_order_array(order_array: List[int], index: int) -> None:
    """
    Remove an index from an order array and shift all higher indices down by one, keeping the order intact.

    Args:
        order_array: The order array like trigger.condition_order
        index: The index of the removed element in its list (not its position in the order array)
    """
    order_array[:] = [i - 1 if i > index else i for i in order_array if i != index]


# Written by: Ned Batchelder @ https://stackoverflow.com/a/312464/7230293
def list_chuncks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
