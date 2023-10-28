import json
def jsonattr(filename):
    with open(filename) as f:
        d=json.load(f)
    def wrapper(cls):
        for key, value in d.items():
            setattr(cls, key, value)
        return cls
    return wrapper


with open('test.json', 'w') as file:
    file.write('{"x": 1, "y": 2}')


@jsonattr('test.json')
class MyClass:
    pass


print(MyClass.x)
print(MyClass.y)