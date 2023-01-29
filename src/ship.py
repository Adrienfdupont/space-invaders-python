import pygame
import os
from missile import Missile

class Ship(pygame.sprite.Sprite):
    def __init__(self, window_width, window_height, width, height, velocity):
        super().__init__()

        self.width = width
        self.height = height
        self.velocity = velocity

        raw_image = pygame.image.load(os.path.join("assets", "images", "ship.png"))
        scaled_image = pygame.transform.scale(raw_image, (self.width, self.height))

        self.image = scaled_image
        self.rect = self.image.get_rect()
        self.rect.x = window_width // 2 - self.width // 2
        self.rect.y = window_height - self.height

        self.missiles = pygame.sprite.Group()
    
    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= self.velocity

    def move_right(self, window_width):
        if self.rect.x + self.width < window_width:
            self.rect.x += self.velocity

    def shoot(self):
        self.missiles.add(Missile(
            self.rect.x, self.rect.y, 5, 19, 5
        ))