import numpy as np
import pygame as pg


class Tiles(object):
    def __init__(self, map_size):
        self.map_size = map_size

        self.tile_rects = np.empty((map_size, map_size), pg.Rect)
        self.screen_rect = pg.display.get_surface().get_rect()
        self.screen_width = self.screen_rect.width
        self.screen_height = self.screen_rect.height

        self.tile_size = min(self.screen_width, self.screen_height) // self.map_size

        self.x_offset, self.y_offset = self.calculate_offsets()

        for i in range(self.map_size):
            for j in range(self.map_size):
                tile_rect = [self.x_offset + i * self.tile_size, self.y_offset + j * self.tile_size,
                             self.tile_size, self.tile_size]
                self.tile_rects[i][j] = tile_rect

        self.bright_green = pg.Color("GreenYellow")
        self.dark_green = pg.Color("LawnGreen")
        self.font = pg.font.SysFont('Arial', 35)

    def calculate_offsets(self):
        x_offset = 0
        y_offset = 0

        map_middle = (self.map_size * self.tile_size) // 2

        if self.screen_width != self.screen_height:
            if self.screen_width > self.screen_height:
                x_offset = self.screen_width - map_middle
            else:
                y_offset = self.screen_height - map_middle
        print(x_offset, y_offset)

        return x_offset, y_offset

    def draw(self, surface, score):
        surface.fill(pg.Color(87, 138, 52))

        for i in range(self.map_size):
            for j in range(self.map_size):
                tile_rect = [self.x_offset + i * self.tile_size, self.y_offset + j * self.tile_size,
                             self.tile_size, self.tile_size]

                self.tile_rects[i][j] = tile_rect

                if (j + i) % 2 == 0:
                    pg.draw.rect(surface, self.bright_green, tile_rect)
                else:
                    pg.draw.rect(surface, self.dark_green, tile_rect)

        score_text = self.font.render(f"Score {score}", True, pg.Color("Black"))
        surface.blit(score_text, (self.x_offset, 0))

    def update_window_size(self, width, height):
        self.screen_width = width
        self.screen_height = height

        self.tile_size = min(self.screen_width, self.screen_height) // self.map_size

        self.x_offset, self.y_offset = self.calculate_offsets()

    def get_position(self, coordinates):
        return self.tile_rects[coordinates.x][coordinates.y]
