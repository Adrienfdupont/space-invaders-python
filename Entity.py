import pygame

class Entity:
    def __init__(self, x, y, width, height):
        self.surface = pygame.Rect(x, y, width, height)