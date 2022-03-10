from controller import Controller
from repository import StudentRepo, LaboratorRepo
from ui import Ui

repo_st = StudentRepo("studenti.txt")
repo_lab = LaboratorRepo("laboratoare.txt")
contr = Controller(repo_st, repo_lab)
consola = Ui(contr)
consola.run()