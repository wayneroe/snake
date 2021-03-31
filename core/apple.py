from pathlib import Path
from random import randint

import pygame as pg

from core.tools import Point


class Apple(object):
    def __init__(self, tiles, *snakes):
        self.snakes = snakes
        self.tiles = tiles
        self.coordinate = self.get_point_not_in_snake()

        sound_folder = Path("../sounds/")
        self.eating_sound = pg.mixer.Sound(str(sound_folder / "eat.ogg"))

    def get_point_not_in_snake(self):
        while True:
            coordinate = Point(randint(0, self.tiles.size - 1), randint(0, self.tiles.size - 1))
            for snake in self.snakes:
                if coordinate in snake.body_coordinates:
                    break
            return coordinate

    def update(self, dt):
        for snake in self.snakes:
            if self.coordinate in snake.body_coordinates:
                snake.ate_apple = True
                self.eating_sound.play()
                self.coordinate = self.get_point_not_in_snake()

    def draw(self, surface):
        pg.draw.rect(surface, pg.Color("gold"), self.tiles.get_rectangle(self.coordinate))
