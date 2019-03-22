import pygame
import re

from games.figures_game.operations import random_number
from graphic_objects.plaque import Plaque
from graphic_objects.label import Label
from graphic_objects.button import Button
from games.controller import Controller
import settings


class FiguresGameC(Controller):
    def __init__(self, model):
        Controller.__init__(self, model)

    def new_game(self):
        Controller.new_game(self)
        # select random figures, give result and steps of the solution
        self.game.available_figures.clear()
        self.game.delete_buttons.clear()
        self.game.user_entries.clear()
        self.game.expected_operations.clear()
        self.game.figures, result, self.game.solution = random_number()
        self.game.cursor.text_pos = 0
        self.game.input = ''
        self.game.label.value = ""

        y = settings.win_height * .1

        for i, value in enumerate(self.game.figures):
            x = settings.win_height * .2 * i + settings.win_height * .1
            self.game.available_figures.append(Plaque(value, (x, y)))

        x = settings.win_width * .9 - (settings.plaque_width)
        self.game.objective = Plaque(result, (x, y))

        for j, op in enumerate(('+', '-', 'x', '/', '=', 'AC')):
            i = 2 - (j % 2)
            x = settings.win_width * .7 - i * settings.plaque_width // 2 - i
            y = settings.win_height // 1.3 + j // 2 * settings.plaque_height // 2 + j // 2 + 3
            self.game.operators.append(Plaque(op, (x, y), (settings.plaque_width // 2, settings.plaque_height // 2)))

    def update(self, d_time):
        Controller.update(self, d_time)
        x_offset = (1.2 * (settings.plaque_width))
        y = settings.win_height // 1.3 + (settings.win_height - settings.win_height // 1.3) // 2 - (settings.plaque_height) // 2

        margin = (settings.win_width * .7) // 2 - (
                (len(self.game.available_figures) - 1) * x_offset + (settings.plaque_width)) // 2

        for i, figure in enumerate(self.game.available_figures):
            x = margin + (i * x_offset)
            figure.pos = (x, y)

        self.game.objective.pos = (settings.win_width * .7 + (settings.win_width * .3) // 2 - (settings.plaque_width) // 2, y)
        self.game.cursor.x = settings.win_width // 2 - self.game.label.text.get_width() // 2 + self.game.cursor.text_pos * self.game.label.text.get_width() // max(1, len(self.game.label.value))

        for i, op in enumerate(self.game.user_entries):
            op.y = op.height * i
            self.game.delete_buttons[i].y = op.y + self.game.delete_buttons[i].img.get_height() // 1.5

    def delete_user_op(self, index):
        for op in reversed(self.game.user_entries[index:]):
            expression = r"^([1-9]+[0-9]{,3}) [+-x*/] ([1-9]+[0-9]{,3}) = ([1-9]+[0-9]{,3})$"
            operation = re.search(expression, op.value)

            n1 = int(operation.group(1))
            n2 = int(operation.group(2))
            res = int(operation.group(3))

            for elt in self.game.available_figures:
                if int(elt.value) == res:
                    self.game.available_figures.remove(elt)
                    break

            self.game.available_figures.append(Plaque(n1, (0, 0)))
            self.game.available_figures.append(Plaque(n2, (0, 0)))

        self.game.delete_buttons = self.game.delete_buttons[:index]
        self.game.user_entries = self.game.user_entries[:index]

    def check_input(self):
        valid_number = r"[1-9]+[0-9]{,3}"
        expression = r"^({})*([+-x*/])({})$".format(valid_number, valid_number)
        operation = re.search(expression, self.game.label.value)

        if operation:
            if operation.group(1):
                n1 = int(operation.group(1))
            elif len(self.game.user_entries) > 0:
                n1 = int(self.game.available_figures[-1].value)
            else:
                self.game.error.value = 'Opération incorrecte'
                return False

            op = operation.group(2)
            n2 = int(operation.group(3))

            if op is '/' and (n2 < 1 or n1 / n2 != n1 // n2):
                self.game.error.value = 'Division incorrecte'
                return False
            elif op is '-' and n1 < n2:
                self.game.error.value = 'Résultat négatif'
                return False
            elif op is 'x':
                op = '*'

            ind_n1, ind_n2 = None, None

            for i, fig in enumerate(self.game.available_figures):
                if ind_n1 is None and int(fig.value) == n1:
                    ind_n1 = i
                elif ind_n2 is None and int(fig.value) == n2:
                    ind_n2 = i

            if ind_n1 is not None and ind_n2 is not None:
                result = int(eval(str(n1) + op + str(n2)))

                if result >= 10000:
                    self.game.error.value = 'Résultat trop grand'
                    return False

                for index in sorted([ind_n1, ind_n2], reverse=True):
                    del self.game.available_figures[index]

                self.game.available_figures.append(Plaque(result, (0, 0)))

                if op is '*':
                    op = 'x'
                self.game.user_entries.append(Label((settings.win_width // 1.9, 0),
                                                    "{} {} {} = {}".format(str(n1), op, str(n2), str(result)),
                                                    (settings.win_width // 3.2, settings.win_height // 14)))
                self.game.label.value = ""
                self.game.delete_buttons.append(Button((settings.win_width // 1.9, 0),
                                                       (settings.win_width // 60, settings.win_width // 60),
                                                       'img/remove.png'))

                if result == int(self.game.objective.value):
                    pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'ev': settings.Ev.GOAL_ACHIEVED}))

                return True
            else:
                self.game.error.value = 'Nombre indisponible'
                return False
        else:
            self.game.error.value = 'Opération invalide'

    def display_solution(self):
        for i, op in enumerate(self.game.solution):
            self.game.expected_operations.append(Label((settings.win_width // 5, (i + 1) * settings.win_height // 16),
                                                       ' '.join(op).replace('*', 'x') + ' = ' + str(
                                                           int(eval(''.join(op)))),
                                                       (settings.win_width // 3.2, settings.win_height // 16)))
            self.game.expected_operations[i].color = (40, 191, 80)

        self.game.expected_operations.insert(0, (Label((settings.win_width // 5, 0),
                                                       'SOLUTION',
                                                       (settings.win_width // 3.2, settings.win_height // 14))))
        self.game.expected_operations[0].color = (40, 191, 80)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            Controller.handle_event(self, event)
            x, y = pygame.mouse.get_pos()

            if not self.game.timer.is_finished() and self.game.timer.is_active:
                for i, button in enumerate(self.game.delete_buttons):
                    if button.img.get_rect(topleft=button.pos).collidepoint(x, y):
                        self.delete_user_op(i)
                        break

                for figure in self.game.available_figures:
                    if figure.surface.get_rect(topleft=figure.pos).collidepoint(x, y) and len(self.game.label.value) + len(figure.value) < 10:
                        self.game.label.value += figure.value
                        self.game.cursor.text_pos += len(figure.value)

                        pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'ev': settings.Ev.KEY_PRESSED}))
                        break

                for op in self.game.operators:
                    if op.surface.get_rect(topleft=op.pos).collidepoint(x, y) and len(self.game.label.value) + len(op.value) < 10:
                        if op.value == 'AC':
                            self.game.label.value = ''
                            self.game.cursor.text_pos = 0
                        elif op.value == '=':
                            if self.check_input():
                                self.game.cursor.text_pos = 0
                        else:
                            self.game.label.value += op.value
                            self.game.cursor.text_pos += len(op.value)

                        pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'ev': settings.Ev.KEY_PRESSED}))
                        break

            elif not self.game.timer.is_active:
                if self.game.continue_button.img.get_rect(topleft=self.game.continue_button.pos).collidepoint(x, y):
                    pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'ev': settings.Ev.NEW_FIGURES_GAME}))

        elif not self.game.timer.is_finished() and self.game.timer.is_active:
            symbol = event.unicode

            if len(self.game.label.value) < 10 and '0' <= symbol <= '9' or event.key in [pygame.K_KP_DIVIDE,
                                                                                         pygame.K_KP_MULTIPLY,
                                                                                         pygame.K_KP_MINUS,
                                                                                         pygame.K_KP_PLUS,
                                                                                         pygame.K_x,
                                                                                         pygame.K_ASTERISK,
                                                                                         pygame.K_PLUS,
                                                                                         pygame.K_MINUS,
                                                                                         pygame.K_SLASH]:
                self.game.label.value = self.game.label.value[:self.game.cursor.text_pos] + symbol + \
                                        self.game.label.value[self.game.cursor.text_pos:]
                self.game.cursor.text_pos += 1
                pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'ev': settings.Ev.KEY_PRESSED}))
            # if user confirm his input
            elif symbol == '=' or event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                if self.check_input():
                    self.game.cursor.text_pos = 0
            elif event.key == pygame.K_BACKSPACE and self.game.cursor.text_pos > 0:
                self.game.label.value = self.game.label.value[:self.game.cursor.text_pos - 1] + \
                                        self.game.label.value[self.game.cursor.text_pos:]
                self.game.cursor.text_pos -= 1
            elif event.key == pygame.K_DELETE and self.game.cursor.text_pos < len(self.game.label.value):
                self.game.label.value = self.game.label.value[:self.game.cursor.text_pos] + \
                                        self.game.label.value[self.game.cursor.text_pos + 1:]
            elif event.key == pygame.K_LEFT and self.game.cursor.text_pos > 0:
                self.game.cursor.text_pos -= 1
            elif event.key == pygame.K_RIGHT and self.game.cursor.text_pos < len(self.game.label.value):
                self.game.cursor.text_pos += 1
        elif not self.game.timer.is_active:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'ev': settings.Ev.NEW_FIGURES_GAME}))
