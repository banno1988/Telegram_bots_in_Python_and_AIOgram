def letterCombinations(digits: str):
        from itertools import product
        d = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}

        if digits == '':
            return []
        elif len(digits) == 1:
            return d[digits]

        def qwert(digits):

            if len(digits) == 1:
                return [d[digits]]
            return qwert(digits[:-1]) + qwert(digits[-1])


        return [''.join(i) for i in product(*qwert(digits))]


print(letterCombinations('23'))
