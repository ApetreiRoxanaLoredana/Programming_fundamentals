from domain import Contact
from errors import RepoException


class ContactRepository:
    """
    Entitate abstracta de tipul ContactRepository
    """
    def __init__(self, file_name):
        self.__file_name = file_name

    def getAll(self):
        """"
        Incarca din fisier in memorie lista de contacte
        :return: Lista de contacte din fisier
        """
        try:
            open(self.__file_name, "r")
        except IOError:
            print("Nu am gasit\n")

        rez = []
        with open(self.__file_name, "r") as f:
            for line in f:
                line = line.strip().split(",")
                cont = Contact(int(line[0]), line[1], line[2], line[3])
                rez.append(cont)
        return rez

    def add(self, cont):
        """
        Adauga in fisier un contact nou
        :param cont: Contact
        :return: None
        """
        list_cont = self.getAll()
        for i in list_cont:
            if i.get_id() == cont.get_id():
                raise RepoException("Exista un contact cu acest id!\n")
            if i.get_name() == cont.get_name():
                raise RepoException("Exista un contact cu acest nume!\n")
        list_cont.append(cont)
        f = open(self.__file_name, "w")
        for cont in list_cont:
            cont_file = str(cont.get_id())+","+cont.get_name()+","+cont.get_phoneNr()+","+cont.get_group()+"\n"
            f.write(cont_file)
        f.close()

    def find(self, name):
        """
        cauta contactul care are numele respectiv
        Arunca eroare daca nu il gaseste
        :param name: string
        :return: contactul
        """
        list_cont = self.getAll()
        for i in list_cont:
            if i.get_name() == name:
                return i
        raise RepoException("Nu exista acest nume in contacte!\n")

    def getAllFor(self, group):
        """
        Returneaza lista cu contactele din grupul respectiv
        Arunca eroare daca nu exista nici un contact din acel grup
        :param group: string
        :return: o lista cu toate contactele care au grupul respectiv
        """
        list_cont = self.getAll()
        rez = []
        for i in list_cont:
            if i.get_group() == group:
                rez.append(i)
        if len(rez) == 0:
            raise RepoException("Nu exista nici un contact din acest grup!\n")
        return rez
