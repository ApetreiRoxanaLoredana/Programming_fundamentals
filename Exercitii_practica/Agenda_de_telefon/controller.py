from domain import Contact


class AgendaController:
    """
    Entitate abstracta de tipul AgendaController
    """
    def __init__(self, repo_agenda, val_agenda):
        self.__repo = repo_agenda
        self.__val = val_agenda

    def addContact(self, id, name, phoneNr, group):
        """
        Adauga un contact nou
        :param id: int
        :param name: string
        :param phoneNr: string
        :param group: string
        :return: None
        """
        cont = Contact(id, name, phoneNr, group)
        self.__val.valideaza(cont)
        self.__repo.add(cont)

    def lookup(self, name):
        """
        Cauta contactul cu numele respectiv
        Arunca eroare daca nu gaseste contactul respectiv
        :param name: string
        :return: contactul
        """
        cont = self.__repo.find(name)
        return cont

    def lookupAll(self, group):
        """
        Returneaza o lista cu toate contactele din grupul respectiv ordonate crescator dupa nume
        Arunca eroare daca nu exista nici un contact din acel grup
        Arunca eroare daca grupul nu e corect
        :param group: string
        :return: lista de contacte
        """
        self.__val.valideaza(Contact(1, "a", "9", group))
        list_cont = self.__repo.getAllFor(group)
        list_cont.sort(key=lambda x: x.get_name())
        return list_cont

    def exportCSV(self, group, outFName):
        """
        Incarca in fisier contactele din grupul respectiv
        :param group: string
        :param outFName: string
        :return: None
        """
        f = open(outFName, "w")
        list_cont = self.lookupAll(group)
        for cont in list_cont:
            cont_file = cont.get_name()+","+cont.get_phoneNr()+"\n"
            f.write(cont_file)
        f.close()
