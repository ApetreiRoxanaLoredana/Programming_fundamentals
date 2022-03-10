from controller import Controller_Bicicleta
from repository import Repository_Bicicleta
from ui import Consola

repo_bici = Repository_Bicicleta("produse.txt")
contr_bici = Controller_Bicicleta(repo_bici)
consola = Consola(contr_bici)
consola.run()