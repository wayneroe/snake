import sys
from pathlib import Path

import pygame as pg

from core import tools
from core.states import singleplayer, splash, menu, over, multiplayer, victory

if __name__ == "__main__":
    pg.init()
    pg.mixer.init()
    screen = pg.display.set_mode((720, 720), pg.RESIZABLE)
    images_folder = Path("../images/")
    icon_path = str(images_folder / "snake-icon.png")
    icon = pg.image.load(icon_path)
    pg.display.set_icon(icon)
    pg.display.set_caption("Snake")
    states = {"SINGLEPLAYER": singleplayer.SinglePlayer(),
              "MULTIPLAYER": multiplayer.MultiPlayer(),
              "SPLASH": splash.Splash(),
              "MENU": menu.Menu(),
              "GAME_OVER": over.GameOver(),
              "VICTORY": victory.Victory()
              }

    game = tools.Game(screen, states, "MENU")
    game.run()
    pg.quit()
    sys.exit()
