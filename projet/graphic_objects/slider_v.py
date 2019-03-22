from pygame import Surface
from pygame.colordict import THECOLORS

from graphic_objects.graphic_item import GraphicItem


class SliderV(GraphicItem):
    def __init__(self, pos, height):
        GraphicItem.__init__(self, pos, (2, height))
        self.white_band = Surface((2, height))
        self.white_band.fill(THECOLORS['white'])

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.white_band, self.pos)
