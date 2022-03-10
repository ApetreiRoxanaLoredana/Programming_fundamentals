from domain import Piesa
from errors import RepoException


class TeatruRepo:
    def __init__(self, file_name):
        """
        :param file_name: string
        """
        self.__file_name = file_name

    def get_all(self):
        """
        Incarca lista de piese din fisier in memorie
        :return: lista de piese
        """
        try:
            open(self.__file_name, "r")
        except IOError:
            return []

        rez = []
        with open(self.__file_name) as f:
            for line in f:
                L = line.strip().split(", ")
                piesa = Piesa(L[0], L[1], L[2], int(L[3]))
                rez.append(piesa)
        return rez

    def store_from_file(self, list):
        """
        Incarca lista de piese din memorie in fisier
        :param list: lista de piese
        :return: None
        """
        f = open(self.__file_name, "w")
        for piesa in list:
            piesa_file = str(piesa)+"\n"
            f.write(piesa_file)
        f.close()

    def add(self, piesa):
        """
        Adauga o piesa in lista si o incarca in memorie
        :param piesa: Piesa
        :return: None
        """
        list = self.get_all()
        list.append(piesa)
        self.store_from_file(list)

    def modifica(self, piesa):
        """
        Modifica genul si durata piesei care are titlul si regizorul respectiv
        Arunca RepoException daca nu exista nici o piesa cu titlul si regixorul respectiv
        :param piesa: Piesa
        :return: None
        """
        ok = False
        lista_piesa = self.get_all()
        for i in range(len(lista_piesa)):
            if lista_piesa[i].get_titlu() == piesa.get_titlu() and lista_piesa[i].get_regizor() == piesa.get_regizor():
                lista_piesa[i] = piesa
                ok = True
        if ok == False:
            raise RepoException("Nu exista nici o piesa cu acest titlu si regizor\n")
        self.store_from_file(lista_piesa)

    def export(self, lista, fisier):
        """
        Incarca in fiserul cu numele respectiv lista
        :param lista: lista de piese
        :param fisier: string
        :return: None
        """
        f = open(fisier+".txt", "w")
        for piesa in lista:
            piesa_file = piesa.get_regizor()+", "+piesa.get_titlu()+", "+str(piesa.get_durata())+", "+piesa.get_gen()+"\n"
            f.write(piesa_file)
        f.close()