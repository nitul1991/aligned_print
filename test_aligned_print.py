

import aligned_print
import io


def test_basic():
    output = io.StringIO()
    print_function = lambda msg: output.write(f'{msg}\n')
    with aligned_print.printer(print_function) as print_:
        print_('a', 'a')
        print_('bb', 'b')
        print_('ccc', 'c')
        print_('dddd', 'd')
        print_('eeeee', 'e')

    expected = """
a     => a
bb    => b
ccc   => c
dddd  => d
eeeee => e
"""
    assert(output.getvalue().strip('\n') == expected.strip('\n'))


def test_attribute_printing():
    output = io.StringIO()
    print_function = lambda msg: output.write(f'{msg}\n')

    class Foo(object):
        def __init__(self):
            self.name = 'foo'
            self.id   = 10
            self.age  = 29

    with aligned_print.printer(print_function) as print_:
        foo = Foo()
        list(map(lambda pair: print_(pair[0], pair[1]), foo.__dict__.items()))

    expected = """
name => foo
id   => 10
age  => 29
"""
    assert(output.getvalue().strip('\n') == expected.strip('\n'))


def test_empty_with_statement():
    with aligned_print.printer() as print_:
        pass
