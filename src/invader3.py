from entity import Entity


class Invader3(Entity):
    WIDTH, HEIGHT = 33, 15
    IMAGE_FILE_NAME = "invader_3.png"

    def __init__(self, x, y):
        super().__init__(x, y, Invader3.WIDTH, Invader3.HEIGHT, Invader3.IMAGE_FILE_NAME)