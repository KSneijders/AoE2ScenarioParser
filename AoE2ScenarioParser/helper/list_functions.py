from typing import List


def hash_list(lst: list):
    return hash(tuple(lst))


def list_changed(lst, lst_hash):
    return lst_hash != hash(tuple(lst))


def listify(var) -> list:
    """Always return item as list"""
    if type(var) is list:
        return var
    else:
        return [var]


def update_order_array(order_array: List[int], supposed_length: int) -> None:
    """
    Update an order array.

    Args:
        order_array (List[int]): The order array like trigger.condition_order
        supposed_length (int): The length the array should be

    """
    actual_length = len(order_array)

    if actual_length > supposed_length:
        for i in range(supposed_length, actual_length):
            order_array.remove(i)
    elif supposed_length > actual_length:
        for i in range(supposed_length):
            if i not in order_array:
                order_array.append(i)
