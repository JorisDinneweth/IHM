from pygame.colordict import THECOLORS
from pygame import Surface

import settings
from graphic_objects.plaque import Plaque
from games.view import View


class FiguresGameV(View):
    def __init__(self, model):
        View.__init__(self, model)
        self.border_thickness = 2

        # draw surface where the user's word will take place
        self.outside_border = Surface(((settings.plaque_width) * settings.n_figures + (settings.n_figures + 2) * 0.2 * (settings.plaque_width),
                                       (settings.plaque_height) * 1.5))
        self.outside_border.fill(THECOLORS['white'])
        self.inside_border = Surface((self.outside_border.get_width() - 2 * self.border_thickness,
                                      self.outside_border.get_height() - 2 * self.border_thickness))
        self.inside_border.fill(THECOLORS['black'])

        self.game.label.size = (self.inside_border.get_width(), self.inside_border.get_height())
        self.game.label.pos = (self.outside_border.get_width() // 2 - self.game.label.width // 2,
                               self.outside_border.get_height() // 2 - self.game.label.height // 2)

    def draw(self, screen):
        self.game.result_slider.draw(screen)
        self.game.slider_v_top.draw(screen)
        self.game.slider_v_bottom.draw(screen)
        for figure in self.game.available_figures:
            figure.draw(screen)

        self.inside_border.fill(THECOLORS['black'])
        self.outside_border.blit(self.inside_border, (self.border_thickness, self.border_thickness))

        self.game.label.draw(self.outside_border)

        screen.blit(self.outside_border, (settings.win_width // 2 - self.outside_border.get_width() // 2,
                                          settings.win_height // 2 - self.outside_border.get_height() // 2))

        self.game.objective.draw(screen)

        for i in range(len(self.game.user_entries)):
            self.game.user_entries[i].draw(screen)
            self.game.delete_buttons[i].draw(screen)

        for elt in self.game.expected_operations:
            elt.draw(screen)

        for op in self.game.operators:
            op.draw(screen)

        View.draw(self, screen)
