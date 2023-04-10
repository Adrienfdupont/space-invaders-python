import pygame
from Entity import Entity

class Brick(Entity):
    sprites = pygame.sprite.Group()
    filename = "brick.png"

    def __init__(self, x, y, width):
        super().__init__(x, y, width, width, Brick.filename)
        Brick.sprites.add(self)
