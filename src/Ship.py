import pygame
from threading import Timer
from ShipMissile import ShipMissile
from Entity import Entity

class Ship(Entity):
    sprites = pygame.sprite.Group()
    width = 56
    height = 35
    velocity = 5
    reload_time = 1
    filename = "ship.png"

    def __init__(self, window_width, window_height):
        x = window_width // 2 - Ship.width // 2
        y = window_height - self.height
        self.loaded = True
        super().__init__(Ship.width, Ship.height, x, y, Ship.filename)
        Ship.sprites.add(self)

    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= Ship.velocity

    def move_right(self, window_width):
        if self.rect.x + Ship.width < window_width:
            self.rect.x += Ship.velocity

    def shoot(self):
        if self.loaded:
            ShipMissile(self.rect.x, Ship.width, self.rect.y)
            self.loaded = False
            reload = Timer(Ship.reload_time, self.reload)
            reload.start()

    def reload(self):
        self.loaded = True