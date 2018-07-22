"""
一种unpacking iterable的方法：
获取个别元素，用前缀*符号的变量获取剩余元素列表

"""


if __name__ == '__main__':
    a, b, *c, d, e = range(5)
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
