from entity import Entity


class Missile(Entity):
    WIDTH, HEIGHT = 4.9, 18.9
    IMAGE_FILE_NAME = "missile.png"

    def __init__(self, x, y, velocity, instances):
        x = x - Missile.WIDTH // 2
        y = y - Missile.HEIGHT // 2
        super().__init__(x, y, Missile.WIDTH, Missile.HEIGHT, Missile.IMAGE_FILE_NAME)
        instances.append(self)
        self.velocity = velocity

    def move(self):
        if self.rect.y + Missile.HEIGHT > 0:
            self.rect.y += self.velocity

    def check_collision(self, others):
        if self.alive == False:
            return
        for other in others:
            if other.alive == False:
                continue
            if self.rect.colliderect(other):
                other.die()
                self.die()

    def die(self):
        self.alive = False