from unittest import TestCase
from domain_coffee import  Coffee

class TestCoffee(TestCase):
    def setUp(self):
        self.__coffee = Coffee("Cino", "Romania", 90.9)

    def test_get_nume(self):
        self.assertEqual(self.__coffee.get_nume(), 'Cino')

    def test_get_tara(self):
        self.assertEqual(self.__coffee.get_tara(), "Romania")

    def test_get_pret(self):
        self.assertEqual(self.__coffee.get_pret(), 90.9)

    def test_str(self):
        self.assertEqual(str(self.__coffee), "Cino // Romania // 90.9")

    def test_eq(self):
        cof = Coffee("Cino", "Italia", 100)
        self.assertEqual(cof, self.__coffee)
