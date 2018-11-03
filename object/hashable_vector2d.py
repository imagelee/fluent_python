class Vector2d:

    __slots__ = ('__x', '__y')

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    """The @property decorator marks the getter method of a property."""
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)


if __name__ == '__main__':
    v1 = Vector2d(3, 4)
    v2 = Vector2d(3.1, 6.2)
    print(hash(v1), hash(v2))
    s = {v1, v2}
    print(s)

