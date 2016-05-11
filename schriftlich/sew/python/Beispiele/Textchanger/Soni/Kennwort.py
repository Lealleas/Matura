from BasicVerschluesselung import Basic
class Kennwort(Basic):
    def __init__(self):
        super(Kennwort, self).__init__()
    def setSecretAlphabet(self,t):
        keyword=''.join(sorted(set(t), key=t.index))
        temp=keyword+self.alphabet
        self.secretAlphabet=''.join(sorted(set(temp), key=temp.index))