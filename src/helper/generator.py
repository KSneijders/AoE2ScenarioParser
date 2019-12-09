def create_file_generator(uncompressed_file, chunk_size=4):
    for x in range(0, len(uncompressed_file), chunk_size):
        yield uncompressed_file[x:x + chunk_size]


def repeat_generator(generator, run_times):
    byte_elements = b''
    for i in range(0, run_times):
        byte_elements += next(generator)

    return byte_elements
