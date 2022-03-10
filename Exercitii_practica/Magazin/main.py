from UI import MagazinUi
from controller import MagazinController
from domain import ProdusValidator, Filtru, Undo
from repository import MagazinRepo

val = ProdusValidator()
repo = MagazinRepo("produse.txt")
filtru = Filtru("", -1)
undo = Undo([])
contr = MagazinController(repo, val, filtru, undo)
consola = MagazinUi(contr)
consola.run()