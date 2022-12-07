from entity import Entity
from missile import Missile
from threading import Timer
import random


class Invader(Entity):
    VELOCITY = 3
    MISSILE_VELOCITY = 10
    RELOAD_TIME = 15
    INSTANCES = []
    MISSILES = []

    def __init__(self, x, y, width, height, image_file_name):
        super().__init__(x, y, width, height, image_file_name)
        Invader.INSTANCES.append(self)
        self.move_right = True
        self.width = width
        self.height = height
        self.reload()

    def move(self, game_width, game_height):
        if self.move_right == True:
            if self.rect.x < game_width - 49:
                self.rect.x += Invader.VELOCITY
            else:
                for invader in Invader.INSTANCES:
                    invader.rect.y += 150
                    invader.move_right = False
        else:
            if self.rect.x > 0:
                self.rect.x -= Invader.VELOCITY
            else:
                for invader in Invader.INSTANCES:
                    invader.rect.y += 150
                    invader.move_right = True

    def check_collision(self, walls, ship):
        if self.alive == False:
            return
        for wall in walls:
            if wall.alive == False:
                continue
            if self.rect.colliderect(wall):
                wall.die()
        if self.rect.colliderect(ship):
            ship.die()

    def shoot(self):
        x = self.rect.x + self.width // 2
        y = self.rect.y + self.height // 2
        Missile(x, y, Invader.MISSILE_VELOCITY, Invader.MISSILES)
        self.reload()

    def reload(self):
        reload = Timer(random.randint(1, Invader.RELOAD_TIME), self.shoot)
        reload.start()

    def die(self):
        self.alive = False
        
                
                
