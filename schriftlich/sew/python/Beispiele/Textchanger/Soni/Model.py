from Cesar import Cesar
from Kennwort import Kennwort
class model(object):
    def __init__(self,txtfile=None):
        self.file=txtfile

    def setfile(self,txtfile):
        self.file=txtfile

    def Uppercase(self):
        upper=""
        with open(self.file,'r')as t:
            for line in t:
                upper=upper+line.upper()
        with open(self.file, 'w')as t:
            t.write(upper)
    def Lowercase(self):
        lower = ""
        with open(self.file, 'r')as t:
            for line in t:
                lower = lower + line.lower()
        with open(self.file, 'w')as t:
            t.write(lower)
    def Cesaren(self,shift):
        with open(self.file, 'r')as t:
            lower=""
            for line in t:
                lower = lower + line.lower()
        c=Cesar()
        c.setSecretAlphabet(shift)
        en=c.encript(lower)
        with open(self.file, 'w')as t:
            t.write(en)

    def Cesarde(self, shift):
        with open(self.file, 'r')as t:
            lower = ""
            for line in t:
                lower = lower + line.lower()
        c = Cesar()
        c.setSecretAlphabet(shift)
        en = c.decript(lower)
        with open(self.file, 'w')as t:
            t.write(en)

    def Kennen(self, kenn):
        with open(self.file, 'r')as t:
            lower = ""
            for line in t:
                lower = lower + line.lower()
        kennn = kenn.lower()
        k = Kennwort()
        k.setSecretAlphabet(kennn)
        en = k.encript(lower)
        with open(self.file, 'w')as t:
            t.write(en)

    def Kennde(self, kenn):
        with open(self.file, 'r')as t:
            lower = ""
            for line in t:
                lower = lower + line.lower()
        kennn=kenn.lower()
        k = Kennwort()
        k.setSecretAlphabet(kennn)
        en = k.decript(lower)
        with open(self.file, 'w')as t:
            t.write(en)