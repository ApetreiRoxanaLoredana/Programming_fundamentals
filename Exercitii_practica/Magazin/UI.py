from errors import ValidatorException, RepoException


class MagazinUi:
    def __init__(self, contr):
        """
        :param contr: MagazinController
        """
        self.__contr = contr
        self.__meniu = {
            "1":[self.__adauga_produs, "1 - Adauga produs"],
            "2":[self.__sterge_produse, "2 - Sterge produse"],
            "3":[self.__modifica_filtru, "3 - Seteaza filtru"],
            "4":[self.__undo, "4 - Undo"],
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
        Apeleaza functiile necesare pentru a indeplini comenziile date de utilizator
        Prinde si afiseaza erorile
        :return: None
        """
        while True:
            self.__print_meniu()
            print(self.__contr.get_filtru())
            self.__afiseaza_lista_filtrata()
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
                print("Valoare invalida\n")

    def __adauga_produs(self):
        """
        Citeste id-ul, denumirea si pretul unui produs
        Adauga produsul in fisier
        Arunca ValidatorException daca produsul nu e conform
        Arunca RepoException daca exista deja un produs cu acest id
        :return: None
        """
        id = int(input("Id->"))
        denumire = input("Denumire->")
        pret = float(input("Pret->"))
        self.__contr.adauga_produs(id, denumire, pret)
        print("Adaugare cu succes\n")

    def __sterge_produse(self):
        """
        Citeste o cifra
        Sterge toate produsele care au in id-ul lor cifra respectiva
        Afiseaza numarul de produse sterse
        Afiseaza un mesaj daca cifra nu exista in nici un id
        :return:
        """
        cifra = input("Cifra->")
        nr = self.__contr.sterge_produse(cifra)
        if nr == 0:
            print("Nu exista nici un produs care sa aiba aceasta cifra in id\n")
        else:
            print(nr, "produse au fost sterse")

    def __afiseaza_lista_filtrata(self):
        """
        Afiseaza lista de produse dupa filtrul actual
        :return: None
        """
        list = self.__contr.aplica_filtru()
        for produs in list:
            print(produs)

    def __modifica_filtru(self):
        """
        Citeste un text si un numar
        Modifica filtrul
        :return: None
        """
        text = input("Text->")
        numar = float(input("Numarul->"))
        self.__contr.modifica_filtru(text, numar)

    def __undo(self):
        """
        Adauga ultimele produse sterse anterior
        :return: None
        """
        self.__contr.undo_produse()
