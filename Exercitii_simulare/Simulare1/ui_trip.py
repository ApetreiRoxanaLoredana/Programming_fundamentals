from errors import ValidatorException, RepoException

class UI:
    """
    Entitate abstracta de date de tipul UI
    """
    def __init__(self, contr_trip):
        self.__meniu = {"1":[self.__afiseaza_trips, "1 - Afiseaza lista de excursii"],
                        "2":[self.__add_trip, "2 - Adauga excursie"],
                        "3":[self.__amana_excursii, "3 - Amana excursiile cu locurile cutare"],
                        "X":[self.run, "X - Iesi din aplicatie"]}
        self.__contr_trip = contr_trip

    def run(self):
        while True:
            self.__afiseaza_meniu()
            cmd = input("Inrtodu comanda->")
            cmd.strip()
            if cmd == "X":
                print("Ai iesit din aplicatie!")
                return
            if cmd in self.__meniu:
                try:
                    self.__meniu[cmd][0]()
                except ValidatorException as ve:
                    print(ve)
                except RepoException as re:
                    print(re)
                except ValueError:
                    print("Valoare invalida!\n")

    def __afiseaza_meniu(self):
        """
        Afiseaza meniul principal
        :return:
        """
        for i in self.__meniu:
            print(self.__meniu[i][1])

    def __add_trip(self):
        """
        Adauga o excursie
        :return:
        """
        locatie = input("Introdu locatia->")
        data = input("Introdu data->")
        nr_locuri = int(input("Introdu numarul de locuri->"))
        self.__contr_trip.add_trip(locatie, data, nr_locuri)

    def __afiseaza_trips(self):
        """
        Afiseaza excursile
        :return:
        """
        list = self.__contr_trip.get_trips()
        if len(list) == 0:
            print("Nu exista nici o excursie!\n")
        else:
            for t in list:
                print(t)

    def __amana_excursii(self):
        nr_locuri = int(input("Introdu numarul de locuri->"))
        list = self.__contr_trip.get_trips_locuri(nr_locuri)
        if len(list) != 0:
            for t in list:
                print(t)
        else:
            print("Nu exista nici o excusrie cu locuri mai multe!\n")