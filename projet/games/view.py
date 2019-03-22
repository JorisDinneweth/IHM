class View:
    def __init__(self, model):
        self.game = model

    def draw(self, screen):
        self.game.timer.draw(screen)
        self.game.cursor.draw(screen)
        self.game.draft_slider.draw(screen)
        self.game.exit_button.draw(screen)
        self.game.error.draw(screen)

        if self.game.timer.is_active:
            self.game.stop_button.draw(screen)
        else:
            self.game.continue_button.draw(screen)

