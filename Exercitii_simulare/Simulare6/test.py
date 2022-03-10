from unittest import TestCase

from controller import Controller_Bicicleta
from domain import Bicicleta
from repository import Repository_Bicicleta


class TestBicicleta(TestCase):
    def setUp(self):
        self.__bici = Bicicleta(12, "bmw", 180.5)

    def test_get_id(self):
        self.assertEqual(self.__bici.get_id(), 12)

    def test_get_tip(self):
        self.assertEqual(self.__bici.get_tip(), "bmw")

    def test_get_pret(self):
        self.assertEqual(self.__bici.get_pret(), 180.5)


class TestRepository_Bicicleta(TestCase):
    def setUp(self):
        self.__repo = Repository_Bicicleta("produse_test.txt")

    def tearDown(self):
        f = open("produse_test.txt", "w")
        f.write("34, bicifrumi, 100.5\n")
        f.write("66, ooo, 100.5\n")
        f.write("45, www, 45.6\n")
        f.write("67, www, 90\n")
        f.close()

    def test_get_all(self):
        list = self.__repo.get_all()
        self.assertEqual(len(list), 4)
        self.assertEqual(list[0].get_id(), 34)
        self.assertEqual(list[0].get_tip(), "bicifrumi")
        self.assertEqual(list[0].get_pret(), 100.5)
        self.assertEqual(list[1].get_id(), 66)
        self.assertEqual(list[1].get_tip(), "ooo")
        self.assertEqual(list[1].get_pret(), 100.5)
        self.assertEqual(list[2].get_id(), 45)
        self.assertEqual(list[2].get_tip(), "www")
        self.assertEqual(list[2].get_pret(), 45.6)
        self.assertEqual(list[3].get_id(), 67)
        self.assertEqual(list[3].get_tip(), "www")
        self.assertEqual(list[3].get_pret(), 90)

    def test_delete(self):
        list = self.__repo.get_all()
        self.assertEqual(len(list), 4)
        self.__repo.delete(34)
        list = self.__repo.get_all()
        self.assertEqual(len(list), 3)
        self.__repo.delete(66)
        self.__repo.delete(45)
        list = self.__repo.get_all()
        self.assertEqual(len(list), 1)
        self.assertEqual(list[0].get_id(), 67)
        self.assertEqual(list[0].get_tip(), "www")
        self.assertEqual(list[0].get_pret(), 90)


class TestController_Bicicleta(TestCase):
    def setUp(self):
        self.__repo = Repository_Bicicleta("produse_test.txt")
        self.__contr = Controller_Bicicleta(self.__repo)

    def tearDown(self):
        f = open("produse_test.txt", "w")
        f.write("34, bicifrumi, 100.5\n")
        f.write("66, ooo, 100.5\n")
        f.write("45, www, 45.6\n")
        f.write("67, www, 90\n")
        f.close()

    def test_sterge_tip(self):
        self.__contr.sterge_tip("www")
        list = self.__repo.get_all()
        self.assertEqual(len(list), 2)
        self.assertEqual(list[0].get_tip(), "bicifrumi")
        self.assertEqual(list[1].get_tip(), "ooo")

    def test_sterge_max(self):
        self.__contr.sterge_max()
        list = self.__repo.get_all()
        self.assertEqual(len(list), 2)
        self.assertEqual(list[0].get_pret(), 45.6)
        self.assertEqual(list[1].get_pret(), 90)

