import pygame

import settings


class Controller:
    def __init__(self, model):
        self.game = model

    def new_game(self):
        self.game.timer.is_active = True
        self.game.timer.reset()

    def update(self, d_time):
        self.game.timer.update(d_time)
        self.game.cursor.update(d_time)
        self.game.error.update(d_time)

    def handle_event(self, event):
        x, y = pygame.mouse.get_pos()

        if self.game.exit_button.img.get_rect(topleft=self.game.exit_button.pos).collidepoint(x, y):
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'ev': settings.Ev.GO_TO_MENU}))
        elif self.game.stop_button.img.get_rect(topleft=self.game.stop_button.pos).collidepoint(x, y):
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'ev': settings.Ev.END_TIMER}))
