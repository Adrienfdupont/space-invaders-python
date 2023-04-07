import pygame
from Entity import Entity

class Brick(Entity):
    sprites = pygame.sprite.Group()
    filename = "brick.png"

    def __init__(self, width, x, y):
        super().__init__(width, width, x, y, Brick.filename)
        Brick.sprites.add(self)
