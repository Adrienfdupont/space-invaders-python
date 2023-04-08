import sys
import pygame
from Ship import Ship
from Invader import Invader
from ShipMissile import ShipMissile
from InvaderMissile import InvaderMissile
from Brick import Brick
from data import invader1, invader2, invader3

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
            Invader(invader3["width"], invader3["height"], x, y, invader3["filename"], invader3["velocity"], invader3["reload_time"])

        for i in range(nb_per_line):
            x = 10 + i * self.window_width // nb_per_line
            y = 50
            Invader(invader2["width"], invader2["height"], x, y, invader2["filename"], invader2["velocity"], invader2["reload_time"])
        for i in range(nb_per_line):
            x = 10 + i * self.window_width // nb_per_line
            y = 90
            Invader(invader1["width"], invader1["height"], x, y, invader1["filename"], invader1["velocity"], invader1["reload_time"])

        # generate walls
        nb_rows = 5
        nb_walls = 3
        brick_width = 10
        bricks_per_wall = 15
        wall_length = bricks_per_wall * brick_width
        blank_length = (self.window_width - (wall_length * nb_walls)) // (nb_walls + 1)
        
        for row in range(nb_rows):
            y_start = self.window_height - 100
            for wall in range(nb_walls):
                x_start = wall_length * wall + blank_length * (wall + 1)
                for brick in range(bricks_per_wall):
                    if (row >= nb_rows // 2
                    or brick <= bricks_per_wall * 1/4- 1
                    or brick >= bricks_per_wall * 3/4):
                        x = x_start + brick * brick_width
                        y = y_start - row * brick_width
                        Brick(brick_width, x, y)

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
        ShipMissile.sprites.update(self.window_height, Invader.sprites, Brick.sprites)
        InvaderMissile.sprites.update(self.window_height, Ship.sprites, Brick.sprites)

    def render(self):
        self.window.fill((0,0,0))
        Ship.sprites.draw(self.window)
        Invader.sprites.draw(self.window)
        ShipMissile.sprites.draw(self.window)
        InvaderMissile.sprites.draw(self.window)
        Brick.sprites.draw(self.window)
        pygame.display.flip()

    def clear(self):
        for invader in Invader.sprites.sprites():
            invader.timer.cancel()