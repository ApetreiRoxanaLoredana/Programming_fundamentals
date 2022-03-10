from unittest import TestCase

from controller import Controller_Coffee
from domain import Coffee
from repository import Repository_Coffee


class TestCoffee(TestCase):
    def setUp(self):
        self.__coffee = Coffee("Mohito", "Romania", 28.6)

    def test_get_nume(self):
        self.assertEqual(self.__coffee.get_nume(), "Mohito")

    def test_get_tara(self):
        self.assertEqual(self.__coffee.get_tara(), "Romania")

    def test_get_pret(self):
        self.assertEqual(self.__coffee.get_pret(), 28.6)


class TestRepository_Coffee(TestCase):
    def setUp(self):
        self.__repo = Repository_Coffee("produse_test.txt")

    def test_get_all(self):
        list = self.__repo.get_all()
        self.assertEqual(len(list), 4)
        self.assertEqual(list[0].get_nume(), "Lavaza")
        self.assertEqual(list[0].get_tara(), "Anglia")
        self.assertEqual(list[0].get_pret(), 30)
        self.assertEqual(list[1].get_nume(), "Marago")
        self.assertEqual(list[1].get_tara(), "Brazilia")
        self.assertEqual(list[1].get_pret(), 20.5)
        self.assertEqual(list[2].get_nume(), "Mocha")
        self.assertEqual(list[2].get_tara(), "Anglia")
        self.assertEqual(list[2].get_pret(), 5.7)
        self.assertEqual(list[3].get_nume(), "Marco")
        self.assertEqual(list[3].get_tara(), "Brazilia")
        self.assertEqual(list[3].get_pret(), 9)


class TestController_Coffee(TestCase):
    def setUp(self):
        self.__repo = Repository_Coffee("produse_test.txt")
        self.__contr = Controller_Coffee(self.__repo)

    def test_suma_preturi(self):
        suma = self.__contr.suma_preturi("Anglia")
        self.assertEqual(suma, 35.7)
        suma = self.__contr.suma_preturi("Brazilia")
        self.assertEqual(suma, 29.5)

    def test_sortare(self):
        dic = self.__contr.sortare()
        dic_test = [("Brazilia", 29.5), ("Anglia", 35.7)]
        self.assertListEqual(dic, dic_test)
