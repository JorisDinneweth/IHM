from graphic_objects.button import Button
import settings


class MenuM:
    def __init__(self):
        self.exit_button = Button((settings.win_width // 30, settings.win_height // 25),
                                  (settings.win_width // 15, settings.win_width // 15),
                                  "img/exit.png")

        width = 500
        height = int(width * 1.2)
        y = settings.win_height // 2 - height // 2

        self.letters_button = Button((settings.win_width * .15, y),
                                     (width, height),
                                     "img/letter.png")
        self.figures_button = Button((settings.win_width * .85 - width, y),
                                     (width, height),
                                     "img/figure.png")