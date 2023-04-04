from Invader import Invader

class Invader1(Invader):
    filename = "invader_1.png"
    width = 49
    height = 36
    velocity = 3
    reload_time = 10

    def __init__(self, x, y):
        super().__init__(
            x,
            y,
            Invader1.width,
            Invader1.height,
            Invader1.filename,
            Invader1.velocity,
            Invader1.reload_time
        )