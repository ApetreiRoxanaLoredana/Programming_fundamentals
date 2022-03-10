class Student:
    def __init__(self, id, name):
        """
        :param id: int
        :param name: string
        """
        self.__id = id
        self.__name = name

    def get_id(self):
        """
        :return: id - int
        """
        return self.__id

    def get_name(self):
        """
        :return: name - string
        """
        return self.__name

    def __str__(self):
        """
        Defineste operatorul str
        :return: string
        """
        return str(self.__id)+", "+self.__name

class Laborator:
    def __init__(self, id_st, lab_nr, nr_problemei):
        """
        :param id_st: int
        :param lab_nr: int
        :param nr_problemei: string
        """
        self.__id_st = id_st
        self.__lab_nr = lab_nr
        self.__nr_problemei = nr_problemei

    def get_id_st(self):
        """
        :return: id_st - int
        """
        return self.__id_st

    def get_lab_nr(self):
        """
        :return: lab_nr - int
        """
        return self.__lab_nr

    def get_nr_problemei(self):
        """
        :return: nr_problemei - string
        """
        return self.__nr_problemei

    def __str__(self):
        """
        Defineste operatorul str
        :return: string
        """
        return str(self.__id_st)+", "+str(self.__lab_nr)+", "+self.__nr_problemei