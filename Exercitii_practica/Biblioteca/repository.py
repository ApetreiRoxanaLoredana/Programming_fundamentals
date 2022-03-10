from domain import Carte
from errors import RepoException


class BiblioRepo:
    """
    Entitate abstracta de tipul BiblioRepo
    """
    def __init__(self, name_file):
        self.__name_file = name_file

    def add(self, carte):
        """
        Adauga o carte in lista si in fisier
        :param carte: Carte
        :return: None
        """
        list = self.load_from_file()
        list.append(carte)
        self.store_from_file(list)

    def modifica(self, carte):
        """
        Modifica cartea care are id-ul respectiv
        Modificarea se va vedea si in fisier
        :param carte: Carte
        :return: None
        """
        list = self.load_from_file()
        for i in range(len(list)):
            if list[i].get_id() == carte.get_id():
                list[i] = carte
                self.store_from_file(list)
                return

    def sterge(self, carte):
        """
        Sterge cartea cu id-ul respectiv din lista
        Arunca RepoException daca nu exista
        :param carte: Carte
        :return: None
        """
        poz = -1
        list = self.load_from_file()
        for i in range(len(list)):
            if list[i].get_id() == carte.get_id():
                poz = i
                break
        if poz != -1:
            del list[poz]
            self.store_from_file(list)
            return
        raise RepoException("Nu exista nici o carte cu acest id\n")


    def load_from_file(self):
        """
        Incarca cartiile din fisier in memorie
        :return: o lista cu cartile din fisier
        """
        rez = []
        try:
            open(self.__name_file, "r")
        except IOError:
            return []

        with open(self.__name_file, "r") as f:
            for line in f:
                L = line.strip().split(", ")
                carte = Carte(int(L[0]), L[1], L[2], int(L[3]))
                rez.append(carte)
        return rez

    def store_from_file(self, lista):
        """
        Incarca o lista din memorie in fisier
        :param lista: list
        :return: None
        """
        f = open(self.__name_file, "w")
        for carte in lista:
            carte_file = str(carte)+"\n"
            f.write(carte_file)
        f.close()

class UndoRepo:
    """
    Entitate abstracta de tipul UndoRepo
    """
    def __init__(self):
        self.__list = []

    def add(self, undo):
        """
        Adauga un obiect de tipul undo in lista
        :param undo: Undo
        :return: None
        """
        self.__list.append(undo)

    def pop(self):
        """
        returneaza ultimul element din lista si il sterge
        :return: list[-1]
        """
        if len(self.__list) != 0:
            element = self.__list.pop()
            return element
        raise RepoException("Nu mai poti face undo\n")

    def get_all(self):
        """
        :return: lista
        """
        return self.__list