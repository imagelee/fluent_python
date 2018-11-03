
class Dog:

    __slots__ = ('__mood')

    def __init__(self):
        self.__mood = None

class Beagle(Dog):

    __slots__ = ('what', '__mood')

    def __init__(self):
        super().__init__()
        self.__mood = None
        self.what = 2

dog = Dog()
beagle = Beagle()

print(dog._Dog__mood)
print(beagle._Beagle__mood)
print(beagle.what)
