import functools

class takes_numbers:
    def __init__(self, func):
        functools.update_wrapper(self,func)
        self.func=func

    def __call__(self, *args, **kwargs):
        for i in args:
            if not isinstance(i,(int, float)):
                raise TypeError('Аргументы должны принадлежать типам int или float')

        for i in kwargs:
            if not isinstance(kwargs[i],(int, float)):
                raise TypeError('Аргументы должны принадлежать типам int или float')

        return self.func(*args,**kwargs)