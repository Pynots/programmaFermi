class Animale:
    def __init__(self, verso = None):
        self.verso = verso

    def saluta(self):
        print(self.verso)

a = Animale("Quack")
b = Animale("Woof")

a.saluta()
b.saluta()

class Leone(Animale):

    def saluta(self):
        print("Roaaar")

pumbalo = Leone()
pumbalo.saluta()
