class Nollaus:
    def __init__(self, sovellus):
        self._sovellus = sovellus
    
    def suorita(self):
        self._sovellus.nollaa()

class Summa:
    def __init__(self, sovellus, syote):
        self._sovellus = sovellus
        self._syote = syote
    
    def suorita(self):
        arvo = int(self._syote())
        self._sovellus.plus(arvo)

class Erotus:
    def __init__(self, sovellus, syote):
        self._sovellus = sovellus
        self._syote = syote

    def suorita(self):
        arvo = int(self._syote())
        self._sovellus.miinus(arvo)

class Kumoa:
    def __init__(self, sovellus):
        self._sovellus = sovellus

    def suorita(self):
        edellinen = self._sovellus.edellinen
        self._sovellus.aseta_arvo(edellinen)
