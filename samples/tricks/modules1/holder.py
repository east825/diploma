CONSTANT = 'Spam!'


def dump_constant(constant, module=__name__):
    print 'In module {!r}: CONSTANT = {!r}'.format(module, constant)


if __name__ == '__main__':
    import sys

    sys.modules['holder'] = sys.modules['__main__']

    dump_constant(CONSTANT, 'holder')
    import modifier

    dump_constant(CONSTANT, 'holder')