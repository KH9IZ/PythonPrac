class Alpha:
    __slots__ = [chr(i) for i in range(ord('a'), ord('z')+1)]

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    def __str__(self):
        return ", ".join(f"{k}: {getattr(self, k)}" for k in self.__slots__ if hasattr(self, k))

class AlphaQ:
    vals = {}

    def __setattr__(self, name, value):
        self.vals[name] = value

    def __getattr__(self, name):
        try:
            return self.vals[name]
        except KeyError:
            raise AttributeError
    
    def __init__(self, **kwargs):
        self.vals.update(kwargs)

    def __str__(self):
        return ", ".join(f"{i}: {j}" for i, j in sorted(self.vals.items()))
            

import sys
exec(sys.stdin.read())

