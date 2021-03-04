import pygame as pg
from collections import deque


class Snake(object):
    def __init__(self, width, height):
        self.body = deque([(5, 5)])
        self.image = pg.Surface((width, height))
        self.block_size = width // 10

        self.directionx = 1
        self.directiony = 0
        print("created Snake")

    def update(self, dt):
        new_block = (self.body[len(self.body)-1][0] + self.directionx*dt, self.body[len(self.body)-1][1] + self.directiony)
        self.body.append(new_block)

    def draw(self, screen):
        for block in self.body:
            pg.draw.rect(screen, pg.Color("red"), [block[0] * self.block_size, block[1] * self.block_size, self.block_size, self.block_size])


