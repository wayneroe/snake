import sys
import pygame as pg
from data.states import game, splash, menu
from data import tools

if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((720, 720))
    states = {"GAME": game.Game(),
              "SPLASH": splash.Splash(),
              "MENU": menu.Menu()
              }
    game = tools.Game(screen, states, "MENU")
    game.run()
    pg.quit()
    sys.exit()
