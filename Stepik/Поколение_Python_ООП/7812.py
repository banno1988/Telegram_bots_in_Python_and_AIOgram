from collections import deque

class Queue():
    def __init__(self, pairs=[]):
        if isinstance(pairs,dict):
            pairs=pairs.items()
        self.pairs=deque(pairs)

    def add(self, other):

        for i in self.pairs:
            if i[0]==other[0]:
                self.pairs.remove(i)
                break
        self.pairs.append(other)

    def __str__(self):
        return f'Queue{str(self.pairs)[5:]}'

    def __len__(self):
        return len(self.pairs)

    def pop(self):
        if len(self.pairs)>0:
            return self.pairs.popleft()
        raise KeyError('Очередь пуста')

