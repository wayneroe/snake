import pygame as pg

from core.tools import Point, Directions


class Snake(object):
    def __init__(self, game, snake_speed, tiles):
        self.game = game
        self.tiles = tiles
        self.snake_speed = snake_speed
        self.score = 0
        self.game_over = False

        middle = tiles.size // 2

        self.body_color = pg.Color("red")
        self.head_color = pg.Color("blue")

        self.ate_apple = False

        self.body_coordinates = list([Point(middle, middle)])

        self.direction = Directions.RIGHT
        self.old_direction = Directions.RIGHT
        # How far the snakes is on the last block
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

        # check if outside of screen
        if not new_head.in_range(self.tiles.size):
            self.game_over = True
            return
        # check if crashed in itself
        if new_head in self.body_coordinates:
            self.game_over = True
            return

        self.body_coordinates.append(new_head)

        if self.ate_apple:
            self.score += 1
            self.ate_apple = False
            if self.score == (self.tiles.size ^ 2 - 1):
                self.game.done = True
                self.game.next_state = "VICTORY"
                return
        else:
            self.body_coordinates.pop(0)

    def draw(self, screen):
        # draw body parts
        for block in self.body_coordinates[:-1]:
            pg.draw.rect(screen, self.body_color, self.tiles.get_rectangle(block))
        # draw head
        pg.draw.rect(screen, self.head_color, self.tiles.get_rectangle(self.body_coordinates[-1]))

    def change_direction(self, direction):
        # If the old and new coordinates zero each other out,
        # the snake tries to move into the direction it came from
        if (self.old_direction.value[0] + direction.value[0] == 0) \
                and (self.old_direction.value[1] + direction.value[1] == 0):
            return
        else:
            self.direction = direction
