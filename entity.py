import pygame
import os

class Entity:
    def __init__(self, x, y, width, height, image_file_name):
        image_path = os.path.join("assets", "images", image_file_name)
        image = pygame.image.load(image_path).convert()
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = pygame.Rect(x, y, width, height)