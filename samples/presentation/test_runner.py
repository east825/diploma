from __future__ import print_function
import sys
import traceback


def run_tests(module_name):
    module = __import__(module_name)
    for name, attr in vars(module).items():
        if name.startswith('test_') and callable(attr):
            try:
                attr()
            except AssertionError:
                print('Error in function {!r}'.format(name), file=sys.stderr)
                traceback.print_exc()


if __name__ == '__main__':
    run_tests('foo')
