from errors import RepoException, ContrException


class Ui:
    def __init__(self, contr):
        """
        :param contr: Controller
        """
        self.__contr = contr
        self.__meniu = {
            "1":[self.__afiseaza_studenti, "1 - Afiseaza studenti"],
            "2":[self.__cauta_student, "2 - Cauta student dupa id"],
            "3":[self.__adauga_lab, "3 - Adauga un laborator"],
            "4":[self.__afiseaza_laboratoare_student, "4 - Afiseaza laboratoarele unui student"],
            "5":[self.__afiseaza_studenti_lab, "5 - Afiseaza studentii cu probleme la laboratorul cu numarul..."],
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
        Apeleaza funtiile necesare pentru a indeplini comnenziile date de utilizator
        Prinde si afiseaza erorile
        """
        while True:
            self.__print_meniu()
            cmd = input("Comanda->")
            if cmd == "x":
                print("La revedere !")
                return
            try:
                self.__meniu[cmd][0]()
            except RepoException as re:
                print(re)
            except ContrException as ce:
                print(ce)
            except KeyError:
                print("Comanda invalida!\n")

    def __afiseaza_studenti(self):
        """
        Afiseaza lista de studenti
        :return: None
        """
        lista_st = self.__contr.get_all_st()
        for st in lista_st:
            print(st)

    def __cauta_student(self):
        """
        Citeste un id
        Afiseaza studentul cu id ul respectiv
        :return:
        """
        id = int(input("Id->"))
        st = self.__contr.cauta_student(id)
        print(st)

    def __adauga_lab(self):
        """
        Citeste id_st, lab_nr, nr_problemei
        Adauga Laboratorul in lista
        :return: None
        """
        id_st = int(input("Id student->"))
        lab_nr = int(input("Laboratorul cu numarul->"))
        nr_problemei = input("Numarul problemei->")
        self.__contr.adauga_laborator(id_st, lab_nr, nr_problemei)

    def __afiseaza_laboratoare_student(self):
        """
        Citeste id ul unui student
        Afiseaza toate laboratoarele studentului
        :return: None
        """
        id = int(input("Id student->"))
        list = self.__contr.get_laboratoare_st(id)
        for lab in list:
            print(lab)

    def __afiseaza_studenti_lab(self):
        """
        Citeste numarul unui laborator
        Afiseaza toti studentii care au o problema la acel laborator
        :return: None
        """
        nr_lab = int(input("Numarul laboratorului->"))
        list = self.__contr.get_studenti_nr_lab(nr_lab)
        for st in list:
            print(st)
