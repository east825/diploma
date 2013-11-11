class Bunch(dict):
    def __init__(self, *args, **kwargs):
        super(Bunch, self).__init__(*args, **kwargs)
        self.__dict__ = self

    def __str__(self):
        attrs = ', '.join('{}={!r}'.format(k, v) for k, v in vars(self).items())
        return 'Bunch({})'.format(attrs)


if __name__ == '__main__':
    bunch = Bunch(foo='bar', baz=[42, 'quux', None])
    bunch.ham = 'spam'
    print bunch, bunch['foo']



