from pygame.font import SysFont
from pygame import Surface
from pygame.colordict import THECOLORS

from graphic_objects.graphic_item import GraphicItem
import settings


class SliderH(GraphicItem):
    def __init__(self, pos, text, width):
        GraphicItem.__init__(self, pos, (width, settings.win_width // 30))
        font = SysFont("Arial", settings.win_width // 30)
        self.font = font.render(text, 1, THECOLORS['white'])
        self.surface = Surface((self.font.get_width() * 1.1, self.font.get_height() * 1.1))
        self.surface.fill(settings.game_bg_color)
        self.white_band = Surface((width, 2))
        self.white_band.fill(THECOLORS['white'])

        self.surface.blit(self.font, (self.surface.get_width() // 2 - self.font.get_width() // 2,
                                      self.surface.get_height() // 2 - self.font.get_height() // 2))

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.white_band, self.pos)
        screen.blit(self.surface, (self.x + self.white_band.get_width() // 2 - self.surface.get_width() // 2,
                                   self.y - self.surface.get_height() // 2))
