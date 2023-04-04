from Invader import Invader

class Invader3(Invader):
    filename = "invader_3.png"
    width = 49
    height = 23
    velocity = 4
    reload_time = 10

    def __init__(self, x, y):
        super().__init__(
            x,
            y,
            Invader3.width,
            Invader3.height,
            Invader3.filename,
            Invader3.velocity,
            Invader3.reload_time
        )