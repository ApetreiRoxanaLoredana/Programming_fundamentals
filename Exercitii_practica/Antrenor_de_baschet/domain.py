from errors import ValidatorException


class Jucator:
    def __init__(self, nume, prenume, inaltime, post):
        """
        :param nume: string
        :param prenume: string
        :param inaltime: int
        :param post: string
        """
        self.__nume = nume
        self.__prenume = prenume
        self.__inaltime = inaltime
        self.__post = post

    def get_nume(self):
        """
        :return: nume - string
        """
        return self.__nume

    def get_prenume(self):
        """
        :return: prenume - string
        """
        return self.__prenume

    def get_inaltime(self):
        """
        :return: inaltime - int
        """
        return self.__inaltime

    def get_post(self):
        """
        :return: post - string
        """
        return self.__post

    def __str__(self):
        """
        Defineste operatorul str
        :return: string
        """
        return self.__nume+", "+self.__prenume+", "+str(self.__inaltime)+", "+self.__post


class JucatorValidator:
    def valideaza(self, jucator):
        """
        Arunca ValidatorException daca jucatorul nu e conform
        :param jucator: Jucator
        :return: None
        """
        errors = ""
        if jucator.get_nume() == "":
            errors += "Numele nu poate fi vid\n"
        if jucator.get_prenume() == "":
            errors += "Prenumele nu poate fi vid\n"
        if jucator.get_post() != "Fundas" and jucator.get_post() != "Pivot" and jucator.get_post() != "Extrema":
            errors += "Postul nu e corect\n"
        if jucator.get_inaltime() < 0:
            errors += "Inaltimea nu poate fi negativa\n"
        if len(errors) > 0:
            raise ValidatorException(errors)