from pygame.font import Font
from pygame import Surface
from pygame.colordict import THECOLORS
import pygame

from graphic_objects.graphic_item import GraphicItem


class Label(GraphicItem):
    def __init__(self, pos, value, size):
        GraphicItem.__init__(self, pos, size)
        self.__value = value
        self.__color = THECOLORS["white"]
        self.__font_name = 'fonts/courier.ttf'
        self.font = Font(self.__font_name, int(self.height // 1.5))
        self.text = self.font.render(value, 1, self.__color)
        self.bg = Surface((self.width, self.height), pygame.SRCALPHA)
        self.bg.fill((0, 0, 0, 0))
        w, h = self.text.get_width(), self.text.get_height()
        self.bg.blit(self.text, [self.width // 2 - w // 2, self.height // 2 - h // 2])

    def draw(self, screen):
        screen.blit(self.bg, self.pos)

    def reload(self):
        self.font = Font(self.__font_name, int(self.height // 1.5))
        self.text = self.font.render(self.__value, 1, self.__color)
        self.bg = Surface((self.width, self.height), pygame.SRCALPHA)
        self.bg.fill((0, 0, 0, 0))
        w, h = self.text.get_width(), self.text.get_height()
        self.bg.blit(self.text, [self.width // 2 - w // 2, self.height // 2 - h // 2])

    def _get_value(self):
        return self.__value

    def _set_value(self, value):
        self.__value = value
        self.reload()
    value = property(_get_value, _set_value)

    def _get_color(self):
        return self.__color

    def _set_color(self, font_color):
        self.__color = font_color
        self.reload()
    color = property(_get_color, _set_color)

    def _get_font(self):
        return self.__font_name

    def _set_font(self, font_name):
        self.__font_name = 'fonts/' + font_name + '.ttf'
        self.reload()
    font_name = property(_get_font, _set_font)
