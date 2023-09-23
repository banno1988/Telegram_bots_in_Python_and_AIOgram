from collections import UserList

class NumberList(UserList):
    def __init__(self,iterable=[]):
        super().__init__()
        for i in iterable:
            self.check(i)
            self.data.append(i)
    def __setitem__(self, key, value):
        self.check(value)
        if key:
            self.data[key]=value
        else:
            self.data.append(value)
    def append(self, item):
        self.check(item)
        self.data.append(item)
    @staticmethod
    def check(n):
        if not isinstance(n, (int,float)):
            raise TypeError("Элементами экземпляра класса NumberList должны быть числа")
        return n

    def __add__(self, other):
        return super().__add__(self.check(i) for i in other)

    __radd__ = __iadd__ = __add__
    
    def insert(self, i, item):
        self.check(item)
        super().insert(i,item)
    def extend(self, item):
        super().extend(self.check(i) for i in item)