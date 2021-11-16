

import contextlib
import logging


@contextlib.contextmanager
def printer(print_function=print, separator=" => "):
    """A context manager that prints key value pairs, with the keys being
    printed with a fixed width that is equal to the width of the longest key
    """
    key_values = []
    def printer_impl(key, value):
        key_values.append((key, value))

    try:
        yield printer_impl
    finally:
        if key_values:
            max_key_width = max(map(lambda kv: len(kv[0]), key_values))
            for key, value in key_values:
                print_function(f'{key:{max_key_width}}{separator}{value}')
