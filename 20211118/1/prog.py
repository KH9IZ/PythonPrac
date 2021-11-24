def objcount(cls):
    cls.counter = 0
    
    def init_gen(old):
        def __init__(self, *args, old=old, **kwargs):
            type(self).counter += 1
            old(self, *args, **kwargs)
        return __init__
    cls.__init__ = init_gen(cls.__init__)

    def del_gen(old):
        def __del__(self, old=old):
            if callable(old):
                old(self)
            type(self).counter -= 1
        return __del__
    cls.__del__ = del_gen(getattr(cls, '__del__', None))

    return cls

import sys
exec(sys.stdin.read())
