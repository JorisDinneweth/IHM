import pygame

from graphic_objects.graphic_item import GraphicItem


class Button(GraphicItem):
    def __init__(self, pos, size, img):
        GraphicItem.__init__(self, pos, size)
        self.img = pygame.transform.smoothscale(pygame.image.load(img).convert_alpha(), size)

    def draw(self, screen):
        screen.blit(self.img, self.pos)
