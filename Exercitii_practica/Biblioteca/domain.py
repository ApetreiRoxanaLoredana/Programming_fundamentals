import datetime

from errors import ValidatorException


class Carte:
    """
    Ebtitate abstracta de tipul Carte
    """
    def __init__(self, id, titlu, autor, an_aparitie):
        """
        :param id: int
        :param titlu: string
        :param autor: string
        :param an_aparitie: int
        """
        self.__id = id
        self.__titlu = titlu
        self.__autor = autor
        self.__an_aparitie = an_aparitie

    def get_id(self):
        """
        :return: id -ul (int)
        """
        return self.__id

    def get_titlu(self):
        """
        :return: titlul (string)
        """
        return self.__titlu

    def get_autor(self):
        """
        :return: autor (string)
        """
        return self.__autor

    def get_an_aparitie(self):
        """
        :return: anul aparitiei (int)
        """
        return self.__an_aparitie

    def __str__(self):
        """
        Defineste operatorul str
        :return: string
        """
        return str(self.__id)+", "+self.__titlu+", "+self.__autor+", "+str(self.__an_aparitie)

class Undo:
    """
    Entitate abstracta de tipul Undo
    """
    def __init__(self, status, lista_carti):
        """
        :param status: adaugat/modificat string
        :param carte: Carte
        """
        self.__status = status
        self.__lista_carti = lista_carti

    def get_status(self):
        """
        :return: status - string
        """
        return self.__status

    def get_lista_carti(self):
        """
        :return: carte -Carte
        """
        return self.__lista_carti

class CarteValidator:
    """
    Entitate abstracta de tipul BiblioValidator
    """
    def valideaza(self, carte):
        """
        Arunca ValidatorException daca obiectul carte nu e conform
        :param carte: Carte
        :return: None
        """
        errors = ""
        if carte.get_id() < 0:
            errors += "Id invalid\n"
        if carte.get_an_aparitie() < 1000 or carte.get_an_aparitie() > 2021:
            errors += "An invalid\n"
        if len(errors) > 0:
            raise ValidatorException(errors)

class Filtru:
    """
    Entitate abstracta de tipul Filtru
    """
    def __init__(self, text, numar):
        """
        :param text: string
        :param numar: int
        """
        self.__text = text
        self.__numar = numar

    def get_text(self):
        """
        :return: text
        """
        return self.__text

    def get_numar(self):
        """
        :return: numar
        """
        return self.__numar

    def set_text(self, other):
        """
        Modifica textul
        :return:
        """
        self.__text = other

    def set_numar(self, other):
        """
        modifica numarul
        :param other: int
        :return: None
        """
        self.__numar = other
