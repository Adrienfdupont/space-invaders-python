from entity import Entity


class Missile(Entity):
    WIDTH, HEIGHT = 4.9, 18.9
    IMAGE_FILE_NAME = "missile.png"
    VELOCITY = 10

    def __init__(self, x, y):
        x = x - Missile.WIDTH // 2
        y = y - Missile.HEIGHT // 2
        super().__init__(x, y, Missile.WIDTH, Missile.HEIGHT, Missile.IMAGE_FILE_NAME)

    def move(self):
        if self.rect.y + Missile.HEIGHT > 0:
            self.rect.y -= Missile.VELOCITY
