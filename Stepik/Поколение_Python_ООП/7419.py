class AdvancedList(list):
    def join(self, n=' '):
        return n.join(str(i) for i in self)

    def map(self, func):
        self[:] = map(func, self)

    def filter(self, func):
        self[:]=filter(func, self)
