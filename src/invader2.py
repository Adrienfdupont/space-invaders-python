from entity import Entity


class Invader2(Entity):
    WIDTH, HEIGHT = 33, 22
    IMAGE_FILE_NAME = "invader_2.png"

    def __init__(self, x, y):
        super().__init__(x, y, Invader2.WIDTH, Invader2.HEIGHT, Invader2.IMAGE_FILE_NAME)
