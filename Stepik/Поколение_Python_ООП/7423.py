from collections import UserString

class MutableString(UserString):

    def lower(self):
        self.data = self.data.lower()
        return self

    def upper(self):
        self.data = self.data.upper()
        return self

    def sort(self, key=None, reverse=False):
        self.data=''.join(sorted(self.data,key=key,reverse=reverse))
        return self

    def __setitem__(self, key, value):
        t=list(self.data)
        t[key]=value
        self.data=''.join(t)
        return self

    def __delitem__(self, key):
        t = list(self.data)
        del t[key]
        self.data = ''.join(t)
        return self