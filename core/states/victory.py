from pathlib import Path

import numpy as np
import pygame as pg

from core import animation_snake
from core.tiles import Tiles
from core.tools import GameState, Point


class Victory(GameState):
    def __init__(self):
        super(Victory, self).__init__()
        sound_folder = Path("../sounds/")
        self.victory_sound = pg.mixer.Sound(str(sound_folder / "smb_stage_clear.wav"))

        self.board_size = 26
        self.snake_speed = 0.01
        self.tiles = Tiles(self.board_size)

        # "Snake" written in Silverfinster
        title = np.array([[0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0],
                          [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
                          [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0],
                          [0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0]],
                         dtype=np.int32)

        # find out coordinates of the "Snake" pixels
        title_path = list()
        title_offset = 2

        for y in range(0, 4):
            for x in range(0, self.board_size):
                if title[y][x]:
                    title_path.append(Point(x, y + title_offset))

        # Title Snake
        data = {
            'speed': 0.05,
            'tiles': self.tiles,
            'path': title_path,
            'length': len(title_path)
        }
        self.title_snake = animation_snake.Snake(**data)

        self.path = list()

        for i in range(16):
            self.path.append(Point(i, 10))

        message = "RETRY"
        data = {
            'speed': self.snake_speed,
            'tiles': self.tiles,
            'path': self.path,
            'length': len(message) + 1,
            'message': message
        }
        self.retry_snake = animation_snake.Snake(**data)

    def startup(self, persistent):
        self.persist = persistent
        self.victory_sound.play()

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        if event.type == pg.VIDEORESIZE:
            self.tiles.update_window_size(event.w, event.h)
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.retry_snake.clicked_snake(event.pos):
                self.done = True
                self.next_state = "MENU"

    def update(self, dt):
        self.title_snake.update(dt)
        self.retry_snake.update(dt)

    def draw(self, surface):
        surface.fill(pg.Color("black"))
        self.tiles.draw(surface)
        self.title_snake.draw(surface)
        self.retry_snake.draw(surface)
