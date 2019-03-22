class MenuV:
    def __init__(self, model):
        self.game = model

    def draw(self, screen):
        self.game.exit_button.draw(screen)
        self.game.letters_button.draw(screen)
        self.game.figures_button.draw(screen)
