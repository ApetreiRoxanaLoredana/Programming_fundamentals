from domain import Bicicleta


class Repository_Bicicleta:
    """
    Entitate abstracta de tipul Repository_Bicicleta
    """
    def __init__(self, name_f):
        self.__name_f = name_f

    def get_all(self):
        """
        :return: Lista de biciclete din fisierul cu numele name_f sau
        o lista goala daca nu gaseste fisierul
        """
        try:
            open(self.__name_f, "r")
        except IOError:
            return []

        rez = []
        with open(self.__name_f, "r") as f:
            for line in f:
                line = line.strip().split(", ")
                bici = Bicicleta(int(line[0]), line[1], float(line[2]))
                rez.append(bici)
        return rez

    def delete(self, id_bicicleta):
        """
        Sterge din fisier bicicleta cu id-ul respectiv
        :param id_bicicleta-int
        :return:
        """
        poz = -1
        list = self.get_all()
        for i in list:
            if i.get_id() == id_bicicleta:
                poz = list.index(i)
                break

        if poz != -1:
            del list[poz]
            f = open(self.__name_f, "w")
            for i in list:
                line = str(i.get_id())+", "+i.get_tip()+", "+str(i.get_pret())+"\n"
                f.write(line)
            f.close()
