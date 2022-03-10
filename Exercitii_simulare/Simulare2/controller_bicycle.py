from domain_bicycle import Bicycle

class Controller_bike:
    """
    Entitate abstracta de tipul Controller_bike
    """
    def __init__(self, repo_bike, val_bike):
        self.__repo = repo_bike
        self.__val = val_bike

    def apply_discount(self, type, procent):
        """
        Aplica o reducere de procent la bicicletele de tipul type
        :param type:
        :param procent:
        :return:
        """
        list = self.__repo.get_by_type(type)
        for i in list:
            new_price = i.get_price() - (procent/100*i.get_price())
            i.set_price(new_price)
            self.__repo.update(i.get_code(), i)

    def get_all_bike(self):
        """
        :return: Lista cu toate bicicletele
        """
        return self.__repo.get_all_bike()