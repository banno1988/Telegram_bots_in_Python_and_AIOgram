class Testpaper:

    def __init__(self, predmet, otvets, proc):
        self.predmet = predmet
        self.otvets = otvets
        self.proc = int(proc[:-1])


class Student:
    def __init__(self):
        self.tests_taken = 'No tests taken'

    def take_test(self, testpaper, otv):
        if self.tests_taken == 'No tests taken':
            self.tests_taken = {}
        t = []
        for i in range(len(otv)):
            if otv[i] == testpaper.otvets[i]:
                t.append(otv[i])
        p = round(len(t) / len(otv) * 100)
        if p >= testpaper.proc:
            self.tests_taken[testpaper.predmet] = f'Passed! ({p}%)'
        else:
            self.tests_taken[testpaper.predmet] = f'Failed! ({p}%)'


testpaper1 = Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
testpaper2 = Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
testpaper3 = Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')

student1 = Student()
student2 = Student()

student1.take_test(testpaper1, ['1A', '2D', '3D', '4A', '5A'])
student2.take_test(testpaper2, ['1C', '2D', '3A', '4C'])
student2.take_test(testpaper3, ['1A', '2C', '3A', '4C', '5D', '6C', '7B'])

print(student1.tests_taken)    # {'Maths': 'Passed! (80%)'}
print(student2.tests_taken)