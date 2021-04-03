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


def update_order_array(order_array, supposed_length):
    for i in range(supposed_length):
        if i not in order_array:
            order_array.append(i)
