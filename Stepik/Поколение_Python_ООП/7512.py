from abc import ABC, abstractmethod


class ChessPiece(ABC):

    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    @abstractmethod
    def can_move(self):
        pass


class King(ChessPiece):

    def can_move(self, h, v):
        d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        if self.horizontal==h and self.vertical==v:
            return False
        h1 = d[self.horizontal]
        v1 = self.vertical
        h2 = d[h]
        v2 = v
        if -1 <= (h1 - h2) <= 1 and -1 <= (v1 - v2) <= 1:
            return True
        else:
            return False


class Knight(ChessPiece):

    def can_move(self, h, v):
        d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        if self.horizontal==h and self.vertical==v:
            return False
        h1 = d[self.horizontal]
        v1 = self.vertical
        h2 = d[h]
        v2 = v
        if abs((h1 - h2) * (v1 - v2)) == 2:
            return True
        else:
            return False
