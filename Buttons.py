import pygame as pg


class PushButton(object):
    def __init__(self, text, x, y) -> None:
        self.width = 200
        self.height = 40
        self.color = pg.Color("blue")
        self.font = pg.font.SysFont('Arial', 35)
        self.text = self.font.render(text, True, pg.Color("green"))
        self.text_rect = self.text.get_rect(center=(x, y))
        self.rect = self.text_rect.inflate(20, 20)
        print(self.rect)

    def display(self, surface):
        pg.draw.rect(surface, self.color, self.rect)
        surface.blit(self.text, self.text_rect)

    def on_hover(self):
        self.color = pg.Color("Purple")
