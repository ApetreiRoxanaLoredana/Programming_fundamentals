from unittest import TestCase

from domain import Movie
from repository import MovieRepository
from validator import ValidatorException, Validator_Movie


class TestMovie(TestCase):
    def setUp(self):
        self.__movie = Movie(12, "Hobbit", 12.5, 89)

    def test_get_id(self):
        self.assertEqual(self.__movie.getID(), 12)

    def test_get_name(self):
        self.assertEqual(self.__movie.getName(), "Hobbit")

    def test_get_price(self):
        self.assertEqual(self.__movie.getPrice(), 12.5)

    def test_get_booked_seats(self):
        self.assertEqual(self.__movie.getBookedSeats(), 89)

    def test_str(self):
        self.assertEqual(str(self.__movie), "12,Hobbit,12.5,89")

    def test_eq(self):
        movie = Movie(12, "", 0, 0)
        self.assertEqual(movie, self.__movie)


class TestMovieRepository(TestCase):

    def setUp(self):
        self.__repo = MovieRepository("filme_test.txt")

    def tearDown(self):
        self.__repo.update(Movie(14, "Anna", 15, 67))

    def test_get_all(self):
        list = self.__repo.getAll()
        self.assertEqual(len(list), 1)
        self.assertEqual(list[0].getID(), 14)
        self.assertEqual(list[0].getName(), "Anna")
        self.assertEqual(list[0].getPrice(), 15)
        self.assertEqual(list[0].getBookedSeats(), 67)

    def test_update(self):
        self.__repo.update(Movie(14, "Comoara", 20, 100))
        list = self.__repo.getAll()
        self.assertEqual(list[0].getID(), 14)
        self.assertEqual(list[0].getName(), "Comoara")
        self.assertEqual(list[0].getPrice(), 20)
        self.assertEqual(list[0].getBookedSeats(), 100)


class TestValidator_Movie(TestCase):
    def setUp(self):
        self.__val = Validator_Movie()

    def test_valideaza(self):

        movie = Movie(12, "Ana", 12, 809)

        self.assertRaisesRegex(ValidatorException, "Numarul locurilor rezervate trebuie sa fie in intervalul inchis 0, 100!\n", self.__val.valideaza, movie)
        movie = Movie(12, "Ana", -12, 90)
        self.assertRaisesRegex(ValidatorException, "Pretul trebuie sa fie in intervalul inchis 10, 20!\n", self.__val.valideaza, movie)
        movie = Movie("", "Anaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 12, 90)
        self.assertRaisesRegex(ValidatorException, "Id-ul nu poate fi vid!\n"
                                                   "Numele nu poate depasi 30 de caractere!\n", self.__val.valideaza, movie)
