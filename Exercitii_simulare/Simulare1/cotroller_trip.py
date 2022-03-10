from domain_trip import  Trip
from datetime import datetime, timedelta


class Controller_trip:
    """
    Entitate abstracta de date de tipul Controller_trip
    """
    def __init__(self, repo_trip, val_trip):
        self.__repo_trip = repo_trip
        self.__val_trip = val_trip

    def add_trip(self, locatie, data, nr_locuri):
        """
        Adauga o excurise in lista
        :param locatie:
        :param data:
        :param nr_locuri:
        :return:
        """
        trip = Trip(locatie, data, nr_locuri)
        self.__val_trip.valideaza(trip)
        self.__repo_trip.add_trip(trip)

    def get_trips(self):
        """
        :return: lista de excursii
        """
        return self.__repo_trip.get_all_trips()

    def get_trips_locuri(self, nr_locuri):
        """
        Returneaza o lista cu excursile a caror numar de locuri e mai mare deccat nr_locuri
        si modifica data lor scazand o zi
        :param nr_locuri:
        :return:
        """
        rez = []
        list_trips = self.__repo_trip.get_all_trips()
        for t in list_trips:
            if t.get_nr_locuri() > nr_locuri:
                data = t.get_data().split(".")
                data = datetime(int(data[2]), int(data[1]), int(data[0]))
                day = timedelta(1)
                data = data - day
                data = str(data.day)+"."+str(data.month)+"."+str(data.year)
                t.set_data(data)
                rez.append(t)
        return rez

