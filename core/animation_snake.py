import pygame as pg


class Snake(object):
    def __init__(self, speed, tiles, path, length, message=None):
        self.tiles = tiles
        self.speed = speed
        self.length = length
        self.message = message

        self.body_color = pg.Color("red")
        self.head_color = pg.Color("blue")

        self.body_coordinates = [path[0]]
        self.path = path
        self.path.pop(0)

        # How far the snakes is on the last block
        self.progress = 0
        self.last_dt = 0

    def update(self, dt):
        self.progress = self.progress + (dt * self.speed)
        if self.progress > 1:
            self.move()
            self.progress = self.progress - 1

    def move(self):
        if self.path:
            self.body_coordinates.append(self.path[0])
            self.path.pop(0)
            if len(self.body_coordinates) > self.length:
                self.body_coordinates.pop(0)

    def draw(self, screen):
        # draw body parts
        for i, position in enumerate(self.body_coordinates[:-1]):
            rectangle = self.tiles.get_rectangle(position)
            pg.draw.rect(screen, self.body_color, self.tiles.get_rectangle(position))

            if self.message:
                font = pg.font.SysFont("arial", rectangle.height)
                letter_surface = font.render(self.message[i], True, pg.Color("Black"))
                screen.blit(letter_surface, rectangle.topleft)

        # draw head
        head_rectangle = self.tiles.get_rectangle(self.body_coordinates[-1])
        pg.draw.rect(screen, self.head_color, head_rectangle)

    def clicked_snake(self, position):
        for coordinate in self.body_coordinates:
            if self.tiles.get_rectangle(coordinate).collidepoint(position):
                return True
        return False
