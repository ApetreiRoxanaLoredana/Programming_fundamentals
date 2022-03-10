from controller import Controller_Coffee
from repository import Repository_Coffee
from ui import Consola

repo_coffee = Repository_Coffee("produse.txt")
contr_coffee = Controller_Coffee(repo_coffee)
consola = Consola(contr_coffee)
consola.run()