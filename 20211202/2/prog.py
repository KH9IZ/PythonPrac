from __future__ import annotations
import sys
import typing

class check(type):
    def __init__(self, name, parents, ns):
        def check_annotations(self):
            annot = typing.get_type_hints(self, globalns=globals(), localns=ns)
            for name in annot:
                if not hasattr(self, name) or not issubclass(type(getattr(self, name)), annot[name]):
                    return False
            return True
        setattr(self, 'check_annotations', check_annotations)

exec(sys.stdin.read())
