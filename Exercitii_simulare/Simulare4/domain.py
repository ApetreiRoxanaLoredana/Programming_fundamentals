class Bere:
    """
    Entitate abstracta de tipul Bere
    """
    def __init__(self, nume, tip, pret):
        self.__nume = nume
        self.__tip = tip
        self.__pret = pret

    def get_nume(self):
        """
        :return: numele berii
        """
        return self.__nume

    def get_tip(self):
        """
        :return: tipul berii
        """
        return self.__tip

    def get_pret(self):
        """
        :return: pretul berii
        """
        return self.__pret

    def get_id(self):
        """
        :return:un string format din nume si tip despartite prin spatiu
        """
        return self.__nume+" "+self.__tip