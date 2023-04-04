import pygame
import os
import random
from threading import Timer
from InvaderMissile import InvaderMissile

class Invader(pygame.sprite.Sprite):
    sprites = pygame.sprite.Group()

    def __init__(self, x, y, width, height, filename):
        super().__init__()
        Invader.sprites.add(self)
        self.width = width
        self.height = height
        self.direction = self.velocity
        
        raw_image = pygame.image.load(filename)
        scaled_image = pygame.transform.scale(raw_image, (self.width, self.height))
        self.image = scaled_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

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
            InvaderMissile(self.rect.x, self.rect.width, self.rect.y)
            self.reload()

    def reload(self):
        min = self.reload_time // 2
        max = self.reload_time * 1.5
        self.timer = Timer(random.randint(min, max), self.shoot)
        self.timer.start()