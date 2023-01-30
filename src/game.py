import pygame
from ship import Ship
from missile import Missile
from invader import Invader

class Game:
    def __init__(self):
        pygame.init()

        # generate window
        self.window_width = 1280
        self.window_height = 720
        self.window = pygame.display.set_mode((self.window_width, self.window_height))

        # generate ship
        self.ship = Ship(self.window_width, self.window_height)

        # generate invaders
        nb_lines, nb_rows = 3, 7
        for line in range(nb_lines):
            for row in range(nb_rows):
                x = 10 * line + 1 + self.window_width // nb_rows * row
                y = 50 * line
                Invader(x, y, line)

        # generate walls

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
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
        Ship.instances.update()
        Missile.instances.update()
        Invader.instances.update(self.window_width)

    def render(self):
        self.window.fill((0,0,0))
        Ship.instances.draw(self.window)
        Missile.instances.draw(self.window)
        Invader.instances.draw(self.window)
        pygame.display.flip()