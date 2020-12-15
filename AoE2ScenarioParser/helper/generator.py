
def create_generator(uncompressed_file):
    for x in uncompressed_file:
        yield bytes(x)


def create_advanced_generator(uncompressed_file, chunk_size=4):
    for x in range(0, len(uncompressed_file), chunk_size):
        yield uncompressed_file[x:x + chunk_size]


def repeat_generator(generator, run_times, intended_stop_iteration=False, return_bytes=True):
    elements = b'' if return_bytes else []

    try:
        for i in range(0, run_times):
            elements += next(generator)
    except StopIteration as e:
        if not intended_stop_iteration:
            print(f"\n\n[StopIteration] in repeat_generator while retrieving {run_times} bytes.")
        raise e
    return elements
