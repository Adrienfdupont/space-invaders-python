import pygame
import os

class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, velocity):
        super().__init__()

        self.width = width
        self.height = height
        self.velocity = velocity

        raw_image = pygame.image.load(os.path.join("assets", "images", "missile.png"))
        scaled_image = pygame.transform.scale(raw_image, (self.width, self.height))

        self.image = scaled_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if self.rect.y + self.height > 0:
            self.rect.y -= self.velocity
        else:
            self.die()