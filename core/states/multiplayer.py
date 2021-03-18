import math

import pygame as pg

from core.multiplayer_apple import Apple
from core.tools import Point
from core.snake import Snake
from core.tiles import Tiles
from core.tools import GameState, Directions

snake1_key_to_direction = {
    pg.K_RIGHT: Directions.RIGHT,
    pg.K_DOWN: Directions.DOWN,
    pg.K_LEFT: Directions.LEFT,
    pg.K_UP: Directions.UP
}

snake2_key_to_direction = {
    pg.K_d: Directions.RIGHT,
    pg.K_s: Directions.DOWN,
    pg.K_a: Directions.LEFT,
    pg.K_w: Directions.UP,
}


class Multiplayer(GameState):
    def __init__(self):
        super(Multiplayer, self).__init__()
        self.board_size = 10

        self.tiles = Tiles(20)
        snake_speed = 0.001
        self.snake1 = Snake(self, snake_speed, self.tiles)
        self.snake2 = Snake(self, snake_speed, self.tiles)
        self.snake2.direction = Directions.LEFT
        self.snake2.old_direction = Directions.LEFT

        if self.board_size % 2:
            middle = self.board_size // 2
            self.snake1.body_coordinates = list([Point(middle, middle)])
            self.snake2.body_coordinates = list([Point(middle + 1, middle + 1)])
        else:
            middle = self.board_size / 2
            lower = math.floor(middle)
            upper = math.ceil(middle)

            self.snake1.body_coordinates = list([Point(lower, lower)])
            self.snake2.body_coordinates = list([Point(upper, upper)])

        self.apple = Apple(self.tiles, [self.snake1, self.snake2])

    def startup(self, persistent):
        self.persist = persistent

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        if event.type == pg.VIDEORESIZE:
            self.tiles.update_window_size(event.w, event.h)
        if event.type == pg.KEYDOWN:
            self.on_key_down(event)

    def on_key_down(self, event):
        if event.key in snake1_key_to_direction:
            direction = snake1_key_to_direction[event.key]
            self.snake1.change_direction(direction)
        if event.key in snake2_key_to_direction:
            direction = snake2_key_to_direction[event.key]
            self.snake2.change_direction(direction)
        if event.key == pg.K_ESCAPE:
            pass
            # TODO Add pausing functionality

    def update(self, dt):
        self.snake1.update(dt)
        self.snake2.update(dt)
        self.apple.update(dt)

        self.check_collisions(self.snake1, self.snake2)

        if self.snake1.game_over and self.snake2.game_over:
            print("Draw")
            self.next_state = "PLAYER_VICTORY"
            self.persist["winner"] = "DRAW!"
            self.done = True

        if self.snake1.game_over:
            self.next_state = "PLAYER_VICTORY"
            self.persist["winner"] = "PLAYER 2"
            self.done = True

        if self.snake2.game_over:
            self.next_state = "PLAYER_VICTORY"
            self.persist["winner"] = "PLAYER 1"
            self.done = True

    def draw(self, surface):
        self.tiles.draw(surface, self.snake1.score)
        self.snake1.draw(surface)
        self.snake2.draw(surface)
        self.apple.draw(surface)
        pg.display.flip()


    def check_collisions(self, snake1, snake2):
        if snake1.body_coordinates[-1] == snake2.body_coordinates[-1]:
            # Draw
            snake1.game_over = True
            snake2.game_over = True
            return
        if snake1.body_coordinates[-1] in snake2.body_coordinates[:-1]:
            snake1.game_over = True

        if snake2.body_coordinates[-1] in snake1.body_coordinates[:-1]:
            snake2.game_over = True


