from errors import ValidatorException, RepoException

class UI:
    """
    Entitate abstracta de tipul UI
    """
    def __init__(self, contr_bike):
        self.__contr = contr_bike
        self.__meniu = {"1":[self.__afiseaza_biciclete, "1 - Afiseaza"],
                        "2":[self.__aplica_discount, "2 - Aplica discount"],
                        "x":[None, "x - Iesi din aplicatie"]
            }

    def run(self):
        """
        Controleaza comenzile date de utilizator si apeleaza functiile corespunzatoare
        :return:
        """
        while True:
            self.__afiseaza_meniu()
            cmd = input("Introdu comanda->").strip()
            if cmd == "x":
                print("Ai iesit din aplicatie")
                return
            try:
                self.__meniu[cmd][0]()
            except ValidatorException as ve:
                print(ve)
            except RepoException as re:
                print(re)
            except ValueError as ve:
                print(ve)


    def __afiseaza_meniu(self):
        """
        Afiseaza meniul
        :return:
        """
        for i in self.__meniu:
            print(self.__meniu[i][1])

    def __afiseaza_biciclete(self):
        """
        Afiseaza lista de biciclete
        :return:
        """
        list = self.__contr.get_all_bike()
        for i in list:
            print(i)

    def __aplica_discount(self):
        """
        Citeste tipul si procentul pentru reducere
        Afiseaza toate bicicletele al caror pret a fost modificat
        :return:
        """
        type = input("Introdu tipul bicicletei->")
        try:
            procent = int(input("Introdu procentul de reducere->"))
        except ValueError:
            raise ValueError("Procent invalid!\n")
        self.__contr.apply_discount(type, procent)
        list = self.__contr.get_all_bike()
        for i in list:
            print(i)
