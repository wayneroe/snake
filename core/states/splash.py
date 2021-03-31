import pygame as pg

from core.snake import Snake
from core.tiles import Tiles
from ..tools import GameState


class Splash(GameState):
    def __init__(self):
        super(Splash, self).__init__()
        self.board_size = 10

        self.tiles = Tiles(self.board_size)
        snake_speed = 0.001
        self.snake = Snake(self, snake_speed, self.tiles)

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        if event.type == pg.VIDEORESIZE:
            self.tiles.update_window_size(event.w, event.h)

    def update(self, dt):
        self.snake.update(dt)

    def draw(self, surface):
        self.tiles.draw(surface)
        self.snake.draw(surface)
