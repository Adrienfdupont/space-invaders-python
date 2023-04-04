import pygame
import os
import random
from threading import Timer
from InvaderMissile import InvaderMissile

class Invader(pygame.sprite.Sprite):
    sprites = pygame.sprite.Group()
    velocity = 3
    levels = [
        {
            'image': 'invader_1.png',
            'width': 49, 
            'height': 36,
        },
        {
            'image': 'invader_2.png',
            'width': 49,
            'height': 33,
        },
        {
            'image': 'invader_3.png',
            'width': 49,
            'height': 23,
        },
    ]

    def __init__(self, x, y, line):
        self.width = Invader.levels[2 - line]['width']
        self.height = Invader.levels[2 - line]['height']
        self.direction = self.velocity
        self.reload_time = 10
        super().__init__()
        Invader.sprites.add(self)

        path = os.path.join("assets", "images", Invader.levels[2 - line]['image'])
        raw_image = pygame.image.load(path)
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