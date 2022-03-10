from controller import BiblioController
from domain import CarteValidator, Filtru
from repository import BiblioRepo, UndoRepo
from ui import BiblioUi

val = CarteValidator()
repo_undo = UndoRepo()
repo = BiblioRepo("carti.txt")
filtru = Filtru("", -1)
contr = BiblioController(repo, repo_undo, val, filtru)
consola = BiblioUi(contr)
consola.run()