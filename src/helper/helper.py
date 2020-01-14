def update_order_array(order_array, supposed_length):
    for i in range(0, supposed_length):
        if i not in order_array:
            order_array.append(i)
