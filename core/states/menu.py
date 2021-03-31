import numpy as np
import pygame as pg

from core import animation_snake
from core.tiles import Tiles
from core.tools import GameState, Point


class Menu(GameState):
    def __init__(self):
        super(Menu, self).__init__()

        self.board_size = 26
        self.snake_speed = 0.01

        # Animation Snakes with their corresponding next States
        self.snakes = list()
        self.redirects = list()

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

        self.single_player_path = list()
        self.multi_player_path = list()

        for i in range(20):
            self.single_player_path.append(Point(i, 10))
            self.multi_player_path.append(Point(i, 12))

        # Title Snake
        data = {
            'speed': 0.05,
            'tiles': self.tiles,
            'path': title_path,
            'length': len(title_path)
        }
        self.snakes.append(animation_snake.Snake(**data))

        # Single Player Snake
        message = "SINGLEPLAYER"
        data = {
            'speed': self.snake_speed,
            'tiles': self.tiles,
            'path': self.single_player_path,
            'length': len(message) + 1,
            'message': message
        }
        self.snakes.append(animation_snake.Snake(**data))

        # Multi Player Snake
        message = "MULTIPLAYER"
        data = {
            'speed': self.snake_speed,
            'tiles': self.tiles,
            'path': self.multi_player_path,
            'length': len(message) + 1,
            'message': message
        }
        self.snakes.append(animation_snake.Snake(**data))

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        if event.type == pg.VIDEORESIZE:
            self.tiles.update_window_size(event.w, event.h)
        if event.type == pg.MOUSEBUTTONDOWN:
            for snake in self.snakes:
                if snake.message:
                    if snake.clicked_snake(event.pos):
                        self.done = True
                        self.next_state = snake.message

    def update(self, dt):
        for snake in self.snakes:
            snake.update(dt)

    def draw(self, surface):
        surface.fill(pg.Color("black"))
        self.tiles.draw(surface)
        for snake in self.snakes:
            snake.draw(surface)
