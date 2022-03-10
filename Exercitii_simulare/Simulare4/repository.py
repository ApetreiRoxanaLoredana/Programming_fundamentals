from domain import Bere
from errors import RepoException


class Repo_bere:
    """
    Entitate abstracta de tipul Repo_bere
    """
    def __init__(self, name_f):
        self.__name_f = name_f

    def get_all(self):
        """
        Returneaza lista de beri care se afla in fisier
        :return: o lista cu obiecte de tipul Bere
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
                bere = Bere(line[0], line[1], float(line[2]))
                rez.append(bere)

        return rez

    def update(self, id_bere, bere):
        """
        modifica in fisier berea cu id_bere cu atributele obiectului bere
        :param id_bere:
        :param bere:
        :return:
        """
        ok = False
        list = self.get_all()
        f = open(self.__name_f, "w")
        for i in list:
            if id_bere == i.get_id():
                i = bere
                ok = True
                pret = "{:.2f}".format(i.get_pret())
            bere_str = i.get_nume() + ", " + i.get_tip() + ", " + str(round(i.get_pret(), 2)) + "\n"
            f.write(bere_str)
        f.close()

        if ok == False:
            raise RepoException("Nu exista nici o bere cu acest id!\n")

