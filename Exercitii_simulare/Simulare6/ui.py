class Consola:
    """
    Entitate abstracta de tipul Consola
    """
    def __init__(self, contr_bici):
        self.__contr = contr_bici
        self.__meniu = {
            "1":[self.__sterge_tip, "1 - Sterge tip"],
            "2":[self.__sterge_max, "2 - Sterge max"],
            "x":[None, "x - Exit"]
        }

    def run(self):
        """
        Controleaza comenzile introduse de utilizator si apeleaza
        functiile necesare pentru a indeplini comanda
        :return:
        """
        while True:
            self.__afiseaza_meniu()
            cmd = input("Introdu comanda->")
            cmd = cmd.strip()
            if cmd == "x":
                print("Ai iesit din aplicatie!\n")
                return
            try:
                self.__meniu[cmd][0]()
            except KeyError:
                print("Comanda invalida!\n")
            except ValueError:
                print("Valoare invalida!\n")


    def __afiseaza_meniu(self):
        """
        Afiseaza meniul cu comenzi
        :return:
        """
        for i in self.__meniu:
            print(self.__meniu[i][1])

    def __sterge_tip(self):
        """
        Citeste tipul unei biciclete(string)
        Sterge din fisier bicicletele cu tipul respetiv
        :return:
        """
        tip = input("Introdu tipul bicicletei->")
        self.__contr.sterge_tip(tip)

    def __sterge_max(self):
        """
        Sterge din fisier bicicletele cu pretul maxim
        :return:
        """
        self.__contr.sterge_max()