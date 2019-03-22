from graphic_objects.timer import Timer
from graphic_objects.slider_h import SliderH
from graphic_objects.label import Label
from games.model import Model
import settings


class LettersGameM(Model):
    def __init__(self):
        Model.__init__(self)
        self.n_letters = 10
        self.available_letters = []
        self.used_letters = []
        self.is_valid = False
        self.draft = ''
        self.longest_word = ''
        self.end_timer = 0
        self.expected_solution = None
        self.max_len = Label((settings.win_width // 2 - settings.win_width // 8, settings.win_height * .65),
                             'Max: 10 lettres',
                             (settings.win_width // 4, settings.win_height // 15))

        with open("games/letters_game/dico.txt", 'r') as dict_file:
            self.dictionary = [word[:-1] for word in dict_file if 3 < len(word) < self.n_letters + 1]

        self.draft_slider = SliderH((0, settings.win_height // 1.3), "TIRAGE", settings.win_width)
        self.timer = Timer((settings.win_width - int(Timer.radius * 1.5), int(Timer.radius * 1.5)), 30)
