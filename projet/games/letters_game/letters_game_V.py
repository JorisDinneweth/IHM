from pygame.colordict import THECOLORS
from pygame import Surface

import settings
from graphic_objects.plaque import Plaque
from games.view import View


class LettersGameV(View):
    def __init__(self, model):
        View.__init__(self, model)
        self.thickness = 2

        # draw surface where the user's word will take place
        self.outside_border = Surface(((settings.plaque_width) * self.game.n_letters + (self.game.n_letters + 2) * 0.2 * (settings.plaque_width),
                                       (settings.plaque_height) * 1.5))
        self.outside_border.fill(THECOLORS['white'])
        self.inside_border = Surface((self.outside_border.get_width() - 2 * self.thickness,
                                      self.outside_border.get_height() - 2 * self.thickness))
        self.inside_border.fill(THECOLORS['black'])

    def draw(self, screen):
        for letter in self.game.available_letters:
            letter.set_bg_color(THECOLORS['white'])
            letter.draw(screen)

        self.inside_border.fill(THECOLORS['black'])
        self.outside_border.blit(self.inside_border, (self.thickness, self.thickness))
        screen.blit(self.outside_border, (settings.win_width // 2 - self.outside_border.get_width() // 2,
                                          settings.win_height // 2 - self.outside_border.get_height() // 2))

        for letter in self.game.used_letters:
            if self.game.is_valid:
                letter.set_bg_color((40, 191, 80)) # green
            else:
                letter.set_bg_color((255, 50, 50)) # red

            letter.draw(screen)

        self.game.expected_solution.draw(screen)

        if self.game.timer.is_active:
            self.game.max_len.draw(screen)

        View.draw(self, screen)
