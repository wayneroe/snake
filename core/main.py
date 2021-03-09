import sys

import pygame as pg

from core import tools
from core.states import game, splash, menu, over

if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((720, 720), pg.RESIZABLE)
    states = {"GAME": game.Game(),
              "SPLASH": splash.Splash(),
              "MENU": menu.Menu(),
              "GAME_OVER": over.GameOver()
              }
    game = tools.Game(screen, states, "GAME")
    game.run()
    pg.quit()
    sys.exit()
