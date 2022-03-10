class Consola:
    """
    Entitate abstracta de tipul Consola
    """
    def __init__(self, contr_coffee):
        self.__contr = contr_coffee
        self.__meniu = {
            "1":[self.__suma_preturi, "1 - Suma preturi"],
            "2":[self.__sortare, "2 - Sortare"],
            "x":[None, "x - Exit"]
        }

    def run(self):
        """
        Controleaza comenzile introduse de utilizator si apeleaza functiile necesare
        pentru a realiza comanda
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
            except ValueError:
                print("Valoare invalida!\n")
            except KeyError:
                print("Comanda invalida!\n")

    def __afiseaza_meniu(self):
        """
        Afiseaza meniul comenzilor
        :return:
        """
        for i in self.__meniu:
            print(self.__meniu[i][1])

    def __suma_preturi(self):
        """
        Citeste o tara (string)
        Afiseaza suma tuturor preturilor cafelelor din aceea tara
        :return:
        """
        tara = input("Introdu o tara->")
        suma = self.__contr.suma_preturi(tara)
        if suma == 0:
            print("Nu exista nici o cafea din aceasta tara!\n")
        else:
            print(suma)

    def __sortare(self):
        """
        Afiseaza o lista cu tarile de origine a cafelelor si suma totala a cafelelor din tara
        respetiva
        :return:
        """
        dic = self.__contr.sortare()
        for i in dic:
            print(i)