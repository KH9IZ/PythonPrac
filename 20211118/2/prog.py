class Num:
    def __get__(self, obj, cls):
        return getattr(obj, 'val', 0)
    def __set__(self, obj, val):
        if getattr(val, 'real', None) is not None:
            obj.val = val
        elif getattr(val, '__len__', None) is not None:
            obj.val = len(val)
