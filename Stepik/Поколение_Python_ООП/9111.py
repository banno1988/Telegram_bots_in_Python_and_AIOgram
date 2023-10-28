class Currency:
    __RATE = {
        'EUR': {'EUR': 1, 'USD': 1.1, 'RUB': 90},
        'USD': {'EUR': 1 / 1.1, 'USD': 1, 'RUB': 1 / 1.1 * 90},
        'RUB': {'EUR': 1 / 90, 'USD': 1 / 90 * 1.1, 'RUB': 1}
    }

    def __init__(self, m, v):
        self.m = m
        self.v = v

    def __str__(self):
        return f'{round(self.m,2)} {self.v}'

    def change_to(self, v):
        self.m = self.m * Currency.__RATE[self.v][v]
        self.v = v

    def __add__(self, other):
        m=self.m + other.m * Currency.__RATE[other.v][self.v]
        return Currency(m,self.v)
    def __mul__(self, other):
        m=self.m * other.m * Currency.__RATE[other.v][self.v]
        return Currency(m,self.v)
    def __sub__(self, other):
        m=self.m - other.m * Currency.__RATE[other.v][self.v]
        return Currency(m,self.v)
    def __truediv__(self, other):
        m=self.m / (other.m * Currency.__RATE[other.v][self.v])
        return Currency(m,self.v)




print(Currency(5, 'EUR') + Currency(5, 'EUR'))
print(Currency(11, 'USD') - Currency(5, 'EUR'))
print(Currency(5, 'RUB') * Currency(11, 'USD'))
print(Currency(5, 'USD') / Currency(5, 'EUR'))