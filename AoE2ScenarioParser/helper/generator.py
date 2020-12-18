from AoE2ScenarioParser.helper import helper


def create_generator(uncompressed_file, chunk_size=4):
    for x in range(0, len(uncompressed_file), chunk_size):
        yield uncompressed_file[x:x + chunk_size]


def repeat_generator(generator, run_times, intended_stop_iteration=False, return_bytes=True):
    elements = b'' if return_bytes else []

    try:
        for i in range(0, run_times):
            if return_bytes:
                elements += next(generator)
            else:
                # Generator returns list. So lists are merged
                elements += next(generator)
    except StopIteration as e:
        if not intended_stop_iteration:
            print(f"\n\n[StopIteration] in repeat_generator while retrieving {run_times} bytes.")
        raise e
    return elements
