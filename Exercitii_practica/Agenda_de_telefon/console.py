from errors import ValidatorException, RepoException


class AgendaUI:
    """
    Entitate abstracta de tipul AgendaUI
    """
    def __init__(self, contr_agenda):
        self.__contr = contr_agenda
        self.__meniu = {
            "1":[self.__adauga_contact, "1 - Adauga un contact nou"],
            "2":[self.__cauta_nume, "2 - Cauta dupa dume"],
            "3":[self.__afiseaza_contacte_grup, "3 - Afiseaza contacte dupa grup"],
            "4":[self.export_CSV, "4 - Export"],
            "x":[None, "x - Exit"]
        }

    def run(self):
        """
        Apeleaza functiile necesare pentru a indeplini comanda data de utilizator
        :return: None
        """
        while True:
            self.__afiseaza_meniu()
            cmd = input("Introdu comanda->")
            cmd = cmd.strip()
            if cmd == "x":
                print("La revedere!")
                return
            try:
                self.__meniu[cmd][0]()
            except ValidatorException as val:
                print(val)
            except RepoException as re:
                print(re)
            except IndexError:
                print("Comanda invalida!\n")
            except KeyError:
                print("Comanda invalida!\n")
            except ValueError:
                print("Valoare invalida!\n")

    def __afiseaza_meniu(self):
        """
        Afiseaza meniul
        :return: None
        """
        for i in self.__meniu:
            print(self.__meniu[i][1])

    def __adauga_contact(self):
        """
        Adauga in agenda un contact nou
        :return: None
        """
        id = int(input("Id->"))
        name = input("Nume->")
        phoneNr = input("Numar de telefon->")
        group = input("Grup->")
        self.__contr.addContact(id, name, phoneNr, group)
        print("Adaugare cu succes!\n")

    def __cauta_nume(self):
        """
        Cauta un contact dupa numele acestuia
        Arunca eroare daca nu gaseste contactul
        :return: None
        """
        name = input("Nume->")
        cont = self.__contr.lookup(name)
        print(cont)

    def __afiseaza_contacte_grup(self):
        """
        Citeste un grup
        Afiseaza toate contactele din acel grup
        :return: None
        """
        group = input("Grup->")
        list_cont = self.__contr.lookupAll(group)
        for i in list_cont:
            print(i)

    def export_CSV(self):
        """
        Citeste un grup
        Exporta intr-un fisier CSV contactele care au grupul respectiv
        :return: None
        """
        group = input("Grup->")
        self.__contr.exportCSV(group, "CSV.txt")