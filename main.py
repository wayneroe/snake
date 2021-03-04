# This code is licensed as CC0 1.0 (https://creativecommons.org/publicdomain/zero/1.0/legalcode).

import sys
import pygame as pg
from Buttons import PushButton
from snake import Snake


class Game(object):
    """
    A single instance of this class is responsible for
    managing which individual game state is active
    and keeping it updated. It also handles many of
    pygame's nuts and bolts (managing the event
    queue, framerate, updating the display, etc.).
    and its run method serves as the "game loop".
    """

    def __init__(self, screen, states, start_state):
        """
        Initialize the Game object.

        screen: the pygame display surface
        states: a dict mapping state-names to GameState objects
        start_state: name of the first active game state
        """
        self.done = False
        self.screen = screen
        self.clock = pg.time.Clock()
        self.fps = 60
        self.states = states
        self.state_name = start_state
        self.state = self.states[self.state_name]

    def event_loop(self):
        """Events are passed for handling to the current state."""
        for event in pg.event.get():
            self.state.get_event(event)

    def flip_state(self):
        """Switch to the next game state."""
        current_state = self.state_name
        next_state = self.state.next_state
        self.state.done = False
        self.state_name = next_state
        persistent = self.state.persist
        self.state = self.states[self.state_name]
        self.state.startup(persistent)

    def update(self, dt):
        """
        Check for state flip and update active state.

        dt: milliseconds since last frame
        """
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(dt)

    def draw(self):
        """Pass display surface to active state for drawing."""
        self.state.draw(self.screen)

    def run(self):
        """
        Pretty much the entirety of the game's runtime will be
        spent inside this while loop.
        """
        while not self.done:
            dt = self.clock.tick(self.fps)
            self.event_loop()
            self.update(dt)
            self.draw()
            pg.display.update()


class GameState(object):
    """
    Parent class for individual game states to inherit from.
    """

    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pg.display.get_surface().get_rect()
        self.persist = {}
        self.font = pg.font.Font(None, 24)

    def startup(self, persistent):
        """
        Called when a state resumes being active.
        Allows information to be passed between states.

        persistent: a dict passed from state to state
        """
        self.persist = persistent

    def get_event(self, event):
        """
        Handle a single event passed by the Game object.
        """
        pass

    def update(self, dt):
        """
        Update the state. Called by the Game object once
        per frame.

        dt: time since last frame
        """
        pass

    def draw(self, surface):
        """
        Draw everything to the screen.
        """
        pass


class SplashScreen(GameState):
    def __init__(self):
        super(SplashScreen, self).__init__()
        self.persist["screen_color"] = "black"
        self.next_state = "GAMEPLAY"

        self.start_button = PushButton("Start Game", self.screen_rect.centerx, 30)
        self.multiplayer_button = PushButton("Multiplayer", self.screen_rect.centerx, 120)

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYUP:
            self.persist["screen_color"] = "gold"
            self.done = True
        elif event.type == pg.MOUSEBUTTONUP:
            self.persist["screen_color"] = "dodgerblue"
            self.done = True
        if self.start_button.rect.collidepoint(pg.mouse.get_pos()):
            self.start_button.on_hover()

    def draw(self, surface):
        surface.fill(pg.Color("black"))
        self.start_button.display(surface)
        self.multiplayer_button.display(surface)


class Gameplay(GameState):
    def __init__(self):
        super(Gameplay, self).__init__()
        self.board_size = 10
        self.bright_green = pg.Color("GreenYellow")
        self.dark_green = pg.Color("LawnGreen")
        self.snake = Snake(720, 720)

    def startup(self, persistent):
        self.persist = persistent

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True

    def update(self, dt):
        self.snake.update(dt)

    def draw(self, surface):
        tile_size = self.screen_rect.width // 10
        self.draw_tiles(surface, tile_size)
        self.snake.draw(surface)
        pg.display.flip()
    
    def draw_tiles(self, surface, tile_size):
        for i in range(self.board_size):
            for j in range(self.board_size):
                if (j + i) % 2 == 0:
                    pg.draw.rect(surface, self.bright_green, [i * tile_size, j * tile_size, tile_size, tile_size])
                else:
                    pg.draw.rect(surface, self.dark_green, [i * tile_size, j * tile_size, tile_size, tile_size])


if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((720, 720))
    states = {"GAMEPLAY": Gameplay()}
    game = Game(screen, states, "GAMEPLAY")
    game.run()
    pg.quit()
    sys.exit()