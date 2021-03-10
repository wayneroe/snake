import pygame as pg

from core.buttons import PushButton
from core.tools import GameState


class GameOver(GameState):
    def __init__(self):
        super(GameOver, self).__init__()

        self.font = pg.font.SysFont('Arial', 100)
        self.text = self.font.render("GAME OVER", True, pg.Color("red"))
        self.retry_button = PushButton("Retry", self.screen_rect.width / 2, self.screen_rect.height / 2)

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True

    def draw(self, surface):
        surface.fill(pg.Color("black"))
        text_rect = self.text.get_rect(center=(self.screen_rect.width / 2, 100))
        surface.blit(self.text, text_rect)
        self.retry_button.display(surface)
