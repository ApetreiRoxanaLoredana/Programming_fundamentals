from unittest import TestCase

from domain import Contact
from errors import ValidatorException, RepoException
from repository import ContactRepository
from validator import ContactValidator


class TestContact(TestCase):
    def setUp(self):
        self.__cont = Contact(23, "Maria", "0723", "Altele")

    def test_get_id(self):
        self.assertEqual(self.__cont.get_id(), 23)

    def test_get_name(self):
        self.assertEqual(self.__cont.get_name(), "Maria")

    def test_get_phone_nr(self):
        self.assertEqual(self.__cont.get_phoneNr(), "0723")

    def test_get_group(self):
        self.assertEqual(self.__cont.get_group(), "Altele")


class TestContactValidator(TestCase):
    def setUp(self):
        self.__cont1 = Contact(-12, "", "", "")
        self.__cont2 = Contact(12, "ana", "323f", "mas")
        self.__val = ContactValidator()

    def test_valideaza(self):
        self.assertRaisesRegex(ValidatorException, "Id ivalid!\n"
                                                   "Numele nu poate fi vid!\n"
                                                   "Grupul nu e corect!\n"
                                                   "Numarul de telefon nu poate fi vid!\n", self.__val.valideaza,
                               self.__cont1)
        self.assertRaisesRegex(ValidatorException, "Grupul nu e corect!\n"
                                                   "Numarul de telefon trebuie sa contina doar cifre!\n",
                               self.__val.valideaza, self.__cont2)


class TestContactRepository(TestCase):
    def setUp(self):
        self.__repo = ContactRepository("Contacte_test.txt")
        self.__repo2 = ContactRepository("Contacte_test.txt")

    def tearDown(self):
        f = open("Contacte_test.txt", "w")
        f.write("")
        f.close()

    def test_get_all(self):
        list = self.__repo.getAll()
        self.assertEqual(len(list), 0)
        self.__repo.add(Contact(12, "a", "3", "Altele"))
        list = self.__repo.getAll()
        self.assertEqual(len(list), 1)

        list = self.__repo2.getAll()
        self.assertEqual(len(list), 1)

    def test_add(self):
        self.__repo.add(Contact(12, "ana", "09", "Altele"))
        list_cont = self.__repo.getAll()
        self.assertEqual(len(list_cont), 1)
        self.assertEqual(list_cont[0].get_id(), 12)
        self.assertEqual(list_cont[0].get_name(), "ana")
        self.assertEqual(list_cont[0].get_phoneNr(), "09")
        self.assertEqual(list_cont[0].get_group(), "Altele")

        list = self.__repo2.getAll()
        self.assertEqual(len(list), 1)

        self.assertRaisesRegex(RepoException, "Exista un contact cu acest id!\n", self.__repo2.add, Contact(12, "mama", "098", "Altele"))
        self.assertRaisesRegex(RepoException, "Exista un contact cu acest nume!\n", self.__repo2.add, Contact(14, "ana", "098", "Altele"))

    def test_find(self):
        self.assertRaisesRegex(RepoException, "Nu exista acest nume in contacte!\n", self.__repo.find, "Maria")
        self.__repo.add(Contact(12, "ana", "87", "Job"))
        cont = self.__repo.find("ana")
        self.assertEqual(cont.get_id(), 12)
        self.assertEqual(cont.get_name(), "ana")
        self.assertEqual(cont.get_phoneNr(), "87")
        self.assertEqual(cont.get_group(), "Job")

    def test_get_all_for(self):
        self.assertRaisesRegex(RepoException, "Nu exista nici un contact din acest grup!\n", self.__repo.getAllFor, "Job")
        self.__repo.add(Contact(12, "a", "1", "Job"))
        self.__repo.add(Contact(11, "c", "1", "Altele"))
        self.__repo.add(Contact(13, "b", "1", "Job"))
        list = self.__repo.getAllFor("Job")
        self.assertEqual(len(list), 2)
        list = self.__repo.getAllFor("Altele")
        self.assertEqual(len(list), 1)