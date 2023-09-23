class Paragraph:
    def __init__(self, length):
        self._p=[]
        self.length =length

    def add(self, s):
        self._p.extend(s.split())

class LeftParagraph(Paragraph):
    def end(self):
        t=[]
        o=''
        for i in self._p:
            if len(i)+len(o)>=self.length:
                t.append((o).lstrip())
                o=''
                o+=i
            else:
                o+=' '
                o+=i
        t.append(o)
        print('\n'.join(t))
        self._p=[]

class RightParagraph(Paragraph):
    def end(self):
        t=[]
        o=''
        for i in self._p:
            if len(i)+len(o)>=self.length:
                o=o.lstrip()
                t.append(o.rjust(self.length))
                o=''
                o+=i
            else:
                o+=' '
                o+=i
        t.append(o.rjust(self.length))

        print('\n'.join(t))
        self._p=[]