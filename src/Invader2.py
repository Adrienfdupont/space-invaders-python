from Invader import Invader

class Invader2(Invader):
    filename = "invader_2.png"
    width = 49
    height = 33
    velocity = 4
    reload_time = 10

    def __init__(self, x, y):
        super().__init__(
            x,
            y,
            Invader2.width,
            Invader2.height,
            Invader2.filename,
            Invader2.velocity,
            Invader2.reload_time
        )