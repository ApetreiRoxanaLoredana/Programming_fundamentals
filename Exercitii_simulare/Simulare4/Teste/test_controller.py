from unittest import TestCase

from controller import Controller_bere
from domain import Bere
from repository import Repo_bere


class TestController_bere(TestCase):
    def setUp(self):
        self.__repo = Repo_bere("D:\Fundamentele programarii\Laborator\Exercitii pt simulare\Simulare4\produse_test.txt")
        self.__contr = Controller_bere(self.__repo)
        self.__repo.update("Ciuc blonda", Bere("Ciuc", "blonda", 9))
        self.__repo.update("Ciuc neagra", Bere("Ciuc", "neagra", 4))

    def test_update(self):
        self.__contr.update("Ciuc", 50)
        list = self.__repo.get_all()
        self.assertEqual(list[0].get_pret(), 13.5)
        self.assertEqual(list[2].get_pret(), 6)

    def test_discount(self):
        self.__contr.discount("blonda")
        list = self.__repo.get_all()
        self.assertEqual(list[0].get_pret(), 4)
