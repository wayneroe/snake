import pygame as pg


class Snake(object):
    def __init__(self, screen_width, screeen_height):
        self.square_size = screen_width // 10
        self.square_positions = list([(5, 5)])

        self.image = pg.Surface((screen_width, screeen_height))

        self.x_velocity = 1
        self.y_velocity = 0

    def update(self, dt):
        last_block = (self.square_positions[-1][0], self.square_positions[-1][1])
        new_block = (last_block[0] + self.x_velocity * dt, last_block[1] + self.y_velocity * dt)
        self.square_positions.append(new_block)

    def draw(self, screen):
        for block in self.square_positions:
            pg.draw.rect(screen, pg.Color("red"), [block[0] * self.square_size, block[1] * self.square_size, self.square_size, self.square_size])


