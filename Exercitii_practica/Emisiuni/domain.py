class Emisiune:
    """
    Entitate abstracta de tipul Emisiune
    """
    def __init__(self, nume, tip, durata, descriere):
        self.__nume = nume
        self.__tip = tip
        self.__durata = durata
        self.__descriere = descriere

    def get_nume(self):
        """
        :return: nume (string)
        """
        return self.__nume

    def get_tip(self):
        """
        :return: tip (string)
        """
        return self.__tip

    def get_durata(self):
        """
        :return: durata (int)
        """
        return self.__durata

    def get_descriere(self):
        """
        :return:descriere (string)
        """
        return self.__descriere

    def set_descriere(self, other):
        """
        Modifica descrierea emisiunii
        :param other: string
        :return:None
        """
        self.__descriere = other

    def set_durata(self, other):
        """
        Modifica ora emisiunii
        :param other: int
        :return: None
        """
        self.__durata = other

    def __str__(self):
        """
        Defineste operatorul str
        :return: string
        """
        return str(self.__durata)+","+self.__nume+", "+self.__tip+", "+self.__descriere

    def __eq__(self, other):
        return self.__nume == other.__nume and self.__tip == other.__tip