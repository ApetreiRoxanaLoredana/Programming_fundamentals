from errors import ValidatorException
from datetime import datetime

class Validator_trip:
    def valideaza(self, trip):
        """
        Verifica daca obiectul de tipul Trip este corect
        :param trip:
        :return: o lista de erori
        """
        errors = ""
        if trip.get_nr_locuri() <= 0:
            errors += "Valoare invalida!\n"
        try:
            data =trip.get_data().split(".")
            data = datetime(int(data[2]), int(data[1]), int(data[0]))
        except ValueError:
            errors += "Data invalida!\n"
        except IndexError:
            errors += "Data invalida!\n"
        except TypeError:
            errors += "Data invalida!\n"
        if trip.get_locatie() == "":
            errors += "Locatia nu poate fi vida!\n"

        if len(errors) > 0:
            raise ValidatorException(errors)
