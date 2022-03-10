from errors import ValidatorException

class Validator_bike:
    """
    Entitate abstracta de tipul Validator_bike
    """
    def valideaza(self, bike):
        """
        Verifica daca bicicleta este corecta
        :param bike:
        :return: Arunca exceptii daca nu e conforma bicicleta
        """
        errors = ""
        if bike.get_code() == "":
            errors += "Codul nu poate fi vid!\n"

        if bike.get_type() == "":
            errors += "Tipul nu poate fi vid!\n"

        if bike.get_price() == "":
            errors += "Pretul nu poate fi vid!\n"

        if bike.get_price() != "" and  bike.get_price() <= 0:
            errors += "Pret invalid!\n"

        if len(errors) > 0:
            raise ValidatorException(errors)