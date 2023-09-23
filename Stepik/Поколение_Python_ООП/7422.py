from collections import UserDict
from datetime import date
class BirthdayDict(UserDict):
    def __setitem__(self, key, value):
        for i in self.data:
            if self.data[i]==value:
                print(f'Хей, {key}, не только ты празднуешь день рождения в этот день!')
                break
        self.data[key]=value