from pathlib import Path

import pygame as pg

from core.apple import Apple
from core.snake import Snake
from core.tiles import Tiles
from core.tools import GameState, Directions

key_to_direction = {
    pg.K_d: Directions.RIGHT,
    pg.K_RIGHT: Directions.RIGHT,
    pg.K_s: Directions.DOWN,
    pg.K_DOWN: Directions.DOWN,
    pg.K_a: Directions.LEFT,
    pg.K_LEFT: Directions.LEFT,
    pg.K_w: Directions.UP,
    pg.K_UP: Directions.UP
}


class SinglePlayer(GameState):
    def __init__(self):
        super(SinglePlayer, self).__init__()
        self.board_size = 26

        self.tiles = Tiles(self.board_size)
        snake_speed = 0.01
        self.snake = Snake(self, snake_speed, self.tiles)
        self.apple = Apple(self.tiles, self.snake)

        sound_folder = Path("../sounds/")
        self.game_over_sound = pg.mixer.Sound(str(sound_folder / "gameOver.mp3"))

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
        if event.key in key_to_direction:
            direction = key_to_direction[event.key]
            self.snake.change_direction(direction)
        if event.key == pg.K_ESCAPE:
            pass
            # TODO Add pausing functionality

    def update(self, dt):
        self.snake.update(dt)

        if self.snake.game_over:
            self.game_over_sound.play()
            self.done = True
            self.next_state = "GAME_OVER"
            return

        self.apple.update(dt)

    def draw(self, surface):
        self.tiles.draw(surface)
        self.snake.draw(surface)
        self.apple.draw(surface)
        pg.display.flip()
