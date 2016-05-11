from abc import ABCMeta, abstractmethod
class Basic(metaclass=ABCMeta):
    def encript(self,text):
        ltext=list(text)
        slist=list(self.secretAlphabet)
        nlist = list(self.alphabet)
        ret=""
        for l in ltext:
            if l in nlist:
                ret=ret+str(slist[nlist.index(l)])
            else:
                ret=ret+str(l)
        return ret
    def decript(self,text):
        ltext = list(text)
        nlist = list(self.alphabet)
        slist = list(self.secretAlphabet)
        ret = ""
        for l in ltext:
            if l in slist:
                ret = ret + str(nlist[slist.index(l)])
            else:
                ret = ret + str(l)
        return ret
    def __init__(self):
        self.alphabet="abcdefghijklmnopqrstuvwxyz"
        self.secretAlphabet="abcdefghijklmnopqrstuvwxyz"

    @abstractmethod
    def setSecretAlphabet(self,t):
        pass