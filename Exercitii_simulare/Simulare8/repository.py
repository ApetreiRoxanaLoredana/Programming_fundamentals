from domain import Movie


class RepoException(Exception):
    pass


class MovieRepository:
    """
    Entitaet abstracta de tipul MovieRepository
    """
    def __init__(self, fName):
        self.__fName = fName

    def getAll(self):
        """
        :return: Lista filmelor preluate din fisierul cu numele fName sau
        o lista vida daca fisierul nu este gasit
        """
        try:
            open(self.__fName, "r")
        except IOError:
            return []

        rez = []
        with open(self.__fName, "r") as f:
            for line in f:
                line = line.strip().split(",")
                movie = Movie(int(line[0]), line[1], float(line[2]), int(line[3]))
                rez.append(movie)
        return rez

    def update(self, movie):
        """
        Modifica filmul care are id-ul obiectului movie cu atributele obiectului movie
        Modificarile vor fi vizibile in fisier
        :param movie:
        :return: None
        """
        list = self.getAll()
        if movie not in list:
            raise RepoException("Nu exista nici un film cu acest id!\n")

        f = open(self.__fName, "w")
        for i in list:
            if i.getID() == movie.getID():
                i = movie
            movie_f = str(i.getID())+","+i.getName()+","+str(i.getPrice())+","+str(i.getBookedSeats())+"\n"
            f.write(movie_f)
        f.close()

