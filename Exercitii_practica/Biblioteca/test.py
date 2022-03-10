from unittest import TestCase

from controller import BiblioController
from domain import Carte, Undo, CarteValidator, Filtru
from errors import ValidatorException
from repository import BiblioRepo, UndoRepo


class TestCarte(TestCase):
    def setUp(self) -> None:
        self.__carte = Carte(12, "Otilia", "Calinescu", 1883)

    def test_get_id(self):
        self.assertEqual(self.__carte.get_id(), 12)

    def test_get_titlu(self):
        self.assertEqual(self.__carte.get_titlu(), "Otilia")

    def test_get_autor(self):
        self.assertEqual(self.__carte.get_autor(), "Calinescu")

    def test_get_an_aparitie(self):
        self.assertEqual(self.__carte.get_an_aparitie(), 1883)

    def test_str(self):
        self.assertEqual(str(self.__carte), "12, Otilia, Calinescu, 1883")


class TestUndo(TestCase):
    def setUp(self) -> None:
        self.__carte1 = Carte(12, "Otilia", "Calinescu", 1883)
        self.__carte2 = Carte(13, "Ion", "Rebreanu", 1990)
        self.__undo = Undo("modificat", [self.__carte1, self.__carte2])

    def test_get_status(self):
        self.assertEqual(self.__undo.get_status(), "modificat")

    def test_get_lista_carti(self):
        self.assertEqual(self.__undo.get_lista_carti()[0].get_id(), 12)
        self.assertEqual(self.__undo.get_lista_carti()[1].get_id(), 13)


class TestCarteValidator(TestCase):
    def setUp(self):
        self.__carte1 = Carte(-12, "Otilia", "Calinescu", 10)
        self.__val = CarteValidator()

    def test_valideaza(self):
        self.assertRaisesRegex(ValidatorException, "Id invalid\n"
                                                   "An invalid\n", self.__val.valideaza, self.__carte1)


class TestFiltru(TestCase):
    def setUp(self):
        self.__filtru = Filtru("axa", 8)

    def test_get_text(self):
        self.assertEqual(self.__filtru.get_text(), "axa")

    def test_get_numar(self):
        self.assertEqual(self.__filtru.get_numar(), 8)

    def test_set_text(self):
        self.__filtru.set_text("ana")
        self.assertEqual(self.__filtru.get_text(), "ana")

    def test_set_numar(self):
        self.__filtru.set_numar(6)
        self.assertEqual(self.__filtru.get_numar(), 6)


class TestBiblioRepo(TestCase):
    def tearDown(self):
        f = open("carti_test.txt", "w")
        f.write("")
        f.close()

    def setUp(self):
        self.__repo = BiblioRepo("carti_test.txt")
        self.__repo2 = BiblioRepo("carti_test.txt")

    def test_add(self):
        carte = Carte(12, "Otilia", "Calinescu", 1884)
        self.__repo.add(carte)
        list = self.__repo2.load_from_file()
        self.assertEqual(len(list), 1)
        self.assertEqual(list[0].get_id(), 12)

    def test_modifica(self):
        carte = Carte(12, "Otilia", "Calinescu", 1884)
        self.__repo.add(carte)
        carte2 = Carte(12, "Maria", "Ana", 2000)
        self.__repo.modifica(carte2)
        list = self.__repo2.load_from_file()
        self.assertEqual(len(list), 1)
        self.assertEqual(list[0].get_id(), 12)
        self.assertEqual(list[0].get_titlu(), "Maria")
        self.assertEqual(list[0].get_autor(), "Ana")
        self.assertEqual(list[0].get_an_aparitie(), 2000)

    def test_sterge(self):
        carte = Carte(12, "Otilia", "Calinescu", 1884)
        self.__repo.add(carte)
        list = self.__repo2.load_from_file()
        self.assertEqual(len(list), 1)
        self.assertEqual(list[0].get_id(), 12)
        self.__repo.sterge(carte)
        self.assertEqual(len(self.__repo2.load_from_file()), 0)


class TestUndoRepo(TestCase):
    def setUp(self):
        self.__repo_undo = UndoRepo()

    def test_add(self):
        carte1 = Carte(12, "Ion", "Liviu", 1908)
        undo = Undo("adaugare", [carte1])
        self.__repo_undo.add(undo)
        self.assertEqual(len(self.__repo_undo.get_all()), 1)

    def test_pop(self):
        carte1 = Carte(12, "Ion", "Liviu", 1908)
        undo = Undo("adaugare", [carte1])
        self.__repo_undo.add(undo)
        self.assertEqual(len(self.__repo_undo.get_all()), 1)
        carte = self.__repo_undo.pop().get_lista_carti()[0]
        self.assertEqual(carte1.get_id(), carte.get_id())
        self.assertEqual(carte1.get_titlu(), carte.get_titlu())
        self.assertEqual(len(self.__repo_undo.get_all()), 0)

    def test_get_all(self):
        self.assertEqual(len(self.__repo_undo.get_all()), 0)
        carte1 = Carte(12, "Ion", "Liviu", 1908)
        undo = Undo("adaugare", [carte1])
        self.__repo_undo.add(undo)
        self.assertEqual(len(self.__repo_undo.get_all()), 1)


class TestBiblioController(TestCase):
    def setUp(self):
        self.__repo_undo = UndoRepo()
        self.__repo = BiblioRepo("carti_test.txt")
        self.__repo.add(Carte(12, "anamaria", "mama", 1908))
        self.__repo.add(Carte(122, "ana", "ma", 1908))
        self.__val = CarteValidator()
        self.__filtru = Filtru('ana', 2000)
        self.__contr = BiblioController(self.__repo, self.__repo_undo, self.__val, self.__filtru)

    def tearDown(self) -> None:
        f = open("carti_test.txt", "w")
        f.write("")
        f.close()

    def test_adauga_carte(self):
        self.__contr.adauga_carte(13, "mama", "mama", 2009)
        self.assertEqual(len(self.__repo.load_from_file()), 2)

    def test_modifica_carte(self):
        self.__contr.modifica_carte("2", "mircea")
        list = self.__repo.load_from_file()
        self.assertEqual(list[0].get_autor(), "mircea")
        self.assertEqual(list[1].get_autor(), "mircea")

    def test_undo(self):
        self.__contr.adauga_carte(55, "titlu", "autor", 1900)
        self.__contr.modifica_carte("2", "mircea")
        list = self.__repo.load_from_file()
        self.assertEqual(list[0].get_autor(), "mircea")
        self.assertEqual(list[1].get_autor(), "mircea")
        self.__contr.undo()
        list = self.__repo.load_from_file()
        self.assertEqual(list[0].get_autor(), "mama")
        self.assertEqual(list[1].get_autor(), "ma")

        self.assertEqual(len(self.__repo.load_from_file()), 3)
        self.__contr.undo()
        self.assertEqual(len(self.__repo.load_from_file()), 2)


    def test_modifica_filtru(self):
        self.fail()

    def test_aplica_filtru(self):
        self.fail()
