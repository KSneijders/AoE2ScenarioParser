def create_generator(uncompressed_file, chunk_size=4):
    for x in range(0, len(uncompressed_file), chunk_size):
        yield uncompressed_file[x:x + chunk_size]


def repeat_generator(generator, run_times, return_bytes=True):
    elements = b'' if return_bytes else []

    for i in range(0, run_times):
        if return_bytes:
            elements += next(generator)
        else:
            # Generator returns list. So lists are merged
            elements += next(generator)

    return elements
