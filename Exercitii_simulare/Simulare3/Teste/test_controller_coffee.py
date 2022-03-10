from unittest import TestCase
from controller_coffee import Controller_Coffee
from repository_coffee import Repo_Coffee

class TestController_Coffee(TestCase):
    def setUp(self):
        self.__repo = Repo_Coffee("D:\Fundamentele programarii\Laborator\Exercitii pt simulare\Simulare3\produse_test.txt")
        self.__contr = Controller_Coffee(self.__repo)

    def test_filtreaza(self):
        list = self.__contr.filtreaza("Romania", 1000)
        for i in list:
            print(i)
        self.assertEqual(len(list), 2)
        self.assertEqual(list[0].get_nume(), "Cino")
        self.assertEqual(list[0].get_pret(), 100)

        self.assertEqual(list[1].get_nume(), "Merigo")
        self.assertEqual(list[1].get_pret(), 80)

        list = self.__contr.filtreaza("Romania", 50)
        self.assertEqual(len(list), 0)

        list = self.__contr.filtreaza("Romania", 90)
        self.assertEqual(len(list), 1)
        self.assertEqual(list[0].get_nume(), "Merigo")
        self.assertEqual(list[0].get_pret(), 80)

    def test_sortare(self):
        list = self.__contr.sortare()
        self.assertEqual(len(list), 3)
        self.assertEqual(list[0].get_nume(), "Marco")
        self.assertEqual(list[0].get_tara(), "Italia")
        self.assertEqual(list[0].get_pret(), 90)
        self.assertEqual(list[1].get_nume(), "Cino")
        self.assertEqual(list[1].get_tara(), "Romania")
        self.assertEqual(list[1].get_pret(), 100)
        self.assertEqual(list[2].get_nume(), "Merigo")
        self.assertEqual(list[2].get_tara(), "Romania")
        self.assertEqual(list[2].get_pret(), 80)
