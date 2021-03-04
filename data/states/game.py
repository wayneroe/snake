import pygame as pg

from ..tools import GameState
from ..snake import Snake


class Game(GameState):
    def __init__(self):
        super(Game, self).__init__()
        self.board_size = 10
        self.bright_green = pg.Color("GreenYellow")
        self.dark_green = pg.Color("LawnGreen")
        self.snake = Snake(720, 720)

    def startup(self, persistent):
        self.persist = persistent

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True

    def update(self, dt):
        self.snake.update(dt)

    def draw(self, surface):
        self.draw_tiles(surface)
        self.snake.draw(surface)
        pg.display.flip()

    def draw_tiles(self, surface):
        tile_size = self.screen_rect.width // 10

        for i in range(self.board_size):
            for j in range(self.board_size):
                if (j + i) % 2 == 0:
                    pg.draw.rect(surface, self.bright_green, [i * tile_size, j * tile_size, tile_size, tile_size])
                else:
                    pg.draw.rect(surface, self.dark_green, [i * tile_size, j * tile_size, tile_size, tile_size])
