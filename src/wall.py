from entity import Entity

class Wall(Entity):
    WIDTH, HEIGHT = 15, 15
    IMAGE_FILE_NAME = "wall.png"
    INSTANCES = []

    def __init__(self, x, y):
        super().__init__(x, y, Wall.WIDTH, Wall.HEIGHT, Wall.IMAGE_FILE_NAME)
        Wall.INSTANCES.append(self)

    def die(self):
        self.alive = False