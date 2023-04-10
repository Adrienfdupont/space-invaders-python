import pygame
from Missile import Missile

class InvaderMissile(Missile):
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
        InvaderMissile.sprites.add(self)

    def move(self, window_height):
        if self.rect.y < window_height:
            self.rect.y += self.velocity
        else:
            InvaderMissile.sprites.remove(self)
    
    def check_target_collision(self, ship_sprites):
        pygame.sprite.groupcollide(InvaderMissile.sprites, ship_sprites, True, True)
