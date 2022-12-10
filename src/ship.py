import pygame
from threading import Timer
from entity import Entity
from missile import Missile


class Ship(Entity):
    WIDTH, HEIGHT = 56, 35
    IMAGE_FILE_NAME = "ship.png"
    RELOAD_TIME = 1
    VELOCITY = 5
    MISSILE_VELOCITY = -10
    MISSILES = []
    INSTANCES = []

    def __init__(self, x, y):
        self.loaded = True
        super().__init__(x, y, Ship.WIDTH, Ship.HEIGHT, Ship.IMAGE_FILE_NAME)
        Ship.INSTANCES.append(self)

    def move(self, key, window_width):
        if key[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= Ship.VELOCITY
        elif key[pygame.K_RIGHT] and self.rect.x + Ship.WIDTH < window_width:
            self.rect.x += Ship.VELOCITY

    def shoot(self):
        if self.alive and self.loaded:
            x = self.rect.x + Ship.WIDTH // 2
            y = self.rect.y + Ship.HEIGHT // 2
            Missile(x, y, Ship.MISSILE_VELOCITY, Ship.MISSILES)
            self.loaded = False

            reload = Timer(Ship.RELOAD_TIME, self.reload)
            reload.start()

    def reload(self):
        self.loaded = True

    def die(self):
        self.alive = False
