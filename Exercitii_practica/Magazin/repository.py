from domain import Produs
from errors import RepoException


class MagazinRepo:
    def __init__(self, file_name):
        """
        :param file_name: string
        """
        self.__file_name = file_name

    def get_all(self):
        """
        Incarca din fisier in memorie lista de produse
        :return: o lista cu toate produsele din fisier
        """
        try:
            open(self.__file_name, "r")
        except IOError:
            return []

        rez = []
        with open(self.__file_name) as f:
            for line in f:
                L = line.strip().split(", ")
                produs = Produs(int(L[0]), L[1], float(L[2]))
                rez.append(produs)
        return rez

    def store_from_file(self, list):
        """
        Incarca lista de produse in fisier
        :param list: lista de produse
        :return: None
        """
        f = open(self.__file_name, "w")
        for produs in list:
            produs_file = str(produs)+"\n"
            f.write(produs_file)
        f.close()

    def adauga(self, produs):
        """
        Adauga un produs nou
        Arunca REpoException daca exista deja un produs cu acelasi id
        :param produs: Produs
        :return: None
        """
        list = self.get_all()
        for p in list:
            if p.get_id() == produs.get_id():
                raise RepoException("Exista deja un produs cu acest id\n")
        list.append(produs)
        self.store_from_file(list)

    def sterge(self, id):
        """
        Sterge produsul cu id-ul respectiv
        :param id: int
        :return: None
        """
        poz = -1
        list = self.get_all()
        for i in range(len(list)):
            if list[i].get_id() == id:
                poz = i
        if poz != -1:
            del list[poz]
            self.store_from_file(list)