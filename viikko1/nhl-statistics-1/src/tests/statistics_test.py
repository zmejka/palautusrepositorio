import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_nimi_loytyy(self):
        self.assertIsInstance(self.statistics.search("Kurri"), Player)
    
    def test_nimi_ei_loydy(self):
        self.assertEqual(self.statistics.search("nimi"), None)
    
    def test_tiimi_suodatus(self):
        self.assertEqual(len(self.statistics.team("EDM")), 3)
    
    def test_top_lista(self):
        tulos = self.statistics.top(2)
        self.assertEqual(tulos[0].points, 89+35)