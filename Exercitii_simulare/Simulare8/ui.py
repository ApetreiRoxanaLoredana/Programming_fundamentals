from repository import RepoException
from validator import ValidatorException


class MoviesUI:
    """
    Entitate abstracat de tipul MovieUi
    """
    def __init__(self, MovieController):
        self.__movieController = MovieController
        self.__meniu = {
            "1":[self.__afiseaza_filme, "1 - Afiseaza"],
            "2":[self.__modifica_film, "2 - Modifica"],
            "x":[None, "x - Exit"]
        }

    def run(self):
        """
        Controleaza comenziile date de utilizator si apeleaza
        functiile necesare indeplinirii comenzii
        Prinde si afiseaza exceptiile(daca exista)
        :return:
        """
        while True:
            self.__afiseaza_meniu()
            cmd = input("Introdu comanda->")
            cmd.strip()
            if cmd == "x":
                print("Ai iesit din aplicatie!\n")
                return

            try:
                self.__meniu[cmd][0]()
            except ValidatorException as ve:
                print(ve)
            except RepoException as re:
                print(re)
            except KeyError:
                print("Comanda invalida!\n")

    def __afiseaza_meniu(self):
        """
        Afiseaza meniul comenzilor
        :return:
        """
        for i in self.__meniu:
            print(self.__meniu[i][1])

    def __afiseaza_filme(self):
        """
        Afiseaza lista de filme
        :return:
        """
        list = self.__movieController.getAll()
        for i in list:
            print(i)

    def __modifica_film(self):
        """
        Citeste id-ul filmului care trebuie modificat
        Citeste numele, pretul si numarul de locuri rezervate pe care sa
        le primeasca filmul cu id-ul respectiv
        :return:
        """
        id = int(input("Introdu id-ul filmului modificat->"))
        name = input("Introdu numele filmului->")
        price = float(input("Introdu pretul filmului->"))
        seats = int(input("Introdu numarul de locuri rezervale->"))
        self.__movieController.update(id, name, price, seats)