from UI import TeatruUi
from controller import TeatruController
from domain import PiesaValidator
from repository import TeatruRepo

val = PiesaValidator()
repo = TeatruRepo("piese.txt")
contr = TeatruController(repo, val)
consola = TeatruUi(contr)
consola.run()