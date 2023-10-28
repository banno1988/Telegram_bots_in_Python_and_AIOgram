class TicTacToe:
    def __init__(self):
        self.pole = [[' ', ' ', ' '] for i in range(3)]
        self.irok = 0
        self.win = None

    def mark(self, x, y):
        if self.irok == 0:
            self.irok = 'X'
        if self.win is None:
            if self.pole[x - 1][y - 1] != ' ':
                print('Недоступная клетка')
            else:
                self.pole[x - 1][y - 1] = self.irok
                if self.irok == 'X':
                    self.irok = 'O'
                else:
                    self.irok = 'X'
            self.win = self.winner()
        else:
            print('Игра окончена')

    def show(self):
        t = 0
        for i in self.pole:
            t += 1
            print(f'{i[0]}|{i[1]}|{i[2]}')
            if t != 3:
                print('-----')

    def winner(self):
        for i in self.pole:
            if len(list(set(i))) == 1 and list(set(i))[0] == 'X':
                return 'X'
            elif len(list(set(i))) == 1 and list(set(i))[0] == 'O':
                return 'O'

        u = zip(*self.pole)
        for i in u:
            if len(list(set(i))) == 1 and list(set(i))[0] == 'X':
                return 'X'
            elif len(list(set(i))) == 1 and list(set(i))[0] == 'O':
                return 'O'

        if self.pole[0][0] == 'X' and self.pole[1][1] == 'X' and self.pole[2][2] == 'X':
            return 'X'

        if self.pole[0][0] == 'O' and self.pole[1][1] == 'O' and self.pole[2][2] == 'O':
            return 'O'

        if self.pole[0][2] == 'X' and self.pole[1][1] == 'X' and self.pole[2][0] == 'X':
            return 'X'

        if self.pole[0][2] == 'O' and self.pole[1][1] == 'O' and self.pole[2][0] == 'O':
            return 'O'
        w = 0
        for i in self.pole:
            if " " not in i:
                w += 1
        if w == 3:
            return "Ничья"

        return None


tictactoe = TicTacToe()

tictactoe.mark(1, 1)
tictactoe.mark(1, 3)
tictactoe.mark(3, 1)
tictactoe.mark(2, 1)

print(tictactoe.winner())

tictactoe.mark(3, 2)
tictactoe.mark(3, 3)
tictactoe.mark(1, 2)
tictactoe.mark(2, 2)
tictactoe.mark(2, 3)

print(tictactoe.winner())
tictactoe.show()
tictactoe.mark(2, 2)
print(tictactoe.winner())
