from Invader import Invader

class Invader3(Invader):
    filename = "invader_3.png"
    width = 49
    height = 23

    def __init__(self, x, y):
        self.velocity = 5
        self.reload_time = 10
        super().__init__(x, y, Invader3.width, Invader3.height, Invader3.filename)