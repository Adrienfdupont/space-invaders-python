from abc import ABC, abstractmethod
from Entity import Entity

class Missile(Entity):
    filename = "missile.png"

    def __init__(self, width, height, shooter_x, shooter_width, shooter_y):
        x = shooter_x + shooter_width // 2 - width // 2
        y = shooter_y
        super().__init__(width, height, x, y, Missile.filename)