from pathlib import Path

import pygame as pg

from core.tools import Point, Directions


class Snake(object):
    def __init__(self, game, snake_speed, tiles):
        self.game = game
        self.tiles = tiles
        self.snake_speed = snake_speed
        self.score = 0
        self.game_over = False

        middle = tiles.map_size // 2

        self.ate_apple = False
        sound_folder = Path("../sounds/")
        self.game_over_sound = pg.mixer.Sound(str(sound_folder / "gameOver.mp3"))

        self.body_coordinates = list([Point(middle, middle)])

        self.direction = Directions.RIGHT
        self.old_direction = Directions.RIGHT
        # How far the snake is on the last block
        self.progress = 0
        self.last_dt = 0

    def update(self, dt):
        self.progress = self.progress + (dt * self.snake_speed)
        if self.progress > 1:
            self.move()
            self.progress = self.progress - 1

    def move(self):
        head = self.body_coordinates[-1]
        new_head = head.walk(self.direction)
        self.old_direction = self.direction

        if not (new_head.in_range(self.tiles.map_size) or new_head in self.body_coordinates):
            self.game_over_sound.play()
            self.game_over = True
            return

        self.body_coordinates.append(new_head)
        if self.ate_apple:
            self.score += 1
            self.ate_apple = False
            if len(self.body_coordinates) == (self.tiles.map_size ^ 2 - 1):
                self.game.done = True
                self.game.next_state = "VICTORY"
                return
        else:
            self.body_coordinates.pop(0)

    def draw(self, screen):
        for block in self.body_coordinates:
            pg.draw.rect(screen, pg.Color("red"), self.tiles.get_position(block))

    def change_direction(self, direction):
        if (self.old_direction.value[0] + direction.value[0] == 0) \
                and (self.old_direction.value[1] + direction.value[1] == 0):
            # Snake tries to move in the direction it came from
            return
        else:
            self.direction = direction
