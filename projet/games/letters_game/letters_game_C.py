from graphic_objects.plaque import Plaque
from graphic_objects.cursor import Cursor
from graphic_objects.label import Label
from games.controller import Controller
from games.letters_game import alphabet
import settings

import pygame


class LettersGameC(Controller):
    def __init__(self, model):
        Controller.__init__(self, model)

    def new_game(self):
        Controller.new_game(self)
        self.game.available_letters.clear()
        self.game.used_letters.clear()
        self.game.cursor.text_pos = 0
        self.game.draft = alphabet.random_draft(self.game.n_letters)
        self.game.expected_solution = Label(
            (settings.win_width // 2 - settings.win_width // 2, settings.win_height // 4),
            '',
            (settings.win_width, settings.win_width // 25))
        self.game.expected_solution.font_name = 'arial'
        self.game.expected_solution.color = (40, 191, 80)

        x_offset = (1.2 * settings.plaque_width)
        margin = settings.win_width // 2 - ((self.game.n_letters - 1) * x_offset + (settings.plaque_width)) // 2

        for i, letter in enumerate(self.game.draft):
            x = margin + (i * x_offset)
            y = settings.win_height * .1
            self.game.available_letters.append(Plaque(letter, (x, y)))

        self.game.longest_word = self.longest_word()
        self.game.max_len.value = 'Max: {} lettres'.format(len(self.game.longest_word))

    def update(self, d_time):
        Controller.update(self, d_time)
        x_offset = 1.2 * (settings.plaque_width)
        margin = settings.win_width // 2 - (
                (len(self.game.available_letters) - 1) * x_offset + (settings.plaque_width)) // 2

        y = settings.win_height // 1.3 + (settings.win_height - settings.win_height // 1.3) // 2 - \
            (settings.plaque_height) // 2
        for i, sprite in enumerate(self.game.available_letters):
            x = margin + (i * x_offset)
            sprite.pos = (x, y)

        margin = settings.win_width // 2 - (
                (len(self.game.used_letters) - 1) * x_offset + (settings.plaque_width)) // 2

        y = settings.win_height // 2 - (settings.plaque_height) // 2
        for i, sprite in enumerate(self.game.used_letters):
            x = margin + (i * x_offset)

            sprite.pos = (x, y)

        self.game.cursor.x = margin + (self.game.cursor.text_pos - 1) * x_offset + (settings.plaque_width) + (x_offset - (settings.plaque_width)) // 2 - Cursor.width // 2

    def check_word(self):
        word = ''
        for letter in self.game.used_letters:
            word = word + letter.value

        self.game.is_valid = word in self.game.dictionary

        if self.game.is_valid and len(self.game.longest_word) == len(word):
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'ev': settings.Ev.GOAL_ACHIEVED}))
            self.game.expected_solution.value = 'Bravo, il n\'y a pas plus long !'

    def display_solution(self):
        self.game.expected_solution.value = 'Plus long mot: {} ({} lettres)'.format(self.game.longest_word, len(self.game.longest_word))

    def longest_word(self):
        result = ""
        length = 0

        for dict_word in self.game.dictionary:
            if length < len(dict_word) < self.game.n_letters + 1:
                draft = self.game.draft
                is_included = True
                for letter in dict_word:
                    if letter in draft:
                        index = draft.index(letter)
                        draft = draft[:index] + draft[index + 1:]
                    else:
                        is_included = False
                        break

                if is_included:
                    result = dict_word
                    length = len(dict_word)

        return result

    def append_letter(self, letter):
        for letter_sprite in self.game.available_letters:
            if letter_sprite.value == letter:
                self.game.used_letters.insert(self.game.cursor.text_pos, letter_sprite)
                self.game.available_letters.remove(letter_sprite)

                self.check_word()
                pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'ev': settings.Ev.KEY_PRESSED}))
                return True

        return False

    def pop_letter(self, pos):
        if len(self.game.used_letters) > 0:
            self.game.available_letters.append(self.game.used_letters[pos])
            self.game.used_letters.remove(self.game.used_letters[pos])

            self.check_word()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            Controller.handle_event(self, event)
            x, y = pygame.mouse.get_pos()

            if not self.game.timer.is_active and self.game.continue_button.img.get_rect(topleft=self.game.continue_button.pos).collidepoint(x, y):
                pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'ev': settings.Ev.NEW_LETTERS_GAME}))

            if not self.game.timer.is_finished() and self.game.timer.is_active:
                for i, letter in enumerate(self.game.used_letters + self.game.available_letters):
                    if letter.surface.get_rect(topleft=letter.pos).collidepoint(x, y):
                        if i < len(self.game.used_letters):
                            self.pop_letter(i)
                            if self.game.cursor.text_pos > i:
                                self.game.cursor.text_pos -= 1
                        else:
                            self.append_letter(letter.value.upper())
                            self.game.cursor.text_pos += 1

                            pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'ev': settings.Ev.KEY_PRESSED}))

        elif not self.game.timer.is_finished() and self.game.timer.is_active:
            letter = event.unicode
            # if pressed key is into alphabet
            if 'a' <= letter <= 'z':
                if self.append_letter(letter.upper()):
                    self.game.cursor.text_pos += 1
                else:
                    self.game.error.value = 'Lettre indisponible'
            # remove letter from left
            elif event.key == pygame.K_BACKSPACE and self.game.cursor.text_pos > 0:
                self.pop_letter(self.game.cursor.text_pos - 1)
                self.game.cursor.text_pos -= 1
            # remove letter from right
            elif event.key == pygame.K_DELETE and self.game.cursor.text_pos < len(self.game.used_letters):
                self.pop_letter(self.game.cursor.text_pos)
            elif event.key == pygame.K_LEFT and self.game.cursor.text_pos > 0:
                self.game.cursor.text_pos -= 1
            elif event.key == pygame.K_RIGHT and self.game.cursor.text_pos < len(self.game.used_letters):
                self.game.cursor.text_pos += 1
            elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'ev': settings.Ev.END_TIMER}))

        elif not self.game.timer.is_active:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'ev': settings.Ev.NEW_LETTERS_GAME}))
