import pygame as pg

from ..tools import GameState


class Splash(GameState):
    def __init__(self):
        super(Splash, self).__init__()

    def get_event(self, event):
        pass

    def draw(self, surface):
        surface.fill(pg.Color("black"))
