

import contextlib
import logging


@contextlib.contextmanager
def printer(print_function=print):
    """A context manager that prints key value pairs, with the keys being
    printed with a fixed width that is equal to the width of the longest key
    """
    keys   = []
    values = []
    def printer_impl(key, value):
        keys.append(key)
        values.append(value)

    try:
        yield printer_impl
    finally:
        if keys:
            max_key_width = max(map(len, keys))
            for key, value in zip(keys, values):
                print_function(f'{key:{max_key_width}} => {value}')
