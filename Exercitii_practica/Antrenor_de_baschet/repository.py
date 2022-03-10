from domain import Jucator
from errors import RepoException


class JucatoriRepo:
    def __init__(self, file_name):
        """
        :param file_name: string
        """
        self.__file_name = file_name

    def get_all(self):
        """
        Incarca toti jucatorii din fisier in memorie
        :return: lista de jucatori
        """
        try:
            open(self.__file_name, "r")
        except IOError:
            return []
        rez = []

        with open(self.__file_name, "r") as f:
            for line in f:
                L = line.strip().split(", ")
                jucator = Jucator(L[0], L[1], int(L[2]), L[3])
                rez.append(jucator)
        return rez

    def store_from_file(self, lista):
        """
        Incarca lista din memorie in fisier
        :param lista: lista de jucatori
        :return: None
        """
        f = open(self.__file_name, "w")
        for jucator in lista:
            jucator_file = str(jucator)+"\n"
            f.write(jucator_file)
        f.close()

    def add(self, jucator):
        """
        Adauga un jucator in fisier
        :param jucator: Jucator
        :return: None
        """
        lista = self.get_all()
        lista.append(jucator)
        self.store_from_file(lista)

    def modifica(self, jucator):
        """
        Modifica inaltimea jucatorului care are numele si prenumele respectiv
        Arunca RepoException daca nu exista nici un jucator cu acest nume si prenume
        :param jucator: Jucator
        :return: None
        """
        lista = self.get_all()
        for i in range(len(lista)):
            if lista[i].get_nume() == jucator.get_nume() and lista[i].get_prenume() == jucator.get_prenume():
                jucator_nou = Jucator(jucator.get_nume(), jucator.get_prenume(), jucator.get_inaltime(), lista[i].get_post())
                lista[i] = jucator_nou
                self.store_from_file(lista)
                return
        raise RepoException("Nu exista acest jucator\n")

