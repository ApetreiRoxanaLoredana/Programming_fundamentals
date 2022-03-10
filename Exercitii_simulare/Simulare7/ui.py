from domain import ValidatorException
from repository import RepoException


class Console:
    def __init__(self, contr_airport):
        self.__contr = contr_airport
        self.__meniu = {
            "1":[self.__afiseaza_zboruri, "1 - Afiseaza"],
            "2":[self.__sterge, "2 - Sterge"],
            "x":[None, "x - Exit"]
        }

    def run(self):
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
            except ValueError:
                print("Valoare invalida!\n")


    def __afiseaza_meniu(self):
        for i in self.__meniu:
            print(self.__meniu[i][1])

    def __afiseaza_zboruri(self):
        list = self.__contr.get_all_flights()

        if len(list) != 0:
            for i in list:
                print(i)
        else:
            print("Nu exista nici un zbor!\n")

    def __sterge(self):
        company_name = input("Introdu numele companiei->")
        self.__contr.remove_flights(company_name)