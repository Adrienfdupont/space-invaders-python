import pygame
import os

class Missile(pygame.sprite.Sprite):

    def __init__(self, width, height, shooter_x, shooter_width, shooter_y):
        super().__init__()
        
        path = os.path.join("assets", "images", "missile.png")
        raw_image = pygame.image.load(path)
        scaled_image = pygame.transform.scale(raw_image, (width, height))
        self.image = scaled_image
        self.rect = self.image.get_rect()
        self.rect.x = shooter_x + shooter_width // 2 - width // 2
        self.rect.y = shooter_y