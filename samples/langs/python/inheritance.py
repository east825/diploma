from contextlib import contextmanager
import traceback


@contextmanager
def attr_test():
    try:
        yield
    except AttributeError:
        print(traceback.format_exc())


class C:
    @staticmethod
    def foo():
        return 'Method foo found in hierarchy'


class B(C):
    pass


class MetaB(type):
    def foo(cls):
        return 'Method foo resolved by metaclass'

    def __getattr__(cls, item):
        if item == 'bar':
            return lambda: 'Method not found in hierarchy and resolved by __getattr__ in metaclass'
        raise AttributeError()


class MetaA(MetaB):
    def baz(cls):
        return 'Method bar found in metaclass'


class A(B, metaclass=MetaA):
    def __getattr__(self, item):
        if item == 'bar':
            return lambda: 'Method not found in hierarchy and resolved by __getattr__'
        raise AttributeError()


# For instance: instance -> class -> super classes -> __getattr__ (if any)
# For classes: class -> super classes -> metaclass -> metaclass' __getattr__ (if any)
if __name__ == '__main__':
    inst = A()
    # Found in hierarchy
    with attr_test():
        print(A.foo())
    # Found in hierarchy
    with attr_test():
        print(inst.foo())
    # Not found in hierarchy and *not* resolved by __getattr__
    with attr_test():
        print(A.bar())
    # Not found in hierarchy and resolved by __getattr__
    with attr_test():
        print(inst.bar())
    # Found in metaclass
    with attr_test():
        print(A.baz())
    # Not found at all
    with attr_test():
        print(inst.baz())