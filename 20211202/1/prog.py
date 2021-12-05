from functools import wraps

class dump(type):
    def __init__(self, name, parents, ns):
        for f_name, f in filter(lambda x: callable(x[1]), ns.items()):
            @wraps(f)
            def my_f(self, *args, f=f, f_name=f_name, **kwargs):
                print(f"{f_name}: {args}, {kwargs}")
                return f(self, *args, **kwargs)
            setattr(self, f_name, my_f)
        return super().__init__(name, parents, ns)

import sys
exec(sys.stdin.read())
