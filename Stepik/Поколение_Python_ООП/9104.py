class ArithmeticProgression:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.n=1
    def __iter__(self):
        return self

    def __next__(self):
        if self.n:
            self.n=0
            return self.a
        self.a += self.b
        return self.a


class GeometricProgression:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.n = 1
    def __iter__(self):
        return self

    def __next__(self):
        if self.n:
            self.n=0
            return self.a
        self.a *= self.b
        return self.a


progression = GeometricProgression(1, 2)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')  # 1 2 4 8
