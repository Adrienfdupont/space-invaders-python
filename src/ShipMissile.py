import pygame
from Missile import Missile

class ShipMissile(Missile):
    sprites = pygame.sprite.Group()

    def __init__(self, ship_x, ship_width, ship_y):
        self.width = 10
        self.height = 38
        self.velocity = -15
        super().__init__(self.width, self.height, ship_x, ship_width, ship_y)
        ShipMissile.sprites.add(self)

    def update(self, invader_sprites):
        self.move()
        self.check_collision(invader_sprites)

    def move(self):
        if self.rect.y + self.height > 0:
            self.rect.y += self.velocity
        else:
            ShipMissile.sprites.remove(self)

    def check_collision(self, invader_sprites):
        pygame.sprite.groupcollide(ShipMissile.sprites, invader_sprites, True, True)
