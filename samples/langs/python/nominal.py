def ecd(x, y):
    while x != 0:
        x, y = y % x, x
    return y


class Rational:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError('Denominator can not be null')
        self.x = denominator
        self.y = numerator
        self.simplify()

    def __mul__(self, other):
        return Rational(self.x * other.x, self.y * other.y)

    def __int__(self):
        return int(self.x // self.x)

    def simplify(self):
        factor = ecd(self.x, self.y)
        self.x //= factor
        self.y //= factor

    def __str__(self, *args, **kwargs):
        self.simplify()
        return '{:d}/{:d}'.format(self.x, self.y)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class TextRange:
    def __init__(self, x, y):
        if y < x or x < 0:
            raise ValueError('Illegal range: must be y >= x && x >= 0')
        self.x = x
        self.y = y


if __name__ == '__main__':
    TextRange(3, 3)