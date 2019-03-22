from enum import Enum, auto


class View(Enum):
    MENU = auto()
    LETTERS = auto()
    FIGURES = auto()


class Ev(Enum):
    KEY_PRESSED = auto()
    NEW_FIGURES_GAME = auto()
    NEW_LETTERS_GAME = auto()
    GOAL_ACHIEVED = auto()
    END_TIMER = auto()
    GO_TO_MENU = auto()
    QUIT = auto()


win_size = win_width, win_height = 1600, 900
plaque_size = plaque_width, plaque_height = win_width // 15, win_width // 13
frame_rate = 60
menu_bg_color = (40, 40, 40)
game_bg_color = (70, 70, 120)
bg_color = menu_bg_color

n_letters = 10
n_figures = 6
