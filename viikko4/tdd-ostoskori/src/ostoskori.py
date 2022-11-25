from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.kori = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        ostos_lukumaara = 0
        for ostos in self.kori:
            ostos_lukumaara += ostos.lukumaara()
        return ostos_lukumaara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        ostos_summa = 0
        for ostos in self.kori:
            ostos_summa += ostos.hinta()
        return ostos_summa
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self.kori:
            if ostos.tuotteen_nimi() == lisattava.nimi():
                ostos.muuta_lukumaaraa(1)
                return
        self.kori.append(Ostos(lisattava))
        # lisää tuotteen

    def poista_tuote(self, poistettava: Tuote):
        for ostos in self.kori:
            if ostos.tuotteen_nimi() == poistettava.nimi():
                ostos.muuta_lukumaaraa(-1)
            if ostos.lukumaara() == 0:
                self.kori.remove(ostos)
        # poistaa tuotteen


    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.kori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
