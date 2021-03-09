from random import randint

import pygame as pg

from core.tools import Point


class Apple(object):
    def __init__(self, tiles, snake):
        self.snake = snake
        self.tiles = tiles
        self.coordinate = Point(randint(0, tiles.map_size - 1), randint(0, tiles.map_size - 1))

    def update(self, dt):
        print(f"Apple:\n{self.coordinate} Snake:\n{self.snake.body_coordinates}")
        if self.coordinate in self.snake.body_coordinates:
            print("Touched apple!")
            self.snake.ate_apple = True
            self.coordinate = Point(randint(0, self.tiles.map_size - 1), randint(0, self.tiles.map_size - 1))

    def draw(self, surface):
        pg.draw.rect(surface, pg.Color("gold"), self.tiles.get_position(self.coordinate))
