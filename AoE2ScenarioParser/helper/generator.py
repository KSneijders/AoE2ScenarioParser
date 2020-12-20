
def create_generator(uncompressed_file: bytes):
    # Currently below commented code returns ints instead of bytes.
    # Changes proposed on PEP 467 seem exactly what is needed.
    # Unfortunately it doesn't look like those will be implemented anytime soon.
    # PEP 467: https://www.python.org/dev/peps/pep-0467/
    #
    # for x in uncompressed_file:  # To be added into Python: `bytes.iterbytes()`
    #     yield x
    for i in range(len(uncompressed_file)):
        yield uncompressed_file[i:i + 1]


def create_advanced_generator(uncompressed_file, chunk_size=4):
    for x in range(0, len(uncompressed_file), chunk_size):
        yield uncompressed_file[x:x + chunk_size]


def repeat_generator(generator, run_times, intended_stop_iteration=False, return_bytes=True):
    elements = []

    try:
        for i in range(0, run_times):
            elements.append(next(generator))
    except StopIteration as e:
        if not intended_stop_iteration:
            print(f"\n\n[StopIteration] in repeat_generator while retrieving {run_times} bytes.")
        raise e
    return b''.join(elements) if return_bytes else elements
