from domain import Movie


class MovieController:
    """
    Entitate abstracta de tipul MovieController
    """
    def __init__(self, MovieRepository, MovieValidator):
        self.__movieRepository = MovieRepository
        self.__movieValidator = MovieValidator

    def getAll(self):
        """
        :return: Lista cu toate filmele
        """
        return self.__movieRepository.getAll()

    def update(self, id, name, price, seats):
        """
        Modifica filmul cu id-ul respectiv
        Seteaza atributele filmului cu name, price si seats
        :param id: int
        :param name: string
        :param price: float
        :param seats: int
        :return: None
        """
        new_movie = Movie(id, name, price, seats)
        self.__movieValidator.valideaza(new_movie)

        self.__movieRepository.update(new_movie)