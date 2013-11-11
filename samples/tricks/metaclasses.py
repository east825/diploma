import time
import logging
import __builtin__

logging.basicConfig(level=logging.DEBUG)


def logged(func):
    def wrapper(*args, **kwargs):
        start = time.clock()
        res = func(*args, **kwargs)
        logging.debug('{} executed for {:.2f}us'.format(func.__name__, (time.clock() - start) * 10 ** 6))
        return res

    return wrapper


class LoggingMetaclass(type):
    def __new__(cls, class_name, bases, attrs):
        for name, value in attrs.items():
            if callable(value):
                attrs[name] = logged(value)
        return super(LoggingMetaclass, cls).__new__(cls, class_name, bases, attrs)

    def __setattr__(self, name, value):
        if callable(value):
            value = logged(value)
        return super(LoggingMetaclass, self).__setattr__(name, value)


#__builtin__.type = LoggingMetaclass
__builtins__.type = LoggingMetaclass

class MyClass(object):
    __metaclass__ = LoggingMetaclass

    def foo(self):
        pass


if __name__ == '__main__':
    def fib(self, n):
        if n in (0, 1):
            return n
        return fib(self, n - 2) + fib(self, n - 1)

    MyClass.fib = fib
    inst = MyClass()
    inst.foo()
    inst.fib(30)