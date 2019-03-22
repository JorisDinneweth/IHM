import pygame

from games.menu.menu_M import MenuM
from games.menu.menu_V import MenuV
from games.menu.menu_C import MenuC
from games.letters_game.letters_game_M import LettersGameM
from games.letters_game.letters_game_V import LettersGameV
from games.letters_game.letters_game_C import LettersGameC
from games.figures_game.figures_game_M import FiguresGameM
from games.figures_game.figures_game_V import FiguresGameV
from games.figures_game.figures_game_C import FiguresGameC
from music.audio_manager import AudioManager
import settings


class GameEngine:
    def __init__(self):
        # create graphic objects
        self.is_running = True
        self.audio_manager = AudioManager()

        menu_model = MenuM()
        menu_view = MenuV(menu_model)
        menu_controller = MenuC(menu_model)

        letters_model = LettersGameM()
        letters_view = LettersGameV(letters_model)
        letters_controller = LettersGameC(letters_model)

        figures_model = FiguresGameM()
        figures_controller = FiguresGameC(figures_model)
        figures_view = FiguresGameV(figures_model)

        self.model = None
        self.view = None
        self.controller = None

        self.interfaces = {settings.View.MENU: {'m': menu_model, 'v': menu_view, 'c': menu_controller},
                           settings.View.LETTERS: {'m': letters_model, 'v': letters_view, 'c': letters_controller},
                           settings.View.FIGURES: {'m': figures_model, 'v': figures_view, 'c': figures_controller}}

        pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'ev': settings.Ev.GO_TO_MENU}))

    def switch_to(self, state):
        self.model, self.view, self.controller = self.interfaces[state].values()

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                self.controller.handle_event(event)
            elif event.type == pygame.USEREVENT:
                if event.ev == settings.Ev.QUIT:
                    self.is_running = False

                elif event.ev == settings.Ev.KEY_PRESSED:
                    self.audio_manager.play(event.ev)

                elif event.ev == settings.Ev.NEW_LETTERS_GAME or event.ev == settings.Ev.NEW_FIGURES_GAME:
                    if event.ev == settings.Ev.NEW_LETTERS_GAME:
                        self.switch_to(settings.View.LETTERS)
                    else:
                        self.switch_to(settings.View.FIGURES)

                    self.audio_manager.play(event.ev)
                    self.controller.new_game()
                    settings.bg_color = settings.game_bg_color

                elif event.ev == settings.Ev.GO_TO_MENU:
                    self.switch_to(settings.View.MENU)
                    self.audio_manager.play(event.ev)
                    settings.bg_color = settings.menu_bg_color
                elif event.ev == settings.Ev.GOAL_ACHIEVED:
                    self.model.timer.stop()
                    self.audio_manager.play(event.ev)
                elif event.ev == settings.Ev.END_TIMER:
                    self.model.timer.stop()
                    self.controller.display_solution()

    def update(self, d_time):
        self.controller.update(d_time)

    def draw(self, screen):
        self.view.draw(screen)
