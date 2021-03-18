from pathlib import Path
from random import randint, choice
from typing import List
import numpy as np

import pygame as pg

from core.tools import Point
from core.snake import Snake


class Apple(object):
    def __init__(self, tiles, snakes: List[Snake]):
        self.snakes = snakes
        self.tiles = tiles
        self.coordinate = self.get_point_not_in_snake()

        sound_folder = Path("../sounds/")
        self.eating_sound = pg.mixer.Sound(str(sound_folder / "eat.ogg"))

    def get_point_not_in_snake(self):
        all_points = list([Point(i, j) for i in range(self.tiles.map_size - 1) for j in range(self.tiles.map_size - 1)])

        snake_coordinates = set()
        for snake in self.snakes:
            snake_coordinates.union(snake.body_coordinates)

        coordinate = choice([point for point in all_points if point not in snake_coordinates])

        print(coordinate)
        return coordinate

    def update(self, dt):
        for snake in self.snakes:
            if self.coordinate in snake.body_coordinates:
                snake.ate_apple = True
                self.eating_sound.play()
                self.coordinate = self.get_point_not_in_snake()

    def draw(self, surface):
        pg.draw.rect(surface, pg.Color("gold"), self.tiles.get_position(self.coordinate))
