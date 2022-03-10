from unittest import TestCase
from repository_coffee import Repo_Coffee

class TestRepo_Coffee(TestCase):
    def setUp(self):
        self.__repo = Repo_Coffee("D:\Fundamentele programarii\Laborator\Exercitii pt simulare\Simulare3\produse_test.txt")

    def test_get_all(self):
        list = self.__repo.get_all()
        self.assertEqual(len(list), 2)
        self.assertEqual(list[0].get_nume(), "Cino")
        self.assertEqual(list[0].get_tara(), "Romania")
        self.assertEqual(list[0].get_pret(), 100)
        self.assertEqual(list[1].get_nume(), "Marco")
        self.assertEqual(list[1].get_tara(), "Italia")
        self.assertEqual(list[1].get_pret(), 90)
