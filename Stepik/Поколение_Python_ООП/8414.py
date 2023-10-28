import functools


class exception_decorator:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            a = self.func(*args, **kwargs)
            return (a, None)
        except Exception as err:
            return (None, type(err))
