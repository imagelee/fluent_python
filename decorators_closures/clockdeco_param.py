"""A simple decorator to output the running time of functions"""
import time
import functools

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({arg_str}) -> {result}'

def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        @functools.wraps(func)
        def clocked(*args, **kwargs):
            t0 = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            arg_lst = []
            if args:
                arg_lst.append(','.join(repr(arg) for arg in args))
            if kwargs:
                pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
                arg_lst.append(','.join(pairs))

            arg_str = ','.join(arg_lst)
            print(fmt.format(**locals()))
            return result
        return clocked
    return decorate

