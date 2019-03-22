from pygame.font import SysFont
from pygame import Surface
from pygame.colordict import THECOLORS

import settings
from graphic_objects.graphic_item import GraphicItem


class Plaque(GraphicItem):
    bg_color = THECOLORS["white"]

    def __init__(self, value, pos, size = (settings.plaque_width, settings.plaque_height)):
        GraphicItem.__init__(self, pos, size)
        self.value = str(value)
        self.font = SysFont("Arial", int(self.height // 2))
        self.color = THECOLORS["black"]
        self.text_render = self.font.render(self.value, 1, self.color)
        self.surface = Surface((self.width, self.height))
        self.set_bg_color(Plaque.bg_color)

    def set_bg_color(self, color):
        self.surface.fill(color)
        w, h = self.text_render.get_width(), self.text_render.get_height()
        self.surface.blit(self.text_render, [self.width // 2 - w // 2, self.height // 2 - h // 2])

    def draw(self, screen):
        screen.blit(self.surface, self.pos)
