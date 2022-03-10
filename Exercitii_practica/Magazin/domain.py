from errors import ValidatorException


class Produs:
    def __init__(self, id, denumire, pret):
        """
        :param id: int > 0
        :param denumire: string
        :param pret: float > 0
        """
        self.__id = id
        self.__denumire = denumire
        self.__pret = pret

    def get_id(self):
        """
        :return: id - int
        """
        return self.__id

    def get_denumire(self):
        """
        :return: dennumire - string
        """
        return self.__denumire

    def get_pret(self):
        """
        :return: pret - int
        """
        return self.__pret

    def __str__(self):
        """
        Defineste operatorul str
        :return: string
        """
        return str(self.__id)+", "+self.__denumire+", "+str(self.__pret)

class Filtru:
    def __init__(self, text, numar):
        """
        :param text: string
        :param numar: float
        """
        self.__text = text
        self.__numar = numar

    def get_text(self):
        """
        :return: text - string
        """
        return self.__text

    def get_numar(self):
        """
        :return: numar - float
        """
        return self.__numar

    def set_text(self, other):
        """
        :param other: string
        :return: None
        """
        self.__text = other

    def set_numar(self, other):
        """
        :param other: string
        :return: None
        """
        self.__numar = other

    def __str__(self):
        """
        Defineste operatorul str
        :return: string
        """
        return self.__text+", "+str(self.__numar)


class Undo:
    def __init__(self, list):
        """
        :param list: lista de produse sterse
        """
        self.__list = list

    def get_list(self):
        """
        :return: lista de produse sterse
        """
        return self.__list

    def set_list(self, other):
        """
        :param other: lista de produse
        :return: None
        """
        self.__list = other[:]

class ProdusValidator:
    def valideaza(self, produs):
        """
        Arunca ValidatorException daca produsul nu e conform
        :param produs: Produs
        :return: None
        """
        errors = ""
        if produs.get_id() < 0:
            errors += "Id-ul nu poate fi negativ\n"
        if produs.get_denumire() == "":
            errors += "Denumirea nu poate fi vida\n"
        if produs.get_pret() < 0:
            errors += "Pretul nu poate fi negativ\n"
        if len(errors) > 0:
            raise ValidatorException(errors)
