


from functools import reduce



def fact(n):
    return reduce(lambda a,b : a * b, range(1, n+1))


print(fact(10))

from operator import mul
from functools import partial
triple = partial(mul, 3)

print(triple(7))