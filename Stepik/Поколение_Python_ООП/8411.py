import functools


class MaxCallsException(Exception):
    pass


class limited_calls:
    def __init__(self, n):
        self.n = n
        self.t = 0

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if self.t < self.n:
                self.t += 1
                return func(*args, **kwargs)

            else:
                raise MaxCallsException('Превышено допустимое количество вызовов')
        return wrapper

