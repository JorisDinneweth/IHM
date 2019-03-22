from pygame.mixer import Sound
import pygame

import settings


class AudioManager:
    def __init__(self):
        self.key_pressed = Sound('music/accepted.wav')
        self.waiting_30 = Sound('music/letters_waiting.wav')
        self.waiting_45 = Sound('music/figures_waiting.wav')
        self.waiting_menu = Sound('music/menu_waiting.wav')
        self.win = Sound('music/win.wav')

        self.sound_library = {settings.Ev.KEY_PRESSED: self.key_pressed,
                              settings.Ev.NEW_LETTERS_GAME: self.waiting_30,
                              settings.Ev.NEW_FIGURES_GAME: self.waiting_45,
                              settings.Ev.GO_TO_MENU: self.waiting_menu,
                              settings.Ev.GOAL_ACHIEVED: self.win}

    def play(self, song_name):
        if song_name != settings.Ev.KEY_PRESSED:
            pygame.mixer.stop()

        self.sound_library.get(song_name).play(-1 if song_name == settings.Ev.GO_TO_MENU else 0)

    @staticmethod
    def stop():
        pygame.mixer.stop()
