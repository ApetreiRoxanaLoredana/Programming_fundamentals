from controller import EmisiuneController
from repository import EmisiuneRepo, EmisiuniBlocateRepo
from ui import EmisiuneUi


repo = EmisiuneRepo("emisiuni.txt")
repo_blocate = EmisiuniBlocateRepo()
contr = EmisiuneController(repo, repo_blocate)
consola = EmisiuneUi(contr)
consola.run()