class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}, {self.price}$'

class ShoppingCart:
    def __init__(self, items=[]):
        self.items=[i for i in items]

    def add(self, n):
        self.items.append(n)

    def total(self):
        return sum(i.price for i in self.items)

    def remove(self, n):
        self.items = [i for i in self.items if i.name!=n]

    def __str__(self):
        return '\n'.join(str(i) for i in self.items)