KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = self.tarskistus(kapasiteetti, KAPASITEETTI)
        self.kasvatuskoko = self.tarskistus(kasvatuskoko, OLETUSKASVATUS)

        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def tarskistus(self, arvo, oletus):
        if arvo is None:
            return oletus
        if not isinstance(arvo, int) or arvo < 0:
            raise Exception("Väärä syöte")
        else:
            return arvo
    
    def kuuluu(self, luku):
        return luku in self.ljono

    def lisaa(self, luku):
        if self.kuuluu(luku):
            return False
        
        self.ljono[self.alkioiden_lkm] = luku
        self.ljono += [0]*self.kasvatuskoko
        self.alkioiden_lkm +=1
        return True

    def poista(self, luku):
        if luku in self.ljono:
            self.ljono.remove(luku)
            self.alkioiden_lkm -=1
            self.ljono.append(0)
            return True
        else:
            return False

    def kopioi_taulukko(self, vanha_lista, uusi_lista):
        for value in vanha_lista:
            uusi_lista.append(value)

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self.ljono[:self.alkioiden_lkm]
        return taulu

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for value in a_taulu + b_taulu:
            yhdiste.lisaa(value)

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for a_value in a_taulu:
            for b_value in b_taulu:
                if a_value == b_value:
                    leikkaus.lisaa(b_value)

        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for a_value in a_taulu:
            erotus.lisaa(a_value)

        for b_value in b_taulu:
            erotus.poista(b_value)

        return erotus

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        if self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        lista = self.to_int_list()
        tuotos = ""
        for i in range(len(lista)-1):
            tuotos = tuotos + str(lista[i])
            tuotos = tuotos + ', '
        tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
        return '{' + tuotos + '}'
