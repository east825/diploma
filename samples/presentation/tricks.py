# vim: fileencoding=utf-8

import random
import string


# Предположим int -> bool
from datetime import datetime


def is_even(x):
    return x % 2 == 0

# Предположим str -> str
def slugify(s):
    allowed = set(string.ascii_lowercase) | set(string.digits) | {'-', '_'}
    s = '-'.join(s.lower().split())
    return ''.join(c for c in s if c in allowed)

# Предположим str -> str
def reverse(s):
    return ''.join(reversed(s))

# Предположим str -> int
def vowels(s):
    return sum(c in 'aeiouy' for c in s.lower())

funcs = [is_even, slugify]
# ? -> ?
f = random.choice(funcs)

xs = [1, None, 'spam!', []]
# Допустимо?
xs[-1].append(42)
# А теперь?
sorted(xs).append(42)


class TheMachine:
    def meaning_of_life(self):
        return 42

m = TheMachine()
print(m.meaning_of_life > 40)
m.meaning_of_life = lambda: 'Ham'
print(hex(m.meaning_of_life()))


def func():
    return 'string'


exec('def func(): return None')

func().capitalize()

xs = True if [1, None, 'foo'][3].startswith('bar') else max
print(xs('quux', datetime.now()))

if __name__ == '__main__':
    print(slugify('foo bar __bAZ!@!32#'))
