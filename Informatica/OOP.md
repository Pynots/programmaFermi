# La magia della programmazione ad oggetti


```python
class Animale:
    def __init__(self, verso):
        self.verso = verso

    def saluta(self):
        print(self.verso)
```

Dichiara la classe **Animale**. Una volta creato un ogetto della classe Animale specifica il verso.

```python
a = Animale("Quack")
b = Animale("Roaar")

a.saluta()
b.saluta()
```
Crea 2 oggetti e stampa a schermo il loro verso.

## L'ereditarietà

```python
class Leone(Animale):

    def saluta(self):
        print("Roaaar")        
```

Partendo dalla classe **Animale** già esistente, viene creata una classe chiamata **Leone**.
Una volta creato un oggetto della classe Leone però non viene richiesto di specificarne il verso
```python
pumbalo = Leone()
pumbalo.saluta()
```
Crea un oggetto della classe **Leone** e invoca il metodo saluta della classe Leone sovrascritto precedentemente