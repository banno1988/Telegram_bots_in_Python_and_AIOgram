from functools import total_ordering


@total_ordering
class Vector:
    def __init__(self, *s):
        self.s = s

    def __lt__(self, other):
        if len(self.s) == len(other.s):
            return self.s < other.s
        else:
            raise ValueError('Векторы должны иметь равную длину')

    def __eq__(self, other):
        if len(self.s) == len(other.s):
            return self.s == other.s
        else:
            raise ValueError('Векторы должны иметь равную длину')

    def __add__(self, other):
        if len(self.s) == len(other.s):
            return Vector(*[self.s[i] + other.s[i] for i in range(len(self.s))])
        else:
            raise ValueError('Векторы должны иметь равную длину')

    def __sub__(self, other):
        if len(self.s) == len(other.s):
            return Vector(*[self.s[i] - other.s[i] for i in range(len(self.s))])
        else:
            raise ValueError('Векторы должны иметь равную длину')

    def __mul__(self, other):
        if len(self.s) == len(other.s):
            return sum([self.s[i] * other.s[i] for i in range(len(self.s))])
        else:
            raise ValueError('Векторы должны иметь равную длину')

    def norm(self):
        return sum([i**2 for i in self.s])**0.5

    def __repr__(self):
        return str(self.s)

vector1 = Vector(1, 2, 3)
vector2 = Vector(5, 6, 7, 8)

try:
    print(vector1 == vector2)
except ValueError as e:
    print(e)
