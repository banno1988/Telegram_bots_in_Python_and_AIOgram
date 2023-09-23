from collections import UserDict
class TwoWayDict(UserDict):
    def __setitem__(self, key, value):
        self.data[key]=value
        self.data[value]=key