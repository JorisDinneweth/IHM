import pygame
import pygame.gfxdraw

from game_engine import GameEngine
import settings
import math


def main():
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.font.init()
    pygame.init()
    screen = pygame.display.set_mode(settings.win_size)

    game_engine = GameEngine()
    t = pygame.time.Clock()

    while game_engine.is_running:
        # control frame limit
        delta_time = t.tick(settings.frame_rate)

        game_engine.handle_event(pygame.event.get())

        screen.fill(settings.bg_color)
        game_engine.update(delta_time)
        game_engine.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
