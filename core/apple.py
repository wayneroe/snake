from pathlib import Path
from random import randint

import pygame as pg

from core.tools import Point


class Apple(object):
    def __init__(self, tiles, snake):
        self.snake = snake
        self.tiles = tiles
        self.coordinate = self.get_point_not_in_snake()

        sound_folder = Path("../sounds/")
        self.eating_sound = pg.mixer.Sound(str(sound_folder / "eat.ogg"))

    def get_point_not_in_snake(self):
        while True:
            coordinate = Point(randint(0, self.tiles.map_size - 1), randint(0, self.tiles.map_size - 1))
            if coordinate not in self.snake.body_coordinates:
                return coordinate

    def update(self, dt):
        if self.coordinate in self.snake.body_coordinates:
            self.snake.ate_apple = True
            self.eating_sound.play()
            self.coordinate = self.get_point_not_in_snake()

    def draw(self, surface):
        pg.draw.rect(surface, pg.Color("gold"), self.tiles.get_position(self.coordinate))
