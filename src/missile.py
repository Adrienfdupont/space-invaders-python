import pygame
import os

class Missile(pygame.sprite.Sprite):
    instances = pygame.sprite.Group()
    width, height = 5, 19
    velocity = 15

    def __init__(self, ship_x, ship_width, ship_y):
        super().__init__()
        Missile.instances.add(self)

        raw_image = pygame.image.load(os.path.join("assets", "images", "missile.png"))
        scaled_image = pygame.transform.scale(raw_image, (Missile.width, Missile.height))

        self.image = scaled_image
        self.rect = self.image.get_rect()
        self.rect.x = ship_x + ship_width // 2 - Missile.width // 2
        self.rect.y = ship_y

    def update(self):
        self.move()

    def die(self):
        Missile.instances.remove(self)

    def move(self):
        if self.rect.y + Missile.height > 0:
            self.rect.y -= Missile.velocity
        else:
            self.die()