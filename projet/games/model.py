import settings
from graphic_objects.cursor import Cursor
from graphic_objects.button import Button
from graphic_objects.error_message import ErrorMessage


class Model:
    def __init__(self):
        self.exit_button = Button((settings.win_width // 30, settings.win_height // 25),
                                  (settings.win_width // 15, settings.win_width // 15),
                                  "img/exit.png")

        self.stop_button = Button((settings.win_width * .863, settings.win_height * .25),
                                  (settings.win_width // 8, settings.win_width // 32),
                                  "img/stop.png")

        btn_width = settings.win_width // 6
        self.continue_button = Button((settings.win_width // 2 - btn_width // 2, settings.win_height * .62),
                                      (btn_width, settings.win_height // 12),
                                  "img/continue.png")
        self.cursor = Cursor((settings.win_width // 2, settings.win_height // 2 - (settings.win_width // 14) // 2))
        self.error = ErrorMessage((0, settings.win_height * .65),
                           '',
                           (settings.win_width, settings.win_height // 20))
