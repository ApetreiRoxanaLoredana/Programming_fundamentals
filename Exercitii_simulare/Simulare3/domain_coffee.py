class Coffee:
    """
    Entitate abstarcta de tipul Coffee
    """
    def __init__(self, nume, tara_de_origine, pret):
        self.__nume = nume
        self.__tara = tara_de_origine
        self.__pret = pret

    def get_nume(self):
        """
        :return: numele cafelei
        """
        return self.__nume

    def get_tara(self):
        """
        :return: tara de origine a cafelei
        """
        return self.__tara

    def get_pret(self):
        """
        :return: pretul cafelei
        """
        return self.__pret

    def __str__(self):
        """
        Defineste operatorul str
        :return: un string cu informatile despre cafea
        """
        return self.__nume+" // "+self.__tara+" // "+str(self.__pret)

    def __eq__(self, other):
        """
        Defineste operatorul eq
        :param other:
        :return: True sau False
        """
        return self.__nume == other.__nume