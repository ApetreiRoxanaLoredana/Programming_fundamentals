from domain import Student, Laborator
from errors import RepoException


class StudentRepo:
    def __init__(self, file_name):
        """
        :param file_name: string
        """
        self.__file_name = file_name

    def get_all(self):
        """
        Incarca din fisier in memorie lista de studenti
        :return: lista de studenti
        """
        try:
            open(self.__file_name, "r")
        except IOError:
            return []

        rez = []
        with open(self.__file_name, "r") as f:
            for line in f:
                L = line.strip().split(", ")
                st = Student(int(L[0]), L[1])
                rez.append(st)
        return rez

    def cauta(self, id):
        """
        Cauta studentul cu id ul respectiv
        Arunca RepoException daca nu il gaseste
        :param id: int
        :return: Student
        """
        lista_st = self.get_all()
        for st in lista_st:
            if st.get_id() == id:
                return st
        raise RepoException("Nu exista nici un student cu acest id\n")


class LaboratorRepo:
    def __init__(self, file_name):
        self.__file_name = file_name

    def get_all(self):
        """
        Incarca din fisier in memorie lista de studenti
        :return: lista de studenti
        """
        try:
            open(self.__file_name, "r")
        except IOError:
            return []

        rez = []
        with open(self.__file_name, "r") as f:
            for line in f:
                L = line.strip().split(", ")
                st = Laborator(int(L[0]), int(L[1]), L[2])
                rez.append(st)
        return rez

    def store_from_file(self, list_lab):
        """
        Incarca in fisier lista de laboratoare din memorie
        :param list_lab: lista cu Laboratoare
        :return: None
        """
        f = open(self.__file_name, "w")
        for lab in list_lab:
            lab_file = str(lab)+"\n"
            f.write(lab_file)
        f.close()


    def add(self, lab):
        """
        Adauga un nou laborator
        Arunca RepoException daca exista un student care are jeda o problema la laboratorul
        cu lab_nr
        :param lab: Laborator
        :return: None
        """
        list_lab = self.get_all()
        for lab2 in list_lab:
            if lab.get_id_st() == lab2.get_id_st():
                if lab.get_lab_nr() == lab2.get_lab_nr():
                    raise RepoException("Exista deja o problema\n")
        list_lab.append(lab)
        self.store_from_file(list_lab)


