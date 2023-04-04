import pygame
from Missile import Missile

class InvaderMissile(Missile):
    sprites = pygame.sprite.Group()

    def __init__(self, invader_x, invader_width, invader_y):
        self.width = 5
        self.height = 19
        self.velocity = 15
        super().__init__(self.width, self.height, invader_x, invader_width, invader_y)
        InvaderMissile.sprites.add(self)

    def update(self, window_height, ship_sprites):
        self.move(window_height)
        self.check_collision(ship_sprites)

    def move(self, window_height):
        if self.rect.y < window_height:
            self.rect.y += self.velocity
        else:
            InvaderMissile.sprites.remove(self)
    
    def check_collision(self, ship_sprites):
        pygame.sprite.groupcollide(InvaderMissile.sprites, ship_sprites, True, True)
