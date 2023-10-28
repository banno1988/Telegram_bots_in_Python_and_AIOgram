from dataclasses import dataclass
from random import shuffle


@dataclass
class Cell:
    row: int
    col: int
    mine: bool
    open: bool
    neighbours: int


class Game:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        t = [False for i in range(rows * cols - mines)] + [True for i in range(mines)]
        shuffle(t)
        self.board = [[None for j in range(cols)] for i in range(rows)]
        k = 0
        for i in range(rows):
            for j in range(cols):
                self.board[i][j] = Cell(i, j, t[k], False, 0)
                k += 1
        for i in range(rows):
            for j in range(cols):
                m = 0
                if i - 1 >= 0 and j - 1 >= 0 and self.board[i - 1][j - 1].mine:
                    m += 1
                if i - 1 >= 0 and self.board[i - 1][j].mine:
                    m += 1
                if i - 1 >= 0 and j + 1 <= cols-1 and self.board[i - 1][j + 1].mine:
                    m += 1
                if j + 1 <= cols-1 and self.board[i][j + 1].mine:
                    m += 1
                if i + 1 <= rows-1 and j + 1 <= cols-1 and self.board[i + 1][j + 1].mine:
                    m += 1
                if i + 1 <= rows-1 and self.board[i + 1][j].mine:
                    m += 1
                if i + 1 <= rows-1 and j - 1 >= 0 and self.board[i + 1][j - 1].mine:
                    m += 1
                if j - 1 >= 0 and self.board[i][j - 1].mine:
                    m += 1
                self.board[i][j].neighbours = m


n, m = 5, 5
game = Game(n, m, 4)

for r in range(n):
    for c in range(m):
        print(game.board[r][c].mine, end=' ')
    print()
for r in range(n):
    for c in range(m):
        print(game.board[r][c].neighbours, end=' ')
    print()