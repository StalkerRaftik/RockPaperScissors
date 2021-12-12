from modules.main_menu import MainMenu
from modules.rock_paper_scissors import RockPaperScissors
from modules.end_game import EndGame

AVAILABLE_GAME_SIZES = (3, 4, 5)
AVAILABLE_GAME_MODES = ('PVP', 'PVB', 'BVB')

MODULES = [
    MainMenu,
    RockPaperScissors,
    EndGame,
]
