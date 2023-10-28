def auto_repr(args, kwargs):
    def wrapper(cls):
        def repra(self):
            a = [repr(getattr(self, i)) for i in args]
            b = [str(i) +'='+ repr(getattr(self, i)) for i in kwargs]
            c=a+b
            return f"{cls.__name__}({', '.join(c)})"
        cls.__repr__ = repra
        return cls

    return wrapper
