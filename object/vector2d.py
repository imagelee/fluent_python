from array import array
import math


class Vector2d:

    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    """__iter__ makes a Vector2d iterable; this is what makes unpacking work (e.g, x, y = my_vector). """
    def __iter__(self):
        return (i for i in (self.__x, self.__y))

    def __str__(self):
        return str(tuple(self))

    """__repr__ builds a string by interpolating the components with {!r} to get their repr; 
    because Vector2d is iterable, *self feeds the x and y components to format.
    In str.format, !s chooses to use str to format the object whereas !r chooses repr to format the value."""
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.__x, self.__y)

    def __bool__(self):
        return bool(abs(self))

    """The built-in memorview class is a shared-memory sequence type that lets you handle slices of arrays without copying bytes."""
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    """use own format function, and define 'p' for polar coordinates."""
    def __format__(self, format_spec=''):
        if format_spec.endswith('p'):
            format_spec = format_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, format_spec) for c in coords)
        return outer_fmt.format(*components)

    def angle(self):
        return math.atan2(self.__y, self.__x)


class ShortVector2d(Vector2d):

    typecode = 'f'


if __name__ == '__main__':

    vec = Vector2d(3,4)
    print('{!r}'.format(vec))
    print(vec == (3,4))

    octets = bytes(vec)
    print(octets)
    print(str(vec))

    vec1 = Vector2d.frombytes(octets)
    print(vec1)
    print(id(vec))
    print(id(vec1))

    print(format(vec, '0.5f'))
    print(format(vec, '0.5fp'))

    s_vec = ShortVector2d(3, 4)
    short_octets = bytes(s_vec)
    print(short_octets)
    print('{!r}'.format(s_vec))
