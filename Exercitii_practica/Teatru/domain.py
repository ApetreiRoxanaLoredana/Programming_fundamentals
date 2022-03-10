from errors import ValidatorException


class Piesa:
    def __init__(self, titlu, regizor, gen, durata):
        """
        :param titlu: string
        :param regizor: string
        :param gen: string
        :param durata: int
        """
        self.__titlu = titlu
        self.__regizor = regizor
        self.__gen = gen
        self.__durata = durata

    def get_titlu(self):
        """
        :return: titlu - string
        """
        return self.__titlu

    def get_regizor(self):
        """
        :return: regizor - string
        """
        return self.__regizor

    def get_gen(self):
        """
        :return: gen - string
        """
        return self.__gen

    def get_durata(self):
        """
        :return: durata - int
        """
        return self.__durata

    def __str__(self):
        """
        Defineste operatorul str
        :return: string
        """
        return self.__titlu+", "+self.__regizor+", "+self.__gen+", "+str(self.__durata)

class PiesaValidator:
    def valideaza(self, piesa):
        """
        Arunca ValidatorExceptiondaca obiectul de tipul Piesa nu este conform
        :param piesa: Piesa
        :return: None
        """
        errors = ""
        if piesa.get_titlu() == "":
            errors += "Titlul nu poate fi vid\n"
        if piesa.get_regizor() == "":
            errors += "Numele regizotului nu poate fi vid\n"
        if piesa.get_durata() < 0:
            errors += "Durata nu poate fi negativa\n"
        if piesa.get_gen() != "Comedie" and piesa.get_gen() != "Drama" and piesa.get_gen() != "Satira" and piesa.get_gen() != "Altele":
            errors += "Genul nu e corect\n"

        if len(errors) > 0:
            raise ValidatorException(errors)