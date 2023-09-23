from collections.abc import Sequence

class BitArray(Sequence):
    def __init__(self, iterable =[]):
        self.data = list((i for i in iterable ))


    def __getitem__(self, n):
        return self.data[n]

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)

    def __invert__(self):
        return BitArray([~i+2 for i in self.data])

    def __and__(self, other):
        if isinstance(other, BitArray):
            return BitArray([self.data[i]&other.data[i] for i in range(len(self.data))])
        return NotImplemented

    def __or__(self, other):
        if isinstance(other, BitArray):
            return BitArray([self.data[i]|other.data[i] for i in range(len(self.data))])
        return NotImplemented