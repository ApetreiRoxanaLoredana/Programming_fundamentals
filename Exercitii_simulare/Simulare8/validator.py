class ValidatorException(Exception):
    pass


class Validator_Movie:
    """
    Entitate abstarcta de tipul Validator Movie
    """
    def valideaza(self, movie):
        """
        Verifica daca obiectul movie este conform cerintei
        Altfel arunca ValidatorException
        :param movie: obiect de tipul movie
        :return: arunca un string care contine toate erorile
        """
        errors = ""
        if movie.getID() == "":
            errors += "Id-ul nu poate fi vid!\n"
        if movie.getName() == "":
            errors += "Numele nu poate fi vid!\n"
        if len(movie.getName()) > 30:
            errors += "Numele nu poate depasi 30 de caractere!\n"
        if movie.getPrice() < 10 or movie.getPrice() > 20:
            errors += "Pretul trebuie sa fie in intervalul inchis 10, 20!\n"
        if movie.getBookedSeats() < 0 or movie.getBookedSeats() > 100:
            errors += "Numarul locurilor rezervate trebuie sa fie in intervalul inchis 0, 100!\n"
        
        if len(errors) > 0:
            raise ValidatorException(errors)