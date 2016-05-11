from BasicVerschluesselung import Basic
class Cesar(Basic):
    def __init__(self):
        super(Cesar, self).__init__()
    def setSecretAlphabet(self,t):
        super(Cesar, self).setSecretAlphabet(t)
        shift = self.alphabet[t:]
        shift2= self.alphabet[:t]
        self.secretAlphabet=shift+shift2