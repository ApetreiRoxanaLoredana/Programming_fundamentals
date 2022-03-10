from errors import ValidatorException


class ContactValidator:
    """
    Entitate abstarcta de tipul Contact Validator
    """
    def valideaza(self, cont):
        """
        Verifica daca obiectul de tip contact indeplineste cerintele necesare
        Arunca eroare daca nu e conform
        :param: cont - obiect de tipul Contact
        :return:
        """
        errors = ""
        if int(cont.get_id()) < 0:
            errors += "Id ivalid!\n"
        if cont.get_id() == "":
            errors += "Id-ul nu poate fi vid!\n"
        if cont.get_name() == "":
            errors += "Numele nu poate fi vid!\n"
        if cont.get_group() != "Prieteni" and cont.get_group() != "Familie" and cont.get_group() != "Job" and cont.get_group() != "Altele":
            errors += "Grupul nu e corect!\n"
        if cont.get_phoneNr() == "":
            errors += "Numarul de telefon nu poate fi vid!\n"
        for i in cont.get_phoneNr():
            if i < "0" or i > "9":
                errors += "Numarul de telefon trebuie sa contina doar cifre!\n"
                break
        if len(errors) != 0:
            raise ValidatorException(errors)