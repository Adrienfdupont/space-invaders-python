from entity import Entity


class Invader1(Entity):
    WIDTH, HEIGHT = 33, 24
    IMAGE_FILE_NAME = "invader_1.png"

    def __init__(self, x, y):
        super().__init__(x, y, Invader1.WIDTH, Invader1.HEIGHT, Invader1.IMAGE_FILE_NAME)