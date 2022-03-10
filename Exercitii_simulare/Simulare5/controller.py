class Controller_Coffee:
    """
    Entitae abstracta de tipul Controller_Coffee
    """
    def __init__(self, repo_coffee):
        self.__repo = repo_coffee

    def suma_preturi(self, tara):
        """
        Calculeaza suma preturilor tutouror cafelelor din tara respectiva
        :param tara:
        :return: suma (float)
        """
        suma = 0
        list = self.__repo.get_all()
        for i in list:
            if i.get_tara() == tara:
                suma += i.get_pret()
        return suma

    def sortare(self):
        """
        Construieste un dictionar in care cheile sunt numele tarilor iar valoarea
        suma tuturor cafelelor din aceea tara
        Transforma dictionarul intr-o lista de tupluri si sorteaza lista crescator dupa suma
        :return: o lista de tupluri de tipul (tara, suma)
        """
        dic = {}
        list = self.__repo.get_all()
        for i in list:
            if i.get_tara() not in dic:
                dic[i.get_tara()] = self.suma_preturi(i.get_tara())
        print(dic)
        dic = sorted(dic.items(), key=lambda item: item[1])
        print(dic)
        return dic