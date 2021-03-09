import pygame as pg

from core.buttons import PushButton
from core.tools import GameState


class Menu(GameState):
    def __init__(self):
        super(Menu, self).__init__()
        self.persist["screen_color"] = "black"
        self.next_state = "GAME"

        self.start_button = PushButton("Start Game", self.screen_rect.centerx, 30)
        self.multiplayer_button = PushButton("Multiplayer", self.screen_rect.centerx, 120)

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYUP:
            self.persist["screen_color"] = "gold"
            self.done = True
        elif event.type == pg.MOUSEBUTTONUP:
            self.persist["screen_color"] = "dodgerblue"
            self.done = True
        if self.start_button.rect.collidepoint(pg.mouse.get_pos()):
            self.start_button.on_hover()

    def draw(self, surface):
        surface.fill(pg.Color("black"))
        self.start_button.display(surface)
        self.multiplayer_button.display(surface)
