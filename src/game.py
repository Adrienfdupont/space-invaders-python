import pygame
from ship import Ship

class Game:
    def __init__(self):
        pygame.init()

        # generate window
        self.window_width = 1280
        self.window_height = 720
        self.window = pygame.display.set_mode((self.window_width, self.window_height))

        # generate ship
        self.ship = Ship(self.window_width, self.window_height, 56, 35, 5)
        self.ships = pygame.sprite.Group()
        self.ships.add(self.ship)

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
        self.ships.update()
        self.ship.missiles.update()

    def render(self):
        self.window.fill((0,0,0))
        self.ships.draw(self.window)
        self.ship.missiles.draw(self.window)
        pygame.display.flip()