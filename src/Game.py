import pygame
import sys
import os
from Ship import Ship
from Invader import Invader
from ShipMissile import ShipMissile
from InvaderMissile import InvaderMissile
from Brick import Brick
from data import invader1 as i1, invader2 as i2, invader3 as i3,  ship as sh

class Game:
    def __init__(self):
        pygame.init()

        # generate window
        self.window_width = 1280
        self.window_height = 720
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Space Invaders")
        self.title_font = pygame.font.Font(os.path.join("assets", "fonts", "PressStart2P-Regular.ttf"), 24)
        self.title_surface = self.title_font.render("Space Invaders", True, (0, 255, 0))
        # generate ship
        self.ship = Ship(
            self.window_width // 2 - sh["width"] // 2,
            self.window_height - sh["height"],
            sh["width"],
            sh["height"],
            sh["filename"],
            sh["velocity"],
            sh["reload_time"]
        )

        # generate invaders
        nb_per_line = 7
        invader_start = 50
        for i in range(nb_per_line):
            Invader(
                10 + i * self.window_width // nb_per_line,
                invader_start,
                i3["width"],
                i3["height"],
                i3["filename"],
                i3["velocity"],
                i3["reload_time"]
            )
        for i in range(nb_per_line):
            Invader(
                10 + i * self.window_width // nb_per_line,
                invader_start + i3["height"],
                i2["width"],
                i2["height"],
                i2["filename"],
                i2["velocity"],
                i2["reload_time"]
            )
        for i in range(nb_per_line):
            Invader(
                10 + i * self.window_width // nb_per_line,
                invader_start + + i3["height"] +  i2["height"],
                i1["width"],
                i1["height"],
                i1["filename"],
                i1["velocity"],
                i1["reload_time"]
            )

        # generate walls
        nb_rows = 5
        nb_walls = 3
        brick_width = 10
        bricks_per_wall = 15
        wall_length = bricks_per_wall * brick_width
        blank_length = (self.window_width - (wall_length * nb_walls)) // (nb_walls + 1)
        
        for row in range(nb_rows):
            y_start = self.window_height - sh["height"] * 2

            for wall in range(nb_walls):
                x_start = wall_length * wall + blank_length * (wall + 1)

                for brick in range(bricks_per_wall):
                    if (row >= nb_rows // 2
                    or brick <= bricks_per_wall * 1/4 - 1
                    or brick >= bricks_per_wall * 3/4):
                        Brick(
                            x_start + brick * brick_width,
                            y_start - row * brick_width,
                            brick_width
                        )

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
        # print title
        self.window.blit(
            self.title_surface, (self.window_width // 2 - self.title_surface.get_width() // 2, 10)
        )
        Ship.sprites.draw(self.window)
        Invader.sprites.draw(self.window)
        ShipMissile.sprites.draw(self.window)
        InvaderMissile.sprites.draw(self.window)
        Brick.sprites.draw(self.window)
        pygame.display.flip()

    def clear(self):
        for invader in Invader.sprites.sprites():
            invader.timer.cancel()