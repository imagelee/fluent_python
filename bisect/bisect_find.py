import bisect
import sys

HAYSTACK = [1, 4, 5, 6]
NEEDLES = [0, 1, 2, 5]

ROW_FIT = '{0:2d} @ {1:2d}  {2}{0:<2d}'

def demo(bisect_fn):
    """
    bisect finds insertion points for items in a sorted sequence.
    :param bisect_fn:
    :return:
    """
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '   |'
        print(ROW_FIT.format(needle, position, offset))

if __name__ == '__main__':

    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)
    print(HAYSTACK)
