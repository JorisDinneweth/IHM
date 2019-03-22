from pygame.font import SysFont
from pygame import Surface
from pygame.colordict import THECOLORS
import pygame

from graphic_objects.graphic_item import GraphicItem
import settings


class ErrorMessage(GraphicItem):
    def __init__(self, pos, value, size):
        GraphicItem.__init__(self, pos, size)
        self.__value = value
        self.__color = [255, 0, 0]
        self.ref_time = 4.0
        self.remaining_time = self.ref_time
        self.font = SysFont('arial', int(self.height))
        self.text = self.font.render(value, 1, self.__color)
        self.bg_color = [255, 0, 0, 128]
        self.text_surf = Surface(self.text.get_size(), pygame.SRCALPHA)
        self.text_surf.fill(self.bg_color)
        self.text_surf.blit(self.text, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    def draw(self, screen):
        screen.blit(self.text_surf, self.pos)

    def reload(self):
        self.text = self.font.render(self.__value, 1, self.__color)
        self.text_surf = Surface(self.text.get_size(), pygame.SRCALPHA)
        self.text_surf.fill(self.bg_color)
        self.text_surf.blit(self.text, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    def _get_value(self):
        return self.__value

    def _set_value(self, value):
        self.__value = value
        self.bg_color[3] = 255
        self.remaining_time = self.ref_time
        self.reload()
        self.x = settings.win_width // 2 - self.text_surf.get_width() // 2
    value = property(_get_value, _set_value)

    def _get_color(self):
        return self.__color

    def _set_color(self, font_color):
        self.__color = font_color
        self.reload()
    color = property(_get_color, _set_color)

    def update(self, d_time):
        if self.remaining_time > 0:
            self.remaining_time = max(0, self.remaining_time - d_time / 1000)
            self.bg_color[3] = max(0, 255 * self.remaining_time / self.ref_time)
            self.reload()