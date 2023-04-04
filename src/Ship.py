import pygame
import os
from threading import Timer
from ShipMissile import ShipMissile

class Ship(pygame.sprite.Sprite):
    sprites = pygame.sprite.Group()

    def __init__(self, window_width, window_height):
        self.width = 56
        self.height = 35
        self.velocity = 5
        self.reload_time = 1
        self.reload_time = self.reload_time
        self.loaded = True
        super().__init__()
        Ship.sprites.add(self)

        path = os.path.join("assets", "images", "ship.png")
        raw_image = pygame.image.load(path)
        scaled_image = pygame.transform.scale(raw_image, (self.width, self.height))
        self.image = scaled_image
        self.rect = self.image.get_rect()
        self.rect.x = window_width // 2 - self.width // 2
        self.rect.y = window_height - self.height

    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= self.velocity

    def move_right(self, window_width):
        if self.rect.x + self.width < window_width:
            self.rect.x += self.velocity

    def shoot(self):
        if self.loaded:
            ShipMissile(self.rect.x, self.width, self.rect.y)
            self.loaded = False
            reload = Timer(self.reload_time, self.reload)
            reload.start()

    def reload(self):
        self.loaded = True