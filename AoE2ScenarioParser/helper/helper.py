def update_order_array(order_array, supposed_length):
    for i in range(0, supposed_length):
        if i not in order_array:
            order_array.append(i)


def create_readable_hex_string(string):
    return insert_char(insert_char(string, " ", 2), "\n", 48)


# Credits: gurney alex @ https://stackoverflow.com/a/2657733/7230293
def insert_char(string, char, every=64):
    return char.join(string[i:i + every] for i in range(0, len(string), every))