import pygame as pg


class PushButton(object):
    def __init__(self, text, screen_rect) -> None:
        self.font = pg.font.SysFont('Arial', 35)
        self.text = self.font.render(text, True, pg.Color("green"))
        self.text_rect = self.text.get_rect(center=screen_rect.center)

    def display(self, surface):
        pg.draw.rect(surface, pg.Color("blue"), self.text_rect.inflate(20, 20))
        surface.blit(self.text, self.text_rect)
