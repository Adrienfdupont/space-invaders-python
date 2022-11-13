import pygame
from Entity import Entity

class Ship(Entity):
    def __init__(self, x, y):
        SHIP_WIDTH, SHIP_HEIGHT = 56, 35
        
        super().__init__(x, y, SHIP_WIDTH, SHIP_HEIGHT)
    
