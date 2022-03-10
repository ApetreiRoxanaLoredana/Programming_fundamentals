from unittest import TestCase

from domain import Bere


class TestBere(TestCase):
    def setUp(self):
        self.__bere = Bere("Ciuc", "blonda", 90)

    def test_get_nume(self):
        self.assertEqual(self.__bere.get_nume(), "Ciuc")

    def test_get_tip(self):
        self.assertEqual(self.__bere.get_tip(), "blonda")

    def test_get_pret(self):
        self.assertEqual(self.__bere.get_pret(), 90)

    def test_get_id(self):
        self.assertEqual(self.__bere.get_id(), "Ciuc blonda")
