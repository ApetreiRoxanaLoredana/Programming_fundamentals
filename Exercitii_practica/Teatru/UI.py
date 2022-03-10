from errors import ValidatorException, RepoException


class TeatruUi:
    def __init__(self, contr):
        """
        :param contr: TeatruController
        """
        self.__contr = contr
        self.__meniu = {
            "1":[self.__adauga_piesa, "1 - Adauga piesa de teatru"],
            "2":[self.__modifica_piesa, "2 - Modifica piesa de teatru"],
            "3":[self.__genereaza_piese_random, "3 - Genereaza piese random"],
            "4":[self.__export_piese, "4 - Export"],
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
                print("Comanda invalida\n")

    def __adauga_piesa(self):
        """
        Citeste titlul, regizorul, genul si durata unei piese de teatru
        Adauga piesa
        Arunca ValidatorException daca piesa nu e conforma
        :return:None
        """
        titlu = input("Titlu->")
        regizor = input("Regizor->")
        gen = input("Gen->")
        durata = int(input("Durata->"))
        self.__contr.add_piesa(titlu, regizor, gen, durata)
        print("Adaugare cu succes\n")

    def __modifica_piesa(self):
        """
        Citeste titlul, regizorul, genul si durata unei piese de teatru
        Modifica piesa
        Arunca ValidatorException daca piesa nu e conforma
        Arunca REpoException daca nu exista nici o piesa cu titlul si regizorul respectiv
        :return: None
        """
        titlu = input("Titlu->")
        regizor = input("Regizor->")
        gen = input("Gen->")
        durata = int(input("Durata->"))
        self.__contr.modifica_piesa(titlu, regizor, gen, durata)
        print("Modificare cu succes\n")

    def __genereaza_piese_random(self):
        """
        Citeste un nr de piese
        Gnereaza random un nr de piese
        Le adauga in lista din fisier
        Le afiseaza pe ecran
        :return: None
        """
        nr = int(input("Numarul de piese->"))
        lista_piese = self.__contr.genereaza_piese(nr)
        self.__contr.add_mai_multe_piese(lista_piese)
        for i in lista_piese:
            print(i)

    def __export_piese(self):
        """
        Citeste un nume de fisier
        Exporta lista de piese ordonata alfabetic dupa regizor si titlu in fisierul respectiv
        :return: None
        """
        fisier = input("Numele fisierului->")
        self.__contr.exporta_piese(fisier)
        print("Export cu succes\n")