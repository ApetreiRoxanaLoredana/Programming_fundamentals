from domain import Emisiune
from errors import RepoException


class EmisiuneRepo:
    """
    Entitate abstracat de tipul EmisiuneRepo
    """
    def __init__(self, name_file):
        self.__name_file = name_file

    def modifica(self, emisiune):
        """
        Modifica durata si descrierea emisiunii care are numele si tipul emisiunii respective
        Arunca RepoException daca nu gaseste emisiunea respectiva
        :param emisiune:Emisiune
        :return:None
        """
        list = self.loadFromFile()
        ok  = False
        for emi in list:
            if emi == emisiune:
                emi.set_descriere(emisiune.get_descriere())
                emi.set_durata(emisiune.get_durata())
                ok = True
        if ok == False:
            raise RepoException("Nu exista nici o emisiune cu acest nume si tip\n")
        self.storeFromFile(list)


    def sterge(self, nume, tip):
        """
        Sterge emisiunea care are numele si tipul respectiv
        Daca nu exista arunca RepoException
        :param nume:string
        :param tip:string
        :return:None
        """
        poz = -1
        list = self.loadFromFile()
        for i in range(len(list)):
            if list[i].get_tip() == tip and list[i].get_nume() == nume:
                poz = i
                break
        if poz == -1:
            raise RepoException("Nu exista aceasta emisiune\n")
        del list[poz]
        self.storeFromFile(list)

    def loadFromFile(self):
        """
        Incarca emisiunile din fiesier in memorie
        :return: lista de emisiuni
        """
        try:
            open(self.__name_file, "r")
        except IOError:
            return []

        list_rez = []
        with open(self.__name_file, "r") as f:
            for linie in f:
                L = linie.strip().split(",")
                emisiune = Emisiune(L[0], L[1], int(L[2]), L[3])
                list_rez.append(emisiune)
        return list_rez

    def storeFromFile(self, list):
        """
        Incarca toate emisiunile din memorie in fisier
        :return: None
        """
        f = open(self.__name_file, "w")
        for emi in list:
            emi_file = emi.get_nume()+","+emi.get_tip()+","+str(emi.get_durata())+","+emi.get_descriere()+"\n"
            f.write(emi_file)
        f.close()


class EmisiuniBlocateRepo:
    """
    Entitate abstracta de tipul EmisiuniBlocateRepo
    """
    def __init__(self):
        self.__lista = []

    def adauga(self, tip):
        """
        Se adauga in lista tipul de emisiuni care trebuie blocate
        Arunca RepoException daca exista deja tipul respectiv in lista
        :param tip: string
        :return: None
        """
        if tip in self.__lista:
            raise RepoException("Acest tip e deja blocat\n")
        self.__lista.append(tip)

    def sterge(self, tip):
        """
        Sterge tipul respectiv din lista
        Arunca RepoException daca nu exista tipul in lista
        :param tip: string
        :return: None
        """
        poz = -1
        if tip not in self.__lista:
            raise RepoException("Acest tip nu e in lista celor blocate\n")
        for i in range(len(self.__lista)):
            if self.__lista[i] == tip:
                poz = i
        del self.__lista[poz]

    def reseteaza(self):
        """
        Reseteaza lista si o face vida
        :return: None
        """
        self.__lista = []

    def get_all(self):
        """
        :return: toata lista
        """
        return self.__lista
