import pygame
import os

class Invader(pygame.sprite.Sprite):
    instances = pygame.sprite.Group()
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
        super().__init__()
        Invader.instances.add(self)

        self.width = Invader.levels[2 - line]['width']
        self.height = Invader.levels[2 - line]['height']

        raw_image = pygame.image.load(os.path.join("assets", "images", Invader.levels[2 - line]['image']))
        scaled_image = pygame.transform.scale(raw_image, (self.width, self.height))

        self.image = scaled_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = self.velocity

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