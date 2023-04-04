import sys
import pygame
from Ship import Ship
from Invader import Invader
from Invader1 import Invader1
from Invader2 import Invader2
from Invader3 import Invader3
from ShipMissile import ShipMissile
from InvaderMissile import InvaderMissile

class Game:
    def __init__(self):
        pygame.init()

        # generate window
        self.window_width = 1280
        self.window_height = 720
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Space Invaders")

        # generate ship
        self.ship = Ship(self.window_width, self.window_height)

        # generate invaders
        nb_per_line = 7
        for i in range(nb_per_line):
            x = 10 + i * self.window_width // nb_per_line
            y = 10
            Invader3(x, y)

        for i in range(nb_per_line):
            x = 10 + i * self.window_width // nb_per_line
            y = 50
            Invader2(x, y)

        for i in range(nb_per_line):
            x = 10 + i * self.window_width // nb_per_line
            y = 90
            Invader1(x, y)

        # generate walls

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.clear()
                    pygame.quit()
                    sys.exit()
            self.handle_input(pygame.key.get_pressed())
            self.update()
            self.render()

    def handle_input(self, keys):
        if keys[pygame.K_LEFT]:
            self.ship.move_left()
        if keys[pygame.K_RIGHT]:
            self.ship.move_right(self.window_width)
        if keys[pygame.K_SPACE]:
            self.ship.shoot()

    def update(self):
        Ship.sprites.update()
        Invader.sprites.update(self.window_width)
        ShipMissile.sprites.update(Invader.sprites)
        InvaderMissile.sprites.update(self.window_height, Ship.sprites)

    def render(self):
        self.window.fill((0,0,0))
        Ship.sprites.draw(self.window)
        Invader.sprites.draw(self.window)
        ShipMissile.sprites.draw(self.window)
        InvaderMissile.sprites.draw(self.window)
        pygame.display.flip()

    def clear(self):
        for invader in Invader.sprites.sprites():
            invader.timer.cancel()