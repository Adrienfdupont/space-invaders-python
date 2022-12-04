import pygame
from threading import Timer
from entity import Entity
from missile import Missile


class Ship(Entity):
    WIDTH, HEIGHT = 56, 35
    IMAGE_FILE_NAME = "ship.png"
    RELOAD_TIME = 3
    VELOCITY = 5

    def __init__(self, x, y):
        self.missiles = []
        self.loaded = True
        x = x - Ship.WIDTH // 2
        y = y - Ship.HEIGHT // 2
        super().__init__(x, y, Ship.WIDTH, Ship.HEIGHT, Ship.IMAGE_FILE_NAME)

    def move(self, key, window_width):
        if key[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= Ship.VELOCITY
        elif key[pygame.K_RIGHT] and self.rect.x + Ship.WIDTH < window_width:
            self.rect.x += Ship.VELOCITY

    def shoot(self):
        if self.loaded:
            x = self.rect.x + Ship.WIDTH // 2
            y = self.rect.y + Ship.HEIGHT // 2
            self.missiles.append(Missile(x, y))
            self.loaded = False

            reload = Timer(Ship.RELOAD_TIME, self.reload)
            reload.start()

    def reload(self):
        self.loaded = True
