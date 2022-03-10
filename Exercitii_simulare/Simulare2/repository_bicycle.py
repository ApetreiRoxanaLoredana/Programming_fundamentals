from domain_bicycle import Bicycle
from errors import RepoException

class Repository_bike:
    """
    Entitate abstracta de tipul Repository_bike
    """
    def __init__(self):
        self.__list = [Bicycle(10, "Monten", 100.5), Bicycle(9, "Monten", 150),
                       Bicycle(8, "Monten", 50), Bicycle(6, "Tango", 88)]

    def update(self, code, bike):
        """
        Modifica bicicleta cu codul respectiv
        :param code:
        :param bike:
        :return:None
        """
        for i in self.__list:
            if i.get_code() == code:
                i = bike

    def get_by_type(self, type):
        """
        :param type:
        :return: Returneaza lista de biciclete care au tipul type
        """
        rez = []
        ok = False
        for i in self.__list:
            if i.get_type() == type:
                rez.append(i)
                ok = True
        if ok == False:
            raise RepoException("Nu exista nici o bicicleta de acest tip!\n")
        return rez

    def get_all_bike(self):
        """
        :return: Lista cu toate bicicletele
        """
        return self.__list

