from controller import Controller_bere
from repository import Repo_bere
from ui import Consola

repo_bere = Repo_bere("produse.txt")
contr_bere = Controller_bere(repo_bere)
consola = Consola(contr_bere)
consola.run()