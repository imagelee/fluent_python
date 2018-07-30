class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        # bug:RecursionError: maximum recursion depth exceeded while calling a Python object
        # return key in self
        return key in self.keys() or str(key) in self.keys()


import collections


class StrKeyDict(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, item):
        return str(item) in self.keys()

    def __setitem__(self, key, value):
        self.data[str(key)] = value


d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(2 in d)
