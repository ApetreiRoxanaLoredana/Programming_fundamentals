from repository_coffee import Repo_Coffee
from controller_coffee import Controller_Coffee
from ui import Consola


repo_coffee = Repo_Coffee("produse.txt")
contr_coffee = Controller_Coffee(repo_coffee)
consola = Consola(contr_coffee)
consola.run()