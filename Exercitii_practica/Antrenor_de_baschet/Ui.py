from errors import ValidatorException, RepoException


class JucatoriUi:
    def __init__(self, contr):
        """
        :param contr: JucatoriController
        """
        self.__contr = contr
        self.__meniu = {
            "1":[self.__adauga_jucator, "1 - Adauga un jucator"],
            "2":[self.__modifica_jucator, "2 - Modifica jucator"],
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
        Apeleaza functiile necesare pentru a indeplinii comenzile date de utilizator
        Prinde si afiseaza erorile
        :return: None
        """
        while True:
            self.__print_meniu()
            cmd = input("Comanda->")
            if cmd == "x":
                print("La revedere\n")
                return
            try:
                self.__meniu[cmd][0]()
            except ValidatorException as ve:
                print(ve)
            except RepoException as re:
                print(re)
            except KeyError:
                print("Comanda invalida\n")
            except ValueError:
                print("Valoare invalida")

    def __adauga_jucator(self):
        """
        Citeste numele, prenumele, inaltimea si postul unui jucator
        Adauga jucatorul in fisier
        :return: None
        """
        nume = input("Nume->")
        prenume = input("Prenume->")
        inaltime = int(input("Inaltime->"))
        post = input("Post->")
        self.__contr.adauga_jucator(nume, prenume, inaltime, post)
        print("Adaugare cu succes\n")

    def __modifica_jucator(self):
        """
        Citeste un numele, prenumele si inaltimea unui jucator
        Arunca ValidatorException daca jucatorul nu e conform
        Arunca RepoException daca nu exista jucatorul
        :return:
        """
        nume = input("Nume->")
        prenume = input("Prenume->")
        inaltime = int(input("Inaltime->"))
        self.__contr.modifica_jucator(nume, prenume, inaltime)
        print("Modificare cu succes\n")