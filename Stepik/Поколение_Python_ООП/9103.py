from string import ascii_lowercase, ascii_uppercase, ascii_letters


class CaesarCipher:
    def __init__(self, n):
        self.n = n

    def encode(self, t):
        s = ''
        for i in t:
            if i not in ascii_letters:
                s += i
            elif i in ascii_lowercase:
                j = ascii_lowercase.find(i)
                j2 = (j + self.n) % 26
                s += ascii_lowercase[j2]
            elif i in ascii_uppercase:
                j = ascii_uppercase.find(i)
                j2 = (j + self.n) % 26
                s += ascii_uppercase[j2]
        return s

    def decode(self, t):
        s = ''
        for i in t:
            if i not in ascii_letters:
                s += i
            elif i in ascii_lowercase:
                j = ascii_lowercase.find(i)
                j2 = (j - self.n) % 26
                s += ascii_lowercase[j2]
            elif i in ascii_uppercase:
                j = ascii_uppercase.find(i)
                j2 = (j - self.n) % 26
                s += ascii_uppercase[j2]
        return s


cipher = CaesarCipher(15)

words = ['EvEr', 'WoUlD', 'CeRtAiN', 'WhIcH', 'WiTh', 'ThErE', 'EnViRoNmEnTaL', 'StRuCtUrE', 'NeWs', 'ThRoW', 'NoTe',
         'If', 'WiN', 'ShOuLdEr', 'NeEd', 'WhErE', 'MeThOd', 'FiRsT', 'CiViL', 'BaSe']

encode_words = [cipher.encode(word) for word in words]
print(encode_words)

decode_words = [cipher.decode(word) for word in encode_words]
print(decode_words)
