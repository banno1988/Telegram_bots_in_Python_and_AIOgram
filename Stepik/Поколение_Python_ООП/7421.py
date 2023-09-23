class ValueDict(dict):
    def key_of(self, value):
        for i in self:
            if self[i]==value:
                return i

    def keys_of(self, value):
        s=[]
        for i in self:
            if self[i]==value:
                s.append(i)
        return s