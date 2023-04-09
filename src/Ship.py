import pygame
from threading import Timer
from ShipMissile import ShipMissile
from Entity import Entity
from data import ship_missile as sm

class Ship(Entity):
    sprites = pygame.sprite.Group()

    def __init__(self, x, y, width, height, filename, velocity, reload_time):
        super().__init__(x, y, width, height, filename)
        Ship.sprites.add(self)
        self.velocity = velocity
        self.reload_time = reload_time
        self.loaded = True

    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= self.velocity

    def move_right(self, window_width):
        if self.rect.x + self.width < window_width:
            self.rect.x += self.velocity

    def shoot(self):
        if self.loaded:
            ShipMissile(
                self.rect.x + self.width // 2 - sm["width"] // 2,
                self.rect.y,
                sm["width"],
                sm["height"],
                sm["filename"],
                sm["velocity"]
            )
            self.loaded = False
            reload = Timer(self.reload_time, self.reload)
            reload.start()

    def reload(self):
        self.loaded = True