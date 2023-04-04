from Invader import Invader

class Invader2(Invader):
    filename = "invader_1.png"
    width = 49
    height = 33

    def __init__(self, x, y):
        self.velocity = 10
        self.reload_time = 10
        super().__init__(x, y, Invader2.width, Invader2.height)