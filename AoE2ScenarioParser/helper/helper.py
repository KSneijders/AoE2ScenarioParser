def update_order_array(order_array, supposed_length):
    for i in range(0, supposed_length):
        if i not in order_array:
            order_array.append(i)


def create_textual_hex(string, space_distance=2, enter_distance=48):
    """Please note that the 'enter_distance' parameter is including the - to be added - spaces. If you calculated it
    without the spaces, please multiply the number by: `block size incl space / block size excl space`"""
    return insert_char(insert_char(string, " ", space_distance), "\n", enter_distance)


# Credits: gurney alex @ https://stackoverflow.com/a/2657733/7230293
def insert_char(string, char, every=64):
    return char.join(string[i:i + every] for i in range(0, len(string), every))


def del_str_trail(string):
    return string.replace('\x00', "")


def pretty_print_list(plist):
    return_string = "[\n"
    for x in plist:
        return_string += "\t" + str(x)
    return return_string + "]\n"


def add_prefix_chars(string, char, length):
    if len(string) > length:
        return string
    else:
        return char * (length - len(string)) + string


def add_suffix_chars(string, char, length):
    if len(string) > length:
        return string
    else:
        return string + char * (length - len(string))
