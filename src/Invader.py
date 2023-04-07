import pygame
import random
from threading import Timer
from InvaderMissile import InvaderMissile
from Entity import Entity

class Invader(Entity):
    sprites = pygame.sprite.Group()

    def __init__(self, x, y, width, height, filename, velocity, reload_time):
        self.velocity = velocity
        self.reload_time = reload_time
        self.direction = self.velocity
        self.reload()
        super().__init__(width, height, x, y, filename)
        Invader.sprites.add(self)

    def update(self, window_width):
        self.move(window_width)

    def move(self, window_width):
        if self.rect.x <= 0:
            self.direction = self.velocity
            self.rect.y += self.height
        if self.rect.x + self.width >= window_width:
            self.direction = - self.velocity
            self.rect.y += self.height
        self.rect.x += self.direction

    def shoot(self):
        if Invader.sprites.has(self):
            InvaderMissile(self.rect.x, self.rect.width, self.rect.y)
            self.reload()

    def reload(self):
        min = self.reload_time // 2
        max = self.reload_time * 1.5
        self.timer = Timer(random.randint(min, max), self.shoot)
        self.timer.start()