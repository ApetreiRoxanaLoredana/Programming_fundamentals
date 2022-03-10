from ui import MoviesUI
from controller import MovieController
from repository import MovieRepository
from validator import Validator_Movie

MovieValidator = Validator_Movie()
MovieRepository = MovieRepository("filme.txt")
MovieController = MovieController(MovieRepository, MovieValidator)
consola = MoviesUI(MovieController)
consola.run()