class predicate:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __and__(self, other):
        return predicate(lambda *args, **kwargs: self.func(*args, **kwargs) and other.func(*args, **kwargs))

    def __or__(self, other):
        return predicate(lambda *args, **kwargs: self.func(*args, **kwargs) or other.func(*args, **kwargs))

    def __invert__(self):
        return predicate(lambda *args, **kwargs: not self.func(*args, **kwargs))


@predicate
def char_in_word(char, word):
    return char in word


print(char_in_word('e', 'beegeek'))
print((~char_in_word & char_in_word)('e', 'beegeek'))
print((char_in_word | ~char_in_word)(word='beegeek', char='e'))


