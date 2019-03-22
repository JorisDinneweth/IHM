from pygame import Surface
from pygame.colordict import THECOLORS

from graphic_objects.graphic_item import GraphicItem
from graphic_objects.plaque import Plaque
import settings


class Cursor(GraphicItem):
    width = 5

    def __init__(self, pos, size = (5, settings.plaque_height)):
        GraphicItem.__init__(self, pos, size)
        self.text_pos = 0
        self.surface = Surface(size)
        self.surface.fill(THECOLORS['white'])
        self.is_active = True
        self.toggle_time = 0
        self.is_visible = True

    def update(self, d_time):
        self.toggle_time -= d_time / 1000

        if self.toggle_time <= 0:
            self.toggle_time = .7
            self.is_visible = not self.is_visible

    def draw(self, screen):
        if self.is_visible:
            screen.blit(self.surface, self.pos)
