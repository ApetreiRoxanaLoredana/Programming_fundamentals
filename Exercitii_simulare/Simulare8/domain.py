class Movie:
    """
    Entitate abstracta de tipul Movie
    """
    def __init__(self, id, name, price, booked_seats):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__booked_seats = booked_seats

    def getID(self):
        """
        :return: id - int
        """
        return self.__id

    def getName(self):
        """
        :return: name - string
        """
        return self.__name

    def getPrice(self):
        """
        :return: price - float
        """
        return self.__price

    def getBookedSeats(self):
        """
        :return: booked seats - int
        """
        return self.__booked_seats

    def __eq__(self, other):
        """
        Defineste operatorul eq
        :param other:
        :return:
        """
        return self.__id == other.__id

    def __str__(self):
        """
        Defineste operatorul str
        :return:
        """
        return str(self.__id)+","+self.__name+","+str(self.__price)+","+str(self.__booked_seats)

