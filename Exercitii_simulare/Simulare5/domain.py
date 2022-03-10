class Coffee:
    """
    Entitate abstracta de tipul Coffee
    """
    def __init__(self, nume, tara_de_origine, pret):
        self.__nume = nume
        self.__tara = tara_de_origine
        self.__pret = pret

    def get_nume(self):
        """
        :return: numele cafelei (string)
        """
        return self.__nume

    def get_tara(self):
        """
        :return: Tara de origine a cafelei (string)
        """
        return self.__tara

    def get_pret(self):
        """
        :return: Pretul cafelei (float)
        """
        return self.__pret

    def __str__(self):
        """
        Defineste operatorul str
        :return: un string cu informatiile despre cafea
        """
        return self.__nume+" // "+self.__tara+" // "+str(self.__pret)