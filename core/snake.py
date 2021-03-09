import pygame as pg

from core.tools import Point, Directions


class Snake(object):
    def __init__(self, game, snake_speed, tiles):
        self.game = game
        self.screen_rect = pg.display.get_surface().get_rect()
        self.screen_height = self.screen_rect.height
        self.screen_width = self.screen_rect.width

        middle = tiles.map_size // 2
        self.ate_apple = False
        self.body_coordinates = list([Point(middle, middle)])

        self.tiles = tiles

        self.image = pg.Surface((self.screen_width, self.screen_height))

        self.snake_speed = snake_speed
        self.direction = Directions.RIGHT
        # How far the snake is on the last block
        self.block_progress = 0
        self.last_dt = 0

    def update(self, dt):
        self.block_progress = self.block_progress + dt * self.snake_speed
        if self.block_progress > 1:
            new_body_part = self.body_coordinates[-1].walk(self.direction)
            if not new_body_part.in_range(self.tiles.map_size):
                return False
            if self.ate_apple:
                self.body_coordinates.append(new_body_part)
                self.ate_apple = False
            else:
                if len(self.body_coordinates) > 1:
                    self.body_coordinates.append(new_body_part)
                    self.body_coordinates.pop(0)
                else:
                    self.body_coordinates[-1] = new_body_part
            self.block_progress = self.block_progress - 1
        return True

    def draw(self, screen):
        for block in self.body_coordinates:
            pg.draw.rect(screen, pg.Color("red"), self.tiles.get_position(block))

    def direction_allowed(self, direction):
        if (self.direction.value[0] + direction.value[0] == 0) and (self.direction.value[1] + direction.value[1] == 0):
            return False
        else:
            return True
