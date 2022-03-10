class Bicycle:
    """
    Entitate abstracta de tipul Bicycle
    """
    def __init__(self, code, type, price):
        self.__code = code
        self.__type = type
        self.__price = price

    def get_code(self):
        """
        :return: Codul bicicletei
        """
        return self.__code

    def get_type(self):
        """
        :return: Tipul icicletei
        """
        return self.__type

    def get_price(self):
        """
        :return: Pretul bicicletei
        """
        return self.__price

    def set_price(self, other):
        """
        Seteaza pretul bicicletei cu o alta valoare
        :param other:
        :return:
        """
        self.__price = other

    def __str__(self):
        """
        Defineste operatorul str
        :return: un string
        """
        return str(self.__code)+" // "+self.__type+" // "+str(self.__price)

    def __eq__(self, other):
        """
        Defineste operatorul ==
        :param other:
        :return: True sau False
        """
        return self.__code == other.__code