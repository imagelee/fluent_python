from functools import singledispatch
from collections import abc
import numbers
import html


@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<p>{0}</p>'.format(content)


@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)


@htmlize.register(numbers.Integral)
def _(n):
    return '<p>{0} (0x{0:x})</p>'.format(n)


@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '<li>\n</li>'.join(htmlize(item) for item in seq)
    return '<ul>\n</li>' + inner + '<li>\n<ul>'

print(htmlize(['alpha', 66, {3,2,1}]))
