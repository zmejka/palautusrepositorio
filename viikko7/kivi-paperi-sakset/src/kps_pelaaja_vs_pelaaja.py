from kps import KiviPaperiSakset

class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _toka_siirto(self, ekan_siirto):
        return input("Toisen pelaajan siirto: ")
