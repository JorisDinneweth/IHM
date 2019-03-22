import pygame
import pygame.gfxdraw
from pygame.font import SysFont
from pygame.colordict import THECOLORS
import math

import settings
from graphic_objects.graphic_item import GraphicItem


class Timer(GraphicItem):
    radius = settings.win_width // 20
    thickness = radius // 10

    def __init__(self, pos, n_seconds, size = (settings.win_width // 20, settings.win_width // 20)):
        GraphicItem.__init__(self, pos, size)
        self.ref_time = n_seconds
        self.remaining_time = n_seconds
        self.rect = (self.x - Timer.radius, self.y - Timer.radius, Timer.radius * 2, Timer.radius * 2)
        self.font = SysFont("Arial", int(Timer.radius))
        self.text_render = self.font.render(str(int(self.remaining_time)), 1, THECOLORS['white'])
        self.is_active = False
        self.timer_color = THECOLORS['white']
        self.n_points = 720
        self.points = [(self.x + int(Timer.radius * math.cos(math.pi / 2 + math.pi * i / self.n_points)),
                        self.y + int(Timer.radius * math.sin(math.pi / 2 + math.pi * i / self.n_points))) for i in range(-self.n_points, self.n_points)]

    def reset(self):
        self.remaining_time = self.ref_time
        self.n_points = 720

    def start(self):
        self.is_active = True

    def stop(self):
        self.is_active = False

    def remaining_time(self):
        return self.remaining_time

    def is_finished(self):
        return self.remaining_time == 0

    def update(self, d_time):
        if self.is_active:
            self.n_points = max(2, int(len(self.points) * self.remaining_time / self.ref_time))
            self.remaining_time = max(0, self.remaining_time - d_time / 1000)
            self.text_render = self.font.render(str(int(self.remaining_time)), 1, THECOLORS['white'])
            self.timer_color = 255, 255 * self.remaining_time / self.ref_time, 255 * self.remaining_time / self.ref_time

            if self.is_finished():
                pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'ev': settings.Ev.END_TIMER}))
                self.is_active = False

    def draw(self, screen):
        pygame.draw.lines(screen, self.timer_color, False, self.points[:self.n_points], 10)

        screen.blit(self.text_render,
                    (self.x - self.text_render.get_width() // 2,
                     self.y - self.text_render.get_height() // 2))
