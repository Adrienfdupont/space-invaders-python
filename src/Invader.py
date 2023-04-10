import pygame
import random
from threading import Timer
from InvaderMissile import InvaderMissile
from Entity import Entity
from data import invader_missile as im

class Invader(Entity):
    sprites = pygame.sprite.Group()

    def __init__(self, x, y, width, height, filename, velocity, reload_time):
        super().__init__(x, y, width, height, filename)
        Invader.sprites.add(self)
        self.velocity = velocity
        self.direction = self.velocity
        self.reload_time = reload_time
        self.reload()

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
            InvaderMissile(
                self.rect.x + self.width // 2 - im["width"] // 2,
                self.rect.y,
                im["width"],
                im["height"],
                im["filename"],
                im["velocity"]
            )
            self.reload()

    def reload(self):
        min = self.reload_time // 2
        max = self.reload_time * 1.5
        self.timer = Timer(random.randint(min, max), self.shoot)
        self.timer.start()