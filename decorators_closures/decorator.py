def deco(func):
    def inner():
        print('inner')

    return inner


@deco
def target():
    print('target')


target()

import time
from clockdeco_param import clock


@clock()
def snooze(seconds):
    time.sleep(seconds)


@clock()
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


@clock(fmt='{elapsed}|{name}({arg_str})|{result}')
def haha(x, y, a=1, b=2, c=3):
    print('haha')
    print(x, y, a, b, c)


if __name__ == '__main__':
    # print('*' * 40, 'Calling snooze(.123)')
    # snooze(.123)
    # print('*' * 40, 'Calling factorial(6)')
    # print('6! = ', factorial(6))
    print(haha(1, y=3))
