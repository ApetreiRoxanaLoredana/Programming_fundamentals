from errors import ValidatorException, RepoException


class BiblioUi:
    """
    Entitate abstracta de tipul BiblioUi
    """
    def __init__(self, contr):
        """
        :param contr: BiblioController
        """
        self.__contr = contr
        self.__meniu = {
            "1":[self.__adauga, "1 - Adauga"],
            "2":[self.__modifica, "2 - Modifica"],
            "3":[self.__undo, "3 - Undo"],
            "4":[self.__modifica_filtru, "4 - Modifica filtru"],
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
        Apeleaza functiile necesare pentru a indeplini comenziile
        date de utilizator
        Prinde erorile si le afiseaza
        :return: None
        """
        while True:
            self.__print_meniu()
            self.__aplica_filtru()
            cmd = input("Introdu comanda->")
            if cmd == "x":
                print("La revedere!")
                return
            try:
                self.__meniu[cmd][0]()
            except ValidatorException as ve:
                print(ve)
            except RepoException as re:
                print(re)
            except ValueError:
                print("Comanda invalida\n")
            except KeyError:
                print("Comanda invalida!\n")

    def __adauga(self):
        """
        Citeste id-ul, titlul, autorul si anul aparitiei unei carti
        Adauga cartea in fisier
        :return: None
        """
        id = int(input("Id->"))
        titlu = input("Titlu->")
        autor = input("Autor->")
        an_aparitie = int(input("Anul aparitiei->"))
        self.__contr.adauga_carte(id, titlu, autor, an_aparitie)

    def __modifica(self):
        """
        Citeste o cifra si un autor
        Modifica autorul cartilor care au in id-ul lor cifra resepectiva
        :return: None
        """
        cifra = input("Cifra->")
        autor = input("Autor->")
        self.__contr.modifica_carte(cifra, autor)

    def __undo(self):
        """
        Reface ultima operatie efectuata
        :return:
        """
        self.__contr.undo()

    def __modifica_filtru(self):
        """
        Citeste un text si un numar
        Modifica filtrul
        :return: None
        """
        text = input("Text->")
        numar = int(input("Numar->"))
        self.__contr.modifica_filtru(text, numar)

    def __aplica_filtru(self):
        """
        Afiseaza lista de carti dupa filtru
        :return: None
        """
        list = self.__contr.aplica_filtru()
        for i in list:
            print(i)