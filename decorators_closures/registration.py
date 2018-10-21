registry = []

"""
1. A real decorator is usually defined in one module and applied to functions in other modules.
2. In practice, most decorators define an inner function and return it.
"""
def register(func):
    print('register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('f1')


@register
def f2():
    print('f2')


def f3():
    print('f3')


def main():
    print('main')
    print('registry ->', registry)
    f1()
    f2()
    f3()


if __name__ == '__main__':
    main()
