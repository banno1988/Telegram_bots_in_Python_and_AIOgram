from random import shuffle
class Card:
    def __init__(self,suit, rank):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.suit}{self.rank}'
class Deck:
    __suits = ("♣", "♢", "♡", "♠")
    __ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

    def __init__(self):
        self.deck=[]
        for i in self.__suits:
            for j in self.__ranks:
                self.deck.append(Card(i,j))
    def deal(self):
        if self.deck:
            return self.deck.pop()
        raise ValueError('Все карты разыграны')

    def shuffle(self):
        if len(self.deck)==52:
            shuffle(self.deck)
        else:
            raise ValueError('Перемешивать можно только полную колоду')

    def __str__(self):
        return f'Карт в колоде: {len(self.deck)}'