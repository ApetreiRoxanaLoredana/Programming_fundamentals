class Bicicleta:
    """
    Entitate abstracta de tipul Bicicleta
    """
    def __init__(self, id_bicicleta, tip, pret):
        self.__id = id_bicicleta
        self.__tip = tip
        self.__pret = pret

    def get_id(self):
        """
        :return: id-ul bicicletei(int)
        """
        return self.__id

    def get_tip(self):
        """
        :return: tipul bicicletei(string)
        """
        return self.__tip

    def get_pret(self):
        """
        :return: preturl biciletei(float)
        """
        return self.__pret