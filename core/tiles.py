import numpy as np
import pygame as pg


class Tiles(object):
    def __init__(self, size):
        """
        :param size: How many tiles wide and high
        """
        self.size = size

        self.screen_rect = pg.display.get_surface().get_rect()
        self.screen_width = self.screen_rect.width
        self.screen_height = self.screen_rect.height

        # shorter side is used as maximum size
        self.tile_size = min(self.screen_width, self.screen_height) // self.size

        x_offset, y_offset = self.calculate_offsets()
        self.tile_rects = self.calculate_rects(x_offset, y_offset)

        self.bright_green = pg.Color("GreenYellow")
        self.dark_green = pg.Color("LawnGreen")

    def calculate_offsets(self):
        tiles_size = self.size * self.tile_size

        x_offset = (self.screen_width - tiles_size) / 2
        y_offset = (self.screen_height - tiles_size) / 2

        return x_offset, y_offset

    def calculate_rects(self, x_offset, y_offset):
        tile_rects = np.empty((self.size, self.size), pg.Rect)

        for i in range(self.size):
            for j in range(self.size):
                tile_rects[i][j] = pg.Rect(x_offset + i * self.tile_size, y_offset + j * self.tile_size,
                                           self.tile_size, self.tile_size)
        return tile_rects

    def draw(self, surface):
        for i in range(self.size):
            for j in range(self.size):
                if (j + i) % 2 == 0:
                    pg.draw.rect(surface, self.bright_green, self.tile_rects[i][j])
                else:
                    pg.draw.rect(surface, self.dark_green, self.tile_rects[i][j])

    def update_window_size(self, width, height):
        self.screen_width = width
        self.screen_height = height

        self.tile_size = min(self.screen_width, self.screen_height) // self.size

        x_offset, y_offset = self.calculate_offsets()
        self.tile_rects = self.calculate_rects(x_offset, y_offset)

    def get_rectangle(self, coordinate) -> pg.Rect:
        return self.tile_rects[coordinate.x][coordinate.y]
