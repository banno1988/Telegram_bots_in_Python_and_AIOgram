from dataclasses import dataclass, field
from functools import total_ordering


@total_ordering
@dataclass
class FootballPlayer:
    name: str = field(compare=False)
    surname: str = field(compare=False)
    value: int = field(repr=False)

    def __lt__(self, other):
        return self.value < other.value


@dataclass
class FootballTeam:
    name: str
    players: list = field(default_factory=list, repr=False, compare=False)

    def add_players(self, *args):
        for i in args:
            self.players.append(i)
