import pygame
import os
from missile import Missile
from threading import Timer

class Ship(pygame.sprite.Sprite):
    instances = pygame.sprite.Group()
    width, height = 56, 35
    reload_time = 1
    velocity = 5

    def __init__(self, window_width, window_height):
        super().__init__()
        Ship.instances.add(self)

        self.reload_time = Ship.reload_time
        self.loaded = True

        raw_image = pygame.image.load(os.path.join("assets", "images", "ship.png"))
        scaled_image = pygame.transform.scale(raw_image, (Ship.width, Ship.height))

        self.image = scaled_image
        self.rect = self.image.get_rect()
        self.rect.x = window_width // 2 - Ship.width // 2
        self.rect.y = window_height - Ship.height

    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= Ship.velocity

    def move_right(self, window_width):
        if self.rect.x + Ship.width < window_width:
            self.rect.x += Ship.velocity

    def shoot(self):
        if self.loaded:
            Missile(self.rect.x, Ship.width, self.rect.y)
            self.loaded = False
            reload = Timer(self.reload_time, self.reload)
            reload.start()

    def reload(self):
        self.loaded = True