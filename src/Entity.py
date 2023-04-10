import pygame
import os

class Entity(pygame.sprite.Sprite):
    sprites = pygame.sprite.Group()

    def __init__(self, x, y, width, height, filename):
        super().__init__()
        self.width = width
        self.height = height
        image_path = os.path.join("assets", "images", filename)
        raw_image = pygame.image.load(image_path)
        scaled_image = pygame.transform.scale(raw_image, (width, height))
        self.image = scaled_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y