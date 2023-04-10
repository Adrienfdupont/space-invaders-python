from abc import ABC, abstractmethod
import pygame
from Entity import Entity

class Missile(ABC, Entity):
    filename = "missile.png"

    def __init__(self,x, y, width, height, filename, velocity):
        super().__init__(x, y, width, height, filename)
        self.velocity = velocity

    def update(self, window_height, target_sprites, brick_sprites):
        self.move(window_height)
        self.check_target_collision(target_sprites)
        self.check_wall_collision(brick_sprites)

    @abstractmethod
    def move(self, window_height):
        pass

    @abstractmethod
    def check_target_collision(self, target_sprites):
        pass

    def check_wall_collision(self, brick_sprites):
        pygame.sprite.groupcollide(type(self).sprites, brick_sprites, True, True)