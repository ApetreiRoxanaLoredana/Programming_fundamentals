from domain import Coffee


class Repository_Coffee:
    """
    Entitate abstracta de tipul Repository_Coffee
    """
    def __init__(self, name_f):
        self.__name_f = name_f

    def get_all(self):
        """
        :return: Lista cafelelor din fisierul name_f
        """
        try:
            open(self.__name_f, "r")
        except IOError:
            return []

        rez = []
        with open(self.__name_f, "r") as f:
            for line in f:
                line = line.strip()
                line = line.split(", ")
                cof = Coffee(line[0], line[1], float(line[2]))
                rez.append(cof)
        return rez
