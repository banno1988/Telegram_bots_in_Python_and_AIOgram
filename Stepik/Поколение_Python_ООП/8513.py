def singleton(cls):
    cls._ins = None
    def new_new(*args, **kwargs):
        if cls._ins is None:
            cls._ins = object.__new__(cls)
        return cls._ins
    cls.__new__=new_new
    return cls

