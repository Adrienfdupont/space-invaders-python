import pygame
from Missile import Missile

class ShipMissile(Missile):
    sprites = pygame.sprite.Group()

    def __init__(self, x, y, width, height, filename, velocity):
        super().__init__(
            x,
            y,
            width,
            height,
            filename,
            velocity
        )
        ShipMissile.sprites.add(self)

    def move(self, window_height):
        if self.rect.y + self.height > 0:
            self.rect.y += self.velocity
        else:
            ShipMissile.sprites.remove(self)

    def check_target_collision(self, invader_sprites):
        pygame.sprite.groupcollide(ShipMissile.sprites, invader_sprites, True, True)
