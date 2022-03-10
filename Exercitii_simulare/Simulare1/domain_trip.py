class Trip:
    """
    Etitate abstracta de date de tipul Trip
    """
    def __init__(self, locatie, data, nr_locuri):
        self.__locatie = locatie
        self.__data = data
        self.__nr_locuri = nr_locuri

    def get_locatie(self):
        """
        :return: locatia (string)
        """
        return self.__locatie

    def get_data(self):
        """
        :return: data (string)
        """
        return self.__data

    def get_nr_locuri(self):
        """
        :return: nr_locuri (int)
        """
        return self.__nr_locuri

    def set_locatie(self, other):
        """
        Seteaza locatia cu o alta valoare
        :param other:
        :return: None
        """
        self.__locatie = other

    def set_data(self, other):
        """
        Seteaza data cu o alta valoare
        :param other:
        :return: None
        """
        self.__data = other

    def set_nr_locuri(self, other):
        """
        Seteaza nr_locuri cu o alta valoare
        :param other:
        :return: None
        """
        self.__nr_locuri = other

    def __str__(self):
        """
        Defineste functionalitatea str
        :return: un string
        """
        return "Locatia: "+self.get_locatie()+" // "+"Data: "+self.get_data()+" // "+"Numarul de locuri: " \
                ""+str(self.get_nr_locuri())

    def __eq__(self, other):
        """
        Defineste functionalitatea ==
        :param other:
        :return: True, False
        """
        return self.get_locatie() == other.get_locatie()