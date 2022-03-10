from unittest import TestCase

from domain import Bere
from repository import Repo_bere


class TestRepo_bere(TestCase):
    def setUp(self):
        self.__repo = Repo_bere("D:\Fundamentele programarii\Laborator\Exercitii pt simulare\Simulare4\produse_test.txt")

    def test_get_all(self):
        list = self.__repo.get_all()
        self.assertEqual(len(list), 3)
        self.assertEqual(list[0].get_nume(), "Ciuc")
        self.assertEqual(list[0].get_tip(), "blonda")
        self.assertEqual(list[0].get_pret(), 9)
        self.assertEqual(list[1].get_nume(), "Lefe")
        self.assertEqual(list[1].get_tip(), "neagra")
        self.assertEqual(list[1].get_pret(), 7)

    def test_update(self):
        self.__repo.update("Ciuc blonda", Bere("Haineker", "bruna", 100))
        list = self.__repo.get_all()
        self.assertEqual(list[0].get_nume(), "Haineker")
        self.assertEqual(list[0].get_tip(), "bruna")
        self.assertEqual(list[0].get_pret(), 100)
        self.__repo.update("Haineker bruna", Bere("Ciuc", "blonda", 9))
