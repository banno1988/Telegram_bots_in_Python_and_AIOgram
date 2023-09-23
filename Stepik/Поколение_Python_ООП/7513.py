from abc import ABC, abstractmethod
class Validator(ABC):

    @abstractmethod
    def validate(self,obj):
        pass

    def __set_name__(self, cls, name):
        self.name=name

    def __get__(self, obj, cls):
        if self.name in obj.__dict__:
            return obj.__dict__[self.name]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if self.validate(value):
            obj.__dict__[self.name] = value

class Number(Validator):
    def __init__(self,minvalue=None,maxvalue=None ):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self,obj):
        if not isinstance(obj,(int,float)):
            raise TypeError('Устанавливаемое значение должно быть числом')
        if self.minvalue is not None:
            if obj<self.minvalue:
                raise ValueError(f'Устанавливаемое число должно быть больше или равно {self.minvalue}')
        if self.maxvalue is not None:
            if self.maxvalue<obj:
                raise ValueError(f'Устанавливаемое число должно быть меньше или равно {self.maxvalue}')
        return True

class String(Validator):
    def __init__(self,minsize=None,maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self,obj):
        if not isinstance(obj,str):
            raise TypeError('Устанавливаемое значение должно быть строкой')
        if self.minsize is not None:
            if len(obj)<self.minsize:
                raise ValueError(f'Длина устанавливаемой строки должна быть больше или равна {self.minsize}')
        if self.maxsize is not None:
            if self.maxsize<len(obj):
                raise ValueError(f'Длина устанавливаемой строки должна быть меньше или равна {self.maxsize}')
        if self.predicate is not None:
            if not self.predicate(obj):
                raise ValueError(f'Устанавливаемая строка не удовлетворяет дополнительным условиям')
        return True


