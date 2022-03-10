import random

from domain import Piesa


class TeatruController:
    def __init__(self, repo, val):
        """
        :param repo: TeatruRepo
        :param val: PiesaValidator
        """
        self.__repo = repo
        self.__val = val

    def add_piesa(self, titlu, regizor, gen, durata):
        """
        Adauga in lista o piesa noua
        Arunca ValidatorException daca piesa noua nu e conforma
        :param titlu: string
        :param regizor: string
        :param gen: string
        :param durata: int
        :return: None
        """
        piesa = Piesa(titlu, regizor, gen, durata)
        self.__val.valideaza(piesa)
        self.__repo.add(piesa)

    def modifica_piesa(self, titlu, regizor, gen, durata):
        """
        Modifica genul si durata piesei care are titlul si regizorul respectiv
        Arunca ValidatorException daca piesa nu e conforma
        Arunca RepoException daca nu exista nici o piesa cu titlul si regizorul respectiv
        :param titlu: string
        :param regizor: string
        :param gen: string
        :param durata: int
        :return: None
        """
        piesa = Piesa(titlu, regizor, gen, durata)
        self.__val.valideaza(piesa)
        self.__repo.modifica(piesa)

    def genereaza_titlu_regizor(self):
        """
        Gnereaza un titlu sau un regizor
        :return: titlul sau piesa
        """
        vocale = "aeiou"
        consoane = "bcdfghjklmnpqrstvwxyz"
        titlu = ""

        lungime = random.randint(8, 12)
        spatiu = random.randint(1, lungime-1)
        for i in range(lungime+1):
            if i == spatiu:
                titlu += " "
            else:
                if i % 2 == 0:
                    titlu += random.choice(vocale)
                else:
                    titlu += random.choice(consoane)
        return titlu

    def genereaza_piese(self, nr):
        """
        Genereaza random nr de piese
        :param nr: int
        :return: lista de piese
        """
        lista_gen = ["Comedie", "Drama", "Satira", "Altele"]
        lista_piese = []

        while nr != 0:
            gen = random.choice(lista_gen)
            durata = random.randint(0, 100000)
            titlu = self.genereaza_titlu_regizor()
            regizor = self.genereaza_titlu_regizor()
            lista_piese.append(Piesa(titlu, regizor, gen, durata))
            nr -= 1

        return lista_piese

    def add_mai_multe_piese(self, list):
        """
        Adauga in fiser lista de de piese
        :param list: lista de piese
        :return: None
        """
        for i in list:
            self.__repo.add(i)

    def exporta_piese(self, fisier):
        """
        Sorteaza lista dupa regizor si titlu
        Exporta lista de piese in fisierul respectiv
        :param fisier:
        :return: None
        """
        lista_piese = self.__repo.get_all()
        lista_piese = sorted(lista_piese, key=lambda Piesa: Piesa.get_regizor())
        lista_piese = sorted(lista_piese, key=lambda Piesa: Piesa.get_titlu())
        self.__repo.export(lista_piese, fisier)


