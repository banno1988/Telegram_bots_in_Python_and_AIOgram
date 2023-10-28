import functools


class type_check:
    def __init__(self, types):
        self.types = types

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in zip(self.types, args):
                if not isinstance(i[1], i[0]):
                    raise TypeError
            return func(*args, **kwargs)

        return wrapper
