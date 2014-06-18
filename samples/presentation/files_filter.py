import os
from pathlib import Path

def python_modules(dir_path:str, extension='.py'):
    """Returns list of Python modules in directory.

    :type extension: str
    :type dir_path: str
    :rtype: list[str]
    """
    p = Path(dir_path)
    result = []
    for child in p.iterdir():
        if child.is_file() and child.suffix == extension:
            result.append(str(child))
    return result


if __name__ == '__main__':
    print(python_modules(os.getcwd()))

