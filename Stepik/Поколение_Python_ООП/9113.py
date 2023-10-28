from collections import UserDict


class MultiKeyDict(UserDict):
    def __init__(self,*args, **kwargs):
        self.dic = {}
        super().__init__(*args, **kwargs)

    def alias(self, a, b):
        # self.dic[a] = b
        self.dic[b] = a

    def __getitem__(self, item):
        if item in self.data:
            return self.data[item]
        if item in self.dic:
            return self.data[self.dic[item]]
        raise KeyError

    def __setitem__(self, key, value):
        if key in self.dic:
            self.data[self.dic[key]] = value
        self.data[key] = value

    def __delitem__(self, key):
        a=None
        for i, j in self.dic.items():
            if j==key:
                self.data[i]=self.data[key]
                del self.dic[i]
                a=i
                break
        for i, j in self.dic.items():
            if j==key:
                self.dic[i]=a
        del self.data[key]
        # elif key in self.dic:
        #     a=self.dic[key]
        #     self.data[self.dic[key]] = self.data[key]
        #     for i, j in self.dic.items():
        #         if j==key:
        #             self.dic[i]=a
        #     del self.dic[a]
        #     del self.dic[key]



multikeydict = MultiKeyDict(lecture='python', lesson='object oriented programming')

multikeydict.alias('lecture', 'lesson')
print(multikeydict['lesson'])

multikeydict.alias('lecture', 'lesson')
print(multikeydict['lesson'])

del multikeydict['lesson']
print(multikeydict['lesson'])

