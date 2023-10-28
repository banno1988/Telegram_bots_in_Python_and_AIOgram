def limiter(limit, unique, lookup):
    def wrapper(cls):
        cls.t = {}

        def qwetr(*args, **kwargs):
            o = cls(*args, **kwargs)
            a = getattr(o, unique)
            if len(cls.t) < limit:
                if a in cls.t:
                    return cls.t[a]
                else:
                    cls.t[a] = o
                    return o
            elif a in cls.t:
                return cls.t[a]
            elif lookup == 'FIRST':
                return cls.t[list(cls.t.keys())[0]]
            elif lookup == 'LAST':
                return cls.t[list(cls.t.keys())[-1]]

        return qwetr

    return wrapper
