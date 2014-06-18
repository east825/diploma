# vim: fileencoding=utf-8

class MyClass(object):
    def method(self):
        print('Success')
#
# inst = FooClass()
# inst.bar() # ошибка AttributeError
#
#
# class BarClass(object):
#     def bar(self):
#         pass
#
#
# def condition_holds():
#     return True
#
# if condition_holds():
#     inst = BarClass() # определяет метод bar()
# else:
#     inst = FooClass()
#
# inst.bar()

class MyClass(object):
    def method(self):
        print('Success')

inst = MyClass()

inst.missing()

getattr(inst, ''.join(['m', chr(105), 'ssing']))()

exec('inst' + '.missing()')

del MyClass.method
inst.method()

from pathlib import Path

def python_modules(dir_path:str, extension='.py'):
    """Returns list of Python modules in directory.

    :type extension: str
    :type dir_path: str
    :rtype: list[str]
    """
    assert isinstance(extension, str)

    p = Path(dir_path)
    result = []
    for child in p.iterdir():
        if child.is_file() and child.suffix == extension:
            result.append(str(child))
    return result

def sanitize_url(url):
    sanitized = url.lower()
    if url.endswith('/'):
        sanitized = sanitized[:-1]
    return sanitized