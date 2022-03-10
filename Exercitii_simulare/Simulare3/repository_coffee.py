from domain_coffee import Coffee

class Repo_Coffee:
    """
    Entitate abstracta de tipul Repo_coffee
    """
    def __init__(self, nume_fisier):
        self.__list = []
        self.__nume_fisier = nume_fisier

    def get_all(self):
        """
        Incarca informatiile din fisier in memorie
        :return: lista cu cafele
        """
        rez = []

        with open(self.__nume_fisier, "r") as f:
            for line in f:
                line = line.strip()
                line = line.split(", ")
                cof = Coffee(line[0], line[1], float(line[2]))
                rez.append(cof)
        return rez
