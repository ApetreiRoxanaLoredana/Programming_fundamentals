from errors import RepoException, ControllerException


class EmisiuneUi:
    """
    Entitate abstracta de tipul EmisiuneUi
    """
    def __init__(self, contr):
        self.__contr = contr
        self.__meniu = {
            "1":[self.__sterge, "1 - Sterge emisiune"],
            "2":[self.__modifica, "2 - Modifica emisiune"],
            "3":[self.__genereaza, "3 - Genereaza program"],
            "4":[self.__adauga_emisiune_blocata, "4 - Blocheaza un tip de emisiune"],
            "5":[self.__sterge_emisiune_blocata, "5 - Sterge un tip de emisiune blocat"],
            "6":[self.__reseteaza_emisiune_blocata, "6 - Reseteaza lista de emisiuni blocate"],
            "x":[None, "x - Exit"]
        }

    def __print_meniu(self):
        """
        Afiseaza meniul
        :return: None
        """
        for i in self.__meniu:
            print(self.__meniu[i][1])

    def run(self):
        """
        Apeleaza functiile necesare pentru a indeplini comenzile
        date de utilizator
        Prinde erorile
        :return: None
        """
        while True:
            self.__print_meniu()
            cmd = input("Introdu comanda->")
            if cmd == "x":
                print("La revedere!\n")
                return
            try:
                self.__meniu[cmd][0]()
            except RepoException as re:
                print(re)
            except ControllerException as ce:
                print(ce)
            except KeyError:
                print("Comanda invalida\n")
            except ValueError:
                print("Comanda invalida\n")
            except IndexError:
                print("Comanda invalida\n")

    def __sterge(self):
        """
        Citeste numele si tipul emisiunii
        Sterge din fisier emisiunea cu numele si tipul respectiv
        :return: None
        """
        nume = input("Nume->")
        tip = input("Tip->")
        self.__contr.sterge_emisiune(nume, tip)

    def __modifica(self):
        """
        Citeste numele, tipul durata si descrierea unei emisiunii
        Modifica durata si descrierea emisiunii cu tipul si numele respectiv
        :return: None
        """
        nume = input("Nume->")
        tip = input("Tip->")
        durata = int(input("Durata->"))
        descriere = input("Descriere->")
        self.__contr.modifica_emisiune(nume, tip, durata, descriere)

    def __adauga_emisiune_blocata(self):
        """
        Citeste un tip de emisiune
        Il adauga in lista de emisiuni blocate
        :return: None
        """
        tip = input("Tip->")
        self.__contr.adauga_bloc(tip)

    def __sterge_emisiune_blocata(self):
        """
        Citeste un tip de emisiune
        Sterge tipul emisiunii din lista de blocate
        :return: None
        """
        tip = input("Tip->")
        self.__contr.sterge_bloc(tip)

    def __reseteaza_emisiune_blocata(self):
        """
        Citeste un tip de emisiune
        Reseteaza lista de tipuri de emisiuni blocate
        :return: None
        """
        self.__contr.reseteaza_bloc()

    def __genereaza(self):
        """
        Citeste ora de inceput si de inal
        Afiseaza random un program tv
        :return: None
        """
        ora_inceput = int(input("Ora de inceput->"))
        ora_final = int(input("Ora de final->"))
        lista = self.__contr.genereaza_program(ora_inceput, ora_final)
        for i in lista:
            print(i)
