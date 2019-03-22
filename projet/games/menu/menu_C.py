import pygame
from pygame.event import Event

import settings


class MenuC:
    def __init__(self, model):
        self.game = model

    def update(self, d_time):
        pass

    def handle_event(self, event):
        x, y = pygame.mouse.get_pos()

        if self.game.letters_button.img.get_rect(topleft=self.game.letters_button.pos).collidepoint(x, y):
            pygame.event.post(Event(pygame.USEREVENT, {'ev': settings.Ev.NEW_LETTERS_GAME}))
        elif self.game.figures_button.img.get_rect(topleft=self.game.figures_button.pos).collidepoint(x, y):
            pygame.event.post(Event(pygame.USEREVENT, {'ev': settings.Ev.NEW_FIGURES_GAME}))
        elif self.game.exit_button.img.get_rect(topleft=self.game.exit_button.pos).collidepoint(x, y):
            pygame.event.post(Event(pygame.USEREVENT, {'ev': settings.Ev.QUIT}))
