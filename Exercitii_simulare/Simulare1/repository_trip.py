class Repository_trip:
    """
    Entitate abstracata de date de tipul Repository_trip
    """
    def __init__(self):
        self.__trips = []

    def get_all_trips(self):
        """
        :return: lista de escursii
        """
        return self.__trips[:]

    def add_trip(self, trip):
        """
        Adauga in lista un obiect de tipul trip
        :param trip:
        :return: None
        """
        self.__trips.append(trip)

    def __len__(self):
        """
        Defineste operatprul len
        :return: Lungimea listei
        """
        return len(self.__trips)