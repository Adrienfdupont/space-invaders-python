from Invader import Invader

class Invader1(Invader):
    filename = "invader_1.png"
    width = 49
    height = 36

    def __init__(self, x, y):
        self.velocity = 3
        self.reload_time = 10
        super().__init__(x, y, Invader1.width, Invader1.height, Invader1.filename)